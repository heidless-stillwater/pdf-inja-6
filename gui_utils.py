import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.scrolled import ScrolledText

from tkinter import filedialog as fd

# from dashboard import *

from pdf_toolbox import PdfToolbox
from get_combo_dialog import GetComboDialog

import logging_utils_2 as pn_log
import pathlib
from pdf2image import convert_from_path
from PIL import Image, ImageTk
from icecream import ic
import os
import os.path
from os import path

# pathlib
# setuptools

from constants import *

class PdfNinja(ttk.Frame):
    root_dir = os.getcwd()
    # ic(root_dir)

    def __init__(self, master_window):
        super().__init__(master_window, padding=(0, 0))
        # self.pack(fill=BOTH, expand=YES)

        self.pdf_t = PdfToolbox()

        self.current_combo_name = ''

        # reveal app window
        self.grid(row=0, column=0)

        self.name = ttk.StringVar(value='')
        self.student_id = ttk.StringVar(value='')
        self.course_name = ttk.StringVar(value='')
        self.final_score = ttk.DoubleVar(value=0)
        self.data = []
        self.colors = master_window.style.colors

        self.app_mgr_container = ttk.Frame(
            master_window,
            width=5000,
            height=5000,
            # style=WARNING,
        )
        self.app_mgr_container.grid(row=0, column=0, rowspan=1, padx=(20, 20), pady=(20, 20), sticky='nsew')

        self.app_mgr_container.rowconfigure(0, weight=1)
        self.app_mgr_container.columnconfigure(0, weight=1)
        self.app_mgr_container.columnconfigure(1, weight=1)

        self.appMgrCreate()

        self.njDashboardCreate()

        self.njSupportCreate()

        # self.page_switch_to_support()
        self.pageSwitchToDashboard()

    #@pn_log.pn_logger
    # @pn_log.pn_timer
    def appMgrCreate(self) -> None:
        # ic('in app mgr create')
        self.app_mgr_sidebar = ttk.Frame(
            master=self.app_mgr_container,
            width=500,
            height=500,
            # style=INFO,
        )
        self.app_mgr_sidebar.grid(row=0, column=0, rowspan=1, padx=(5, 5), pady=(5, 5), sticky='ne')

        self.app_mgr_sidebar.columnconfigure(0, weight=1)
        self.app_mgr_sidebar.rowconfigure(0, weight=1)
        self.app_mgr_sidebar.rowconfigure(1, weight=1)
        #
        self.appNgrCreateBranding()
        self.appMgrControls()

    #@pn_log.pn_logger
    # @pn_log.pn_timer
    def appNgrCreateBranding(self) -> None:
        self.branding_container = ttk.Frame(
            master=self.app_mgr_sidebar,
            width=300,
            height=300,
            # style=SUCCESS,
        )
        self.branding_container.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky='')

        self.appMgrLogo()

    #@pn_log.pn_logger
    # @pn_log.pn_timer
    def appMgrLogo(self) -> None:
        # logo
        # sz_h = int(sz_w * 1.41)

        sz_w = 150
        sz_h = sz_w
        # sz_h = int(sz_w * 1.41)
        id('load image...)')
        # ic(PDF_NINJA_LOGO)

        icon_img = Image.open(PDF_NINJA_LOGO).resize((sz_w, sz_h))
        logo_img = ImageTk.PhotoImage(icon_img)

        # logo_img = ImageTk.PhotoImage(master=self, file=PDF_NINJA_LOGO)
        # ic(logo_img)

        self.logo_widget = ttk.Label(
          master=self.branding_container,
          image=logo_img,
        )
        self.logo_widget.image = logo_img
        self.logo_widget.grid(row=0, column=0, rowspan=1, padx=(5, 5), pady=(5, 5), ipady=0, sticky='n')

    #@pn_log.pn_logger
    # @pn_log.pn_timer
    def appMgrControls(self) -> None:
        self.app_mgr_controls = ttk.Frame(
            master=self.app_mgr_sidebar,
            # width=600,
            height=600,
            # style=PRIMARY,
        )
        self.app_mgr_controls.grid(row=1, column=0, rowspan=1, padx=5, pady=5, sticky='')

        self.app_mgr_controls.columnconfigure(0, weight=1)
        self.app_mgr_controls.rowconfigure(0, weight=1)
        self.app_mgr_controls.rowconfigure(1, weight=1)
        self.app_mgr_controls.rowconfigure(2, weight=1)

        self.appMgrButtonbox()

    #@pn_log.pn_logger
    # @pn_log.pn_timer
    def appMgrButtonbox(self) -> None:
        self.button_container = ttk.Frame(
            self.app_mgr_controls,
            width=200,
            height=200,
            # style=INFO,
        )
        self.button_container.grid(row=0, column=0, rowspan=1, padx=(20, 20), pady=(20, 20), sticky='ew')
        self.button_container.columnconfigure(0, weight=1)
        self.button_container.rowconfigure(0, weight=1)
        self.button_container.rowconfigure(1, weight=1)
        self.button_container.rowconfigure(2, weight=1)

        label = ttk.Label(self, text="Startpage", font=LARGEFONT)

        switch_to_dashboard_btn = ttk.Button(
            master=self.button_container,
            text='Dashboard',
            command=self.pageSwitchToDashboard,
            # style=DANGER,
            # width=15
        )
        switch_to_dashboard_btn.grid(row=0, column=0, rowspan=1, padx=(5, 5), pady=(5, 5), sticky='nsew')

        switch_to_dashboard_btn = ttk.Button(
            master=self.button_container,
            text='Support',
            command=self.pageSwitchToSupport,
            style=PRIMARY,
            width=15
        )
        switch_to_dashboard_btn.grid(row=1, column=0, rowspan=1, padx=(5, 5), pady=(5, 5), sticky='ew')

        cancel_btn = ttk.Button(
            master=self.button_container,
            text='Remove ALL pdf_files',
            command=self.pdfFilesRemoveAll,
            style=WARNING,
            width=20
        )
        cancel_btn.grid(row=2, column=0, rowspan=1, padx=(5, 5), pady=(30, 30), sticky='ew')
        #
        # cancel_btn_1 = ttk.Button(
        #     master=self.button_container,
        #     text='Cancel 1',
        #     command=self.app_mgr_on_cancel,
        #     style=SECONDARY,
        #     width=6
        # )
        # cancel_btn_1.grid(row=3, column=0, rowspan=1, padx=(5, 5), pady=(5, 5), sticky='')

        cancel_btn_2 = ttk.Button(
            master=self.button_container,
            text='Cancel',
            command=self.appMgrOnCancel,
            style=DANGER,
            width=6
        )
        cancel_btn_2.grid(row=4, column=0, rowspan=1, padx=(5, 5), pady=(100, 5), sticky='nsew')

    #@pn_log.pn_logger
    # @pn_log.pn_timer
    def pdfFilesRemoveAll(self) -> None:
        home_dir = os.getcwd()
        # ic(home_dir)

        # pdf infiles
        # ic(PDF_INFILES)
        os.chdir(PDF_INFILES)

        this_dir = os.getcwd()
        # ic(this_dir)

        listing = self.dirFiles(this_dir)
        ic(type(listing), listing)
        os.chdir(home_dir)

        self.unlinkFiles(listing)

        # pdf pages
        # ic(PDF_PAGES_DIR)
        os.chdir(PDF_PAGES_DIR)

        this_dir = os.getcwd()
        # ic(this_dir)

        listing = self.dirFiles(this_dir)
        # ic(listing)
        os.chdir(home_dir)

        self.unlinkFiles(listing)


        # combo infiles
        # ic(COMBO_INFILES_DIR)
        os.chdir(COMBO_INFILES_DIR)

        this_dir = os.getcwd()
        # ic(this_dir)

        listing = self.dirFiles(this_dir)
        # ic(listing)
        os.chdir(home_dir)

        self.unlinkFiles(listing)


        # combo pages
        # ic(COMBO_PAGES_DIR)
        os.chdir(COMBO_PAGES_DIR)

        this_dir = os.getcwd()
        # ic(this_dir)

        listing = self.dirFiles(this_dir)
        # ic('pdf_files_remove_all:', listing)

        os.chdir(home_dir)

        self.unlinkFiles(listing)

        # combo images
        # ic(COMBO_IMAGES_DIR)
        os.chdir(COMBO_IMAGES_DIR)

        this_dir = os.getcwd()
        # ic(this_dir)

        listing = self.dirFiles(this_dir)
        # ic(listing)
        os.chdir(home_dir)

        self.unlinkFiles(listing)

        self.njSupportMainWindow()
        # ic('calling dashboard_combo_pages_images_refresh')
        self.njDashboardMainFrame()
        # self.nj_dashboard_create()

    #@pn_log.pn_logger
    # @pn_log.pn_timer
    def pdfFilesRemove(self, listing: list) -> None:
        ic(listing, type(listing))
        self.unlinkFiles(listing)

    #@pn_log.pn_logger
    # @pn_log.pn_timer
    def unlinkFiles(self, listing:list) -> None:
        for i in listing:
            # ic('deleting:', i)
            i.unlink()

    #@pn_log.pn_logger
    # @pn_log.pn_timer
    def dirFiles(self, dir_path: str) -> list:
        # import pathlib

        # folder path
        # dir_path = r'E:\\account\\'

        # to store file names
        res = []

        # construct path object
        d = pathlib.Path(dir_path)

        # iterate directory
        for entry in d.iterdir():
            # check if it a file
            if entry.is_file():
                res.append(entry)
        return(res)

    #@pn_log.pn_logger
    # @pn_log.pn_timer
    def pageSwitchToDashboard(self) -> None:
        self.nj_supp_0.grid_forget()
        self.nj_dash_0.grid(row=0, column=1, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='')
        self.nj_dash_0.tkraise()

    #@pn_log.pn_logger
    # @pn_log.pn_timer
    def pageSwitchToSupport(self) -> None:
        # ic('in page_switch_to_support')
        self.nj_dash_0.grid_forget()
        self.nj_supp_0.grid(row=0, column=1, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='')
        self.nj_supp_0.tkraise()

    ######################
    # SUPPORT
    ######################

    #@pn_log.pn_timer
    def njSupportCreate(self):
        self.nj_supp_0 = ttk.Frame(
            self.app_mgr_container,
            width=500,
            height=500,
            # style=SUCCESS
        )
        self.nj_supp_0.grid(row=0, column=1, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='')

        self.njSupportHeader()
        self.njSupportTopBar()
        self.njSupportMainWindow()
        self.njSupportBottomBar()
        #
        # ###########################
        # refresh listings

        # infiles
        self.supportComboInfilesRefresh()

        # pages
        self.supportComboPagesRefresh()

        # pages images
        self.supportComboPagesImagesRefresh()

    # @pn_log.pn_timer
    def njSupportHeader(self):
        self.njSupportHeader = ttk.Frame(
            master=self.nj_supp_0,
            width=200,
            height=500,
            # style=PRIMARY,
        )
        self.njSupportHeader.grid(row=0, column=0, rowspan=1, columnspan=1, padx=(5, 5), pady=(5, 5), sticky='')

        self.nj_support_header_lbl = ttk.Label(
            master=self.njSupportHeader,
            text='Support - master',
            font=TITLE_FONT,
            style=LIGHT,
        )
        self.nj_support_header_lbl.grid(row=0, column=0, rowspan=1, columnspan=1, padx=(5, 5), pady=(5, 5), sticky='')

    # @pn_log.pn_timer
    def njSupportTopBar(self):
        self.pn_supp_top_bar = ttk.Frame(
            master=self.nj_supp_0,
            # width=500,
            # height=10,
            # style=DARK,
        )
        self.pn_supp_top_bar.grid(row=1, column=0, rowspan=1, columnspan=1, padx=(5, 5), pady=(5, 5), sticky='n')

        self.pn_supp_top_bar.rowconfigure(0, weight=2)

        self.pn_supp_top_bar.columnconfigure(0, weight=1)
        self.pn_supp_top_bar.columnconfigure(1, weight=1)
        self.pn_supp_top_bar.columnconfigure(2, weight=1)
        self.pn_supp_top_bar.columnconfigure(3, weight=1)
        self.pn_supp_top_bar.columnconfigure(4, weight=1)

        self.support_operations = ttk.Frame(
            master=self.pn_supp_top_bar,
            # style=DARK
        )
        self.support_operations.grid(row=1, column=0, rowspan=1, padx=(5, 5), pady=(5, 5), sticky='')

        button_0 = ttk.Button(
            master=self.support_operations,
            text='Load PDF File - TST',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.loadPdfFile(),
        )
        button_0.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky='')

        button_1 = ttk.Button(
            master=self.support_operations,
            text='Generate PDF Pages',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.genPdfPagesFromAllInfiles(),
        )
        button_1.grid(row=1, column=1, padx=(5, 5), pady=(5, 5), sticky='')

        button_2 = ttk.Button(
            master=self.support_operations,
            text='Generate Combo Infiles',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.buildComboAll(),
        )
        button_2.grid(row=1, column=2, padx=(5, 5), pady=(5, 5), sticky='')

        button_3 = ttk.Button(
            master=self.support_operations,
            text='Generate Combo Pages',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.genComboPagesFromComboPages(),
        )
        button_3.grid(row=1, column=3, padx=(5, 5), pady=(5, 5), sticky='')

        button_4 = ttk.Button(
            master=self.support_operations,
            text='Generate Combo Images',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.generateComboPagesImages(),
        )
        button_4.grid(row=1, column=4, padx=(5, 5), pady=(5, 5), sticky='')

        button_5 = ttk.Button(
            master=self.support_operations,
            text='Full Wash Cycle - Support',
            # style=DANGER,
            cursor='hand2',
            command=lambda: self.supportFullWashCycle(),
        )
        button_5.grid(row=1, column=5, padx=(5, 5), pady=(5, 5), sticky='')

    # @pn_log.pn_timer
    def njSupportMainWindow(self):
        # ic('in nj_support_main_window')
        self.nj_support_main = ttk.Frame(
            master=self.nj_supp_0,
            # width=200,
            # height=500,
            style=SECONDARY,
        )
        self.nj_support_main.grid(row=2, column=0, rowspan=1, columnspan=1, padx=(10, 10), pady=(10, 10), sticky='')

        self.nj_support_main.columnconfigure(0, weight=1)
        self.nj_support_main.columnconfigure(1, weight=1)
        self.nj_support_main.columnconfigure(2, weight=1)
        self.nj_support_main.rowconfigure(0, weight=1)
        self.nj_support_main.rowconfigure(1, weight=1)

        self.nj_support_scroll_combo_infiles = ScrolledFrame(
            master=self.nj_support_main,
            autohide=True,
            width=SCROLLFRAME_WIDTH + 20,
            height=SCROLLFRAME_HEIGHT,
            # style=DARK,
        )
        self.nj_support_scroll_combo_infiles.grid(row=0, column=0, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='nsew')

        self.nj_support_scroll_combo_pages = ScrolledFrame(
            master=self.nj_support_main,
            autohide=True,
            width=SCROLLFRAME_WIDTH + 75,
            height=SCROLLFRAME_HEIGHT,
            # style=DARK,
        )
        self.nj_support_scroll_combo_pages.grid(row=0, column=1, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='nsew')

        self.nj_support_scroll_combo_images = ScrolledFrame(
            master=self.nj_support_main,
            autohide=True,
            width=SUPPORT_SCROLLFRAME_WIDTH,
            height=SUPPORT_SCROLLFRAME_HEIGHT,
            # style=WARNING,
        )
        self.nj_support_scroll_combo_images.grid(row=0, column=2, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='')

        self.nj_support_scroll_combo_images.columnconfigure(0, weight=1)
        self.nj_support_scroll_combo_images.columnconfigure(1, weight=1)
        # self.nj_support_main.rowconfigure(0, weight=1)

        self.nj_support_scroll_combo_images_switches = []

    # @pn_log.pn_timer
    def njSupportBottomBar(self):
        # pdf_ninja
        self.pn_supp_bottom_bar = ttk.Frame(
            master=self.nj_supp_0,
            # width=500,
            # height=10,
            # style=SECONDARY,
        )
        self.pn_supp_bottom_bar.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(10, 10), pady=(10, 10), sticky='')

        self.pn_supp_bottom_bar.rowconfigure(0, weight=2)
        self.pn_supp_bottom_bar.rowconfigure(1, weight=1)

        self.pn_supp_bottom_bar.columnconfigure(0, weight=1)
        self.pn_supp_bottom_bar.columnconfigure(1, weight=1)
        self.pn_supp_bottom_bar.columnconfigure(2, weight=1)
        self.pn_supp_bottom_bar.columnconfigure(3, weight=1)
        self.pn_supp_bottom_bar.columnconfigure(4, weight=1)

        supp_bottom_btn_0 = ttk.Button(
            master=self.pn_supp_bottom_bar,
            text='Gen COMBO Infiles',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.dummyFunc(),
        )
        supp_bottom_btn_0.grid(row=0, column=0, padx=(10, 5), pady=(5, 5), sticky='')

        supp_bottom_btn_1 = ttk.Button(
            master=self.pn_supp_bottom_bar,
            text='Gen COMBO Pages',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.genComboPagesFromComboPages(),
        )
        supp_bottom_btn_1.grid(row=0, column=1, padx=(10, 5), pady=(5, 5), sticky='')

        supp_bottom_btn_2 = ttk.Button(
            master=self.pn_supp_bottom_bar,
            text='Gen COMBO Pages Images',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.generateComboPagesImages(),
        )
        supp_bottom_btn_2.grid(row=0, column=2, padx=(10, 5), pady=(5, 5), sticky='')

        refresh_combo_infiles_btn = ttk.Button(
            master=self.pn_supp_bottom_bar,
            text='Combo INFILES Refresh',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.supportComboInfilesRefresh(),
        )
        refresh_combo_infiles_btn.grid(row=1, column=1, padx=(10, 5), pady=(5, 5), sticky='')

        refresh_combo_pages_btn = ttk.Button(
            master=self.pn_supp_bottom_bar,
            text='Combo PAGES Refresh',
            style=PRIMARY,
            cursor='hand2',
            command=lambda: self.supportComboPagesRefresh(),
        )
        refresh_combo_pages_btn.grid(row=1, column=0, padx=(10, 5), pady=(5, 5), sticky='')

        self.support_info_txt = ScrolledText(
            master=self.pn_supp_bottom_bar,
            # autohide=False,
            # hbar=True,
            width=74,
            height=5,
            # style=PRIMARY,
        )
        self.support_info_txt.grid(row=0, column=3, rowspan=2, padx=(10, 5), pady=(5, 5), sticky='')

    # @pn_log.pn_timer
    def supportComboInfilesRefresh(self):
        # ic(f'support_combo_infiles_refresh')

        self.combo_sort_infiles_listing_frame_switches = []
        row = 0

        title_infiles = ttk.Label(
            master=self.nj_support_scroll_combo_infiles,
            font=HEADING_FONT,
            style=LIGHT,
            text='combo infiles'
        )
        title_infiles.grid(row=row, column=0, padx=(125, 0), pady=(0, 0), sticky='W')

        combo_infiles_lst = self.comboInfilesListing()
        # ic(combo_infiles_lst)

        row += 1
        for in_file in combo_infiles_lst:
            # print(f'combo_pages_refresh:combo:{combo}')
            switch_name = ttk.Checkbutton(
                master=self.nj_support_scroll_combo_infiles,
                text=f"{in_file}",
                # fg_color='yellow',
                style=WARNING
            )
            switch_name.grid(row=row, column=0, padx=(10, 0), pady=(20, 0), sticky='w')
            row += 1
            self.combo_sort_infiles_listing_frame_switches.append(switch_name)

        return combo_infiles_lst

    # @pn_log.pn_timer
    def supportComboPagesRefresh(self):
        # ic('in support_combo_pages_refresh')
        self.combo_pages_listing_frame_switches = []

        # ic('combo pages heading - start')
        row = 0
        title_combo_pages = ttk.Label(
            master=self.nj_support_scroll_combo_pages,
            font=HEADING_FONT,
            style=LIGHT,
            text='combo pages'
        )
        title_combo_pages.grid(row=row, column=0, padx=(125, 0), pady=(0, 0), sticky='E')
        # ic('support_combo_pages_refresh - start')

        combo_lst = self.getComboPagesListing()
        # ic('support_combo_pages_refresh', combo_lst)

        row += 1
        for combo in combo_lst:
            # ic(f'support_combo_pages_refresh:combo:{combo}')
            switch_name = ttk.Checkbutton(
                master=self.nj_support_scroll_combo_pages,
                text=f"{combo}",
                style=PRIMARY,
            )
            switch_name.grid(row=row, column=0, padx=(10, 0), pady=(20, 0), sticky='W')
            row += 1
            self.combo_pages_listing_frame_switches.append(switch_name)

        return combo_lst

    @pn_log.pn_timer
    def supportComboPagesImagesRefresh(self):
        # ic('in support_combo_pages_images_refresh')
        combo_lst = self.getComboPagesImagesListing()
        # ic(f'combo_pages_images_refresh: {combo_lst}')

        ##############################

        ##############################

        self.nj_support_scroll_combo_images_switches = []

        row = 0
        support_combo_images = ttk.Label(
            master=self.nj_support_scroll_combo_images,
            font=HEADING_FONT,
            style=LIGHT,
            text='combo images'
        )
        support_combo_images.grid(row=row, column=0, padx=(0, 0), pady=(0, 0), sticky='')
        # ic('support_combo_images_refresh - start')

        row += 1
        col_index = 0
        for combo in combo_lst:
            # ic(row, col_index)
            if col_index >= SUPPORT_NUM_COLS:
                col_index = 0
                row += 1
            # ic(row, col_index)

            combo_pages_image_frame = ttk.Frame(
                master=self.nj_support_scroll_combo_images,
                # style=LIGHT,
            )
            combo_pages_image_frame.grid(row=row, column=col_index, padx=(10, 10), pady=(20, 0), sticky='')
            # combo_pages_image_frame.grid(row=row, column=col_index, padx=(0, 0), pady=(0, 0), sticky='')

            combo_pages_image_frame.rowconfigure(0, weight=1)
            combo_pages_image_frame.rowconfigure(1, weight=1)
            combo_pages_image_frame.columnconfigure(0, weight=1)
            combo_pages_image_frame.columnconfigure(1, weight=1)
            combo_pages_image_frame.columnconfigure(2, weight=1)

            # ic(row, col_index)
            # ic(combo)
            # ic(row, col_index)

            sz_w = SUPPORT_COMBO_ICON_WIDTH
            sz_h = int(sz_w * 1.41)
            icon_img = Image.open(f'{COMBO_IMAGES_DIR}/{combo}').resize((sz_w, sz_h))
            img_path = f'{COMBO_IMAGES_DIR}/{combo}'
            # ic(img_path)
            # skip if image already exists
            # if img_path.exists():

            icon_img = Image.open(img_path).resize((sz_w, sz_h))
            photo_img = ImageTk.PhotoImage(icon_img)

            switch_initial_state = ttk.IntVar(value=1)
            switch_name = ttk.Checkbutton(
                master=combo_pages_image_frame,
                # width=50,
                # height=50,
                style=WARNING,
                variable=switch_initial_state,
            )
            switch_name.grid(row=1, column=0, padx=(5, 5), pady=(5, 10), sticky='')
            self.nj_support_scroll_combo_images_switches.append(switch_name)

            # test_pages_image_label = ttk.Label(
            #     master=combo_pages_image_frame,
            #     # image=photo_img,
            #     # font='helvetica 18 bold',
            #     # width=100,
            #     text='TESTER',
            #     # compound='top',
            #     style=LIGHT,
            # )
            # test_pages_image_label.grid(row=0, column=0, padx=(0, 0), pady=(5, 5))

            combo_pages_image_label = ttk.Label(
                master=combo_pages_image_frame,
                image=photo_img,
                # font='helvetica 18 bold',
                # width=100,
                text=combo,
                compound='top',
                style=LIGHT,
            )
            combo_pages_image_label.image = photo_img
            combo_pages_image_label.grid(row=0, column=0, padx=(0, 0), pady=(5, 5))

            col_index += 1

    # @pn_log.pn_timer
    def supportDisplayListing(self, lst):
        # print(f'display_pdf_listing:lst: {lst}')
        out_txt = ''
        for f in lst:
            out_txt += f'{f}\n'
            # ic(out_txt)
        self.support_info_txt.delete("0.0", "end")  # delete all text
        self.support_info_txt.insert("0.0", out_txt)

    ########## END SUPPORT #############


    ######################
    # DASHBOARD
    ######################

    # @pn_log.pn_timer
    def njDashboardCreate(self):
        self.nj_dash_0 = ttk.Frame(
            self.app_mgr_container,
            width=800,
            height=500,
            # style=SUCCESS
        )
        self.nj_dash_0.grid(row=0, column=1, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='')

        self.njDashboardHeader()
        self.njDashboardTopBar()
        self.njDashboardMainFrame()
        self.njDashboardBottomBar()

    # @pn_log.pn_timer
    def njDashboardHeader(self):
        self.nj_dashboard_header = ttk.Frame(
            master=self.nj_dash_0,
            width=200,
            height=500,
            # style=PRIMARY,
        )
        self.nj_dashboard_header.grid(row=0, column=0, rowspan=1, columnspan=1, padx=(5, 5), pady=(5, 5), sticky='')

        self.nj_dashboard_header_lbl = ttk.Label(
            master=self.nj_dashboard_header,
            text='DashBoard',
            font=TITLE_FONT,
            style=LIGHT,
        )
        self.nj_dashboard_header_lbl.grid(row=0, column=0, rowspan=1, columnspan=1, padx=(5, 5), pady=(5, 5), sticky='')

    # @pn_log.pn_timer
    def njDashboardTopBar(self):
        self.pn_top_bar = ttk.Frame(
            master=self.nj_dash_0,
            # width=500,
            # height=10,
            # style=DARK,
        )
        self.pn_top_bar.grid(row=1, column=0, rowspan=1, columnspan=1, padx=(5, 5), pady=(5, 5), sticky='n')

        self.pn_top_bar.rowconfigure(0, weight=2)

        self.pn_top_bar.columnconfigure(0, weight=1)
        self.pn_top_bar.columnconfigure(1, weight=1)
        self.pn_top_bar.columnconfigure(2, weight=1)
        self.pn_top_bar.columnconfigure(3, weight=1)
        self.pn_top_bar.columnconfigure(4, weight=1)

        self.dashboard_operations = ttk.Frame(
            master=self.pn_top_bar,
            # style=DARK
        )
        self.dashboard_operations.grid(row=1, column=0, rowspan=1, padx=(5, 5), pady=(5, 5), sticky='')

        dash_get_selection_btn = ttk.Button(
            master=self.dashboard_operations,
            text='Get Selection - DASH',
            # style=DANGER,
            cursor='hand2',
            command=lambda: self.dashGetImageSelection(),
        )
        dash_get_selection_btn.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky='')

        dash_full_was_cycle_btn = ttk.Button(
            master=self.dashboard_operations,
            text='Full Wash Cycle - DASH',
            # style=DANGER,
            cursor='hand2',
            command=lambda: self.fullWashCycle(),
        )
        dash_full_was_cycle_btn.grid(row=1, column=1, padx=(5, 5), pady=(5, 5), sticky='')

        #
        # button_0 = ttk.Button(
        #     master=self.dashboard_operations,
        #     text='Load PDF File - TST',
        #     style=PRIMARY,
        #     cursor='hand2',
        #     command=lambda: self.load_pdf_file(),
        # )
        # button_0.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky='')
        #
        # button_1 = ttk.Button(
        #     master=self.dashboard_operations,
        #     text='Generate PDF Pages',
        #     style=PRIMARY,
        #     cursor='hand2',
        #     command=lambda: self.gen_pdf_pages_from_all_infiles(),
        # )
        # button_1.grid(row=1, column=1, padx=(5, 5), pady=(5, 5), sticky='')
        #
        # button_2 = ttk.Button(
        #     master=self.dashboard_operations,
        #     text='Generate Combo Infiles',
        #     style=PRIMARY,
        #     cursor='hand2',
        #     command=lambda: self.build_combo_all(),
        # )
        # button_2.grid(row=1, column=2, padx=(5, 5), pady=(5, 5), sticky='')
        #
        # button_3 = ttk.Button(
        #     master=self.dashboard_operations,
        #     text='Generate Combo Pages',
        #     style=PRIMARY,
        #     cursor='hand2',
        #     command=lambda: self.gen_combo_pages_from_combo_pages(),
        # )
        # button_3.grid(row=1, column=3, padx=(5, 5), pady=(5, 5), sticky='')
        #
        # button_4 = ttk.Button(
        #     master=self.dashboard_operations,
        #     text='Generate Combo Images',
        #     style=PRIMARY,
        #     cursor='hand2',
        #     command=lambda: self.generate_combo_pages_images(),
        # )
        # button_4.grid(row=1, column=4, padx=(5, 5), pady=(5, 5), sticky='')

    # @pn_log.pn_timer
    def njDashboardMainFrame(self):
        self.nj_dashboard_main = ttk.Frame(
            master=self.nj_dash_0,
            # width=200,
            # height=500,
            style=DARK,
        )
        self.nj_dashboard_main.grid(row=2, column=0, rowspan=1, columnspan=1, padx=(10, 10), pady=(10, 10), sticky='')

        self.nj_dashboard_main.columnconfigure(0, weight=1)
        self.nj_dashboard_main.rowconfigure(0, weight=1)
        self.nj_dashboard_main.rowconfigure(1, weight=1)

        self.nj_dashboard_scroll_pages = ScrolledFrame(
            master=self.nj_dashboard_main,
            autohide=True,
            width=1200,
            height=600,
            # style=SECONDARY,
        )
        self.nj_dashboard_scroll_pages.grid(row=0, column=0, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='nsew')
        self.nj_dashboard_scroll_pages_switches = []

        self.dashboardComboPagesImagesRefresh()

        #
        # self.test_button = ttk.Button(
        #     master=self.nj_dash_0,
        #     style=WARNING
        # )
        # self.test_button.grid(row=1, column=1, rowspan=1, padx=(10, 10), pady=(10, 10), sticky='nsew')

    # @pn_log.pn_timer
    def njDashboardBottomBar(self):
        # pdf_ninja
        self.pn_bottom_bar = ttk.Frame(
            master=self.nj_dash_0,
            # width=500,
            # height=10,
            # style=SECONDARY,
        )
        self.pn_bottom_bar.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(10, 10), pady=(10, 10), sticky='')

        self.pn_bottom_bar.rowconfigure(0, weight=2)
        self.pn_bottom_bar.rowconfigure(1, weight=1)

        self.pn_bottom_bar.columnconfigure(0, weight=1)
        self.pn_bottom_bar.columnconfigure(1, weight=1)
        self.pn_bottom_bar.columnconfigure(2, weight=1)
        self.pn_bottom_bar.columnconfigure(3, weight=1)
        self.pn_bottom_bar.columnconfigure(4, weight=1)

        self.bottom_lbl_0 = ttk.Label(
            master=self.pn_bottom_bar,
            text='Status Label: ',
            style=LIGHT,
            font='Helvetica, 12',
        )
        self.bottom_lbl_0.grid(row=0, column=0, columnspan=6, padx=(10, 5), pady=(5, 5), sticky='')

    # @pn_log.pn_timer
    def dashboardComboPagesImagesRefresh(self):
        row = 0
        col_index = 0
        combo_lst = self.getComboPagesImagesListing()
        self.dash_switches = []

        # self.dashGetImageSelection()

        # ic(f'dashboard_combo_pages_images_refresh: {combo_lst}')

        # self.combo_pages_images_listing_frame_switches = []

        # self.nj_dashboard_scroll_pages_switches = []


        for combo in combo_lst:
            switch_index = 0
            # ic(row, col_index)
            if col_index >= DASHBOARD_NUM_COLS:
                col_index = 0
                row += 1
            # ic(row, col_index)

            combo_pages_image_frame = ttk.Frame(
                master=self.nj_dashboard_scroll_pages,
            )
            combo_pages_image_frame.grid(row=row, column=col_index, padx=(0, 0), pady=(0, 0))

            combo_pages_image_frame.rowconfigure(0, weight=1)
            combo_pages_image_frame.rowconfigure(1, weight=1)
            combo_pages_image_frame.columnconfigure(0, weight=1)
            combo_pages_image_frame.columnconfigure(1, weight=1)
            combo_pages_image_frame.columnconfigure(2, weight=1)

            # ic(row, col_index)
            # ic(combo)
            # ic(row, col_index)

            sz_w = COMBO_ICON_WIDTH
            # sz_w = 500
            sz_h = int(sz_w * 1.41)
            icon_img = Image.open(f'{COMBO_IMAGES_DIR}/{combo}').resize((sz_w, sz_h))
            img_path = f'{COMBO_IMAGES_DIR}/{combo}'
            # ic(img_path)
            # skip if image already exists
            # if img_path.exists():

            icon_img = Image.open(img_path).resize((sz_w, sz_h))
            photo_img = ImageTk.PhotoImage(icon_img)

            combo_pages_image_label = ttk.Label(
                master=combo_pages_image_frame,
                image=photo_img,
                # font='helvetica 18 bold',
                # width=100,
                text=combo,
                compound='top',
                # style=LIGHT,
            )
            combo_pages_image_label.image = photo_img
            combo_pages_image_label.grid(row=0, column=0, padx=(0, 0), pady=(5, 5))

            switchStateVariable = ttk.BooleanVar()
            check_button = ttk.Checkbutton(
                master=combo_pages_image_frame,
                # width=50,
                # height=50,
                style=WARNING,
                variable=switchStateVariable,
                # command=self.checkbutton_clicked
            )
            check_button.grid(row=1, column=0, padx=(5, 5), pady=(5, 10), sticky='')
            self.nj_dashboard_scroll_pages_switches.append(check_button)
            self.dash_switches.append(check_button)

            # self.dashGetImageSelection()

            col_index += 1
    #
    # def checkbutton_clicked(obj):
    #     print("New state:", obj.switchStateVariable.get())

    # @pn_log.pn_timer
    def dashGetImageSelection(self):
        ic('in dash_get_image_selection')

        # switches = self.dash_switches

        switches = [tk.BooleanVar() for i in self.dash_switches]

        ic(self.dash_switches)
        switch_variable = ttk.BooleanVar()

        for i, switch in enumerate(switches):
            ic(i, switch.get(), switch)

        chks = [tk.BooleanVar() for i in self.nj_dashboard_scroll_pages_switches]
        # ic(chks)

        # self.switchStateVariable.get()

        # self.switchStateVariable
        # lst = [l[i] for i, chk in enumerate(chks) if chk.get()]
        # lst = [chks[i] for i, chk in enumerate(chks) if self.switchStateVariable.get()]

        lst = [chks[i] for i, chk in enumerate(chks) if chk.get()]
        # ic(lst)

        # print("New state:", obj.switchStateVariable.get())

        #
        # for i, switch in enumerate(self.nj_dashboard_scroll_pages_switches):
        #     ssV = switch.get()
        #     ic(i, ssV)
        #
        #     sw = self.nj_dashboard_scroll_pages_switches[i]
        #     ic(sw)

    ############################
        #
        # ic(list(map(func, li)))
        # ic(map(func, li))
        #
        # # comprehension example
        # ic([func(x) for x in li if x % 2 == 0])
        #
############################
        #
        # # self.nj_dashboard_scroll_pages_switches.append(switch_name)
        #
        # # orig_switches = self.nj_dashboard_scroll_pages_switches
        # # ic(orig_switches.get())
        #
        # #
        # # new_switches = [tk.BooleanVar() for i in orig_switches]
        # # ic(new_switches)
        #
        # def on_click():
        #     lst = [l[i] for i, chk in enumerate(chks) if chk.get()]
        #     print(",".join(lst))
        #
        # l = ["apple", "ball", "cat", "dog"]
        #
        # chks = [tk.BooleanVar() for i in l]
        #
        # for i, s in enumerate(l):
        #     tk.Checkbutton(window, text=s, variable=chks[i]).pack(anchor=tk.W)
        #
        # tk.Button(window, text="submit", command=on_click).pack()

###################

        # ic(lst)

        # ic(len(self.nj_dashboard_scroll_pages_switches))



        #
        # def getVal(s):
        #     switchStateVariable = ttk.BooleanVar(s.get())
        #     return switchStateVariable
        #
        # ic(list(map(getVal, chks)))

        #
        # ic(list(
        #     map(
        #         self.switchStateVariable.get(),
        #         chks))
        #     )
        # )

        #
        # for i, val in enumerate(chks):
        #     ic(i, val)
        #     is_selected = self.nj_dashboard_scroll_pages_switches[i].get()
        #     ic(is_selected)
        # #
        # selection = []
        # for i in enumerate(pdf_pages_listing):
        #     is_selected = 1
        #     # is_selected = self.page_listing_frame_switches[i].get()
        #
        #     # ic(is_selected)
        #     # print(f'get_page_selection:is_selected: {is_selected} :: file: {listing[i]}')
        #     if is_selected == 1:
        #         selection.append(pdf_pages_listing[i[0]])
        # # ic(selection)
        # return selection
        #





        # chks = [tk.BooleanVar() for i in self.nj_dashboard_scroll_pages_switches]

        # ic(list(lambda x: ic(x), map(ic, chks)))

        #
        # ic(list(map(func, li)))
        # ic(map(func, li))
        #
        #
        # # comprehension example
        # ic([func(x) for x in li if x % 2 == 0])





        # ic(lambda chks[x]: for x in chks))
        #
        # f1 = lambda x: chks[x]
        # ic(f1(0))

        # ic(lambda x: ic('val:', val)) for val in enumerate(chks)))


    # @pn_log.pn_timer
    def getComboPagesImagesListing(self):
        listing = self.pdf_t.list_combo_images_dir()
        # print(f'XXXX:get_combo_pages_listing: {listing}')
        # self.display_listing(listing)
        return listing
    #
    # def get_combo_pages_images_listing(self):
    #     listing = self.pdf_t.list_combo_images_dir()
    #     # print(f'XXXX:get_combo_pages_listing: {listing}')
    #     # self.display_listing(listing)
    #     return listing

    ########## END DASHBOARD #############

    ##################################
    # General Service Funcs
    @pn_log.pn_timer
    def fullWashCycle(self):
        """ fully process a pdf file - both DASHBOARD & SUPPORT"""
        # print(f'\nfull_wash_cycle')
        self.loadPdfFile()

        # print(f'full_wash_cycle:gen pdf pages')
        self.genPdfPagesFromAllInfiles()

        # print(f'full_wash_cycle: building combo')
        self.buildComboAll()

        # print(f'full_wash_cycle: building combo pages')
        self.genComboPagesFromComboPages()

        # print(f'full_wash_cycle: building combo pages images')
        self.generateComboPagesImages()

        self.comboPagesImagesRefreshSupport()
        self.supportComboInfilesRefresh()
        self.supportComboPagesRefresh()
        self.supportComboPagesImagesRefresh()

        # combo_pages_listing = self.get_combo_pages_listing()
        # combo_pages_in_dir = COMBO_PAGES_DIR
        # self.refresh_all_combo_pages_images(combo_pages_listing, combo_pages_in_dir)

        # refreshing dnd listing
        # self.combo_sort_refresh()

    @pn_log.pn_timer
    def supportFullWashCycle(self):
        """ fully process a pdf file - both DASHBOARD & SUPPORT"""
        # print(f'\nfull_wash_cycle')
        self.loadPdfFile()

        # print(f'full_wash_cycle:gen pdf pages')
        self.genPdfPagesFromAllInfiles()

        # print(f'full_wash_cycle: building combo')
        self.buildComboAll()

        # print(f'full_wash_cycle: building combo pages')
        self.genComboPagesFromComboPages()

        # print(f'full_wash_cycle: building combo pages images')
        self.generateComboPagesImages()

        # combo_pages_listing = self.get_combo_pages_listing()
        # combo_pages_in_dir = COMBO_PAGES_DIR
        # self.refresh_all_combo_pages_images(combo_pages_listing, combo_pages_in_dir)

        # refreshing dnd listing
        # self.combo_sort_refresh()

        self.supportComboInfilesRefresh()
        self.supportComboPagesRefresh()
        self.supportComboPagesImagesRefresh()

    @pn_log.pn_timer
    def openGetComboDialog(self):
        """ pop up data input example """
        getComboDialog = GetComboDialog(self.refreshComboName)

    @pn_log.pn_timer
    def refreshComboName(self, combo_name):
        """ REDUNDANT? """
        # ic('update function from main window...')
        self.current_combo_name = combo_name.get()
        # ic(self.current_combo_name)
        self.bottom_lbl_0.configure(text=f'Current Combo: {self.current_combo_name}')

    @pn_log.pn_timer
    def getComboNameInput(self):
        """ contains Label & Entry Box"""
        self.current_combo_name = ''

        # create label
        self.combo_name_lbl = ttk.Label(
            master=self.dashboard_operations,
            # text='Enter your preferred Combo name: '
        )
        self.combo_name_lbl.grid(row=0, column=3, rowspan=1, columnspan=1, padx=(0, 0), pady=(10, 10), sticky='w')

        def get_combo_name():
            self.combo_name_lbl.config(text=f'You typed: {self.combo_name_entry.get()}')
            new_combo_name = self.combo_name_entry.get()
            # ic(new_combo_name)
            self.current_combo_name = new_combo_name
            # ic(self.current_combo_name)
            return new_combo_name

        # create entry widget
        self.combo_name_entry = ttk.Entry(
            master=self.dashboard_operations,
            style=SUCCESS,
            width=28,
            font=('Helvetica', 10)
        )
        # combo_name_entry.insert(0, "Enter Combo Name: ")
        self.combo_name_entry.grid(row=0, column=0, rowspan=1, columnspan=2, padx=(0, 0), pady=(10, 10), sticky='')

        # create button
        self.combo_name_btn = ttk.Button(
            master=self.dashboard_operations,
            style='SUCCESS OUTLINE',
            text='Use Name',
            command=get_combo_name(),
        )
        self.combo_name_btn.grid(row=0, column=2, rowspan=1, columnspan=1, padx=(0, 0), pady=(10, 10), sticky='w')

        self.combo_name_btn.wait_variable(self.current_combo_name)

        return self.current_combo_name

    @pn_log.pn_timer
    def buildComboAll(self):
        """
            relies on self.combo_filename_entry.get() :: is that called?
        """
        ic('in build_combo_all')
        # get name of combo from user
        # form variables
        self.combo_name = ttk.StringVar(value="")
        # self.current_combo_name = ''

        # outfile = self.combo_filename_entry.get()
        outfile = self.current_combo_name
        ic(outfile)

        new_name = outfile.removesuffix('.pdf')
        ic(new_name)
        # outfile = new_name

        outfile_global = outfile
        # ic(f'outfile set: {outfile}')

        if len(outfile) == 0:
            dummy = 0
            # ic(f'no Entry')
            # self.textbox.delete("0.0", "end")  # delete all text
            # out_txt = 'No Entry'
            # self.textbox.insert("0.0", out_txt)
        else:
            # ic(outfile)
            if len(outfile) == 0:
                ic(f'No Pages Selected...')
            else:
                selection = self.getPageAllSelected(outfile_global)
                # print(f'build_combo_all:selection: {selection}')
                self.pdf_t.merge_files(selection, outfile)

                # c_lst_frame = self.combo_listing_frame.grid_columnconfigure(0, weight=1)
                # self.combo_refresh()
                # FileMgr.combo_refresh(c_lst_frame)
        # print(f'xxxxxxxxxx-#####-xxxxxxxx: build_combo_all: calling combo refresh')

        # self.combo_refresh()

    # @pn_log.pn_timer
    def getPageAllSelected(self, pattern):
        # ic('in get_page_all_selected')
        pdf_pages_listing = self.pdf_t.list_pages_dir(pattern)
        # ic(pattern, pdf_pages_listing)

        # ic(f'{__name__} : {pdf_pages_listing}')

        selection = []
        for i in enumerate(pdf_pages_listing):
            is_selected = 1
            # is_selected = self.page_listing_frame_switches[i].get()

            # ic(is_selected)
            # print(f'get_page_selection:is_selected: {is_selected} :: file: {listing[i]}')
            if is_selected == 1:
                selection.append(pdf_pages_listing[i[0]])
        # ic(selection)
        return selection

    # @pn_log.pn_timer
    def comboInfilesListing(self):
        listing = self.pdf_t.combo_infiles_listing()
        # print(f'combo_infiles_listing:listing: {listing}')
        # self.display_listing(listing)
        return listing

    # @pn_log.pn_timer
    def combo_infiles_listing_PROTO(self):
        listing = self.pdf_t.combo_infiles_listing()
        # ic(listing)

        # ic(self.outfile_global)

        # print(f'combo_infiles_listing:listing: {listing}')
        # print(f'combo_infiles_listing:listing: {listing}')
        # self.display_listing(listing)
        return listing

    # @pn_log.pn_timer
    def getComboPagesListing(self):
        listing = self.pdf_t.list_combo_pages_dir()
        # print(f'XXXX:get_combo_pages_listing: {listing}')
        # ic(listing)
        # self.display_listing(listing)
        return listing

    # @pn_log.pn_timer
    def comboPagesImagesRefresh(self):
        row = 0
        col_index = 0
        combo_lst = self.getComboPagesImagesListing()
        # ic(f'combo_pages_images_refresh: {combo_lst}')

        ##############################

        ##############################

        self.combo_pages_images_listing_frame_switches = []

        for combo in combo_lst:
            # ic(row, col_index)
            if col_index >= DASHBOARD_NUM_COLS:
                col_index = 0
                row += 1
            # ic(row, col_index)

            combo_pages_image_frame = ttk.Frame(
                master=self.nj_dashboard_scroll_pages,
            )
            combo_pages_image_frame.grid(row=row, column=col_index, padx=(0, 0), pady=(0, 0))

            combo_pages_image_frame.rowconfigure(0, weight=1)
            combo_pages_image_frame.rowconfigure(1, weight=1)
            combo_pages_image_frame.columnconfigure(0, weight=1)
            combo_pages_image_frame.columnconfigure(1, weight=1)
            combo_pages_image_frame.columnconfigure(2, weight=1)

            # ic(row, col_index)
            # ic(combo)
            # ic(row, col_index)

            sz_w = COMBO_ICON_WIDTH
            sz_h = int(sz_w * 1.41)
            icon_img = Image.open(f'{COMBO_IMAGES_DIR}/{combo}').resize((sz_w, sz_h))
            img_path = f'{COMBO_IMAGES_DIR}/{combo}'
            # ic(img_path)
            # skip if image already exists
            # if img_path.exists():


            icon_img = Image.open(img_path).resize((sz_w, sz_h))
            photo_img = ImageTk.PhotoImage(icon_img)

            switch_initial_state = ttk.IntVar(value=1)
            switch_name = ttk.Checkbutton(
                master=combo_pages_image_frame,
                # width=50,
                # height=50,
                style=WARNING,
                variable=switch_initial_state,
            )
            switch_name.grid(row=1, column=0, padx=(5, 5), pady=(5, 10), sticky='')
            self.combo_pages_images_listing_frame_switches.append(switch_name)

            # test_pages_image_label = ttk.Label(
            #     master=combo_pages_image_frame,
            #     # image=photo_img,
            #     # font='helvetica 18 bold',
            #     # width=100,
            #     text='TESTER',
            #     # compound='top',
            #     style=LIGHT,
            # )
            # test_pages_image_label.grid(row=0, column=0, padx=(0, 0), pady=(5, 5))

            combo_pages_image_label = ttk.Label(
                master=combo_pages_image_frame,
                image=photo_img,
                # font='helvetica 18 bold',
                # width=100,
                text=combo,
                compound='top',
                # style=LIGHT,
            )
            combo_pages_image_label.image = photo_img
            combo_pages_image_label.grid(row=0, column=0, padx=(0, 0), pady=(5, 5))

            col_index += 1

    @pn_log.pn_timer
    def comboPagesImagesRefreshSupport(self):
        row = 0
        col_index = 0
        combo_lst = self.getComboPagesImagesListing()
        # ic(f'combo_pages_images_refresh: {combo_lst}')

        ##############################

        ##############################

        self.combo_pages_images_listing_frame_switches = []

        for combo in combo_lst:
            # ic(row, col_index)
            if col_index >= DASHBOARD_NUM_COLS:
                col_index = 0
                row += 1
            # ic(row, col_index)

            combo_pages_image_frame = ttk.Frame(
                master=self.nj_dashboard_scroll_pages,
            )
            combo_pages_image_frame.grid(row=row, column=col_index, padx=(0, 0), pady=(0, 0))

            combo_pages_image_frame.rowconfigure(0, weight=1)
            combo_pages_image_frame.rowconfigure(1, weight=1)
            combo_pages_image_frame.columnconfigure(0, weight=1)
            combo_pages_image_frame.columnconfigure(1, weight=1)
            combo_pages_image_frame.columnconfigure(2, weight=1)

            # ic(row, col_index)
            # ic(combo)
            # ic(row, col_index)

            sz_w = COMBO_ICON_WIDTH
            sz_h = int(sz_w * 1.41)
            icon_img = Image.open(f'{COMBO_IMAGES_DIR}/{combo}').resize((sz_w, sz_h))
            img_path = f'{COMBO_IMAGES_DIR}/{combo}'
            # ic(img_path)
            # skip if image already exists
            # if img_path.exists():


            icon_img = Image.open(img_path).resize((sz_w, sz_h))
            photo_img = ImageTk.PhotoImage(icon_img)

            switch_initial_state = ttk.IntVar(value=1)
            switch_name = ttk.Checkbutton(
                master=combo_pages_image_frame,
                # width=50,
                # height=50,
                style=WARNING,
                variable=switch_initial_state,
            )
            switch_name.grid(row=1, column=0, padx=(5, 5), pady=(5, 10), sticky='')
            self.combo_pages_images_listing_frame_switches.append(switch_name)

            # test_pages_image_label = ttk.Label(
            #     master=combo_pages_image_frame,
            #     # image=photo_img,
            #     # font='helvetica 18 bold',
            #     # width=100,
            #     text='TESTER',
            #     # compound='top',
            #     style=LIGHT,
            # )
            # test_pages_image_label.grid(row=0, column=0, padx=(0, 0), pady=(5, 5))

            combo_pages_image_label = ttk.Label(
                master=combo_pages_image_frame,
                image=photo_img,
                # font='helvetica 18 bold',
                # width=100,
                text=combo,
                compound='top',
                # style=LIGHT,
            )
            combo_pages_image_label.image = photo_img
            combo_pages_image_label.grid(row=0, column=0, padx=(0, 0), pady=(5, 5))

            col_index += 1

    @pn_log.pn_timer
    def generateComboPagesImages(self):
        # REDUNDANT
        c_lst = self.getComboPagesListing()
        # ic(f'c_lst: {c_lst}')

        # define out images
        folder_img = ImageTk.PhotoImage(Image.open(DIR_IMG).resize((35, 35)))
        list_image = ImageTk.PhotoImage(Image.open(LIST_IMG).resize((60, 60)))
        icon_lst = []
        # ic(c_lst)

        for in_file in c_lst:

            # ic(in_file)
            images_path = f'{COMBO_IMAGES_DIR}/{in_file}.png'
            # ic(images_path)

            if path.exists(images_path):
                dummy = 0
                # ic(in_file, 'already exists', path.exists(images_path) )
            else:
                # ic(in_file, 'path does NOT exists')

                # ic(in_file)
                with open(in_file, 'wb') as in_img:
                    f_path = f'{COMBO_PAGES_DIR}/{in_file}'
                    # ic(f_path)
                    img = convert_from_path(f_path)

                    for i in range(len(img)):
                        save_file = COMBO_IMAGES_DIR + '/' + in_file + '.png'
                        # ic(save_file)

                        img[i].save(save_file, 'PNG')

        self.comboPagesImagesRefresh()
        self.comboPagesImagesRefreshSupport()

    @pn_log.pn_timer
    def genComboPagesFromComboPages(self):
        # ic('gen_combo_pages_from_combo_pages')
        # converts ALL infiles
        # ic(f'gen_combo_pages_from_combo')
        # get selection
        row = 0

        combo_infiles_lst_PROTO = self.combo_infiles_listing_PROTO()
        # ic(combo_infiles_lst_PROTO)

        # remove all not equal to outfile_global

        # print(f'combo_infiles_lst: {combo_infiles_lst}')

        # which combo infiles have been selected
        selection = []
        row = 0
        # ic(self.combo_pages_listing_frame_switches)

        for in_file in combo_infiles_lst_PROTO:
            # is_set = self.combo_pages_listing_frame_switches[row].get()
            is_set = True
            #
            # print(f'gen_combo_pages_from_combo:is_set: {is_set}')
            # print(f'gen_combo_pages_from_combo:in_file: {in_file}')

            # print(f'is_set:    {is_set} :: infile: {infile}')
            if is_set:
                selection.append(in_file)
            row += 1

        # print(f'gen_combo_pages_from_combo:selection: {selection}')
        # generate combo_pages from selected combo_infiles
        for combo_infile in selection:
            combo_infile = f'{combo_infile}'
            name_of_split = f'{combo_infile}'
            in_dir = COMBO_INFILES_DIR
            out_dir = COMBO_PAGES_DIR
            # print(f'out_dir: {out_dir}')

            # print(f'gen_pdf_pages_from_infile:combo_infile: {combo_infile}')
            self.pdf_t.split_combo_infiles_2_pages(
                combo_infile,
                name_of_split,
                in_dir,
                out_dir
            )

            # print(f'gen_combo_pages_from_combo: calling combo_images_refresh')
            self.supportComboPagesRefresh()
            # self.combo_images_refresh()

    @pn_log.pn_timer
    def loadPdfFile(self):
        # self.refresh_f_listings()
        # ic(f'in load_PDF_file')

        # get entry value
        # load_pdf_file_name = f'{self.load_file_entry.get()}'

        self.current_combo_name = fd.askopenfilename()
        # ic(self.current_combo_name, self.current_combo_name.split('/')[-1])

        # read input file'
        try:
            # ic('opening', self.load_pdf_file )
            with open(self.current_combo_name, 'rb') as in_img:
                pdf_contents = in_img.read()
                # print(f'pdf_contents: {pdf_contents}')
        except:
            print(f'unable to open: {self.current_combo_name}')

        # ic(pdf_contents)

        # write local infile
        out_split = self.current_combo_name.split('/')[-1]
        # ic(out_split)

        # print(f'out_split: {out_split}')

        pdf_save_file = f'{PDF_INFILES}/{out_split}'
        # ic(pdf_save_file)

        combo_infilea = f'{COMBO_INFILES_DIR}/{out_split}'
        # ic(combo_infilea)
        # ic(combo_infilea)

        # print(f'pdf_save_file: {pdf_save_file}')
        try:
            # ic(pdf_save_file)
            with open(pdf_save_file, 'wb') as save_file:
                save_file.write(pdf_contents)
        except FileNotFoundError:
            print(f'unable to save file: {pdf_save_file}')

        try:
            # ic(combo_infilea)
            with open(combo_infilea, 'wb') as save_file:
                save_file.write(pdf_contents)
        except FileNotFoundError:
            print(f'unable to save file: {combo_infilea}')

        # self.refresh_pdf_infiles_listing()

    # @pn_log.pn_timer
    def refreshPdfInfilesListing(self):
        row = 0
        pdf_infiles_list = self.pdfInfilesListing()

        # pdf_infiles_listing
        # print(f's_lst: {s_lst}')
        for in_file in pdf_infiles_list:
            switch_name = customtkinter.CTkSwitch(master=self.file_list_scrollable_frame, text=f"{in_file}")
            switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
            row += 1
            self.file_list_scrollable_frame_switches.append(switch_name)
        # print(f'switches: {self.f_scrollable_frame_switches}')

    # @pn_log.pn_timer
    def pdfInfilesListing(self):
        listing = self.pdf_t.pdf_infiles_listing()
        # print(f'pdf_infiles_listing:listing: {listing}')
        # self.display_listing(listing)
        return listing

    # @pn_log.pn_timer
    def genPdfPagesFromAllInfiles(self):
        # ic(f'\nXXX:gen_pdf_pages_from_all_infiles')

        # get selection
        row = 0

        pdf_infiles_list = self.pdfInfilesListing()
        # ic(pdf_infiles_list)

        selection = []
        row = 0
        for infile in pdf_infiles_list:
            # select ALL
            is_set = 1
            # is_set = self.file_list_scrollable_frame_switches[row].get()
            # print(f'is_set: {is_set} :: infile: {infile}')
            if is_set:
                # print(f'gen_pdf_pages_from_all_infiles: {infile}')
                selection.append(infile)
            row += 1

        # ic(selection)

        #TOD enforce as least one selection

        # for each of selection
            # split into pages & save to pdf_pages directory
        s_cnt = 0
        for pdf_infile in selection:
            pdf_file = f'{pdf_infile}'
            # ic(pdf_file)
            name_of_split = f'{pdf_file}'
            in_dir = PDF_INFILES
            out_dir = PDF_PAGES_DIR
            # ic(pdf_file)

            self.pdf_t.split_pdf_infiles_2_pages(
                pdf_file,
                f'{name_of_split}',
                in_dir,
                out_dir
            )

            # self.pdf_pages_refresh()

    @pn_log.pn_timer
    def appMgrOnCancel(self):
        self.quit()

    # @pn_log.pn_timer
    def dummyFunc(self):
        ic('in dummy_func()')
