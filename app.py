import tkinter as tk
import logging

from providers.mobrag_provider import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def calc_clicked():
    logger.info('Clicked Calculation')
    # static choose provider
    provider = MobileRagnarokProvider()
    provider.fetch_data(provider.get_categories().get('monsters'))

    # calc = Calculator(provider)
    # calc.calc()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.calc = tk.Button(self, text="Start", fg="red", command=calc_clicked)
        self.calc.pack(side="bottom")


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('480x360')
    app = Application(master=root)
    app.mainloop()
