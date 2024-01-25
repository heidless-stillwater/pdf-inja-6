from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import os
from constants import *
from icecream import ic

#
#
# PDF_FILES = './pdf_files'
# PDF_IMG_DIR = './pdf_files/pdf_images'

NOTHING_SELECTED = 'NOTHING_SELECTED'

class PdfToolbox:

    def __init__(self):
        self.dir_listing = self.list_pdf_dir()
        # print(f'in PdfToolbox dir_listing: {self.dir_listing}')

    def list_pdf_dir(self):
        # print(f'in PdfToolbox.list_pdf_dir')
        print(f'in list_pdf_dir: {os.getcwd()}')
        print(f'PDF_INFILES: {PDF_INFILES}')

        # ignore directories
        dir_contents = [f for f in os.listdir(PDF_INFILES) if os.path.isfile(os.path.join(PDF_INFILES, f))]
        # print(f'pdf_toolbox;list_pdf_dir:dir_contents: {dir_contents}')

        file_text = ''
        listing = []
        index = 1
        for file_name in dir_contents:
            # print(f'file_name: {file_name}')
            file_text += f'{file_name}\n'
            listing.append(file_name)
            # UserInterface.dir_listing.insert(index, file_name)
            index += 1
        # print(f'listing: {listing}')
        return listing

    def pdf_infiles_listing(self):
        # print(f'in PdfToolbox.list_pdf_dir')

        # ignore directories
        dir_contents = [f for f in os.listdir(PDF_INFILES) if os.path.isfile(os.path.join(PDF_INFILES, f))]
        # print(f'pdf_toolbox;list_pdf_dir:dir_contents: {dir_contents}')

        file_text = ''
        listing = []
        index = 1
        for file_name in dir_contents:
            # print(f'file_name: {file_name}')
            file_text += f'{file_name}\n'
            listing.append(file_name)
            # UserInterface.dir_listing.insert(index, file_name)
            index += 1
        # print(f'listing: {listing}')
        return listing

    def combo_infiles_listing(self):
        # print(f'in PdfToolbox.list_pdf_dir')

        # ignore directories
        dir_contents = [f for f in os.listdir(COMBO_INFILES_DIR) if os.path.isfile(os.path.join(COMBO_INFILES_DIR, f))]
        # ic(dir_contents)

        # print(f'combo_infiles_listing:dir_contents: {dir_contents}')

        file_text = ''
        listing = []
        index = 1
        for file_name in dir_contents:
            # print(f'file_name: {file_name}')
            file_text += f'{file_name}\n'
            listing.append(file_name)
            # UserInterface.dir_listing.insert(index, file_name)
            index += 1
        # print(f'listing: {listing}')
        return listing

    def list_pages_dir(self, combo_name):
        # ic(combo_name)
        #
        # print(f'pdf_t:.list_pages_dir')

        # ignore directories
        dir_contents = [f for f in os.listdir(PAGES_DIR) if os.path.isfile(os.path.join(PAGES_DIR, f))]
        # ic(combo_name, dir_contents)

        # print(f'pdf_toolbox:list_pdf_dir:dir_contents: {dir_contents}')

        file_text = ''
        listing = []
        index = 1
        for file_name in dir_contents:
            # print(f'file_name: {file_name}')
            file_text += f'{file_name}\n'
            listing.append(file_name)
            # UserInterface.dir_listing.insert(index, file_name)
            index += 1
        # print(f'listing: {listing}')
        return listing

    def list_combo_pages_dir(self):
        # print(f'in PdfToolbox.list_pdf_dir')

        # ignore directories
        dir_contents = [f for f in os.listdir(COMBO_PAGES_DIR) if os.path.isfile(os.path.join(COMBO_PAGES_DIR, f))]

        # ic(dir_contents)

        # print(f'pdf_toolbox;list_pdf_dir:dir_contents: {dir_contents}')

        file_text = ''
        listing = []
        index = 1
        for file_name in dir_contents:
            # print(f'file_name: {file_name}')
            file_text += f'{file_name}\n'
            listing.append(file_name)
            # UserInterface.dir_listing.insert(index, file_name)
            index += 1
        # print(f'listing: {listing}')
        return listing

    def list_combo_images_dir(self):
        # print(f'in PdfToolbox.list_combo_images_dir')

        # ignore directories
        dir_contents = [f for f in os.listdir(COMBO_IMAGES_DIR) if os.path.isfile(os.path.join(COMBO_IMAGES_DIR, f))]
        # print(f'pdf_toolbox;list_pdf_dir:dir_contents: {dir_contents}')

        file_text = ''
        listing = []
        index = 1
        for file_name in dir_contents:
            # print(f'file_name: {file_name}')
            file_text += f'{file_name}\n'
            listing.append(file_name)
            # UserInterface.dir_listing.insert(index, file_name)
            index += 1
        # print(f'listing: {listing}')
        return listing

    def list_images_dir(self):
        # print(f'in PdfToolbox.list_pdf_dir')

        # ignore directories
        dir_contents = [f for f in os.listdir(PDF_IMG_DIR) if os.path.isfile(os.path.join(PDF_IMG_DIR, f))]
        # print(f'pdf_toolbox;list_pdf_dir:dir_contents: {dir_contents}')

        file_text = ''
        listing = []
        index = 1
        for file_name in dir_contents:
            # print(f'file_name: {file_name}')
            file_text += f'{file_name}\n'
            listing.append(file_name)
            # UserInterface.dir_listing.insert(index, file_name)
            index += 1
        # print(f'images listing: {listing}')
        return listing

    def list_combo_dir(self):
        # print(f'in PdfToolbox.list_pdf_dir')

        # ignore directories
        dir_contents = [f for f in os.listdir(COMBO_INFILES_DIR) if os.path.isfile(os.path.join(COMBO_INFILES_DIR, f))]
        # print(f'pdf_toolbox:list_combo_dir:COMBO_INFILES_DIR: {COMBO_INFILES_DIR}')
        # print(f'pdf_toolbox:list_combo_dir:dir_contents: {dir_contents}')

        file_text = ''
        listing = []
        index = 1
        for file_name in dir_contents:
            # file_name = f'{COMBO_INFILES_DIR}/{file_name}'
            # print(f'pdf_toolbox:list_combo_dir:file_name: {file_name}')
            file_text += f'{file_name}\n'
            listing.append(file_name)
            # UserInterface.dir_listing.insert(index, file_name)
            index += 1
        # print(f'COMBO DIR:listing: {listing}')
        # print(f'pdf_toolbox:list_combo_dir:listing: {listing}')

        return listing

    def list_combo_combo_dir(self):
        # print(f'in PdfToolbox.list_pdf_dir')

        # ignore directories
        dir_contents = [f for f in os.listdir(COMBO_COMBO_DIR) if os.path.isfile(os.path.join(COMBO_COMBO_DIR, f))]
        # print(f'pdf_toolbox;list_pdf_dir:dir_contents: {dir_contents}')

        file_text = ''
        listing = []
        index = 1
        for file_name in dir_contents:
            # print(f'file_name: {file_name}')
            file_text += f'{file_name}\n'
            listing.append(file_name)
            # UserInterface.dir_listing.insert(index, file_name)
            index += 1
        # print(f'COMBO DIR:listing: {listing}')
        return listing

    def list_combo_combo_pages_dir(self):
        # print(f'in PdfToolbox.list_pdf_dir')

        # ignore directories
        dir_contents = [f for f in os.listdir(COMBO_PAGES_DIR) if os.path.isfile(os.path.join(COMBO_PAGES_DIR, f))]
        # print(f'pdf_toolbox;list_pdf_dir:dir_contents: {dir_contents}')

        file_text = ''
        listing = []
        index = 1
        for file_name in dir_contents:
            # print(f'file_name: {file_name}')
            file_text += f'{file_name}\n'
            listing.append(file_name)
            # UserInterface.dir_listing.insert(index, file_name)
            index += 1
        print(f'list_combo_combo_pages_dir:listing: {listing}')
        return listing

    def list_combo_pages_dir(self):
        # print(f'in PdfToolbox.list_pdf_dir')

        # ignore directories
        dir_contents = [f for f in os.listdir(COMBO_PAGES_DIR) if os.path.isfile(os.path.join(COMBO_PAGES_DIR, f))]
        # print(f'pdf_toolbox;list_pdf_dir:dir_contents: {dir_contents}')
        # print(f'pdf_t:list_combo_pages_dir:COMBO_PAGES_DIR: {COMBO_PAGES_DIR}: dir_contents: {dir_contents}')

        file_text = ''
        listing = []
        index = 1
        for file_name in dir_contents:
            # print(f'file_name: {file_name}')
            file_text += f'{file_name}\n'
            listing.append(file_name)
            # UserInterface.dir_listing.insert(index, file_name)
            index += 1
        # print(f'listing: {listing}')
        return listing

    def list_combo_infiles_dir(self):
        # print(f'in PdfToolbox.list_pdf_dir')

        # ignore directories
        dir_contents = [f for f in os.listdir(COMBO_INFILES_DIR) if os.path.isfile(os.path.join(COMBO_INFILES_DIR, f))]
        # print(f'pdf_toolbox;list_pdf_dir:dir_contents: {dir_contents}')
        # print(f'pdf_t:list_combo_pages_dir:COMBO_PAGES_DIR: {COMBO_PAGES_DIR}: dir_contents: {dir_contents}')

        file_text = ''
        listing = []
        index = 1
        for file_name in dir_contents:
            # print(f'file_name: {file_name}')
            file_text += f'{file_name}\n'
            listing.append(file_name)
            # UserInterface.dir_listing.insert(index, file_name)
            index += 1
        # print(f'listing: {listing}')
        return listing

    def list_combo_combo_infiles_dir(self):
        # print(f'in PdfToolbox.list_combo_combo_infiles_dir')
        # ignore directories
        dir_contents = [f for f in os.listdir(COMBO_INFILES_DIR) if os.path.isfile(os.path.join(COMBO_INFILES_DIR, f))]
        # print(f'list_combo_combo_infiles_dir:COMBO_INFILES_DIR: {COMBO_INFILES_DIR}')
        # print(f'pdf_toolbox;list_pdf_dir:dir_contents: {dir_contents}')
        # print(f'pdf_t:list_combo_pages_dir:COMBO_PAGES_DIR: {COMBO_PAGES_DIR}: dir_contents: {dir_contents}')

        file_text = ''
        listing = []
        index = 1

        print(f'4:list_combo_combo_infiles_dir:dir_contents: {dir_contents}')
        for file_name in dir_contents:
            print(f'5:list_combo_combo_infiles_dir:file_name: {file_name}')
            file_text += file_name
            listing.append(file_name)
            # UserInterface.dir_listing.insert(index, file_name)
            index += 1
        print(f'6:list_combo_combo_infiles_dir listing: {listing}')
        # print(f'7:list_combo_combo_infiles_dir:listing[0]: {listing[0]}')

        return listing
    #
    # def split_combo_pdf_into_pages(self, pdf_file, name_of_split, in_dir, out_dir):
    #     print(f'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx: ############### in pdf_t:split_combo_pdf_into_pages')
    #     # print(f'split_combo_pdf_into_pages:pdf_file: {pdf_file}')
    #     # print(f'split_combo_pdf_into_pages:name_of_split: {name_of_split}')
    #     # print(f'split_combo_pdf_into_pages:in_dir: {in_dir}')
    #     # print(f'split_combo_pdf_into_pages:out_dir: {out_dir}')
    #     in_dir = COMBO_INFILES_DIR
    #     print(f'############## in_dir: {in_dir}')
    #     pdf_path = f'{in_dir}/{pdf_file}'
    #     print(f'split_combo_pdf_into_pages:pdf_path: {pdf_path}')
    #     with open(pdf_path, 'rb') as f:
    #         # print(f'0: opening file')
    #         pdf = PdfFileReader(f)
    #         information = pdf.getDocumentInfo()
    #         number_of_pages = pdf.getNumPages()
    #         # print(f'x: number_of_pages: {number_of_pages}')
    #
    #         for page in range(number_of_pages):
    #             # print(f'1:processing page: {page}')
    #             pdf_writer = PdfFileWriter()
    #             pdf_writer.addPage(pdf.getPage(page))
    #
    #             output = f'{out_dir}/{name_of_split}{page}.pdf'
    #             print(f'split_pdf_into_pages:output: {output}')
    #
    #             with open(output, 'wb') as output_pdf:
    #                 pdf_writer.write(output_pdf)

    def split_pdf_infiles_2_pages(self, pdf_file, name_of_split, in_dir, out_dir):
        # out_dir = PAGES_DIR
        # print(f'pdf_t:split_pdf_infiles_2_pages:pdf_file: {pdf_file}')
        # print(f'pdf_t:split_pdf_infiles_2_pages:name_of_split: {name_of_split}')
        # print(f'pdf_t:split_pdf_infiles_2_pages:in_dir: {in_dir}')
        # print(f'pdf_t:split_pdf_infiles_2_pages:out_dir: {out_dir}')
        # in_dir = COMBO_INFILES_DIR
        # print(f'split_pdf_infiles_2_pages:in_dir: {in_dir}')
        pdf_path = f'{in_dir}/{pdf_file}'
        # ic(pdf_path)

        with open(pdf_path, 'rb') as f:
            # print(f'0: opening file')
            pdf = PdfFileReader(f, strict=False)
            information = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()
            # ic(number_of_pages)

            page_index = 0
            for page in range(number_of_pages):
                # print(f'1:processing page: {page}')
                pdf_writer = PdfFileWriter()
                pdf_writer.addPage(pdf.getPage(page))

                output = f'{out_dir}/{name_of_split}-{page_index}'
                page_index += 1
                # ic(output, page_index)

                with open(output, 'wb') as output_pdf:
                    pdf_writer.write(output_pdf)

    def split_combo_infiles_2_pages(self, pdf_file, name_of_split, in_dir, out_dir):
        # print(f'pdf_t:split_combo_infiles_2_pages:pdf_file: {pdf_file}')
        # print(f'pdf_t:split_combo_infiles_2_pages:name_of_split: {name_of_split}')
        # print(f'pdf_t:split_combo_infiles_2_pages:in_dir: {in_dir}')
        # print(f'pdf_t:split_combo_infiles_2_pages:out_dir: {out_dir}')
        # in_dir = COMBO_INFILES_DIR

        pdf_path = f'{in_dir}/{pdf_file}'
        # ic(in_dir, pdf_file, pdf_path)

        # print(f'split_combo_infiles_2_pages:pdf_path: {pdf_path}')
        with open(pdf_path, 'rb') as f:
            # print(f'0: opening file')
            pdf = PdfFileReader(f)
            information = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()
            # print(f'x: number_of_pages: {number_of_pages}')

            pg_indx = 0
            for page in range(number_of_pages):
                # print(f'1:processing page: {page}')
                pdf_writer = PdfFileWriter()
                pdf_writer.addPage(pdf.getPage(page))

                output = f'{out_dir}/{name_of_split}-{pg_indx}'
                pg_indx += 1

                # ic(output)

                with open(output, 'wb') as output_pdf:
                    pdf_writer.write(output_pdf)

    def split_pdf_into_pages(self, in_dir, pdf_file, name_of_split):
        print(f'split_pdf_into_pages:pdf_file: {pdf_file}')
        pdf_path = f'{in_dir}/{pdf_file}'
        print(f'split_pdf_into_pages:xxx:pdf_path: {pdf_path}')
        with open(pdf_path, 'rb') as f:
            pdf = PdfFileReader(f)
            information = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()

            for page in range(number_of_pages):
                print(f'split_pdf_into_pages:page: {page}')
                pdf_writer = PdfFileWriter()
                pdf_writer.addPage(pdf.getPage(page))

                output = f'{PAGES_DIR}/{name_of_split}'
                print(f'split_pdf_into_pageszzz:output: {output}')

                with open(output, 'wb') as output_pdf:
                    pdf_writer.write(output_pdf)

    def split_combo_pdf_into_pages(self, in_dir, pdf_file, name_of_split, out_dir):
        print(f'in split_combo_pdf_into_pages')
        print(f'split_combo_pdf_into_pages:in_dir: {in_dir}')
        pdf_path = f'{in_dir}/{pdf_file}'
        print(f'pdf_path: {pdf_path}')
        with open(pdf_path, 'rb') as f:
            pdf = PdfFileReader(f)
            information = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()

            for page in range(number_of_pages):
                pdf_writer = PdfFileWriter()
                pdf_writer.addPage(pdf.getPage(page))

                output = f'{COMBO_PAGES_DIR}/{name_of_split}'
                # print(f'################################# split_combo_pdf_into_pages:output: {output}')
                # print(f'split_pdf_into_pages:output: {output}')

                with open(output, 'wb') as output_pdf:
                    pdf_writer.write(output_pdf)

    def extract_information(self, pdf_file):
        # print(f'pdf_t:extract_information')
        pdf_path = f'{PDF_FILES}/{pdf_file}'
        # print(f'extract_information:pdf_path: {pdf_path}')
        if pdf_path == NOTHING_SELECTED:
            information = pdf_path
        else:
            with open(pdf_path, 'rb') as f:
                pdf = PdfFileReader(f)
                information = pdf.getDocumentInfo()
                number_of_pages = pdf.getNumPages()

            txt = f"""
            Information about {pdf_path}:
    
            Author: {information.author}
            Creator: {information.creator}
            Producer: {information.producer}
            Subject: {information.subject}
            Title: {information.title}
            Number of pages: {number_of_pages}
            """
            information = txt
            # print(txt)
        return information

    def merge_files(self, m_lst, o_file):
        # print(f'pdf_t:merge_files:m_lst: {m_lst}: o_file: {o_file}')

        merger = PdfFileMerger()
        listing = m_lst

        for pdf in listing:
            pdf = f'{PAGES_DIR}/{pdf}'
            # print(f'pdf_t:merge_files:pdf: {pdf}')
            merger.append(pdf)

        # target = f"{COMBO_INFILES_DIR}/{o_file}"
        target = f"{o_file}"
        # ic(o_file)
        ic(target)
        merger.write(target)
        merger.close()
