import tkinter as tk
from tkinter import ttk
import xml.etree.cElementTree as ET
from xlwt import Workbook
import xlwt
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import xlrd
import xlsxwriter
import os
from tkinter.messagebox import showwarning, showinfo
import logging
import time
#wb = Workbook()
global OPTIONS
OPTIONS = ["Expresspay", "    C4    "]
OPTIONS_P = ["Expresspay", "    C4    "]
global profile_list
profile_list = []
global Lib_name
Lib_name = "Expresspay"
#style = xlwt.XFStyle()

# borders
#borders = xlwt.Borders()
#borders.bottom = xlwt.Borders.DASHED
#style.borders = borders
lib_selection_inc = 0

logging.basicConfig(filename="logfile.log", level=logging.ERROR)

def lib_selection(lib_name_option):

    global sheet1
    global Lib_name
    Lib_name = lib_name_option
    if not Lib_name:
        Lib_name_raw.set(OPTIONS[0])
        Lib_name = Lib_name_raw.get()

def lib_selection_p (lib_name_option_p):

    global sheet1
    global Lib_name_p
    Lib_name_p = lib_name_option_p
    if not Lib_name_p:
        Lib_name_p_raw.set(OPTIONS.P[0])
        Lib_name_p = Lib_name_p_raw.get()

def output_path():
    output_location = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                 filetypes=(("XML Files", "*.xml"), ("all files", "*.*")))
    # output_label_1.configure(text=output_location)
    # output_label_1.update()
    # print(output_location)
    if not output_location.endswith('.xml') or not output_location:
        showwarning('Select Output XML', 'Please select correct output XML file')
        logging.error('Output(Amex) XML file error')
    global a
    a = output_location
    output_path_raw.set(a)

def input_path1():
    input1_location = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                 filetypes=(("XML Files", "*.xml"), ("all files", "*.*")))
    # input1_label_1.configure(text=input1_location)
    # input1_label_1.update()
    if not input1_location.endswith('.xml') or not input1_location:
        showwarning('Select Common XML', 'Please select correct common XML file')
        logging.error('Common (tool) XML file error')
    global b
    b = input1_location
    input1_path_raw.set(b)

def input_path2():
    input2_location = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                 filetypes=(("XML Files", "*.xml"), ("all files", "*.*")))
    # input2_label_1.configure(text=input2_location)
    # input2_label_1.update()
    if not input2_location.endswith('.xml') or not input2_location:
        showwarning('Select XP/C4 XML', 'Please select correct XP/C4 XML file')
        logging.error(' XP/C4 (tool) XML file error')
    global c
    c = input2_location
    input2_path_raw.set(c)

def clear():

    #Lib_name_raw.set('')
    #lib_menu['menu'].delete(0, 'end')
    save_name_Label.delete(0, 'end')
    save_name = ' '
    a = ' '
    b = ' '
    c = ' '
    save_directory = ' '
    output_number.configure(text=' ')
    input_number.configure(text=' ')
    Result_Display.configure(text='')
    list_output.delete(0, 'end')
    list_input.delete(0, 'end')
    list_mismatch.delete(0, 'end')
    input1_path_raw.set('')
    input2_path_raw.set('')
    output_path_raw.set('')
    save_path_raw.set('')
    progress.destroy()

def save_path():
    global save_name
    save_name = save_name_raw.get()
    if not save_name:
        showwarning('File Name', 'Please give file name')
        logging.error('File name is not valid')
    global wb
    wb = Workbook(save_name)
    #print(save_name)
    global save_directory
    save_directory = filedialog.askdirectory()
    if not save_directory:
        showwarning('Folder Select', 'Please select correct Folder ')
        logging.error('Selected folder is not valid')
    save_path_raw.set(save_directory)

def back():
    window.destroy()

def file_check():

    try:
        if a and b and c and save_name and save_directory:
            check = 123
        return True
    except:
        showwarning('Wrong Input Files/Folder', 'Please select all the files and re-execute the test ')
        logging.error('Files are not valid')
        raise
        return false

def compare():

    profile_list = []
    file_check()
    sheet1 = wb.add_sheet(Lib_name, cell_overwrite_ok=True)
    global progress
    #s = ttk.Style()
    #s.theme_use("default")
    #s.configure("TProgressbar", thickness=50)
    #pb = ttk.Progressbar(root, style="TProgressbar")
    progress = ttk.Progressbar(window, orient=HORIZONTAL, length=1200, mode='determinate')
    progress.place(x=140, y=677)
    # progress.update(value =20)
    # print(a,b,c,save_name,save_directory)


    # if not a and not b and not c and not save_name and not save_directory:
    #    showwarning('Files selection', 'Please select all the files and re-execute the test  ')

    tree1 = ET.parse(a)
    tree2 = ET.parse(b)
    tree3 = ET.parse(c)
    root1 = tree1.getroot()
    root2 = tree2.getroot()
    root3 = tree3.getroot()
    progress['value'] = 10
    progress.update ()
    # ttk.update_idletasks()
    # time.sleep(1)
    # ICS_Lib = input('Please Enter library name ')
    # ICS_Num = input('Please enter ICS number')

    j = 1
    l = 0
    n = 1
    z = 2
    output_profile = 0
    input_profile = 0
    # output_list = []
    number1 = 1
    number2 = 1
    g = 0
    f = 0

    progress['value'] = 20
    progress.update()


    style = xlwt.easyxf('pattern: pattern solid, fore_colour purple_ega;' 'font: colour white, bold True ,height 220;' 'align: horiz center;' 'borders: top_color black, bottom_color black, right_color black, left_color black,left thin, right thin, top thin, bottom thin;')

    style_cell = xlwt.easyxf(' borders: top_color black, bottom_color black, right_color black, left_color black,left thin, right thin, top thin, bottom thin;')

    style_cell_mis = xlwt.easyxf('pattern: pattern solid,fore_colour yellow;''borders: top_color black, bottom_color black, right_color black, left_color black,left thin, right thin, top thin, bottom thin;')

    for row_border in range(0,1000):

        for coln_border in range(0,100):

           sheet1.write(row_border,coln_border, style= style_cell)

    for child1 in root1:

        if child1.attrib.get('Applicable') == 'true':
            output_profile_number = str(number1) + ' . Profile '
            output_profile_number = output_profile_number + ' ' + child1.attrib['Id']
            profile_list.append(output_profile_number)
            list_output.insert(g, '     ' + output_profile_number)
            g += 1
            # output_list.append(output_profile_number)
            output_profile = output_profile + 1
            # print("Profile", child1.attrib['Id'])
            i = 0
            first_op = 'Output Profile' + ' ' + child1.attrib['Id'] + ' (AMEX)'
            sheet1.write(i, j, first_op,style=style)
            sheet1.write(0, j + 1, 'Mismatches',style=style)
            number1 += 1
            # print(child.attrib['Applicable'])
            for sibling1 in child1:
                i += 1
                # print(sibling1.attrib['Id'])
                second_op = sibling1.attrib['Id']
                sheet1.write(i, j, second_op,style=style_cell)
            j += 3

    # print(output_list)
    # input_display_label.configure(text=output_list + '\n')
    # First input tree (Common)
    progress['value'] = 30
    progress.update()
    for child2 in root2:
        if child2.attrib.get('Applicable') == 'true':
            input_profile_number = str(number2) + ' . Profile '
            input_profile_number = input_profile_number + ' ' + child2.attrib['Id']
            list_input.insert(f, '     ' + input_profile_number)
            f += 1
            number2 += 1
            input_profile = input_profile + 1
            # print("Profile", child2.attrib['Id'])
            k = 0
            first_ip1 = 'Input Profile' + ' ' + child2.attrib['Id'] + ' (EVAL Tool)'
            sheet1.write(k, l, first_ip1,style=style)

            # print(child.attrib['Applicable'])
            for sibling2 in child2:
                k += 1
                # print(sibling2.attrib['Id'])
                second_ip1 = sibling2.attrib['Id']
                sheet1.write(k, l, second_ip1,style=style_cell)

            # Second Input tree (XP or C4)
            input_profile_2 = 0
            for child3 in root3:
                if child3.attrib.get('Applicable') == 'true':
                    input_profile_2 = input_profile_2 + 1
                    first_ip2 = 'Input Profile' + ' ' + child3.attrib['Id'] + ' (EVAL Tool)'
                    # print(child.attrib['Applicable'])
                    if first_ip1 == first_ip2:
                        for sibling3 in child3:
                            k += 1
                            # print(sibling3.attrib['Id'])
                            second_ip2 = sibling3.attrib['Id']
                            sheet1.write(k, l, second_ip2,style=style_cell)
            l += 3

    progress['value'] = 50
    progress.update()
    # ttk.update_idletasks()
    # time.sleep(1)
    # print(input_profile)
    # print(input_profile_2)
    # progress['value'] = 50

    final_file_name = save_name + '.xls'
    # wb.save(save_path,final_file_name)
    # filedialog.askdirectory(mode = 'w', defaultextension = 'final_file_name'+'.txt')

    global no_output_profile
    no_output_profile = StringVar()
    no_output_profile = output_profile
    global no_input_profile
    no_input_profile = input_profile
    output_number.configure(text=no_output_profile)
    input_number.configure(text=no_input_profile)
    if output_profile == input_profile:
        # print('Applicable Input and Output profiles are equal.The number of applicale profiles',output_profile)
        output_number.configure(fg="green")
        input_number.configure(fg="green")
        number_of_columns = output_profile + 1
    else:
        output_number.configure(fg="red")
        input_number.configure(fg="red")
        progress.destroy()
        Result_Display.configure(text='FAIL', fg="red")
        logging.error('Output and Input XML profile Mismatch')
        showwarning('Output and Input XML profile Mismatch',
                    'Output profiles and input profiles are not matching.Please check final comparison result sheet')
        # print('Applicable Input and Output profiles are not equal.The number of input profile',input_profile,'The number of output profile',output_profile)

    if (input_profile != input_profile_2):
        list_input.delete(0, 'end')
        input_number.configure(fg="red")
        Result_Display.configure(text='FAIL', fg="red")
        progress.destroy()
        logging.error('Input XML files are not matching ')
        showwarning('XML File Mismatch',
                    'Common XML and XP/C4 XML files are not matching.Clear the screen and re excute the test with correct file')

    wb.save(save_directory + '/' + final_file_name)
    saved_file = save_directory + '/' + final_file_name

    progress['value'] = 60
    progress.update()
    # ttk.update_idletasks()
    # time.sleep(1)
    excel_path = file = save_directory + '/' + final_file_name

    # print(excel_path)
    path_to_open = excel_path

    excel_path = file = path_to_open

    excel_file = xlrd.open_workbook(excel_path)

    excel_write_path = xlsxwriter.Workbook(excel_path)

    sheet = excel_file.sheet_by_index(0)

    sheet.cell_value(0, 0)

    number_of_rows = sheet.nrows

    count = 0
    write = 1
    count_1 = 0
    z = 0
    f = 0
    mismatch_count = 0

    progress['value'] = 70
    progress.update()
    # ttk.update_idletasks()
    # time.sleep(1)

    for d in range(1, number_of_columns):

        list_mismatch.insert(f, '    ' + profile_list[d - 1] + '\n')
        # print(f)
        f += 1
        write = 1
        out = 0
        fg_change1 = 0
        fg_change2 = 0
        for i in range(sheet.nrows):
            # print(sheet.cell_value(i, 0))
            z_first_value = sheet.cell_value(i, ((d - 1) * 3))
            count = 0
            for j in range(sheet.nrows):
                z_second_value = sheet.cell_value(j, ((d * 3) - 2))
                if (z_first_value != z_second_value):
                    count += 1
                    if (count == number_of_rows) and z_first_value:
                        # print(z_first_value)
                        # if (fg_change1 > 0):
                        #   list_mismatch.itemconfig(f, {'fg': 'red'})

                        if "Profile" not in z_first_value:
                            #if (z_first_value == 'MOD_CHECKSUM_01'):
                            sheet1.write(write, ((d * 3) - 1), z_first_value,style =style_cell_mis)
                            sheet1.write(i, ((d - 1) * 3), z_first_value, style=style_cell_mis)
                            #else:
                            #   sheet1.write(write, ((d * 3) - 1), z_first_value,style=style_cell)
                            # list_mismatch.itemconfig(f, {'fg': 'red'})
                            list_mismatch.insert(f, '    ' + z_first_value)
                            list_mismatch.itemconfig(f, {'fg': 'red'})
                            write += 1
                            fg_change1 += 1
                            # print(f)
                            f += 1
                        # print(z_first_value)

        for r in range(sheet.nrows):
            # print(sheet.cell_value(r, 1))

            y_first_value_1 = sheet.cell_value(r, ((d * 3) - 2))

            count = 0
            for s in range(sheet.nrows):
                y_second_value_1 = sheet.cell_value(s, ((d - 1) * 3))
                if (y_first_value_1 != y_second_value_1):
                    count += 1
                    if (count == number_of_rows) and y_first_value_1:
                        # print(y_first_value_1)

                        if (fg_change2 > 0):
                            list_mismatch.itemconfig(f, {'fg': 'red'})

                        if "Profile" not in y_first_value_1:

                            #if (y_first_value_1 == 'MOD_CHECKSUM_01'):
                            sheet1.write(write, ((d * 3) - 1), y_first_value_1,style=style_cell_mis)
                            sheet1.write(r, ((d * 3) - 2), y_first_value_1, style=style_cell_mis)
                            #else:
                            #   sheet1.write(write, ((d * 3) - 1), y_first_value_1,style =style_cell)

                            # if  (y_first_value_1 == "MOD_CHECKSUM_01"):
                            #    sheet1.write_comment(write, ((d * 3) - 1), y_first_value_1)
                            list_mismatch.insert(f, '    ' + y_first_value_1)
                            list_mismatch.itemconfig(f, {'fg': 'red'})
                            # print(f)
                            f += 1
                            fg_change2 += 1
                            write += 1

        if (write == 1):
            # print('out')
            list_mismatch.insert(f, '    ' + 'No mismatch')
            list_mismatch.itemconfig(f, {'fg': 'green'})
            f += 1
            sheet1.write(write, ((d * 3) - 1), 'No mismatch')
            mismatch_count += 1
        list_mismatch.insert(f, '------------------------------------------------------------------------')
        f += 1
        z += 3

    progress['value'] = 90
    progress.update()
    # ttk.update_idletasks()
    # time.sleep(1)

    profile_cal = no_output_profile
    print(mismatch_count)
    print(profile_cal)
    if (mismatch_count == profile_cal):
        Result_Display.configure(text='PASS', fg="Green")
    else:
        Result_Display.configure(text='FAIL', fg="red")

    # print(mismatch_count)

    wb.save(save_directory + '/' + final_file_name)
    progress['value'] = 100
    progress.update()
    # ttk.update_idletasks()
    # time.sleep(1)
    # final_save_location.write()
    # final_save_location.close()
    progress.destroy()
    showinfo('Result File', 'XML Comparison has been completed.Please take comparison file from ' + excel_path)

def testcase_path():
    testcase_location = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                 filetypes=(("XML Files", "*.xml"), ("all files", "*.*")))

    if not testcase_location.endswith('.xml') or not testcase_location:
        showwarning('Select Common XML', 'Please select correct XML file')
        logging.error('Common XML file error')
    global d
    d = testcase_location

def testcase_path_xp():
    testcase_location_xp = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                      filetypes=(("XML Files", "*.xml"), ("all files", "*.*")))

    if not testcase_location_xp.endswith('.xml') or not testcase_location_xp:
        showwarning('Select XP/C4 XML', 'Please select correct XML file')
        logging.error('XP/C4 XML file error')
    global w
    w = testcase_location_xp

def save_path_testcase():
    global save_name_testcase
    save_name_testcase = save_name_testcase_raw.get()
    if not save_name_testcase:
        showwarning('File Name', 'Please give file name')
        logging.error('File name is not valid')
    global wb
    wb = Workbook(save_name_testcase)
    global save_directory_testcase
    save_directory_testcase = filedialog.askdirectory()
    if not save_directory_testcase:
        showwarning('Folder Select', 'Please select correct Folder ')
        logging.error('Selected folder is not valid')

def clearing():

    Lib_name_raw.set(OPTIONS[0])
    save_name_Label_profile.delete(0,'end')
    save_name_tesecase = ' '
    d = ' '
    save_directory_tescase = ' '
    list_profile.delete(0, 'end')
    list_testcase.delete(0, 'end')

def exit_window():
    window.destroy()

def file_check_parse():

    try:
        if d and save_name_testcase and save_directory_testcase:
            check = 123
        return True
    except:
        logging.error('Wrong Input Files/Folder')
        showwarning('Wrong Input Files/Folder', 'Please select all the files and re-execute the test ')
        raise
        return false

def parsing():

    file_check_parse()
    sheet1 = wb.add_sheet(Lib_name_p, cell_overwrite_ok=True)
    tree = ET.parse(d)
    tree_xp = ET.parse(w)
    root = tree.getroot()
    root_xp = tree_xp.getroot()

    style = xlwt.easyxf('pattern: pattern solid, fore_colour purple_ega;' 'font: colour white, bold True ,height 220;' 'align: horiz center;' 'borders: top_color black, bottom_color black, right_color black, left_color black,left thin, right thin, top thin, bottom thin;')

    style_cell = xlwt.easyxf(' borders: top_color black, bottom_color black, right_color black, left_color black,left thin, right thin, top thin, bottom thin;')

    for row_border in range(0, 1000):

        for coln_border in range(0,42):
            sheet1.write(row_border, coln_border, style=style_cell)

    number1 = 1
    number2 = 1
    h = 0
    j = 0
    u =0
    for child in root:
        if child.attrib.get('Applicable') == 'true':
            profile_number = str(number1) + ' . Profile '
            profile_number = profile_number + ' ' + child.attrib['Id']
            list_profile.insert(h, '     ' + profile_number)
            h += 1
            number1 += 1
            i = 0
            first_op = 'Profile' + ' ' + child.attrib['Id']
            sheet1.write(i, j, first_op,style=style)
            testcase_count = 0
        # print(child.attrib['Applicable'])
            for sibling1 in child:
                i += 1
                # print(sibling1.attrib['Id'])
                second_op = sibling1.attrib['Id']
                sheet1.write(i, j, second_op,style_cell)
                testcase_count += 1
            # Second Input tree (XP or C4)

            for child_xp in root_xp:
                if child_xp.attrib.get('Applicable') == 'true':

                    first_op_xp = 'Profile' + ' ' + child_xp.attrib['Id']
                    # print(child.attrib['Applicable'])
                    if first_op == first_op_xp:
                        for sibling2 in child_xp:
                            i += 1
                            # print(sibling3.attrib['Id'])
                            second_op_xp = sibling2.attrib['Id']
                            sheet1.write(i, j, second_op_xp,style= style_cell)
                            testcase_count += 1
            j += 1

            list_testcase.insert(h, '                   ' + str(testcase_count))


    final_file_name = save_name_testcase + '.xls'
    parse_excel_path = save_directory_testcase + '/' + final_file_name
    wb.save(save_directory_testcase + '/' + final_file_name)
    showinfo('Result File', 'Profiles Parsing has been completed.Please take profiles file from ' + parse_excel_path)

def is_hex(str_str):

    try:
        int(str_str, 16)
        return True
    except ValueError :
        showwarning('Incorrect Hexadecimal value', 'Please enter Hexadecimal number')
        logging.error('Hexadecimal error')
        raise
        return False

def tvr_validation():

    global str_str
    str_str = tvr_value_raw.get()
    len_tvr =len(str_str)
    int_str_str =int(len_tvr)
    hex_length = str(len_tvr/2)
    is_hex(str_str)

    if (len_tvr == 10 ) :
        binary_string = bin(int(str_str, 16))[2:].zfill(num_of_bits)
        check_btn = 1
        for n in binary_string:

            if n == '1':
                if check_btn == 1:
                    c11.set(1)
                    b11.configure(fg="green")
                elif check_btn == 2:
                    c12.set(1)
                    b12.configure(fg="green")
                elif check_btn == 3:
                    c13.set(1)
                    b13.configure(fg="green")
                elif check_btn == 4:
                    c14.set(1)
                    b14.configure(fg="green")
                elif check_btn == 5:
                    c15.set(1)
                    b15.configure(fg="green")
                elif check_btn == 6:
                    c16.set(1)
                    b16.configure(fg="green")
                elif check_btn == 7:
                    c17.set(1)
                    b17.configure(fg="green")
                elif check_btn == 8:
                    c18.set(1)
                    b18.configure(fg="green")
                elif check_btn == 9:
                    c21.set(1)
                    b21.configure(fg="green")
                elif check_btn == 10:
                    c22.set(1)
                    b22.configure(fg="green")
                elif check_btn == 11:
                    c23.set(1)
                    b23.configure(fg="green")
                elif check_btn == 12:
                    c24.set(1)
                    b24.configure(fg="green")
                elif check_btn == 13:
                    c25.set(1)
                    b25.configure(fg="green")
                elif check_btn == 14:
                    c26.set(1)
                    b26.configure(fg="green")
                elif check_btn == 15:
                    c27.set(1)
                    b27.configure(fg="green")
                elif check_btn == 16:
                    c28.set(1)
                    b28.configure(fg="green")
                elif check_btn == 17:
                    c31.set(1)
                    b31.configure(fg="green")
                elif check_btn == 18:
                    c32.set(1)
                    b32.configure(fg="green")
                elif check_btn == 19:
                    c33.set(1)
                    b33.configure(fg="green")
                elif check_btn == 20:
                    c34.set(1)
                    b34.configure(fg="green")
                elif check_btn == 21:
                    c35.set(1)
                    b35.configure(fg="green")
                elif check_btn == 22:
                    c36.set(1)
                    b36.configure(fg="green")
                elif check_btn == 23:
                    c37.set(1)
                    b37.configure(fg="green")
                elif check_btn == 24:
                    c38.set(1)
                    b38.configure(fg="green")
                elif check_btn == 25:
                    c41.set(1)
                    b41.configure(fg="green")
                elif check_btn == 26:
                    c42.set(1)
                    b42.configure(fg="green")
                elif check_btn == 27:
                    c43.set(1)
                    b43.configure(fg="green")
                elif check_btn == 28:
                    c44.set(1)
                    b44.configure(fg="green")
                elif check_btn == 29:
                    c45.set(1)
                    b45.configure(fg="green")
                elif check_btn == 30:
                    c46.set(1)
                    b46.configure(fg="green")
                elif check_btn == 31:
                    c47.set(1)
                    b47.configure(fg="green")
                elif check_btn == 32:
                    c48.set(1)
                    b48.configure(fg="green")
                elif check_btn == 33:
                    c51.set(1)
                    b51.configure(fg="green")
                elif check_btn == 34:
                    c52.set(1)
                    b52.configure(fg="green")
                elif check_btn == 35:
                    c53.set(1)
                    b53.configure(fg="green")
                elif check_btn == 36:
                    c54.set(1)
                    b54.configure(fg="green")
                elif check_btn == 37:
                    c55.set(1)
                    b55.configure(fg="green")
                elif check_btn == 38:
                    c56.set(1)
                    b56.configure(fg="green")
                elif check_btn == 39:
                    c57.set(1)
                    b57.configure(fg="green")
                elif check_btn == 40:
                    c58.set(1)
                    b58.configure(fg="green")
            check_btn += 1

    else:
        showwarning('Incorrect TVR Length', 'Length of the TVR is'+hex_length+'.'+'Please enter 5 bytes TVR value')
        logging.error('Wrong TVR length')

def clear_tvr():

    tvr_Label.delete(0, 'end')
    b11.configure(fg="black")
    b12.configure(fg="black")
    b13.configure(fg="black")
    b14.configure(fg="black")
    b15.configure(fg="black")
    b16.configure(fg="black")
    b17.configure(fg="black")
    b18.configure(fg="black")
    b21.configure(fg="black")
    b22.configure(fg="black")
    b23.configure(fg="black")
    b24.configure(fg="black")
    b25.configure(fg="black")
    b26.configure(fg="black")
    b27.configure(fg="black")
    b28.configure(fg="black")
    b31.configure(fg="black")
    b32.configure(fg="black")
    b33.configure(fg="black")
    b34.configure(fg="black")
    b35.configure(fg="black")
    b36.configure(fg="black")
    b37.configure(fg="black")
    b38.configure(fg="black")
    b41.configure(fg="black")
    b42.configure(fg="black")
    b43.configure(fg="black")
    b44.configure(fg="black")
    b45.configure(fg="black")
    b46.configure(fg="black")
    b47.configure(fg="black")
    b48.configure(fg="black")
    b51.configure(fg="black")
    b52.configure(fg="black")
    b53.configure(fg="black")
    b54.configure(fg="black")
    b55.configure(fg="black")
    b56.configure(fg="black")
    b57.configure(fg="black")
    b58.configure(fg="black")

    # Clearing checkbox
    c11.set(0)
    c12.set(0)
    c13.set(0)
    c14.set(0)
    c15.set(0)
    c16.set(0)
    c17.set(0)
    c18.set(0)
    c21.set(0)
    c22.set(0)
    c23.set(0)
    c24.set(0)
    c25.set(0)
    c26.set(0)
    c27.set(0)
    c28.set(0)
    c31.set(0)
    c32.set(0)
    c33.set(0)
    c34.set(0)
    c35.set(0)
    c36.set(0)
    c37.set(0)
    c38.set(0)
    c41.set(0)
    c42.set(0)
    c43.set(0)
    c44.set(0)
    c45.set(0)
    c46.set(0)
    c47.set(0)
    c48.set(0)
    c51.set(0)
    c52.set(0)
    c53.set(0)
    c54.set(0)
    c55.set(0)
    c56.set(0)
    c57.set(0)
    c58.set(0)

def tag_9f6e_validation():

    global str_str
    str_str = tag_9f6e_value_raw.get()
    len_tag_9f6e =len(str_str)
    hex_length_9f6e = str(len_tag_9f6e/2)
    is_hex(str_str)

    if (len_tag_9f6e == 8 ) :
        binary_string = bin(int(str_str, 16))[2:].zfill(num_of_bits_9f6e)
        check_btn_9f6e = 1
        for n in binary_string:

            if n == '1':
                if check_btn_9f6e == 1:
                    d11.set(1)
                    f11.configure(fg="green")
                elif check_btn_9f6e == 2:
                    d12.set(1)
                    f12.configure(fg="green")
                elif check_btn_9f6e == 3:
                    d13.set(1)
                    f13.configure(fg="green")
                elif check_btn_9f6e == 4:
                    d14.set(1)
                    f14.configure(fg="green")
                elif check_btn_9f6e == 5:
                    d15.set(1)
                    f15.configure(fg="green")
                elif check_btn_9f6e == 6:
                    d16.set(1)
                    f16.configure(fg="green")
                elif check_btn_9f6e == 7:
                    d17.set(1)
                    f17.configure(fg="green")
                elif check_btn_9f6e == 8:
                    d18.set(1)
                    f18.configure(fg="green")
                elif check_btn_9f6e == 9:
                    d21.set(1)
                    f21.configure(fg="green")
                elif check_btn_9f6e == 10:
                    d22.set(1)
                    f22.configure(fg="green")
                elif check_btn_9f6e == 11:
                    d23.set(1)
                    f23.configure(fg="green")
                elif check_btn_9f6e == 12:
                    d24.set(1)
                    f24.configure(fg="green")
                elif check_btn_9f6e == 13:
                    d25.set(1)
                    f25.configure(fg="green")
                elif check_btn_9f6e == 14:
                    d26.set(1)
                    f26.configure(fg="green")
                elif check_btn_9f6e == 15:
                    d27.set(1)
                    f27.configure(fg="green")
                elif check_btn_9f6e == 16:
                    d28.set(1)
                    f28.configure(fg="green")
                elif check_btn_9f6e == 17:
                    d31.set(1)
                    f31.configure(fg="green")
                elif check_btn_9f6e == 18:
                    d32.set(1)
                    f32.configure(fg="green")
                elif check_btn_9f6e == 19:
                    d33.set(1)
                    f33.configure(fg="green")
                elif check_btn_9f6e == 20:
                    d34.set(1)
                    f34.configure(fg="green")
                elif check_btn_9f6e == 21:
                    d35.set(1)
                    f35.configure(fg="green")
                elif check_btn_9f6e == 22:
                    d36.set(1)
                    f36.configure(fg="green")
                elif check_btn_9f6e == 23:
                    d37.set(1)
                    f37.configure(fg="green")
                elif check_btn_9f6e == 24:
                    d38.set(1)
                    f38.configure(fg="green")
                elif check_btn_9f6e == 25:
                    d41.set(1)
                    f41.configure(fg="green")
                elif check_btn_9f6e == 26:
                    d42.set(1)
                    f42.configure(fg="green")
                elif check_btn_9f6e == 27:
                    d43.set(1)
                    f43.configure(fg="green")
                elif check_btn_9f6e == 28:
                    d44.set(1)
                    f44.configure(fg="green")
                elif check_btn_9f6e == 29:
                    d45.set(1)
                    f45.configure(fg="green")
                elif check_btn_9f6e == 30:
                    d46.set(1)
                    f46.configure(fg="green")
                elif check_btn_9f6e == 31:
                    d47.set(1)
                    f47.configure(fg="green")
                elif check_btn_9f6e == 32:
                    d48.set(1)
                    f48.configure(fg="green")

            check_btn_9f6e += 1

    else:
        showwarning('Incorrect Tag_9f6e Length', 'Length of the Tag 9f6e is'+hex_length_9f6e+'.'+'Please enter 4 bytes tag_9f6e value')
        logging.error('Wrong Tag 9F6E length')

def clear_tag_9f6e():

    tag_9f6e_Label.delete(0, 'end')
    f11.configure(fg="black")
    f12.configure(fg="black")
    f13.configure(fg="black")
    f14.configure(fg="black")
    f15.configure(fg="black")
    f16.configure(fg="black")
    f17.configure(fg="black")
    f18.configure(fg="black")
    f21.configure(fg="black")
    f22.configure(fg="black")
    f23.configure(fg="black")
    f24.configure(fg="black")
    f25.configure(fg="black")
    f26.configure(fg="black")
    f27.configure(fg="black")
    f28.configure(fg="black")
    f31.configure(fg="black")
    f32.configure(fg="black")
    f33.configure(fg="black")
    f34.configure(fg="black")
    f35.configure(fg="black")
    f36.configure(fg="black")
    f37.configure(fg="black")
    f38.configure(fg="black")
    f41.configure(fg="black")
    f42.configure(fg="black")
    f43.configure(fg="black")
    f44.configure(fg="black")
    f45.configure(fg="black")
    f46.configure(fg="black")
    f47.configure(fg="black")
    f48.configure(fg="black")

    # Clearing checkbox
    d11.set(0)
    d12.set(0)
    d13.set(0)
    d14.set(0)
    d15.set(0)
    d16.set(0)
    d17.set(0)
    d18.set(0)
    d21.set(0)
    d22.set(0)
    d23.set(0)
    d24.set(0)
    d25.set(0)
    d26.set(0)
    d27.set(0)
    d28.set(0)
    d31.set(0)
    d32.set(0)
    d33.set(0)
    d34.set(0)
    d35.set(0)
    d36.set(0)
    d37.set(0)
    d38.set(0)
    d41.set(0)
    d42.set(0)
    d43.set(0)
    d44.set(0)
    d45.set(0)
    d46.set(0)
    d47.set(0)
    d48.set(0)

def tag_9f70_validation():

    global str_str
    str_str = tag_9f70_value_raw.get()
    len_tag_9f70 =len(str_str)
    hex_length_9f70 = str(len_tag_9f70/2)
    is_hex(str_str)

    if (len_tag_9f70 == 4 ) :
        binary_string = bin(int(str_str, 16))[2:].zfill(num_of_bits_9f70)
        check_btn_9f70 = 1
        for n in binary_string:

            if n == '1':
                if check_btn_9f70 == 1:
                    g11.set(1)
                    h11.configure(fg="green")
                elif check_btn_9f70 == 2:
                    g12.set(1)
                    h12.configure(fg="green")
                elif check_btn_9f70 == 3:
                    g13.set(1)
                    h13.configure(fg="green")
                elif check_btn_9f70 == 4:
                    g14.set(1)
                    h14.configure(fg="green")
                elif check_btn_9f70 == 5:
                    g15.set(1)
                    h15.configure(fg="green")
                elif check_btn_9f70 == 6:
                    g16.set(1)
                    h16.configure(fg="green")
                elif check_btn_9f70 == 7:
                    g17.set(1)
                    h17.configure(fg="green")
                elif check_btn_9f70 == 8:
                    g18.set(1)
                    h18.configure(fg="green")
                elif check_btn_9f70 == 9:
                    g21.set(1)
                    h21.configure(fg="green")
                elif check_btn_9f70 == 10:
                    g22.set(1)
                    h22.configure(fg="green")
                elif check_btn_9f70 == 11:
                    g23.set(1)
                    h23.configure(fg="green")
                elif check_btn_9f70 == 12:
                    g24.set(1)
                    h24.configure(fg="green")
                elif check_btn_9f70 == 13:
                    g25.set(1)
                    h25.configure(fg="green")
                elif check_btn_9f70 == 14:
                    g26.set(1)
                    h26.configure(fg="green")
                elif check_btn_9f70 == 15:
                    g27.set(1)
                    h27.configure(fg="green")
                elif check_btn_9f70 == 16:
                    g28.set(1)
                    h28.configure(fg="green")

            check_btn_9f70 += 1

    else:
        showwarning('Incorrect Tag 9F70 Length', 'Length of the Tag 9F70 is'+hex_length_9f70+'.'+'Please enter 2 bytes tag 9F70 value')
        logging.error('Wrong Tag 9F70 length')

def clear_tag_9f70():

    tag_9f70_Label.delete(0, 'end')
    h11.configure(fg="black")
    h12.configure(fg="black")
    h13.configure(fg="black")
    h14.configure(fg="black")
    h15.configure(fg="black")
    h16.configure(fg="black")
    h17.configure(fg="black")
    h18.configure(fg="black")
    h21.configure(fg="black")
    h22.configure(fg="black")
    h23.configure(fg="black")
    h24.configure(fg="black")
    h25.configure(fg="black")
    h26.configure(fg="black")
    h27.configure(fg="black")
    h28.configure(fg="black")

    # Clearing checkbox
    g11.set(0)
    g12.set(0)
    g13.set(0)
    g14.set(0)
    g15.set(0)
    g16.set(0)
    g17.set(0)
    g18.set(0)
    g21.set(0)
    g22.set(0)
    g23.set(0)
    g24.set(0)
    g25.set(0)
    g26.set(0)
    g27.set(0)
    g28.set(0)

def tag_82_validation():

    global str_str
    str_str = tag_82_value_raw.get()
    len_tag_82 =len(str_str)
    hex_length_82 = str(len_tag_82/2)
    is_hex(str_str)

    if (len_tag_82 == 4 ) :
        binary_string = bin(int(str_str, 16))[2:].zfill(num_of_bits_82)
        check_btn_82 = 1
        emv = 0
        m_mag = 0
        m_emv = 0
        m_emv_1 = 0

        for n in binary_string:

            if n == '1':
                if check_btn_82 == 1:
                    i11.set(1)
                    j11.configure(fg="green")
                elif check_btn_82 == 2:
                    i12.set(1)
                    j12.configure(fg="green")
                elif check_btn_82 == 3:
                    i13.set(1)
                    j13.configure(fg="green")
                elif check_btn_82 == 4:
                    i14.set(1)
                    j14.configure(fg="green")
                elif check_btn_82 == 5:
                    i15.set(1)
                    j15.configure(fg="green")
                elif check_btn_82 == 6:
                    i16.set(1)
                    j16.configure(fg="green")
                elif check_btn_82 == 7:
                    i17.set(1)
                    j17.configure(fg="green")
                elif check_btn_82 == 8:
                    i18.set(1)
                    j18.configure(fg="green")
                elif check_btn_82 == 9:
                    emv += 1
                    m_emv += 1
                    i21.set(1)
                    j21.configure(fg="green")
                elif check_btn_82 == 10:
                    m_mag += 1
                    m_emv_1 += 1
                    i22.set(1)
                    j22.configure(fg="green")
                elif check_btn_82 == 11:
                    i23.set(1)
                    j23.configure(fg="green")
                elif check_btn_82 == 12:
                    i24.set(1)
                    j24.configure(fg="green")
                elif check_btn_82 == 13:
                    i25.set(1)
                    j25.configure(fg="green")
                elif check_btn_82 == 14:
                    i26.set(1)
                    j26.configure(fg="green")
                elif check_btn_82 == 15:
                    i27.set(1)
                    j27.configure(fg="green")
                elif check_btn_82 == 16:
                    i28.set(1)
                    j28.configure(fg="green")

            if n == '0' and check_btn_82 == 9:
                mag = 5

            check_btn_82 += 1


        if m_emv == 1 and m_emv_1 == 1 :

            mode_result.configure(text="Mobile EMV")

        elif emv == 1:

            mode_result.configure(text="EMV")

        elif m_mag == 1:

            mode_result.configure(text="Mobile Magstripe")

        elif emv == 0:

            mode_result.configure(text="Magstripe")

        else:

            mode_result.configure(text="NA",fg="red")
    else:
        showwarning('Incorrect Tag 82 Length', 'Length of the Tag 82 is'+hex_length_82+'.'+'Please enter 2 bytes tag 82 value')
        logging.error('Wrong Tag 82 length')

def clear_tag_82():

    tag_82_Label.delete(0, 'end')
    j11.configure(fg="black")
    j12.configure(fg="black")
    j13.configure(fg="black")
    j14.configure(fg="black")
    j15.configure(fg="black")
    j16.configure(fg="black")
    j17.configure(fg="black")
    j18.configure(fg="black")
    j21.configure(fg="black")
    j22.configure(fg="black")
    j23.configure(fg="black")
    j24.configure(fg="black")
    j25.configure(fg="black")
    j26.configure(fg="black")
    j27.configure(fg="black")
    j28.configure(fg="black")

    # Clearing checkbox
    i11.set(0)
    i12.set(0)
    i13.set(0)
    i14.set(0)
    i15.set(0)
    i16.set(0)
    i17.set(0)
    i18.set(0)
    i21.set(0)
    i22.set(0)
    i23.set(0)
    i24.set(0)
    i25.set(0)
    i26.set(0)
    i27.set(0)
    i28.set(0)

    mode_result.configure(text=" ")

def tag_9f6d_validation():

    global str_str
    str_str = tag_9f6d_raw .get()
    len_tag_9f6d = len(str_str)
    hex_length_9f6d = str(len_tag_9f6d / 2)
    is_hex(str_str)
    temp_9f6d = str(0)
    if (len_tag_9f6d == 2 ) :
        binary_string = bin(int(str_str, 16))[2:].zfill(num_of_bits_9f6d)
        check_btn_9f6d  = 1

        for n in binary_string:

            if check_btn_9f6d == 1 or check_btn_9f6d == 2 or check_btn_9f6d == 5:

                temp_9f6d = temp_9f6d+str(n)

            check_btn_9f6d += 1

        if temp_9f6d == '0111' :

            input_9f6d_meaning.configure(text =' Contactless: EMV and Mag-Stripe - CVM Required',fg="green")

        elif temp_9f6d == '0110':

            input_9f6d_meaning.configure(text=' Contactless: EMV and Mag-Stripe - CVM Not Required',fg="green")

        elif temp_9f6d == '0010':

            input_9f6d_meaning.configure(text=' Mag-Stripe – CVM Not Required',fg="green")

        elif temp_9f6d == '0011':

            input_9f6d_meaning.configure(text=' Mag-Stripe – CVM Required',fg="green")

        else:

            input_9f6d_meaning.configure(text='Please enter valid input',fg ='red')

    else:
        showwarning('Incorrect Tag 9F6D Length', 'Length of the Tag 9F6D is'+hex_length_9f6d+'.'+'Please enter 1 byte tag 9F6D value')
        logging.error('Wrong Tag 9F6D length')

def tag_9f6d_clear():

    input_9f6d_meaning.configure(text=' ')
    tag_9f6d_Label.delete(0,'end')

def tag_9f71_validation():

    global str_str
    str_str = tag_9f71_raw.get()
    len_tag_9f71 = len(str_str)
    hex_length_9f71 = str(len_tag_9f71 / 2)
    is_hex(str_str)
    temp_9f71_1 = str(0)
    temp_9f71_2 = str(0)
    temp_9f71_3 = str(0)

    if (len_tag_9f71 == 6 ) :
        binary_string = bin(int(str_str, 16))[2:].zfill(num_of_bits_9f71)
        check_btn_9f71  = 1

        for n in binary_string:

            if check_btn_9f71 <= 8 :

                temp_9f71_1 = temp_9f71_1+str(n)

            elif (check_btn_9f71 >= 8 and check_btn_9f71 <= 16):

                temp_9f71_2 = temp_9f71_2 + str(n)

            elif (check_btn_9f71 >= 16 and check_btn_9f71 <= 24):

                temp_9f71_3 = temp_9f71_3 + str(n)

            check_btn_9f71 += 1

        if temp_9f71_1 == '000000001' :

            input_9f71_meaning_byte1.configure(text =' Mobile CVM Performed ',fg="green")

        elif temp_9f71_1 == '000111111':

            input_9f71_meaning_byte1.configure(text =' Mobile CVM Performed ',fg="green")

        else:

            input_9f71_meaning_byte1.configure(text='Please enter valid input' ,fg ="red")

        if temp_9f71_2 == '000000000' :

            input_9f71_meaning_byte2.configure(text =' Mobile CVM not Required ',fg="green")

        elif temp_9f71_2 == '000000011':

            input_9f71_meaning_byte2.configure(text =' Terminal Required CVM ',fg="green")

        else:

            input_9f71_meaning_byte2.configure(text='Please enter valid input' ,fg ="red")

        if temp_9f71_3 == '000000000' :

            input_9f71_meaning_byte3.configure(text =' Unknown (if Mobile CVM not performed) ',fg="green")

        elif temp_9f71_3 == '000000001':

            input_9f71_meaning_byte3.configure(text =' Mobile CVM Failed ',fg="green")

        elif temp_9f71_3 == '000000010':

            input_9f71_meaning_byte3.configure(text =' Mobile CVM Successful ',fg="green")

        elif temp_9f71_3 == '000000001':

            input_9f71_meaning_byte3.configure(text =' Mobile CVM Blocked ',fg="green")
        else:

            input_9f71_meaning_byte3.configure(text='Please enter valid input' ,fg ="red")

    else:
        showwarning('Incorrect Tag 9F71 Length', 'Length of the Tag 9f71 is'+hex_length_9f71+'.'+'Please enter 3 byte tag 9F71 value')
        logging.error('Wrong Tag 9F71 length')

def tag_9f71_clear():

    tag_9f71_Label.delete(0,'end')
    input_9f71_meaning_byte3.configure(text=' ')
    input_9f71_meaning_byte2.configure(text=' ')
    input_9f71_meaning_byte1.configure(text=' ')

def pdf_open():

    os.startfile("Amex_User_Manual.pdf")

window = tk.Tk()
window.title(" AMEX Util")
window.geometry("1650x800")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
screen_resolution = str(screen_width)+'x'+str(screen_height)
window.geometry(screen_resolution)
window.iconbitmap("Amex_util_logo.ico")
style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition='wn')
notebook = ttk.Notebook(window, style='lefttab.TNotebook')
#main = tk.Frame(notebook)
f1 = tk.Frame(notebook,width=screen_width, height=screen_height)
f2 = tk.Frame(notebook, bg='blue',width=screen_width, height=screen_height)
f3 = tk.Frame(notebook, bg='red',width=screen_width, height=screen_height)
f4 = tk.Frame(notebook, bg='purple',width=screen_width, height=screen_height)
f5 = tk.Frame(notebook, bg='white',width=screen_width, height=screen_height)
f6 = tk.Frame(notebook, bg='green',width=screen_width, height=screen_height)
f7 = tk.Frame(notebook, bg='yellow',width=screen_width, height=screen_height)
f8 = tk.Frame(notebook, bg='white',width=screen_width, height=screen_height)
f9 = tk.Frame(notebook, bg='red',width=screen_width, height=screen_height)
#ImageTk.PhotoImage(Image.open("xyz.jpg")
amex_logo = PhotoImage(file="amex_logo.png")
dpas_logo = PhotoImage(file="dpas_logo.png")
jcb_logo = PhotoImage(file="jcb_logo.png")
mcl_logo = PhotoImage(file="mcl_logo.png")
cup_logo = PhotoImage(file="cup_logo.png")
eftpos_logo = PhotoImage(file="eftpos_logo.png")
rupay_logo = PhotoImage(file="rupay_logo.png")
fime_logo = PhotoImage(file="fime_logo.png")
visa_logo = PhotoImage(file="visa_logo.png")
emv_logo = PhotoImage(file="emv_logo.png")
#notebook.add(main,image = fime_logo)
notebook.add(f1,image = amex_logo)
notebook.add(f2,image = dpas_logo)
notebook.add(f3,image = jcb_logo)
notebook.add(f4,image = mcl_logo)
notebook.add(f5,image = cup_logo)
notebook.add(f6,image = eftpos_logo)
notebook.add(f7,image = rupay_logo)
notebook.add(f8,image = emv_logo)
notebook.add(f9,image = visa_logo)

user_manual_image = PhotoImage(file="user_manual_logo.png")
user_btn = Button(notebook,command = pdf_open,image=user_manual_image,width ="105" ,height ="75",bg ="purple").place(x=0,y=547)

# Notebook Style
noteStyler = ttk.Style()
# Import the Notebook.tab element from the default theme
#noteStyler.element_create('left.Notebook.tab', "from", 'default')
# Redefine the TNotebook Tab layout to use the new element
noteStyler.layout("TNotebook.Tab",
    [('Plain.Notebook.tab', {'children':
        [('Notebook.padding', {'side': 'top', 'children':
            [('Notebook.focus', {'side': 'top', 'children':
                [('Notebook.label', {'side': 'top', 'sticky': ''})],
            'sticky': 'nswe'})],
        'sticky': 'nswe'})],
    'sticky': 'nswe'})])
noteStyler.configure("TNotebook", background="Purple", borderwidth=0)
noteStyler.configure("TNotebook.Tab", background="gray90", foreground="Purple",
                                      lightcolor="red", borderwidth=4 ,)
noteStyler.configure("TFrame", background="seashell3", foreground="white", borderwidth=0)

tab_control = ttk.Notebook(f1,style='TNotebook')
#tab_control.configure(background ="seashell3")
#tab_control["bg"] = "seashell3"

tab1 = ttk.Frame(tab_control,style='TFrame')
tab2 = ttk.Frame(tab_control,style='TFrame')
tab3 = ttk.Frame(tab_control,style='TFrame')
tab4 = ttk.Frame(tab_control,style='TFrame')
tab5 = ttk.Frame(tab_control,style='TFrame')
tab6 = ttk.Frame(tab_control,style='TFrame')
tab7 = ttk.Frame(tab_control,style='TFrame')
#tab8 = ttk.Button(tab_control,command = output_path)
compare_icon = PhotoImage(file="compare_icon.png")
parser_icon = PhotoImage(file="parser_icon.png")
binary_icon = PhotoImage(file="binary_icon.png")
pos_icon = PhotoImage(file="pos_icon.png")
services_icon = PhotoImage(file="services_icon.png")
card_icon = PhotoImage(file="card_icon.png")
cvm_icon = PhotoImage(file="cvm_icon.png")
verify_icon = PhotoImage(file="verify_icon.png")
tab_control.add(tab1, text='XML Compare',image =compare_icon,compound=tk.TOP)

tab_control.add(tab2, text='Profiles Parser',image =parser_icon,compound=tk.TOP)

tab_control.add(tab3,text ='      TVR(95)      ',image =pos_icon,compound=tk.TOP)

tab_control.add(tab4,text ='        9F6E         ',image =services_icon,compound=tk.TOP)

tab_control.add(tab5,text ='        9F70         ',image =card_icon,compound=tk.TOP)

tab_control.add(tab6,text ='        AIP         ',image =verify_icon,compound=tk.TOP)

tab_control.add(tab7,text =' 9F6D & 9F71 ',image =cvm_icon,compound=tk.TOP)

#tab_control.add(tab8,text =' User Manual ')

# User Manual update
notebook.pack()
#user_manual_image = PhotoImage(file="user_manual_logo.png")
#user_btn = Button(tab_control,command = pdf_open,image=user_manual_image,width ="100" ,height ="70",bg ="purple").place(x=670,y=0)
#tab1.config(bg ="seashell3")

# frame = tk.Frame(gui)
# frame.config(bg ="seashell3")
# frame.pack()
# gui.configure(background ="grey")

# ----------------------------------------------------------------------------------------------------------------#

# XML Compare GUI Design

# First frame design
label_title_1 = Label(tab1, text="Amex XML Comparison Files", bg="purple", fg="white",
                      font=("Times New Roman", 16, "bold"), width=40).place(x=10, y=10)
label_title_2 = Label(tab1, text="Multi Configuration Testing Result ", bg="purple", fg="white", font=("Times New Roman", 16, "bold"),
                      width=40).place(x=10, y=425)
label_left_1 = Label(tab1, bg="purple", height=37).place(x=10, y=30)
label_right_1 = Label(tab1, bg="purple", height=37).place(x=490, y=30)
Label_end_1 = Label(tab1, bg="purple", font=("", 1), width=480).place(x=10, y=590)

# w =Canvas(gui,width=1600,height=900)
# w.create_rectangle(0,0,50,50,fill="white",outline="purple")
# w.pack()

# Library Selection

lib_label = Label(tab1, text="Library Name", bg="seashell3", font=("Times New Roman", 12, "bold")).place(x=20,y=70)
global Lib_name_raw
Lib_name_raw = StringVar()
Lib_name_raw.set(OPTIONS[0])
lib_menu = OptionMenu(tab1,Lib_name_raw, *OPTIONS,command =lib_selection)
lib_menu.config(bg="seashell4")
lib_menu["highlightthickness"]=0
lib_menu.place(x=190,y=70)

# Output path to load XML
output_label = Label(tab1, text="Output XML (AMEX) ", bg="seashell3", font=("Times New Roman", 12, "bold")).place(x=20,
                                                                                                                y=120)
output_path_raw = StringVar()
ouput_path_label = Entry(tab1, textvariable= output_path_raw, font=("Times New Roman", 11), width=32)
ouput_path_label.place(x=190, y=120)

button1 = Button(tab1, text="File", bg="seashell4", command=output_path, width=5).place(x=436, y=120)
# output_label_1 = Label (gui,text = " ",font=("bold", 10),width =50)
# output_label_1.place(x=190,y=80)

# First input path to load XML
input11_label = Label(tab1, text="Common XML (Tool)", bg="seashell3", font=("Times New Roman", 12, "bold")).place(x=20,
                                                                                                              y=170)
input1_path_raw = StringVar()
input1_path_label = Entry(tab1, textvariable= input1_path_raw, font=("Times New Roman", 11), width=32)
input1_path_label.place(x=190, y=170)

button2 = Button(tab1, text="File", bg="seashell4", command=input_path1, width=5).place(x=436, y=170)
# input1_label_1 = Label (gui,text = " ",font=("bold", 10),width =50)
# input1_label_1.place(x=190,y=130)

# Second input path
input2_label = Label(tab1, text="XP/C4 XML (Tool)", bg="seashell3", font=("Times New Roman", 12, "bold")).place(x=20,y=220)
input2_path_raw = StringVar()
input2_path_label = Entry(tab1, textvariable= input2_path_raw, font=("Times New Roman", 11), width=32)
input2_path_label.place(x=190, y=220)

button3 = Button(tab1, text="File", bg="seashell4", command=input_path2, width=5).place(x=436, y=220)
# input2_label_1 = Label (gui,text = " ",font=("bold", 10),width =50)
# input2_label_1.place(x=190,y=180)

# Result save path
Result = Label(tab1, text="Select Result path ", bg="seashell3", font=("Times New Roman", 12, "bold")).place(x=20, y=320)
save_path_raw = StringVar()
save_path_label = Entry(tab1, textvariable= save_path_raw, font=("Times New Roman", 11), width=32)
save_path_label.place(x=190, y=320)

# save_label_1 = Label (gui,text = " ",font=("bold", 10),width =50)
# save_label_1.place(x=190,y=230)
button4 = Button(tab1, text="Folder", bg="seashell4", command=save_path, width=5).place(x=436, y=317)

# File name
save_name_raw = StringVar()
global save_name_Label
save_name_Label = Entry(tab1, textvariable=save_name_raw, font=("Times New Roman", 12), width=15)
save_name_Label.place(x=190, y=270)
# save_name = save_name_raw.get()

save_label = Label(tab1, text="File Name ", bg="seashell3", font=("Times New Roman", 12, "bold")).place(x=20, y=270)

# Submit
button5 = Button(tab1, text="Submit", bg="green2", command=compare, width=10,
                 font=("Times New Roman", 10, "bold")).place(x=290, y=380)

# Display output profile
output_profile_label = Label(tab1, text="No of Applicable Profiles in Output XML", bg="seashell3",
                             font=("Times New Roman", 12, "bold")).place(x=20, y=470)
output_number = Label(tab1, text=' ', bg="white", font=("Times New Roman", 12, "bold"), width=5)
output_number.place(x=370, y=470)

# Display input profile

input_profile_label = Label(tab1, text="No of Applicable Profiles in Input XML", bg="seashell3",
                            font=("Times New Roman", 12, "bold")).place(x=20, y=510)
input_number = Label(tab1, text=' ', bg="white", font=("Times New Roman", 12, "bold"), width=5)
input_number.place(x=370, y=510)

# Display Result

Result_Display_label = Label(tab1, text="Result", bg="seashell3", font=("Times New Roman", 16, "bold")).place(x=80,y=550)
global Result_Display
Result_Display = Label(tab1, text=' ', font=("Times New Roman", 16, "bold"),bg="white", width=10)
Result_Display.place(x=210, y=550)

# Clear
button6 = Button(tab1, text="Clear", bg="yellow", command=clear, width=10, font=("Times New Roman", 10, "bold")).place(x=120,y=380)
# button5 = Button(gui, text="Exit", command=master.destroy)
# button5.grid()

#button7 = Button(tab1, text="Exit", bg="yellow", command=back, width=10, font=("Times New Roman", 10, "bold")).place(x=80, y=600)

# Profile Display
Profile_title = Label(tab1, text="Profiles ", bg="purple", fg="white", font=("Times New Roman", 16, "bold"),width=34).place(x=500, y=10)
Profile_right = Label(tab1, bg="purple", height=37).place(x=500, y=30)
Profile_end = Label(tab1, bg="purple", font=("", 1), width=408).place(x=500, y=590)
output_pro_title = Label(tab1, text="Output XML Profiles", bg="plum2", font=("Times New Roman", 12, "bold"),
                         width=22).place(x=506, y=35)
input_pro_title = Label(tab1, text="Input XML Profiles", bg="plum2", font=("Times New Roman", 12, "bold"),
                        width=22).place(x=706, y=35)
profile_centre = Label(tab1, bg="purple", height=37).place(x=704, y=33)
Profile_left = Label(tab1, bg="purple", height=37).place(x=908, y=30)
# output_display_label = Label(gui,text ='',bg="gray",font=("bold", 12), width=25,height=32)
# output_display_label.place(x=442,y=79)
global list_output
list_output = Listbox(tab1,height=26, width=23, font=("Times New Roman", 12, "bold"))
list_output.place(x=510, y=65)
global list_input
list_input = Listbox(tab1,height=26, width=23, font=("Times New Roman", 12, "bold"))
list_input.place(x=715, y=65)

# Mismatch Display
Profile_title = Label(tab1, text="Mismatches", bg="purple", fg="white", font=("Times New Roman", 16, "bold"),
                      width=26).place(x=920, y=10)
Profile_right = Label(tab1, bg="purple", height=37).place(x=920, y=30)
Profile_left = Label(tab1, bg="purple", height=37).place(x=1232, y=30)
global list_mismatch
list_mismatch = Listbox(tab1,height=27, width=36, font=("Times New Roman", 12, "bold"))

#list_mismatch.configure(scrollregion = list_mismatch.bbox("all"))
list_mismatch.place(x=932, y=40)

# Scroball

#scrollbar = Scrollbar(tab1)
#list_mismatch.config(yscrollcommand=scrollbar.set)
#scrollbar.pack(side="right", fill="y")
#scrollbar.place(x=1310, y=50, height=580)

Profile_end = Label(tab1, bg="purple", font=("", 1), width=312).place(x=920, y=590)

# --------------------------------------------------------------------------------------------------------------------#

# Profile Parsing UI Design

lib_label = Label(tab2, text="Library Name", bg="seashell3", font=("Times New Roman", 12, "bold")).place(x=160,y=70)
Lib_name_p_raw = StringVar()
Lib_name_p_raw.set(OPTIONS_P[0])
lib_menu_p = OptionMenu(tab2,Lib_name_p_raw, *OPTIONS_P,command=lib_selection_p)
lib_menu_p.config(bg="seashell4")
lib_menu_p["highlightthickness"]=0
lib_menu_p.place(x=400,y=70)

profile_select = Label(tab2, text="Select Common XML File", bg="seashell3", font=("Times New Roman", 12, "bold")).place(x=160,y=120)
button1 = Button(tab2, text="File", bg="seashell4", command=testcase_path, width=10).place(x=400, y=120)

profile_select_xp = Label(tab2, text="Select XP/C4 XML File", bg="seashell3", font=("Times New Roman", 12, "bold")).place(x=160,y=170)
button1 = Button(tab2, text="File", bg="seashell4", command=testcase_path_xp, width=10).place(x=400, y=170)

global save_name_testcase_raw
save_name_testcase_raw = StringVar()
global save_testcase_label
save_testcase_label = Label(tab2, text="File Name ", bg="seashell3", font=("Times New Roman", 12, "bold")).place(x=160, y=220)
save_name_Label_profile = Entry(tab2, textvariable=save_name_testcase_raw, font=("Times New Roman", 12), width=15)
save_name_Label_profile.place(x=400, y=220)

Result_path = Label(tab2, text="Select Result path ", bg="seashell3", font=("Times New Roman", 12, "bold")).place(x=160,y=270)
button_path_button = Button(tab2, text="Folder", bg="seashell4", command=save_path_testcase, width=10).place(x=400,y=270)

#button_1 = Button(profile_window, text="Clear", bg="red", command=switching,width=10,font=("Times New Roman", 12,"bold"))
#button_1.place(x=200,y=250)

button_2 = Button(tab2, text="Submit", bg="green2", command=parsing,width=10,font=("Times New Roman", 10, "bold"))
button_2.place(x=400, y=360)

button_3 = Button(tab2, text="Clear", bg="yellow", command=clearing,width=10,font=("Times New Roman", 10, "bold"))
button_3.place(x=200, y=360)

#button_4 = Button(tab2, text="Exit", bg="yellow", command=exit_window,width=10,font=("Times New Roman", 10, "bold"))
#button_4.place(x=200, y=310)

# First frame design
label_title_1_profile = Label(tab2, text="Profiles Parser", bg="purple", fg="white",
                      font=("Times New Roman", 16, "bold"), width=33).place(x=140, y=10)
label_left_1_profile = Label(tab2, bg="purple", height=36).place(x=140, y=40)
label_right_1_profile = Label(tab2, bg="purple", height=36).place(x=536, y=40)
Label_end_1_profile = Label(tab2, bg="purple", font=("", 1), width=396).place(x=140, y=580)

global list_profile
list_profile = Listbox(tab2,height=25, width=35, font=("Times New Roman", 12, "bold"))
list_profile.place(x=610, y=70)
global list_testcase
list_testcase = Listbox(tab2,height=25, width=23, font=("Times New Roman", 12, "bold"))
list_testcase.place(x=910, y=70)

# second frame

Profile_title_profile = Label(tab2, text="Result ", bg="purple", fg="white", font=("Times New Roman", 16, "bold"),
                      width=42).place(x=600, y=10)
Profile_right_profile = Label(tab2, bg="purple", height=36).place(x=600, y=40)
Profile_end_profile = Label(tab2, bg="purple", font=("", 1), width=504).place(x=600, y=580)
output_pro_title_profile= Label(tab2, text="Applicable Profiles ", bg="plum2", font=("Times New Roman", 12, "bold"),
                         width=32).place(x=606, y=40)
input_pro_title_profile = Label(tab2, text="No of Test cases", bg="plum2", font=("Times New Roman", 12, "bold"),
                        width=22).place(x=900, y=40)
profile_centre_profile = Label(tab2, bg="purple", height=36).place(x=900, y=40)
Profile_lef_profile = Label(tab2, bg="purple", height=36).place(x=1104, y=40)

# ------------------------------------------------------------------------------------------------------------------------

# TVR validation

global num_of_bits
num_of_bits = 40

# Frame Design

tvr_title_1 = Label(tab3, text="Terminal Verification Result ( Tag '95' )", bg="purple", fg="white",
                      font=("Times New Roman", 16, "bold"), width=101).place(x=20, y=10)
tvr_left_1 = Label(tab3, bg="purple", height=38).place(x=20, y=40)
tvr_right_1 = Label(tab3, bg="purple", height=38).place(x=1232, y=40)
tvr_end_1 = Label(tab3, bg="purple", font=("", 1), width=1210).place(x=20, y=608)

# TVR value

tvr_input = Label(tab3, text=" TVR Value", bg="seashell3", font=("Times New Roman", 12, "bold")).place(x=830, y=450)
tvr_value_raw = tk.StringVar()
global tvr_Label
tvr_Label = Entry(tab3, textvariable=tvr_value_raw, font=("Times New Roman", 12), width=25)
tvr_Label.bind('<Return>', lambda _: tvr_validation())
tvr_Label.place(x= 970, y= 450)
button_tvr = Button(tab3, text=" Submit ", bg="green2", command=tvr_validation, width=10,font=("Times New Roman", 10, "bold")).place(x=1050, y=550)

# Clear Button

button_btn_tvr = Button(tab3, text=" Clear ", bg="yellow", command=clear_tvr, width=10,font=("Times New Roman", 10, "bold")).place(x=880, y=550)

c11 = IntVar()
c12 = IntVar()
c13 = IntVar()
c14 = IntVar()
c15 = IntVar()
c16 = IntVar()
c17 = IntVar()
c18 = IntVar()
c21 = IntVar()
c22 = IntVar()
c23 = IntVar()
c24 = IntVar()
c25 = IntVar()
c26 = IntVar()
c27 = IntVar()
c28 = IntVar()
c31 = IntVar()
c32 = IntVar()
c33 = IntVar()
c34 = IntVar()
c35 = IntVar()
c36 = IntVar()
c37 = IntVar()
c38 = IntVar()
c41 = IntVar()
c42 = IntVar()
c43 = IntVar()
c44 = IntVar()
c45 = IntVar()
c46 = IntVar()
c47 = IntVar()
c48 = IntVar()
c51 = IntVar()
c52 = IntVar()
c53 = IntVar()
c54 = IntVar()
c55 = IntVar()
c56 = IntVar()
c57 = IntVar()
c58 = IntVar()

# Byte 1

l1 = Label(tab3,text=" Byte 1 ",font=("Times New Roman", 12, "bold"),bg="seashell3").place(x=180, y=50)
b11 = Checkbutton(tab3, text = " Offline Data Authentication was not performed (b8)", variable = c11,onvalue = 1, offvalue = 0, bg="seashell3")
b12 = Checkbutton(tab3, text = " Offline Static Data Authentication Failed (b7)", variable = c12,onvalue = 1, offvalue = 0, bg="seashell3")
b13 = Checkbutton(tab3, text = " Card Data Missing (b6)", variable = c13,onvalue = 1, offvalue = 0, bg="seashell3")
b14 = Checkbutton(tab3, text = " Card appears on Terminal Exception (b5)", variable = c14,onvalue = 1, offvalue = 0, bg="seashell3")
b15 = Checkbutton(tab3, text = " DDA failed (b4)", variable = c15,onvalue = 1, offvalue = 0, bg="seashell3")
b16 = Checkbutton(tab3, text = " CDA failed (b3)", variable = c16,onvalue = 1, offvalue = 0, bg="seashell3")
b17 = Checkbutton(tab3, text = " SDA Selected (b2)", variable = c17,onvalue = 1, offvalue = 0, bg="seashell3")
b18 = Checkbutton(tab3, text = " RFU (b1)", variable = c18,onvalue = 1, offvalue = 0, bg="seashell3")

b11.place(x=60,y=80)
b12.place(x=60,y=110)
b13.place(x=60,y=140)
b14.place(x=60,y=170)
b15.place(x=60,y=200)
b16.place(x=60,y=230)
b17.place(x=60,y=260)
b18.place(x=60,y=290)

# Byte 2

l2 = Label(tab3,text=" Byte 2 ",font=("Times New Roman", 12, "bold"),bg="seashell3").place(x=540, y=50)
b21 = Checkbutton(tab3, text = " Card and Terminal have different application versions (b8)", variable = c21,onvalue = 1, offvalue = 0, bg="seashell3" )
b22 = Checkbutton(tab3, text = " Expired Application (b7)", variable = c22,onvalue = 1, offvalue = 0, bg="seashell3")
b23 = Checkbutton(tab3, text = " Application not effective yet (b6)", variable = c23,onvalue = 1, offvalue = 0, bg="seashell3")
b24 = Checkbutton(tab3, text = " Requested service not allowed for Card product (b5)", variable = c24,onvalue = 1, offvalue = 0, bg="seashell3")
b25 = Checkbutton(tab3, text = " New Card (b4)", variable = c25,onvalue = 1, offvalue = 0, bg="seashell3")
b26 = Checkbutton(tab3, text = " RFU (b3)", variable = c26,onvalue = 1, offvalue = 0, bg="seashell3")
b27 = Checkbutton(tab3, text = " RFU (b2)", variable = c27,onvalue = 1, offvalue = 0, bg="seashell3")
b28 = Checkbutton(tab3, text = " RFU (b1)", variable = c28,onvalue = 1, offvalue = 0, bg="seashell3")

b21.place(x=420,y=80)
b22.place(x=420,y=110)
b23.place(x=420,y=140)
b24.place(x=420,y=170)
b25.place(x=420,y=200)
b26.place(x=420,y=230)
b27.place(x=420,y=260)
b28.place(x=420,y=290)

# Byte 3

l3 = Label(tab3,text=" Byte 3 ",font=("Times New Roman", 12, "bold"),bg="seashell3").place(x=1000, y=50)
b31 = Checkbutton(tab3, text = " Cardholder Verification failed/not successful (b8)", variable = c31,onvalue = 1, offvalue = 0, bg="seashell3" )
b32 = Checkbutton(tab3, text = " Unrecognised CVM (b7)", variable = c32,onvalue = 1, offvalue = 0, bg="seashell3")
b33 = Checkbutton(tab3, text = " Offline PIN Try (or Mobile CVM) Limit Exceeded / Passcode Try Limit (b6)", variable = c33,onvalue = 1, offvalue = 0, bg="seashell3")
b34 = Checkbutton(tab3, text = " PIN entry mandatory and PIN pad not present or not working (b5)", variable = c34,onvalue = 1, offvalue = 0, bg="seashell3")
b35 = Checkbutton(tab3, text = " PIN entry mandatory, PIN pad present, but PIN was not entered (b4)", variable = c35,onvalue = 1, offvalue = 0, bg="seashell3")
b36 = Checkbutton(tab3, text = " Online PIN entered (b3)", variable = c36,onvalue = 1, offvalue = 0, bg="seashell3")
b37 = Checkbutton(tab3, text = " RFU (b2)", variable = c37,onvalue = 1, offvalue = 0, bg="seashell3")
b38 = Checkbutton(tab3, text = " RFU (b1)", variable = c38,onvalue = 1, offvalue = 0, bg="seashell3")

b31.place(x=810,y=80)
b32.place(x=810,y=110)
b33.place(x=810,y=140)
b34.place(x=810,y=170)
b35.place(x=810,y=200)
b36.place(x=810,y=230)
b37.place(x=810,y=260)
b38.place(x=810,y=290)

# Byte 4

l4 = Label(tab3,text=" Byte 4 ",font=("Times New Roman", 12, "bold"),bg="seashell3").place(x=180, y=330)
b41 = Checkbutton(tab3, text = " Transaction Exceeds Floor Limit (b8)", variable = c41,onvalue = 1, offvalue = 0, bg="seashell3" )
b42 = Checkbutton(tab3, text = " Lower consecutive offline limit exceeded (b7)", variable = c42,onvalue = 1, offvalue = 0, bg="seashell3")
b43 = Checkbutton(tab3, text = " Upper consecutive offline limit exceeded (b6)", variable = c43,onvalue = 1, offvalue = 0, bg="seashell3")
b44 = Checkbutton(tab3, text = " Transaction selected randomly for online processing (b5)", variable = c44,onvalue = 1, offvalue = 0, bg="seashell3")
b45 = Checkbutton(tab3, text = " Merchant forced transaction online (b4)", variable = c45,onvalue = 1, offvalue = 0, bg="seashell3")
b46 = Checkbutton(tab3, text = " RFU (b3)", variable = c46,onvalue = 1, offvalue = 0, bg="seashell3")
b47 = Checkbutton(tab3, text = " RFU (b2)", variable = c47,onvalue = 1, offvalue = 0, bg="seashell3")
b48 = Checkbutton(tab3, text = " RFU (b1)", variable = c48,onvalue = 1, offvalue = 0, bg="seashell3")

b41.place(x=60,y=360)
b42.place(x=60,y=390)
b43.place(x=60,y=420)
b44.place(x=60,y=450)
b45.place(x=60,y=480)
b46.place(x=60,y=510)
b47.place(x=60,y=540)
b48.place(x=60,y=570)

# Byte 5

l5 = Label(tab3,text=" Byte 5 ",font=("Times New Roman", 12, "bold"),bg="seashell3").place(x=540, y=330)
b51 = Checkbutton(tab3, text = " Default TDOL used (b8)", variable = c51,onvalue = 1, offvalue = 0, bg="seashell3" )
b52 = Checkbutton(tab3, text = " Issuer Authentication was unsuccessful (b7)", variable = c52,onvalue = 1, offvalue = 0, bg="seashell3")
b53 = Checkbutton(tab3, text = " Script processing failed before final GENERATE AC (b6)", variable = c53,onvalue = 1, offvalue = 0, bg="seashell3")
b54 = Checkbutton(tab3, text = " Script processing failed after final GENERATE AC (b5)", variable = c54,onvalue = 1, offvalue = 0, bg="seashell3")
b55 = Checkbutton(tab3, text = " RFU (b5)", variable = c55,onvalue = 1, offvalue = 0, bg="seashell3")
b56 = Checkbutton(tab3, text = " RFU (b4)", variable = c56,onvalue = 1, offvalue = 0, bg="seashell3")
b57 = Checkbutton(tab3, text = " RFU (b2)", variable = c57,onvalue = 1, offvalue = 0, bg="seashell3")
b58 = Checkbutton(tab3, text = " RFU (b1)", variable = c58,onvalue = 1, offvalue = 0, bg="seashell3")

b51.place(x=420,y=360)
b52.place(x=420,y=390)
b53.place(x=420,y=420)
b54.place(x=420,y=450)
b55.place(x=420,y=480)
b56.place(x=420,y=510)
b57.place(x=420,y=540)
b58.place(x=420,y=570)

#------------------------------------------------------------------------------------------------------------------

# Tag 9F6E validation

num_of_bits_9f6e  = 32

# Frame Design

tag_9f6e_title_1 = Label(tab4, text="Enhanced Contactless Reader Capabilities ( Tag '9F6E' )", bg="purple", fg="white",
                      font=("Times New Roman", 16, "bold"), width=101).place(x=20, y=10)
tag_9f6e_left_1 = Label(tab4, bg="purple", height=38).place(x=20, y=40)
tag_9f6e_right_1 = Label(tab4, bg="purple", height=38).place(x=1232, y=40)
tag_9f6e_end_1 = Label(tab4, bg="purple", font=("", 1), width=1210).place(x=20, y=608)

# tag_9f6e value

tag_9f6e_input = Label(tab4, text=" 9F6E Value ", bg="seashell3", font=("Times New Roman", 12, "bold")).place(x=830, y=350)
tag_9f6e_value_raw = tk.StringVar()
global tag_9f6e_Label
tag_9f6e_Label = Entry(tab4, textvariable=tag_9f6e_value_raw, font=("Times New Roman", 12), width=25)
tag_9f6e_Label.bind('<Return>', lambda _: tag_9f6e_validation())
tag_9f6e_Label.place(x= 970, y= 350)
button_tag_9f6e = Button(tab4, text=" Submit ", bg="green2", command=tag_9f6e_validation, width=10,font=("Times New Roman", 10, "bold")).place(x=1050, y=450)

# Clear Button

button_btn_tag_9f6e = Button(tab4, text=" Clear ", bg="yellow", command=clear_tag_9f6e, width=10,font=("Times New Roman", 10, "bold")).place(x=880, y=450)

d11 = IntVar()
d12 = IntVar()
d13 = IntVar()
d14 = IntVar()
d15 = IntVar()
d16 = IntVar()
d17 = IntVar()
d18 = IntVar()
d21 = IntVar()
d22 = IntVar()
d23 = IntVar()
d24 = IntVar()
d25 = IntVar()
d26 = IntVar()
d27 = IntVar()
d28 = IntVar()
d31 = IntVar()
d32 = IntVar()
d33 = IntVar()
d34 = IntVar()
d35 = IntVar()
d36 = IntVar()
d37 = IntVar()
d38 = IntVar()
d41 = IntVar()
d42 = IntVar()
d43 = IntVar()
d44 = IntVar()
d45 = IntVar()
d46 = IntVar()
d47 = IntVar()
d48 = IntVar()


# Byte 1

l1_9f6e = Label(tab4,text=" Byte 1 ",font=("Times New Roman", 12, "bold"),bg="seashell3").place(x=200, y=50)
f11 = Checkbutton(tab4, text = " Contact mode supported (b8)", variable = d11,onvalue = 1, offvalue = 0, bg="seashell3")
f12 = Checkbutton(tab4, text = " Expresspay /Contactless Mag-Stripe Mode supported (b7)", variable = d12,onvalue = 1, offvalue = 0, bg="seashell3")
f13 = Checkbutton(tab4, text = " Expresspay /Contactless EMV full online mode supported (b6)", variable = d13,onvalue = 1, offvalue = 0, bg="seashell3")
f14 = Checkbutton(tab4, text = " Expresspay/Contactless EMV partial online mode supported (b5)", variable = d14,onvalue = 1, offvalue = 0, bg="seashell3")
f15 = Checkbutton(tab4, text = " Expresspay/Contactless Mobile Supported (b4)", variable = d15,onvalue = 1, offvalue = 0, bg="seashell3")
f16 = Checkbutton(tab4, text = " Try Another Interface after a decline (b3)", variable = d16,onvalue = 1, offvalue = 0, bg="seashell3")
f17 = Checkbutton(tab4, text = " RFU (b2)", variable = d17,onvalue = 1, offvalue = 0, bg="seashell3")
f18 = Checkbutton(tab4, text = " RFU (b1)", variable = d18,onvalue = 1, offvalue = 0, bg="seashell3")

f11.place(x=80,y=80)
f12.place(x=80,y=110)
f13.place(x=80,y=140)
f14.place(x=80,y=170)
f15.place(x=80,y=200)
f16.place(x=80,y=230)
f17.place(x=80,y=260)
f18.place(x=80,y=290)

# Byte 2

l2_9f6e = Label(tab4,text=" Byte 2 ",font=("Times New Roman", 12, "bold"),bg="seashell3").place(x=620, y=50)
f21 = Checkbutton(tab4, text = " Mobile CVM supported (b8)", variable = d21,onvalue = 1, offvalue = 0, bg="seashell3" )
f22 = Checkbutton(tab4, text = " Online PIN supported (b7)", variable = d22,onvalue = 1, offvalue = 0, bg="seashell3")
f23 = Checkbutton(tab4, text = " Signature (b6)", variable = d23,onvalue = 1, offvalue = 0, bg="seashell3")
f24 = Checkbutton(tab4, text = " Plaintext Offline PIN (b5)", variable = d24,onvalue = 1, offvalue = 0, bg="seashell3")
f25 = Checkbutton(tab4, text = " RFU (b4)", variable = d25,onvalue = 1, offvalue = 0, bg="seashell3")
f26 = Checkbutton(tab4, text = " RFU (b3)", variable = d26,onvalue = 1, offvalue = 0, bg="seashell3")
f27 = Checkbutton(tab4, text = " RFU (b2)", variable = d27,onvalue = 1, offvalue = 0, bg="seashell3")
f28 = Checkbutton(tab4, text = " RFU (b1)", variable = d28,onvalue = 1, offvalue = 0, bg="seashell3")

f21.place(x=500,y=80)
f22.place(x=500,y=110)
f23.place(x=500,y=140)
f24.place(x=500,y=170)
f25.place(x=500,y=200)
f26.place(x=500,y=230)
f27.place(x=500,y=260)
f28.place(x=500,y=290)

# Byte 3

l3_9f6e = Label(tab4,text=" Byte 3 ",font=("Times New Roman", 12, "bold"),bg="seashell3").place(x=200, y=330)
f31 = Checkbutton(tab4, text = " Terminal/Reader is offline only (b8)", variable = d31,onvalue = 1, offvalue = 0, bg="seashell3" )
f32 = Checkbutton(tab4, text = " CVM Required (b7)", variable = d32,onvalue = 1, offvalue = 0, bg="seashell3")
f33 = Checkbutton(tab4, text = " RFU (b6)", variable = d33,onvalue = 1, offvalue = 0, bg="seashell3")
f34 = Checkbutton(tab4, text = " RFU (b5)", variable = d34,onvalue = 1, offvalue = 0, bg="seashell3")
f35 = Checkbutton(tab4, text = " RFU (b4)", variable = d35,onvalue = 1, offvalue = 0, bg="seashell3")
f36 = Checkbutton(tab4, text = " RFU (b3)", variable = d36,onvalue = 1, offvalue = 0, bg="seashell3")
f37 = Checkbutton(tab4, text = " RFU (b2)", variable = d37,onvalue = 1, offvalue = 0, bg="seashell3")
f38 = Checkbutton(tab4, text = " RFU (b1)", variable = d38,onvalue = 1, offvalue = 0, bg="seashell3")

f31.place(x=80,y=360)
f32.place(x=80,y=390)
f33.place(x=80,y=420)
f34.place(x=80,y=450)
f35.place(x=80,y=480)
f36.place(x=80,y=510)
f37.place(x=80,y=540)
f38.place(x=80,y=570)

# Byte 4

l4_9f6e = Label(tab4,text=" Byte 4 ",font=("Times New Roman", 12, "bold"),bg="seashell3").place(x=620, y=330)
f41 = Checkbutton(tab4, text = " Terminal exempt from No CVM checks (b8)", variable = d41,onvalue = 1, offvalue = 0, bg="seashell3" )
f42 = Checkbutton(tab4, text = " Delayed Authorisation Terminal (b7)", variable = d42,onvalue = 1, offvalue = 0, bg="seashell3")
f43 = Checkbutton(tab4, text = " Transit Terminal (b6)", variable = d43,onvalue = 1, offvalue = 0, bg="seashell3")
f44 = Checkbutton(tab4, text = " RFU (b5)", variable = d44,onvalue = 1, offvalue = 0, bg="seashell3")
f45 = Checkbutton(tab4, text = " RFU (b4)", variable = d45,onvalue = 1, offvalue = 0, bg="seashell3")
f46 = Checkbutton(tab4, text = " RFU (b3)", variable = d46,onvalue = 1, offvalue = 0, bg="seashell3")
f47 = Checkbutton(tab4, text = " Expresspay Kernel Version 3.1/C-4 Kernel Version: 2.4-2.6 (b2)", variable = d47,onvalue = 1, offvalue = 0, bg="seashell3")
f48 = Checkbutton(tab4, text = " Expresspay Kernel Version 3.0/C-4 Kernel Version: 2.2-2.3 (b1)", variable = d48,onvalue = 1, offvalue = 0, bg="seashell3")

f41.place(x=500,y=360)
f42.place(x=500,y=390)
f43.place(x=500,y=420)
f44.place(x=500,y=450)
f45.place(x=500,y=480)
f46.place(x=500,y=510)
f47.place(x=500,y=540)
f48.place(x=500,y=570)

note_9f6e = Label(tab4,text=" Note: Expresspay Kernel Version 4.0.x / C-4 Kernel Version: 2.4-2.6 when  B4b2 and B4b1 set to 1 ",fg="blue",font=("Times New Roman", 10),bg="seashell3").place(x=700, y=300)

#------------------------------------------------------------------------------------------------------------------------------

# Tag 9F70 Validation

num_of_bits_9f70  = 16

# Frame Design

tag_9f70_title_1 = Label(tab5, text=" Card Interface and Payment Capabilities ( Tag '9F70' )", bg="purple", fg="white",
                      font=("Times New Roman", 16, "bold"), width=101).place(x=20, y=10)
tag_9f70_left_1 = Label(tab5, bg="purple", height=38).place(x=20, y=40)
tag_9f70_right_1 = Label(tab5, bg="purple", height=38).place(x=1232, y=40)
tag_9f70_end_1 = Label(tab5, bg="purple", font=("", 1), width=1210).place(x=20, y=608)

# tag_9f70 value

tag_9f70_input = Label(tab5, text=" 9F70 Value ", bg="seashell3", font=("Times New Roman", 12, "bold")).place(x=880, y=350)
tag_9f70_value_raw = tk.StringVar()
global tag_9f70_Label
tag_9f70_Label = Entry(tab5, textvariable=tag_9f70_value_raw, font=("Times New Roman", 12), width=25)
tag_9f70_Label.bind('<Return>', lambda _: tag_9f70_validation())
tag_9f70_Label.place(x= 1020, y= 350)
button_tag_9f70 = Button(tab5, text=" Submit ", bg="green2", command=tag_9f70_validation, width=10,font=("Times New Roman", 10, "bold")).place(x=1100, y=450)

# Clear Button

button_btn_tag_9f70 = Button(tab5, text=" Clear ", bg="yellow", command=clear_tag_9f70, width=10,font=("Times New Roman", 10, "bold")).place(x=930, y=450)

g11 = IntVar()
g12 = IntVar()
g13 = IntVar()
g14 = IntVar()
g15 = IntVar()
g16 = IntVar()
g17 = IntVar()
g18 = IntVar()
g21 = IntVar()
g22 = IntVar()
g23 = IntVar()
g24 = IntVar()
g25 = IntVar()
g26 = IntVar()
g27 = IntVar()
g28 = IntVar()

# Byte 1

l1_9f70 = Label(tab5,text=" Byte 1 ",font=("Times New Roman", 12, "bold"),bg="seashell3").place(x=200, y=100)
h11 = Checkbutton(tab5, text = " Keyed Data Entry Supported (b8)", variable = g11,onvalue = 1, offvalue = 0, bg="seashell3")
h12 = Checkbutton(tab5, text = " Physical Magnetic Stripe Supported (b7)", variable = g12,onvalue = 1, offvalue = 0, bg="seashell3")
h13 = Checkbutton(tab5, text = " Contact EMV Interface Supported (b6)", variable = g13,onvalue = 1, offvalue = 0, bg="seashell3")
h14 = Checkbutton(tab5, text = " Contactless EMV Interface Supported (b5)", variable = g14,onvalue = 1, offvalue = 0, bg="seashell3")
h15 = Checkbutton(tab5, text = " Mobile Interface Supported (b4)", variable = g15,onvalue = 1, offvalue = 0, bg="seashell3")
h16 = Checkbutton(tab5, text = " Magstripe Mode Not Supported (b3)", variable = g16,onvalue = 1, offvalue = 0, bg="seashell3")
h17 = Checkbutton(tab5, text = " RFU (b2)", variable = g17,onvalue = 1, offvalue = 0, bg="seashell3")
h18 = Checkbutton(tab5, text = " RFU (b1)", variable = g18,onvalue = 1, offvalue = 0, bg="seashell3")

h11.place(x=80,y=150)
h12.place(x=80,y=200)
h13.place(x=80,y=250)
h14.place(x=80,y=300)
h15.place(x=80,y=350)
h16.place(x=80,y=400)
h17.place(x=80,y=450)
h18.place(x=80,y=500)

# Byte 2

l2_9f70 = Label(tab5,text=" Byte 2 ",font=("Times New Roman", 12, "bold"),bg="seashell3").place(x=590, y=100)
h21 = Checkbutton(tab5, text = " Delayed authorisation usage information present (b8)", variable = g21,onvalue = 1, offvalue = 0, bg="seashell3" )
h22 = Checkbutton(tab5, text = " Valid at domestic terminals performing contactless delayed authorisation (b7)", variable = g22,onvalue = 1, offvalue = 0, bg="seashell3")
h23 = Checkbutton(tab5, text = " Valid at international terminals performing contactless delayed authorisation (b6)", variable = g23,onvalue = 1, offvalue = 0, bg="seashell3")
h24 = Checkbutton(tab5, text = " RFU (b5)", variable = g24,onvalue = 1, offvalue = 0, bg="seashell3")
h25 = Checkbutton(tab5, text = " No Dynamic Limit Set information available (b4)", variable = g25,onvalue = 1, offvalue = 0, bg="seashell3")
h26 = Checkbutton(tab5, text = " Dynamic limit set (b3)", variable = g26,onvalue = 1, offvalue = 0, bg="seashell3")
h27 = Checkbutton(tab5, text = " Dynamic limit set (b2)", variable = g27,onvalue = 1, offvalue = 0, bg="seashell3")
h28 = Checkbutton(tab5, text = " Dynamic limit set (b1)", variable = g28,onvalue = 1, offvalue = 0, bg="seashell3")

h21.place(x=420,y=150)
h22.place(x=420,y=200)
h23.place(x=420,y=250)
h24.place(x=420,y=300)
h25.place(x=420,y=350)
h26.place(x=420,y=400)
h27.place(x=420,y=450)
h28.place(x=420,y=500)

# ---------------------------------------------------------------------------------------------------------------------

# AIP Validation

num_of_bits_82  = 16

# Frame Design

tag_82_title_1 = Label(tab6, text=" Application Interchange Profile ( Tag '82' )", bg="purple", fg="white",
                      font=("Times New Roman", 16, "bold"), width=101).place(x=20, y=10)
tag_82_left_1 = Label(tab6, bg="purple", height=38).place(x=20, y=40)
tag_82_right_1 = Label(tab6, bg="purple", height=38).place(x=1232, y=40)
tag_82_end_1 = Label(tab6, bg="purple", font=("", 1), width=1210).place(x=20, y=608)

# tag_82 value

tag_82_input = Label(tab6, text=" AIP Value ", bg="seashell3", font=("Times New Roman", 12, "bold")).place(x=830, y=450)
tag_82_value_raw = tk.StringVar()
global tag_82_Label
tag_82_Label = Entry(tab6, textvariable=tag_82_value_raw, font=("Times New Roman", 12), width=25)
tag_82_Label.bind('<Return>', lambda _: tag_82_validation())
tag_82_Label.place(x= 970, y= 450)
button_tag_82 = Button(tab6, text=" Submit ", bg="green2", command=tag_82_validation, width=10,font=("Times New Roman", 10, "bold")).place(x=1050, y=550)

# Mode validation

mode_label  = Label(tab6, text="Transaction Mode", bg="seashell3", font=("Times New Roman", 12, "bold")).place(x=810, y=300)
global mode_result
mode_result = Label(tab6, text=" ", fg ="blue",bg ="white", font=("Times New Roman", 12, "bold"),width=22)
mode_result.place(x=970, y=300)

# Clear Button

button_btn_tag_82 = Button(tab6, text=" Clear ", bg="yellow", command=clear_tag_82, width=10,font=("Times New Roman", 10, "bold")).place(x=880, y=550)

i11 = IntVar()
i12 = IntVar()
i13 = IntVar()
i14 = IntVar()
i15 = IntVar()
i16 = IntVar()
i17 = IntVar()
i18 = IntVar()
i21 = IntVar()
i22 = IntVar()
i23 = IntVar()
i24 = IntVar()
i25 = IntVar()
i26 = IntVar()
i27 = IntVar()
i28 = IntVar()

# Byte 1

l1_82 = Label(tab6,text=" Byte 1 ",font=("Times New Roman", 12, "bold"),bg="seashell3").place(x=200, y=100)
j11 = Checkbutton(tab6, text = " RFU (b8)", variable = i11,onvalue = 1, offvalue = 0, bg="seashell3")
j12 = Checkbutton(tab6, text = " SDA supported (b7)", variable = i12,onvalue = 1, offvalue = 0, bg="seashell3")
j13 = Checkbutton(tab6, text = " DDA supported (b6)", variable = i13,onvalue = 1, offvalue = 0, bg="seashell3")
j14 = Checkbutton(tab6, text = " Cardholder verification supported (b5)", variable = i14,onvalue = 1, offvalue = 0, bg="seashell3")
j15 = Checkbutton(tab6, text = " Terminal Risk Management is to be performed (b4)", variable = i15,onvalue = 1, offvalue = 0, bg="seashell3")
j16 = Checkbutton(tab6, text = " Issuer Authentication is supported (b3)", variable = i16,onvalue = 1, offvalue = 0, bg="seashell3")
j17 = Checkbutton(tab6, text = " Reserved for use by EMV Contactless Specifications (b2)", variable = i17,onvalue = 1, offvalue = 0, bg="seashell3")
j18 = Checkbutton(tab6, text = " CDA supported (b1)", variable = i18,onvalue = 1, offvalue = 0, bg="seashell3")

j11.place(x=80,y=150)
j12.place(x=80,y=200)
j13.place(x=80,y=250)
j14.place(x=80,y=300)
j15.place(x=80,y=350)
j16.place(x=80,y=400)
j17.place(x=80,y=450)
j18.place(x=80,y=500)

# Byte 2

l2_82 = Label(tab6,text=" Byte 2 ",font=("Times New Roman", 12, "bold"),bg="seashell3").place(x=620, y=100)
j21 = Checkbutton(tab6, text = " EMV and Mag-Stripe Modes Supported (b8)", variable = i21,onvalue = 1, offvalue = 0, bg="seashell3" )
j22 = Checkbutton(tab6, text = " Expresspay/Contactless Mobile supported (b7)", variable = i22,onvalue = 1, offvalue = 0, bg="seashell3")
j23 = Checkbutton(tab6, text = " Expresspay Mobile HCE/HCE is supported (b6)", variable = i23,onvalue = 1, offvalue = 0, bg="seashell3")
j24 = Checkbutton(tab6, text = " RFU (b5)", variable = i24,onvalue = 1, offvalue = 0, bg="seashell3")
j25 = Checkbutton(tab6, text = " RFU (b4)", variable = i25,onvalue = 1, offvalue = 0, bg="seashell3")
j26 = Checkbutton(tab6, text = " RFU (b3)", variable = i26,onvalue = 1, offvalue = 0, bg="seashell3")
j27 = Checkbutton(tab6, text = " RFU (b2)", variable = i27,onvalue = 1, offvalue = 0, bg="seashell3")
j28 = Checkbutton(tab6, text = " RFU (b1)", variable = i28,onvalue = 1, offvalue = 0, bg="seashell3")

j21.place(x=500,y=150)
j22.place(x=500,y=200)
j23.place(x=500,y=250)
j24.place(x=500,y=300)
j25.place(x=500,y=350)
j26.place(x=500,y=400)
j27.place(x=500,y=450)
j28.place(x=500,y=500)

# --------------------------------------------------------------------------------------------------------------------

# 9F6d abd 9F71 validation

tag_9f6d_title_1 = Label(tab7, text=" Contactless Reader Capabilities ( Tag '9F6D' )", bg="purple", fg="white",
                      font=("Times New Roman", 16, "bold"), width=46).place(x=20, y=10)
tag_9f6d_left_1 = Label(tab7, bg="purple", height=38).place(x=20, y=40)
tag_9f6d_right = Label(tab7, bg="purple", height=38).place(x=572, y=40)
tag_9f6d_end_1 = Label(tab7, bg="purple", font=("", 1), width=546).place(x=20, y=608)

tag_9f71_title_1 = Label(tab7, text=" Mobile CVM Results ( Tag '9F71' )", bg="purple", fg="white",
                      font=("Times New Roman", 16, "bold"), width=51).place(x=620, y=10)
tag_9f71_left_1 = Label(tab7, bg="purple", height=38).place(x=620, y=40)
tag_9f71_right_1 = Label(tab7, bg="purple", height=38).place(x=1232, y=40)
tag_9f71_end_1 = Label(tab7, bg="purple", font=("", 1), width=606).place(x=620, y=608)

# 9f6d validation
global num_of_bits_9f6d
num_of_bits_9f6d =8
input_9f6d = Label(tab7,text=" 9F6D Value ",font=("Times New Roman", 12, "bold"),bg="seashell3").place(x=40, y=80)
tag_9f6d_raw = StringVar()
global tag_9f6d_Label
tag_9f6d_Label = Entry(tab7, textvariable= tag_9f6d_raw, font=("Times New Roman", 12), width=15)
tag_9f6d_Label.place(x=180, y=80)
input_9f6d_meaning_label = Label(tab7,text=" Meaning ",font=("Times New Roman", 12, "bold"),bg="seashell3").place(x=40, y=180)
global input_9f6d_meaning
input_9f6d_meaning = Label(tab7, text=' ', bg="white", fg="green",font=("Times New Roman", 12, "bold"), width=41)
input_9f6d_meaning.place(x=180, y=180)
button5_9f6d = Button(tab7, text=" Submit ", bg="green2", command=tag_9f6d_validation, width=10,font=("Times New Roman", 10, "bold")).place(x=400, y=330)
button6_9f6d = Button(tab7, text=" Clear ", bg="yellow", command=tag_9f6d_clear, width=10, font=("Times New Roman", 10, "bold")).place(x=150, y=330)

#9f70 validation

global num_of_bits_9f71
num_of_bits_9f71 =24

input_9f71 = Label(tab7,text=" 9F70 Value ",font=("Times New Roman", 12, "bold"),bg="seashell3").place(x=650, y=80)
tag_9f71_raw = StringVar()
global tag_9f71_Label
tag_9f71_Label = Entry(tab7, textvariable= tag_9f71_raw, font=("Times New Roman", 12), width=15)
tag_9f71_Label.place(x=800, y=80)
input_9f71_meaning_byte1_1 = Label(tab7,text=" Byte 1 Meaning ",font=("Times New Roman", 12, "bold"),bg="seashell3").place(x=650, y=180)
global input_9f71_meaning_byte1
input_9f71_meaning_byte1 = Label(tab7, text=' ', bg="white",fg ="green", font=("Times New Roman", 12, "bold"), width=45)
input_9f71_meaning_byte1.place(x=800, y=180)
input_9f71_meaning_byte2_2 = Label(tab7,text=" Byte 2 Meaning ",font=("Times New Roman", 12, "bold"),bg="seashell3").place(x=650, y=280)
global input_9f71_meaning_byte2
input_9f71_meaning_byte2 = Label(tab7, text=' ', bg="white", fg ="green",font=("Times New Roman", 12, "bold"), width=45)
input_9f71_meaning_byte2.place(x=800, y=280)
input_9f71_meaning_byte3_3 = Label(tab7,text=" Byte 3 Meaning ",font=("Times New Roman", 12, "bold"),bg="seashell3").place(x=650, y=380)
global input_9f71_meaning_byte3
input_9f71_meaning_byte3 = Label(tab7, text=' ', bg="white", fg ="green",font=("Times New Roman", 12, "bold"), width=45)
input_9f71_meaning_byte3.place(x=800, y=380)

button5_9f71 = Button(tab7, text=" Submit ", bg="green2", command= tag_9f71_validation, width=10,font=("Times New Roman", 10, "bold")).place(x=1100, y=530)
button6_9f71 = Button(tab7, text=" Clear ", bg="yellow", command= tag_9f71_clear , width=10, font=("Times New Roman", 10, "bold")).place(x=750, y=530)

tab_control.pack(expand=1, fill='both')
window.mainloop()
#window.mainloop()
