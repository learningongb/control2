import notelist
import notereaderjson

class menu:

    def __init__(self, notelist: notelist.notelist, reader: notereaderjson.notereaderjson) -> None:
        self.notelist = notelist
        self.reader = reader
        self.menuitems = {'1': self.printlist,
                '2': self.addnote,
                '3': self.printnote,
                '4': self.updatenote,
                '5': self.removenote,
                '6': self.printlistwithfilter,
                }

    def printlist(self) -> None:
        for item in self.notelist.notes:
            print(item.modified)
            print(item.caption)
            print(item.uuid)

    def addnote(self) -> None:
        print("Введите заголовок заметки:")
        caption = input()
        print("Введите текст заметки:")
        text = input()
        self.notelist.add(caption, text)
        self.reader.savenotes(self.notelist)

    def printnote(self) -> None:
        print("Введите идентификатор заметки:")
        uid = input()
        note = self.notelist.finditem(uid)
        if note:
            print(note.modified)
            print(note.caption)
            print(note.text)
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

    def printlistwithfilter(self):
        pass


        
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

