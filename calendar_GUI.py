from tkinter import *
import calendar
import datetime

# from click.exceptions import Exit


def show_calendar():
    gui = Tk()
    gui.config(background='grey')
    gui.title('Calendar for the Year')
    gui.geometry("600x600")
    # now = datetime.datetime.now()
    year = int(year_filed.get())
    gui_content = calendar.calendar(year)
    calYear = Label(gui, text = gui_content, font = "Consolas 10 bold")
    calYear.grid(row=5, column=1, padx=20)
    gui.mainloop()

if __name__ == '__main__':
    new = Tk()
    new.config(background='grey')
    new.title('Calendar')
    new.geometry("250x140")
    cal = Label(new, text='Calendar', bg='grey', font=('times', 28, 'bold'))
    year = Label(new, text='Enter Year', bg='dark grey')
    year_filed = Entry(new)
    # print(year_filed)
    button = Button(new, text='Show Calendar',
                    fg='white', bg='blue', command=show_calendar)

    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_filed.grid(row=3, column=1)
    button.grid(row=4, column=1)
    # Exit.grid(row=6, column=1)
    new.mainloop()