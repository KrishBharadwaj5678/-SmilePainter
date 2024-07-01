import pyautogui as pg

def click():
    pg.click()

# Moving to Search Bar and Clicking
pg.moveTo(100,743,1)
pg.click(x=100, y=743,clicks=1,interval=1,button="left",duration=2)
# Searching Paint
pg.write("paint")
pg.press("enter")
pg.sleep(4)

# Moving to Circle
pg.moveTo(420,60,1)
# Selecting the circle
pg.click()
# Moving to center
pg.moveTo(420,220,1)
# Drawing main circle
pg.dragTo(700,540,2,button="left")
# Moving
pg.moveTo(400,200,1)
pg.click()
# Drawing eye 1
pg.moveTo(470,305,1)
pg.dragTo(520,360,1,button="left")
# Drawing eye 2
pg.moveTo(600,305,1)
pg.dragTo(650,360,1,button="left")
# Drawing Line
pg.moveTo(392,60,1)
pg.click()
pg.moveTo(500,440,1)
pg.dragTo(500,440,1,button="left")
pg.dragTo(625,440,1,button="left")
pg.moveTo(562.5,440)
pg.dragTo(562.5,480,1,button="left")
# Selecting Paint Tool
pg.moveTo(270,60,1)
pg.click()
# Selecting Orange Color
pg.moveTo(857,60,1)
pg.click()
# Painting the whole body
pg.moveTo(568,400,1)
click()
# Selecting White Color
pg.moveTo(770,83,1)
click()
pg.moveTo(419,400,1)
click()
pg.moveTo(469,340,1)
click()
pg.moveTo(600,340,1)
click()
pg.moveTo(600,453,1)
click()
pg.moveTo(750,453,1)
