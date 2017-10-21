"""
Creates a right click popup menu
"""

import tkinter as tk
from tkinter import Frame, Entry, END, INSERT


class Popup(Frame):
    """
    Creates two types of popup menus

    entry_popup  - Only works with Entry Widgets
    text_pop     - Only works with Textbox Widgets
    """
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.entry_text = ''
        self.textbox_text = ''

        # Create 3 buttons for th entry_popup menu
        self.entry_widget = tk.Menu(self, tearoff=0, relief='sunken')
        self.entry_widget.add_command(label="Copy", command=self.entry_copy)
        self.entry_widget.add_separator()
        self.entry_widget.add_command(label="Paste", command=self.entry_paste)
        self.entry_widget.add_separator()
        self.entry_widget.add_command(label="Clear", command=self.entry_clear)

        # Create 3 buttons for th text_popup menu
        self.text_widget = tk.Menu(self, tearoff=0, relief='sunken')
        self.text_widget.add_command(label="Copy", command=self.text_copy)
        self.text_widget.add_separator()
        self.text_widget.add_command(label="Paste", command=self.text_paste)
        self.text_widget.add_separator()
        self.text_widget.add_command(label="Clear", command=self.text_clear)

    # Methods for the the popup menu's
    def entry_popup(self, event):
        """ Creates the popup menu for Entry widgets """
        self.entry_widget.post(event.x_root, event.y_root)

    def text_popup(self, event):
        """ Creates the popup menu for Textbox widgets """
        self.text_widget.post(event.x_root, event.y_root)

    # Methods used by the popup menu items
    def entry_copy(self, event=None):
        """ Copies all text from the Entry Widget to clipboard"""
        self.clipboard_clear()
        text = self.entry_text.get()
        self.clipboard_append(text)

    def entry_paste(self):
        """ Pastes text from cliboard """
        self.entry_text.set(self.clipboard_get())

    def entry_clear(self):
        """ Clears all contents in the Entry widget """
        self.entry_text.set('')

    def text_copy(self, event=None):
        """ Copies selected text from the Textbox Widget to clipboard"""
        self.clipboard_clear()
        text = self.textbox_text.get("sel.first", "sel.last")
        self.clipboard_append(text)

    def text_paste(self):
        """ Pastes text from cliboard """
        self.textbox_text.insert(INSERT, self.clipboard_get())

    def text_clear(self):
        """ Clears all contents in the Textbox widget """
        self.textbox_text.delete(1.0, END)
