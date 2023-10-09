import notelist
import notereaderjson
import menu

reader=notereaderjson.notereaderjson()
try:
    notes = reader.readnotes()
except:
    notes=notelist.notelist()
currentmenu = menu.menu(notelist=notes, reader=reader)
currentmenu.run()