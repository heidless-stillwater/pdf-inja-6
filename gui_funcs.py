

####################################
# utiities
#

def combo_infiles_refresh(self):
    ic(f'combo_infiles_refresh')
    # self.combo_sort_infiles_listing_frame.grid_columnconfigure(0, weight=1)
    # self.combo_sort_listing_frame_switches = []
    row = 0

    combo_infiles_lst = self.comboInfilesListing()

    #
    # # print(f'combo_infiles_refresh:combo_infiles_lst: {combo_infiles_lst}')
    # for combo_infile in combo_infiles_lst:
    #     # print(f'combo_infiles_refresh:combo_infile:{combo_infile}')
    #     switch_name = customtkinter.CTkSwitch(
    #         master=self.combo_infiles_listing_frame,
    #         text=f"{combo_infile}",
    #         fg_color='yellow',
    #     )

    for in_file in combo_infiles_lst:
        # print(f'combo_pages_refresh:combo:{combo}')
        switch_name = ttk.Checkbutton(
            master=self.combo_sort_infiles_listing_frame,
            text=f"{in_file}",
            fg_color='yellow',
        )
        switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
        row += 1
        self.combo_sort_infiles_listing_frame_switches.append(switch_name)

    # print(f'switches: {self.scrollable_frame_switches}')
    # print(f'pages_refresh:switches: switch complete')
    # print(f'pages_refresh:c_lst: {c_lst}')
    return combo_infiles_lst


def combo_infiles_listing(self):
    listing = self.pdf_t.comboInfilesListing()
    # print(f'combo_infiles_listing:listing: {listing}')
    self.supportDisplayListing(listing)
    return listing


# action when user clicks cancel
def app_mgr_on_cancel(self):
    self.quit()


def dummy_func(self):
    ic('in dummy_func()')

