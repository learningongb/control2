
import uuid
from datetime import datetime
import json
class note:

    def __init__(self, caption, text) -> None:
        self.uuid = uuid.uuid4().hex
        self.caption = caption
        self.text = text
        self.modified = datetime.now()

    def update(self, caption = None, text = None) -> None:
        if caption:
            self.caption = caption
        if text:
            self.text = text
        self.modified = datetime.now()

    def printnote(self, short: bool):
        print("\033[32m" + self.modified.strftime("%d.%m.%Y %H:%M") + "\033[0m")
        print(self.caption)
        if not short:
            print(self.text)
        print("\033[35mid=" + self.uuid + "\033[0m")


class notelist:

    def __init__(self) -> None:
        self.notes : list[note]
        self.notes = list()

    def add(self, caption, text) -> None:
        self.notes.append(note(caption=caption, text=text))

    def addnote(self, note: note):
        self.notes.append(note)

    def remove(self, noteid) -> bool:
        note = self.finditem(noteid)
        if note:
            self.notes.remove(note)
            return True
        else:
            return False

    def update(self, noteid, caption=None, text=None) -> None:
        note = self.finditem(noteid)
        if note:
            note.update(caption=caption, text=text)

    def finditem(self, noteid) -> note|None:
        for item in self.notes:
            if item.uuid == noteid:
                return item
        return None

class notereaderjson:

    def __init__(self, filename = None) -> None:
        self.filename = filename or 'notes.json'

    def readnotes(self) -> notelist:
        with open(self.filename, "r", encoding="utf-8") as file:
            f = file.read()
            d = json.loads(f)
            return self.notefromjson(d)

    def savenotes(self, notes: notelist) -> None:
        with open(self.filename, "w", encoding="utf-8") as file1:
            file1.write(json.dumps(self.notelisttojson(notes)))

    def notelisttojson(self, notes: notelist):
        newlist = []
        for item in notes.notes:
            newlist.append(self.notetojson(item))
        return newlist

    def notetojson(self, note: note):
        return {"uuid": note.uuid,
                "caption": note.caption,
                "text": note.text,
                "modified": note.modified.isoformat()
                };    

    def notefromjson(self, jsondata: list):
        newnotelist = notelist()
        for item in jsondata:
            newnote = note(item["caption"], item["text"])
            newnote.uuid = item["uuid"]
            newnote.modified = datetime.fromisoformat(item["modified"])
            newnotelist.addnote(newnote)
        
        return newnotelist

class menu:

    def __init__(self, notelist: notelist, reader: notereaderjson) -> None:
        self.notelist = notelist
        self.reader = reader
        self.menuitems = {'1': self.printlist,
                '2': self.addnote,
                '3': self.printnote,
                '4': self.updatenote,
                '5': self.removenote,
                '6': self.printlistwithfilter,
                }

    def printlist(self, begindate: datetime|None = None, enddate: datetime|None = None) -> None:
        if enddate:
            enddate = datetime(enddate.year, enddate.month, enddate.day, 23,59,59,999999)
        for item in self.notelist.notes:
            if (begindate and begindate > item.modified
                or enddate and enddate < item.modified):
                continue
            item.printnote(True)

    def addnote(self) -> None:
        print("Введите заголовок заметки:")
        caption = input()
        print("Введите текст заметки:")
        text = input()
        self.notelist.add(caption, text)
        self.reader.savenotes(self.notelist)
        print("Заметка добавлена")

    def printnote(self) -> None:
        print("Введите идентификатор заметки:")
        uid = input()
        note = self.notelist.finditem(uid)
        if note:
            note.printnote(False)
        else:
            print("Заметка не найдена")

    def updatenote(self):
        print("Введите идентификатор заметки:")
        uid = input()
        note = self.notelist.finditem(uid)
        if note:
            print("Введите новый заголовок (или пустая строка, чтобы оставить как есть)")
            caption = input()
            print("Введите новый текст (или пустая строка, чтобы оставить как есть)")
            text = input()
            if caption or text:
                note.update(caption=caption, text=text)
                self.reader.savenotes(self.notelist)
                print("Заметка изменена")
            else:
                print("Заметка не изменилась")
        else:
            print("Заметка не найдена")

    def removenote(self):
        print("Введите идентификатор заметки:")
        uid = input()
        if self.notelist.remove(uid):
            self.reader.savenotes(self.notelist)    
            print("Заметка удалена")
        else:
            print("Заметка не найдена")

    @staticmethod
    def inputdateorempty(message: str) -> datetime | None:
        while True:
            print(message)
            inputdate = input()
            if inputdate:
                try:
                    dateparts = inputdate.split(".")
                    if len(dateparts) != 3:
                        continue
                    inputdate = datetime(int(dateparts[2]), int(dateparts[1]), int(dateparts[0]))
                    break
                except:
                    continue
            else:
                inputdate = None
                break
        return inputdate

    def printlistwithfilter(self):
        begindate = menu.inputdateorempty("Введите дату начала dd.mm.yyyy (или пустое значение, если дата начала не задана)")
        enddate = menu.inputdateorempty("Введите дату окончания dd.mm.yyyy (или пустое значение, если дата начала не задана)")
        self.printlist(begindate=begindate, enddate=enddate)

    @staticmethod
    def printmenu():
        print("Введите команду:")
        print("1. Вывести список заметок")
        print("2. Добавить заметку")    
        print("3. Вывести заметку")
        print("4. Изменить заметку")
        print("5. Удалить заметку")
        print("6. Вывести список заметок с фильтром")
        print("0. Завершить работу")

    def run(self):
        while (True):
            menu.printmenu()
            answer = input()
            if answer == '0':
                break
            command = self.menuitems.get(answer)
            if command:
                command()

if __name__ == "__main__":
    reader=notereaderjson()
    try:
        notes = reader.readnotes()
    except:
        notes=notelist()
    currentmenu = menu(notelist=notes, reader=reader)
    currentmenu.run()