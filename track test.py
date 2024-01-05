from System.Collections.Generic import List
from System import Byte
import sys

mobs = [
    "slayer",
    "abyss",
    "souls",
    "a silver serpent"
]



def buttonPress() :
    for lineNum in range(len(Gumps.LastGumpGetLineList())):
        lineStr = Gumps.LastGumpGetLine(lineNum)
        for mob in mobs:
            if mob.lower() in lineStr.lower():
                Misc.SendMessage(lineNum, 44)
                Misc.Pause(2000)
                button = lineNum + 1
                return button

def pause():
    if Timer.Check("track") == False :
        Misc.Pause(600)
    else :
        Misc.Pause(10500)
        
def mob_tracking() :
    Player.UseSkill("Tracking")
    Gumps.WaitForGump(2976808305, 10000)
    testtrack = Gumps.LastGumpGetLineList()
    Gumps.SendAction(2976808305, 2)
    Misc.Pause(1200)
    if ("the slayer") in Gumps.LastGumpGetLineList() or ("the Lord of the Abyss") in Gumps.LastGumpGetLineList() or ("collector of souls") in Gumps.LastGumpGetLineList() or ("a silver serpent") in Gumps.LastGumpGetLineList() :
        Gumps.WaitForGump(993494147, 10000)
        Gumps.SendAction(993494147, buttonPress())
        Player.HeadMessage(32, "Rotation mob found")
        return 0
    else :
        Gumps.CloseGump(993494147)  
        Timer.Create("track", 10500)
    
def npc_tracking() :
    Player.UseSkill("Tracking")
    Gumps.WaitForGump(2976808305, 10000)
    Gumps.SendAction(2976808305, 3)
    Misc.Pause(1200)
    if "a chaos dragoon" in Gumps.LastGumpGetLineList() :
        Player.HeadMessage(52,"Found a Chaos Dragoon")
        Gumps.WaitForGump(993494147, 10000)
        Gumps.SendAction(993494147, buttonPress())
        return 0
    else :
        Gumps.CloseGump(993494147)  
        Timer.Create("track", 10500)

while Player.IsGhost == False : 
    mob_tracking()
    pause()
    npc_tracking()
    pause()
