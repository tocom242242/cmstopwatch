import tkinter as Tkinter
import psutil


class StopWatch:
    def __init__(self, root):
        self.root = root
        self.root.title("StopWatch")
        self.root.minsize(width=200, height=70)

        self.seconds = 0
        self.minutes = 0
        self.hour = 0

        self.time_label = Tkinter.Label(
            root,
            text="---",
            fg="black",
            font="Verdana 20 bold")

        self.time_label.pack()

        self.cpu_mem_label = Tkinter.Label(
            self.root,
            text="---",
            fg="black",
            font="Verdana 10 bold")
        self.cpu_mem_label.pack()

        self.start_btn = Tkinter.Button(
            self.root,
            text='Start',
            width=5,
            command=self._start)
        self.stop_btn = Tkinter.Button(
            self.root,
            text='Stop',
            width=5,
            state='disabled',
            command=self._stop)
        self.reset_btn = Tkinter.Button(
            self.root,
            text='Reset',
            width=5,
            state='disabled',
            command=self._reset)

        self.start_btn.pack(side="left")
        self.stop_btn.pack(side="left")
        self.reset_btn.pack(side="left")

        self._display_cpu_mem()

    def run(self):
        self.root.mainloop()

    def _display_cpu_mem(self):
        cpu_str = str(psutil.cpu_percent()) + "%"
        mem_info = dict(psutil.virtual_memory()._asdict())
        mem_str = str(mem_info["percent"]) + "%"
        self.cpu_mem_label['text'] = "CPU:{}, MEM:{}".format(
            cpu_str, mem_str)

        self.cpu_mem_label.after(1000, self._display_cpu_mem)

    def _counter_time(self):
        if self.running:
            if self.seconds == -1:
                display = "Starting..."
            else:
                display = "{0:02d}:{1:02d}:{2:02d}".format(
                    self.hour, self.minutes, self.seconds)

            self.time_label['text'] = display

            self.seconds += 1
            if self.seconds == 60:
                self.minutes += 1
                self.seconds = 0
            if self.minutes == 60:
                self.hour += 1
                self.minutes = 0
            self.time_label.after(1000, self._counter_time)

    def _start(self):
        self.running = True
        self._counter_time()
        self.start_btn['state'] = 'disabled'
        self.stop_btn['state'] = 'normal'
        self.reset_btn['state'] = 'normal'

    def _stop(self):
        self.start_btn['state'] = 'normal'
        self.stop_btn['state'] = 'disabled'
        self.reset_btn['state'] = 'normal'
        self.running = False

    def _reset(self):
        self.seconds = -1
        self.minutes = 0
        self.hour = 0

        if not self.running:
            self.reset_btn['state'] = 'disabled'
            self.time_label['text'] = '...'
        else:
            self.time_label['text'] = '...'


if __name__ == '__main__':
    root = Tkinter.Tk()
    stopwatch = StopWatch(root)
    stopwatch.run()
