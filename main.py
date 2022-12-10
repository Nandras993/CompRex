import PySimpleGUI as sg
import functions

sg.theme_background_color("#fcc200")
sg.theme_text_color("black")
sg.theme_text_element_background_color("#fcc200")
sg.theme_button_color("#85754e")

output_type_label = sg.Text("Archive extension: ", font="times")

label_comp = sg.Text("Select files to compress:  ", font="times")
input_comp = sg.Input(key="input1", font="times")
button_comp = sg.FilesBrowse("Choose", tooltip="To select more than one file, "
                                               "press and hold ctrl while clicking"
                                               " on the files with your left mouse button.",
                             key='files', enable_events=True, font="times")

label_comp2 = sg.Text("Select destination folder:  ", font="times")
input_comp2 = sg.Input(key="input2", font="times")
button_comp2 = sg.FolderBrowse("Choose", tooltip="Choose the destination for the archive.",
                               key="folder", font="times")
type_label1 = sg.Radio(".zip", group_id="comp", default=True, key="zip", background_color="#fcc200", font="times")
type_label2 = sg.Radio(".7z", group_id="comp", default=False, key="7z", background_color="#fcc200", font="times")

compress_button = sg.Button("Compress", font="times")
output_label = sg.Text(key="output", font="times")

#back_button_comp = sg.Button("Back", size=30, key="backt_comp", pad=((20, 0), (0, 0)), button_color="#85754e", font="times")
###############################################################################################################

label_ext = sg.Text("Select archive to extract:", font="times")
input_ext = sg.Input(key="input_ext1", font="times")
button_ext = sg.FileBrowse("Choose", tooltip="Select an archive(.zip, .7z, .rar)",
                           key='archive', enable_events=True, font="times")

label_ext2 = sg.Text("Select destination folder:", font="times")
input_ext2 = sg.Input(key="input_ext2", font="times")
button__ext2 = sg.FolderBrowse("Choose", tooltip="Choose the destination of the extraction.",
                               key="folder_ext", font="times")

ext_button = sg.Button("Extract", key='extract', font="times")
output_label_ext = sg.Text(key="extraction_output", font="times")

#back_button_ext = sg.Button("Back", size=30, key="back_ext", pad=((20, 0), (0, 0)), button_color="#85754e", font="times")
#######################################################################################################

col_left1 = sg.Column([[sg.Image("files/trex_pixelart.png", background_color="#fcc200", size=(300, 300))]])

col_left2 = sg.Column([[sg.Image("files/trex_pixelart.png", background_color="#fcc200", size=(300, 300))]])

col_middle = sg.Column([[label_comp, input_comp, button_comp], [label_comp2, input_comp2, button_comp2],
                        [output_type_label, type_label1, type_label2],
                        [compress_button, output_label]])
col_middle2 = sg.Column([[label_ext, input_ext, button_ext],
                         [label_ext2, input_ext2, button__ext2], [ext_button, output_label_ext]])

########################################################################################################

label_start = sg.Text("Which talent of mine you require master?", pad=((35, 0), (0, 0)), font="times")
choose_comp = sg.Radio("Compress files", group_id="start", default=True, key="comp_start", pad=((35, 0), (0, 0)),
                       background_color="#fcc200", font="times")
choose_ext = sg.Radio("Extract archives", group_id="start", default=False, key="ext_start",
                      background_color="#fcc200", font="times")
start_button = sg.Button("Start", size=30, key="start", pad=((20, 0), (0, 0)), button_color="#85754e", font="times")
exit_button_s = sg.Button("Exit", size=30, key='exit_s', pad=((20, 0), (0, 0)), button_color="#85754e", font="times")
start_image = sg.Image("files/trex_pixelart.png", background_color="#fcc200", size=(300, 300))

start_column = sg.Column([[start_image], [label_start], [choose_comp, choose_ext], [start_button], [exit_button_s]])

start_window = sg.Window("CompRex", layout=[[start_column]])

window = sg.Window("CompREX", layout=[[col_left1, col_middle]])

window_ext = sg.Window("CompREX", layout=[[col_left2, col_middle2]])

while True:
    event, values = start_window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == "exit_s":
        break
    if values['comp_start'] == True:
        start_window.close()
        while True:
            event, values = window.read()
            print(event, values)
            filepaths = values['files'].split(";")
            folder = values['folder']

            if values['zip'] == True:
                functions.make_zip(filepaths, folder)
                window['input1'].update(value="")
                window['input2'].update(value="")
                window["output"].update(value="Compression completed!")
                window.read(timeout=2000)
                window["output"].update(value="Waiting for file/files to compress")

            elif values['7z'] == True:
                functions.make_7z(filepaths, folder)
                window['input1'].update(value="")
                window['input2'].update(value="")
                window["output"].update(value="Compression completed!")
                window.read(timeout=2000)
                window["output"].update(value="Waiting for files to compress")

            if event == sg.WIN_CLOSED or event == "Exit":
                break
        window.close()
    else:
        start_window.close()
        window.close()
        while True:
            event, values = window_ext.read()
            print(event, values)
            archive_path = values['archive']
            dest_dir = values['folder_ext']

            if values['archive'].find('.zip') > 0:
                functions.extract_zip(archive_path, dest_dir)
                window_ext['input_ext1'].update(value="")
                window_ext['input_ext2'].update(value="")
                window_ext['extraction_output'].update(value="Extraction completed master!")
                window_ext.read(timeout=2000)
                window_ext["extraction_output"].update(value="Waiting for archive to extract")
            elif values['archive'].find('.7z') > 0:
                functions.extract_7z(archive_path, dest_dir)
                window_ext['input_ext1'].update(value="")
                window_ext['input_ext2'].update(value="")
                window_ext['extraction_output'].update(value="Extraction completed master!")
                window_ext.read(timeout=2000)
                window_ext["extraction_output"].update(value="Waiting for archive to extract")
            else:
                functions.extract_rar(archive_path, dest_dir)
                window_ext['input_ext1'].update(value="")
                window_ext['input_ext2'].update(value="")
                window_ext['extraction_output'].update(value="Extraction completed master!")
                window_ext.read(timeout=2000)
                window_ext["extraction_output"].update(value="Waiting for archive to extract")

            if event == sg.WIN_CLOSED or event == "Exit":
                break
        window_ext.close()

start_window.close()
