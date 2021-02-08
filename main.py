from tkinter import *
import threading
import datetime


class TimerApp:
    def __init__(self, left_time):
        self.time = left_time
        self.root = Tk()
        self.title = Label(text='Time left:', font=('arial', 22))
        self.title.grid(row=0, column=0)
        self.label = Label(text=str(datetime.timedelta(seconds=self.time)), font=('arial', 22))
        self.label.grid(row=0, column=1)
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        self.time -= 1
        if self.time == 0:
            self.root.destroy()
            return None
        self.label.configure(text=str(datetime.timedelta(seconds=self.time)))
        self.root.after(1000, self.update_clock)


def worker_function(time_left):
    """
    the worker function, this function initiate timer
    :param time_left: initial timer, in seconds
    """
    timer = TimerApp(time_left)


if __name__ == '__main__':
    print("choose the number of seconds for the timer thread\n")
    time_left = int(input())
    worker_thread = threading.Thread(target=worker_function, args=(time_left,))
    worker_thread.start()
    """
    paste your code here
    """
    worker_thread.join()
