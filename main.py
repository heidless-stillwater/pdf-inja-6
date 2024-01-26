import ttkbootstrap as ttk
from gui_utils import PdfNinja

import os
from icecream import ic
from PIL import Image, ImageTk

if __name__ == '__main__':
    print(f'starting: {os.getcwd()}')

    # app = ttk.Window('GradeBook', 'superhero', resizeable=(False, False))

    app = ttk.Window('PDF Ninja', 'superhero')

    app.geometry(f'1600x1000+300+10')

    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)

    PdfNinja(app)

    # GradeBook(app)

    app.mainloop()








