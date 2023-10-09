import note as classnote

class notelist:

    def __init__(self) -> None:
        self.notes : list[classnote.note]
        self.notes = list()

    def add(self, caption, text) -> None:
        self.notes.append(classnote.note(caption=caption, text=text))

    def addnote(self, note: classnote.note):
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

    def finditem(self, noteid) -> classnote.note|None:
        for item in self.notes:
            if item.uuid == noteid:
                return item
        return None