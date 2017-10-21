"""
PyRegexEvaluator  -- A tool to test and improve
                     your python regular expressions

Created by Jack Ackermann
"""

import tkinter as tk
from tkinter import Tk, ttk, Frame, FALSE, Text, Button, \
    Scrollbar, Entry, END, INSERT, messagebox, Checkbutton

from libs.popup import Popup
from libs.highlighter import Highlighter


class PyRegexEvaluator(Frame):

    def centre_window(self):
        """ Display's your gui in the centre of the screen """
        w = 685     # Sets your gui's width
        h = 635     # Sets your gui's height
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - w) // 2   # Use integer devision to avoid having to convert
        y = (sh - h) // 2   # float to int
        self.root.geometry('{:d}x{:d}+{:d}+{:d}'.format(w, h, x, y))

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.centre_window()
        centre_title_text = (' ' * 40)  # Uses spaces to center Title
        title_text = 'Python Regular Expression Checker  -  By Jack Ackermann'
        self.root.title(centre_title_text + title_text)
        self.root.iconbitmap('images\icon.ico')
        self.grid(column=0, row=0, sticky='nsew', padx=12, pady=5)

        # Entry widget and Label Section
        label_text = 'Please enter regex expression to find: '
        self.regex_label = tk.Label(self, text=label_text)
        self.regex_label.grid(row=0, column=0, sticky="w", pady=15)

        self.regex_pattern = tk.StringVar()
        self.regex_string = Entry(self, textvariable=self.regex_pattern)
        self.regex_string.config(borderwidth=2, relief='sunken', width=70)
        self.regex_string.grid(row=0, column=0, sticky="e", pady=15)

        # Data widget and Label Section. Data to be searched.
        label_data1 = 'Enter data below that you want to search.  '
        label_data2 = 'Results are then highlighted using re.finditer'
        self.data_label = tk.Label(self, text=label_data1 + label_data2)
        self.data_label.grid(row=1, column=0, sticky="w")

        self.data_textbox = Text(self, borderwidth=2, relief='sunken')
        self.data_textbox.config(height=15, width=80)
        self.data_textbox.grid(row=2, column=0, sticky="new")
        self.scrollbar = Scrollbar(self, command=self.data_textbox.yview)
        self.scrollbar.grid(row=2, column=1, sticky='ns')
        self.data_textbox['yscrollcommand'] = self.scrollbar.set

        # Display regex results and Label section
        label_output = 'All the matches below were found using re.findall'
        self.label_output = tk.Label(self, text=label_output)
        self.label_output.grid(row=3, column=0, sticky="w")

        self.output_textbox = Text(self, borderwidth=2, relief='sunken')
        self.output_textbox.config(height=15, width=80)
        self.output_textbox.grid(row=4, column=0, sticky="new")
        self.scrollbar2 = Scrollbar(self, command=self.output_textbox.yview)
        self.scrollbar2.grid(row=4, column=1, sticky='ns')
        self.output_textbox['yscrollcommand'] = self.scrollbar2.set

        # Create Two Button Widgets
        self.find_btn = ttk.Button(self, text='Find', command=self.on_find)
        self.find_btn.grid(row=5, sticky='E')
        self.exit_btn = ttk.Button(self, text='Exit', command=self.on_exit)
        self.exit_btn.grid(row=5, column=0, sticky='W', pady=15)

        # Create a Checkbutton Widget
        self.auto_var = tk.IntVar()
        self.auto_find = Checkbutton(self, variable=self.auto_var,
                                     command=self.on_auto, background='pink')
        self.auto_find.config(text='Turns on Auto Search as you type')
        self.auto_find.grid(row=5, column=0, sticky='')
        self.auto_find.deselect()

        # Instanciate the imported popup class
        self.popup = Popup(parent)
        self.popup.entry_text = self.regex_pattern
        self.popup.textbox_text = self.data_textbox
        self.popup2 = Popup(parent)
        self.popup2.textbox_text = self.output_textbox

        # Bind the popup menus and Enter Key to the appropriate widgets.
        self.regex_string.bind("<Button-3>", self.popup.entry_popup)
        self.data_textbox.bind("<Button-3>", self.popup.text_popup)
        self.output_textbox.bind("<Button-3>", self.popup2.text_popup)
        self.regex_string.bind("<Return>", lambda _: self.on_find())

    # Method for the find_btn, <Return> bind and Checkbutton
    def on_find(self, a=None, b=None, c=None):
        """
        Takes three arguments with default values: a, b, c
        These arguments are needed for the trace method of StringVar()

        Instanciate and use the Highlighter class
        """
        self.highlighter = Highlighter(self.regex_pattern, self.data_textbox,
                                       self.output_textbox)
        self.highlighter.find_matches()

    # Method for the self.auto_find checkbutton
    def on_auto(self):
        """
        If the self.auto_find Checkbox is selected,
        the find button is disabled and the <Return> key is unbound
        The self.regex_pattern.trace is created that calls the on_find
        method everytime the variable changes.

        If the self.auto_find Checkbox is unselected,
        the find button gets re-enabled and the <Return> key bind is set.
        And the self.regex_pattern.trace is deleted
        """
        trace_id = ''
        if self.auto_var.get() == 1:
            self.find_btn.config(state='disabled')
            self.regex_string.unbind("<Return>")
            self.regex_pattern.trace_id = self.regex_pattern.trace("w", self.on_find)
        else:
            self.find_btn.config(state='enabled')
            self.regex_string.bind("<Return>", lambda _: self.on_find())
            self.regex_pattern.trace_vdelete("w", self.regex_pattern.trace_id)

    # Exits the program. Linked to the Exit Button
    def on_exit(self):
        self.root.destroy()


def main():
    root = Tk()
    root.resizable(width=FALSE, height=FALSE)
    # root.configure(background="black")
    PyRegexEvaluator(root)
    root.mainloop()


if __name__ == '__main__':
    main()
