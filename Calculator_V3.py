from tkinter import *

expression = ""

def main():
    window = Tk()
    window.geometry('320x450')
    window.resizable(width=False, height=False)
    icon = PhotoImage(file='')
    window.iconphoto(True, icon)
    window.title("Calculator_V3")

    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    # COMMAND:
    def press(num):
        global expression

        expression = expression + str(num)
        equation.set(expression)
        print(equation)

    def equal():
        global expression
        try:
            total = str(eval(expression))
            equation.set(total)
            expression = ""
        except:
            equation.set(" error ")
            expression = ""

    def clear():
        global expression
        try:
            expression = ""
            equation.set("")
        except IndexError:
            pass

    # LABEL:
    equation = StringVar()

    expression_field = Entry(textvariable=equation, bd=6, fg='#2E2C2B', font=("Comic Sans MS", 30, "bold"))
    expression_field.place(x=0, y=0, height=95, width=320)

    # BUTTON:
    button_1 = Button(window, text='CLEAR', height=3, width=100, bg='#2E2C2B', fg='#FFFFFF', font=('Arial', 12, 'bold'),
                      command=lambda: [clear()])
    button_2 = Button(window, text='/', height=3, width=7, bg='#0757D3', fg='#FFFFFF', font=('Arial', 12, 'bold'),
                      command=lambda: [press('/')])
    button_3 = Button(window, text='7', height=3, width=7, bg='#2E2C2B', fg='#FFFFFF', font=('Arial', 12, 'bold'),
                      command=lambda: [press(7)])
    button_4 = Button(window, text='8', height=3, width=7, bg='#2E2C2B', fg='#FFFFFF', font=('Arial', 12, 'bold'),
                      command=lambda: [press(8)])
    button_5 = Button(window, text='9', height=3, width=7, bg='#2E2C2B', fg='#FFFFFF', font=('Arial', 12, 'bold'),
                      command=lambda: [press(9)])
    button_6 = Button(window, text='x', height=3, width=7, bg='#0757D3', fg='#FFFFFF', font=('Arial', 12, 'bold'),
                      command=lambda: [press('*')])
    button_7 = Button(window, text='4', height=3, width=7, bg='#2E2C2B', fg='#FFFFFF', font=('Arial', 12, 'bold'),
                      command=lambda: [press(4)])
    button_8 = Button(window, text='5', height=3, width=7, bg='#2E2C2B', fg='#FFFFFF', font=('Arial', 12, 'bold'),
                      command=lambda: [press(5)])
    button_9 = Button(window, text='6', height=3, width=7, bg='#2E2C2B', fg='#FFFFFF', font=('Arial', 12, 'bold'),
                      command=lambda: [press(6)])
    button_10 = Button(window, text='-', height=3, width=7, bg='#0757D3', fg='#FFFFFF', font=('Arial', 12, 'bold'),
                       command=lambda: [press('-')])
    button_11 = Button(window, text='1', height=3, width=7, bg='#2E2C2B', fg='#FFFFFF', font=('Arial', 12, 'bold'),
                       command=lambda: [press(1)])
    button_12 = Button(window, text='2', height=3, width=7, bg='#2E2C2B', fg='#FFFFFF', font=('Arial', 12, 'bold'),
                       command=lambda: [press(2)])
    button_13 = Button(window, text='3', height=3, width=7, bg='#2E2C2B', fg='#FFFFFF', font=('Arial', 12, 'bold'),
                       command=lambda: [press(3)])
    button_14 = Button(window, text='+', height=3, width=7, bg='#0757D3', fg='#FFFFFF', font=('Arial', 12, 'bold'),
                       command=lambda: [press('+')])
    button_15 = Button(window, text='0', height=3, width=7, bg='#2E2C2B', fg='#FFFFFF', font=('Arial', 12, 'bold'),
                       command=lambda: [press(0)])
    button_16 = Button(window, text='.', height=3, width=7, bg='#2E2C2B', fg='#FFFFFF', font=('Arial', 12, 'bold'),
                       command=lambda: [press('.')])
    button_17 = Button(window, text='TOTAL',
                       height=3, width=14, bg='#0757D3', fg='#FFFFFF', font=('Arial', 12, 'bold'), padx=6,
                       command=lambda: [equal()])

    # GRID:
    button_1.grid(row=1, column=0, columnspan=3)
    button_2.grid(row=1, column=3)
    button_3.grid(row=2, column=0)
    button_4.grid(row=2, column=1)
    button_5.grid(row=2, column=2)
    button_6.grid(row=2, column=3)
    button_7.grid(row=3, column=0)
    button_8.grid(row=3, column=1)
    button_9.grid(row=3, column=2)
    button_10.grid(row=3, column=3)
    button_11.grid(row=4, column=0)
    button_12.grid(row=4, column=1)
    button_13.grid(row=4, column=2)
    button_14.grid(row=4, column=3)
    button_15.grid(row=5, column=0)
    button_16.grid(row=5, column=1)
    button_17.grid(row=5, column=2, columnspan=2)

    window.mainloop()


if __name__ == '__main__':
    main()