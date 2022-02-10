from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import Menu
from os import path
import pandas as pd

window = Tk()
window.title("Taxi-route estimator")
window.geometry('420x220+300+300')
window.resizable(width=0, height=0)

file = StringVar()
file.set('')
selected = IntVar()

single_data = {"passenger_count": [IntVar()], "pickup_longitude": [DoubleVar()], "pickup_latitude": [DoubleVar()],
			   "dropoff_longitude": [DoubleVar()], "dropoff_latitude": [DoubleVar()], "date": [StringVar()]}
linecount = 10
data = pd.DataFrame({})

def processHandler(file):
	global data
	# тут будет обрабатываться датасет
	data = pd.read_csv(file)


def startProcessingOne():
	createResultWindow('Обработка строки №' + str(selected.get()))


def startProcessingAll():
    createResultWindow('Обработка всего набора данных')


def startSingleProcessing():
	for k in single_data.keys():
		print(single_data[k][0].get())

def showAbout():
    res = Tk()
    res.title("About")
    res.geometry('220x220+630+330')

    txt = scrolledtext.ScrolledText(res, width=28, height=27, wrap=WORD)
    txt.place(x=0,y=0)

    txt.insert(1.0, 'Мой хэлп текст, сделал я, права мои')
    res.mainloop()

def showSingleUpdater():
	res = Tk()
	res.title("HandInput")
	res.geometry('340x520+230+130')
	txt = Label(res, text="Заполните информацию о поездке для расчёта времени")
	txt.place(x=10, y=20)

	txt = Label(res, text="Введите долготу места отправки")
	field = Entry(res, textvariable=single_data["pickup_longitude"][0])
	field.place(x=5, y=75)
	txt.place(x=5, y=50)

	txt = Label(res, text="Введите широту места отправки")
	field = Entry(res, textvariable=single_data["pickup_latitude"][0])
	field.place(x=5, y=125)
	txt.place(x=5, y=100)

	txt = Label(res, text="Введите долготу места прибытия")
	field = Entry(res, textvariable=single_data["dropoff_longitude"][0])
	field.place(x=5, y=175)
	txt.place(x=5, y=150)

	txt = Label(res, text="Введите широту места прибытия")
	field = Entry(res, textvariable=single_data["dropoff_latitude"][0])
	field.place(x=5, y=225)
	txt.place(x=5, y=200)

	txt = Label(res, text="Введите дату маршрута в формате 'день-месяц-год'")
	field = Entry(res, textvariable=single_data["date"][0])
	field.place(x=5, y=275)
	txt.place(x=5, y=250)

	txt = Label(res, text="Введите количество пассажиров'")
	field = Entry(res, textvariable=single_data["passenger_count"][0])
	field.insert(0, 1)
	field.place(x=5, y=325)
	txt.place(x=5, y=300)

	chk = Button(res, text="Предсказать время маршрута", command=startSingleProcessing)
	chk.place(x=45, y=370)
	res.mainloop()

def createResultWindow(substring):
    res = Tk()
    res.title("Prediction Info")
    res.geometry('220x420+330+330')

    txt = scrolledtext.ScrolledText(res, width=28, height=27, wrap=WORD)
    txt.place(x=0, y=0)

    txt.insert(1.0, substring)
    res.mainloop()


def showSelector():
    global chk, chk_state
    lbl = Label(window, text="Укажите номер")
    lbl.place(x=30, y=120)
    spin = Spinbox(window, textvariable=selected, from_=0, to=linecount, width=13, wrap=True)
    spin.place(x=152, y=105)
    chk = Button(window, text="Обработать эту", command=startProcessingOne)
    chk.place(x=150, y=126)
    chk = Button(window, text="Обработать все", command=startProcessingAll)
    chk.place(x=150, y=156)


def selectFile():
    fileTemp = filedialog.askopenfilename(initialdir= path.dirname(__file__))
    if not fileTemp: return
    if fileTemp.split(".")[-1] != "csv":
    	res = Tk()
    	res.title("Ошибка в формате данных!")
    	res.geometry('320x120+630+330')
    	txt = Label(res, text="поддерживается только .csv формат!")
    	txt.place(x=50, y=50)
    	res.mainloop()
    else:
	    file.set(fileTemp[:5] + '...' + fileTemp[-12:])
	    processHandler(fileTemp)
	    showSelector()



menu = Menu(window)
aboutmenu = Menu(menu)
aboutmenu.add_command(label='About', command=showAbout)
aboutmenu.add_separator()
aboutmenu.add_command(label='Exit', command=exit)
menu.add_cascade(label='Info', menu=aboutmenu)
window.config(menu=menu)



Label(window, text="Расчетчик времени").place(x=130, y=8)


lbl = Label(window, text="Выберите файл")
lbl.place(x=30, y=40)
btn = Button(window, text="Выбрать", command=selectFile)
btn.place(x=150, y=36)
lx = Label(window, textvariable=file)
lx.place(x=240, y=40)

btn2 = Button(window, text="Ввести данные вручную", command=showSingleUpdater)
btn2.place(x=110, y=70)
'''
el = Label(window, text=chk_state.get())
el.place(x=0, y=0)'''
window.mainloop()