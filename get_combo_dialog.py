import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.scrolled import ScrolledText

from tkinter import filedialog as fd

from pdf_toolbox import PdfToolbox


class GetComboDialog:
    def __init__(self, function):
        self.top = ttk.Toplevel()
        self.top.geometry(f'240x150+750+100')
        self.function = function

        self.combo_name_frame = ttk.Frame(
            master=self.top,
            # width=400,
            # height=400,
            style=SECONDARY,
        )
        self.combo_name_frame.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky='nsew')

        self.combo_name_frame.columnconfigure(0, weight=1)
        self.combo_name_frame.rowconfigure(0, weight=1)
        self.combo_name_frame.rowconfigure(1, weight=1)

        combo_name_lbl = ttk.Label(
            self.combo_name_frame,
            text='enter combo name...',
            width=10,
        )
        combo_name_lbl.grid(row=0, column=0, columnspan=2, padx=(5, 5), pady=(5, 5), sticky='nsew')

        self.combo_name = ttk.StringVar()
        combo_name_entry = ttk.Entry(
            self.combo_name_frame,
            textvariable=self.combo_name,
            width=20,
        )
        combo_name_entry.grid(row=1, column=0, columnspan=2, padx=(5, 5), pady=(5, 5), sticky='nsew')

        combo_name_submit = ttk.Button(
            self.combo_name_frame,
            text='Submit',
            command=self.submit_combo_name,
            # width=40,
        )
        combo_name_submit.grid(row=2, column=0, padx=(5, 5), pady=(5, 5), sticky='nsew')


        combo_name_cancel = ttk.Button(
            self.combo_name_frame,
            text='Close',
            command=self.close_get_combo_dialog,
            # width=40,
            style=DANGER,
        )
        combo_name_cancel.grid(row=2, column=1, padx=(5, 5), pady=(5, 5), sticky='nsew')

    def submit_combo_name(self):
        self.function(self.combo_name)

    def close_get_combo_dialog(self):
        self.top.destroy()

