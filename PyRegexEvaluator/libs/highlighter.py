"""
Textbox text highlighter.

Takes a string or regex expression as input.
All matches that are found, get highlighted.

Created by Jack Ackermann
"""

import re
import tkinter as tkinter
from tkinter import Tk, Frame, END, INSERT


class Highlighter(Frame):
    """
    Class takes in3 arguments: regex_pattern, data_textbox, output_textbox

    Highlights all matches for re.finditer

    Inserts all found re.findall matches into a Text box
    """

    def __init__(self, regex_pattern, data_textbox, output_textbox,
                 *args, **kwargs):
        self.regex_pattern = regex_pattern
        self.data_textbox = data_textbox
        self.output_textbox = output_textbox
        # Setup a tag to highlight the found word  in red
        self.data_textbox.tag_configure("highlight", background="light blue",
                                        foreground="red")

    def find_matches(self):
        """
        Makes sure all tags and found data is cleared before search begins

        Highlights all re.findinter matches found in the data_textbox

        Inserts all re.findall matches found inside the output_textbox
        """

        # Clears tags and data before every search
        self.data_textbox.tag_remove("highlight", 1.0, END)
        self.output_textbox.delete(1.0, END)

        line_no = 0
        keyword = self.regex_pattern.get()
        data = self.data_textbox.get(1.0, END)

        if len(keyword) == 0:
            pass
            # messagebox.showwarning('No Regex Pattern to find',
            #                        'Please enter a regex expression to match')
        else:
            for lines in data.split('\n'):
                line_no += 1
                for m in re.finditer(r'{}'.format(keyword), lines):
                    #print('{0}.{1}, {0}.{2}'.format(line_no, m.start(), m.end()))
                    self.data_textbox.tag_add("highlight",
                                              '{0}.{1}'.format(line_no,
                                                               m.start()),
                                              '{0}.{1}'.format(line_no,
                                                               m.end()))
            find_text = re.findall(keyword, data)
            for items in find_text:
                self.output_textbox.insert(INSERT, items + '\n')
