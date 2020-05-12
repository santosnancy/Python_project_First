from tkinter import *
janela = Tk()
janela.geometry('300x300+300+300')
janela["background"] = 'yellow'
janela.title('python app'.upper())

def output():
    print(inp.get())

inp = Entry(janela)
inp.place(x=100, y=100)

btn = Button(janela, width=20, text='Click here',command=output)
btn.place(x=100, y=150)

lb = Label(janela, text='welcome')
lb.place(x=50, y=200
)




janela.mainloop()
