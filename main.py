from recupMenu import *
from menuToPict import *
from clear import *
from uploadInsta import *

menuDuMoment = menu()
menuDict = menuToDict(menuDuMoment)
date = makePict(menuDict, "Midi")
uploadOnInsta(date)
