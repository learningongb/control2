import json
import datetime

import notelist
import note



class notereaderjson:

    def __init__(self, filename = None) -> None:
        self.filename = filename or 'notes.json'

    def readnotes(self) -> notelist.notelist:
        with open(self.filename, "r", encoding="utf-8") as file:
            f = file.read()
            d = json.loads(f)
            return self.notefromjson(d)

    def savenotes(self, notes: notelist.notelist) -> None:
        with open(self.filename, "w", encoding="utf-8") as file1:
            file1.write(json.dumps(self.notelisttojson(notes)))

    def notelisttojson(self, notes: notelist.notelist):
        newlist = []
        for item in notes.notes:
            newlist.append(self.notetojson(item))
        return newlist

    def notetojson(self, note: note.note):
        return {"uuid": note.uuid,
                "caption": note.caption,
                "text": note.text,
                "modified": note.modified.isoformat()
                };    

    def notefromjson(self, jsondata: list):
        newnotelist = notelist.notelist()
        for item in jsondata:
            newnote = note.note(item["caption"], item["text"])
            newnote.uuid = item["uuid"]
            newnote.modified = datetime.datetime.fromisoformat(item["modified"])
            newnotelist.addnote(newnote)
        
        return newnotelist