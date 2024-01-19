from tkinter import *
from datetime import datetime
def search():
    pass
def reset():
    pass

window = Tk()
window.title("Search Copy")

# icon = PhotoImage(file="icon.png")

cityE = Entry(window, )
searchB = Button(window, text="검색", command=search)
resetB = Button(window, text="초기화", command=reset)

lonL = Label(window, text="경도")
lonV = Label(window, text="")
latL = Label(window, text="위도")
latV = Label(window, text="")
# iconL = Label(window,image=icon,background=iconBackgroudColor)
weatherL = Label(window, text="날씨")
weatherV = Label(window, text="")

countryL = Label(window, text="국가")
countryV = Label(window, text="")
cityL = Label(window, text="도시")
cityV = Label(window, text="")
tempL = Label(window, text="온도")
tempV = Label(window, text="")
humidityL = Label(window, text="습도")
humidityV = Label(window, text="")
windSpeedL = Label(window, text="풍속")
windSpeedV = Label(window, text="")

timeL = Label(window, text="현재시간")
now = datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")
timeV = Label(window, text=now)
userV = Label(window, text="장성익")
githubL = Label(window, text="github")

cityE.grid(row=0, column=0, columnspan=2)
searchB.grid(row=0, column=2)
resetB.grid(row=0, column=3)
latL.grid(row=1, column=0)
lonL.grid(row=1, column=1)
latV.grid(row=2, column=0)
lonV.grid(row=2, column=1)
weatherL.grid(row=3, column=0)
weatherV.grid(row=3, column=1)
# iconL.grid(row=4,column=0,rowspan=2,columnspan=2)
countryL.grid(row=1, column=2)
countryV.grid(row=1, column=3)
cityL.grid(row=2, column=2)
cityV.grid(row=2, column=3)
tempL.grid(row=3, column=2)
tempV.grid(row=3, column=3)
humidityL.grid(row=4, column=2)
humidityV.grid(row=4, column=3)
windSpeedL.grid(row=5, column=2)
windSpeedV.grid(row=5, column=3)

timeL.grid(row=6,column=0)
timeV.grid(row=6,column=1)
userV.grid(row=7, column=0)
githubL.grid(row=7, column=1)

window.mainloop()
