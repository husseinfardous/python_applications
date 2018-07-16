# Database Application
# Bookstore

# Stores Title, Author, Year, ISBN

""" 
Users may:

View All Entries
Search for Entry
Add Entry
Update Entry
Delete Entry
Close
"""

# Import Modules
from tkinter import *
import backend



# Retrieve Selected Row in the Listbox
# Helper Function for update() and delete() Functions Below
def get_selected_row(event):

    try:

        global selected_row
        index = book_list.curselection()[0]
        selected_row = book_list.get(index)

        # Fill Entries with Data of Selected Row

        title_entry.delete(0, END)
        title_entry.insert(END, selected_row[1])

        author_entry.delete(0, END)
        author_entry.insert(END, selected_row[2])

        year_entry.delete(0, END)
        year_entry.insert(END, selected_row[3])

        isbn_entry.delete(0, END)
        isbn_entry.insert(END, selected_row[4])

    except IndexError:
        pass



# Button Commands that Call Corresponding Backend Functions

# View All Entries Button -> backend.view()
def view_command():

    # Prevent Spam from Repetitive Button Clicks
    book_list.delete(0, END)

    # Display All Entries in the Listbox
    for row in backend.view():
        book_list.insert(END, row)

# Search for Entry Button -> backend.search()
def search_command():

    # Delete Entries from Previous Button Clicks
    book_list.delete(0, END)

    # Display Book(s) that match the Query in the Listbox
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        book_list.insert(END, row)

# Add Entry Button -> backend.add()
def add_command():

    backend.add(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

    # Delete Entries from Previous Button Clicks and Display Added Entry
    book_list.delete(0, END)
    book_list.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

# Update Entry Button -> backend.update()
def update_command():
    backend.update(selected_row[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

# Delete Entry Button -> backend.delete()
def delete_command():
    backend.delete(selected_row[0])



# Create Frontend Interface Window
window = Tk()
window.wm_title("Bookstore")



# Create Frontend Interface Labels

# Title Label
title_label = Label(window, text = "Title")
title_label.grid(row = 0, column = 0)

# Author Label
author_label = Label(window, text = "Author")
author_label.grid(row = 0, column = 2)

# Year Label
year_label = Label(window, text = "Year")
year_label.grid(row = 1, column = 0)

# ISBN Label
isbn_label = Label(window, text = "ISBN")
isbn_label.grid(row = 1, column = 2)



# Create Frontend Interface Entries

# Title Entry
title_text = StringVar()
title_entry = Entry(window, textvariable = title_text)
title_entry.grid(row = 0, column = 1)

# Author Entry
author_text = StringVar()
author_entry = Entry(window, textvariable = author_text)
author_entry.grid(row = 0, column = 3)

# Year Entry
year_text = StringVar()
year_entry = Entry(window, textvariable = year_text)
year_entry.grid(row = 1, column = 1)

# ISBN Entry
isbn_text = StringVar()
isbn_entry = Entry(window, textvariable = isbn_text)
isbn_entry.grid(row = 1, column = 3)



# Create Frontend Interface Listbox

# Listbox
book_list = Listbox(window, height = 6, width = 35)
book_list.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

# Listbox Scrollbar
scrollbar = Scrollbar(window)
scrollbar.grid(row = 2, column = 2, rowspan = 6)

# Configuring Listbox and Scrollbar
book_list.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command = book_list.yview)

# Bind get_selected_row() to Widget Event (Select a Row in Listbox)
book_list.bind("<<ListboxSelect>>", get_selected_row)



# Create Frontend Interface Buttons

# View All Entries Button
view = Button(window, text = "View All Entries", width = 12, command = view_command)
view.grid(row = 2, column = 3)

# Search for Entry Button
search = Button(window, text = "Search for Entry", width = 12, command = search_command)
search.grid(row = 3, column = 3)

# Add Entry Button
add = Button(window, text = "Add Entry", width = 12, command = add_command)
add.grid(row = 4, column = 3)

# Update Entry Button
update = Button(window, text = "Update Entry", width = 12, command = update_command)
update.grid(row = 5, column = 3)

# Delete Entry Button
delete = Button(window, text = "Delete Entry", width = 12, command = delete_command)
delete.grid(row = 6, column = 3)

# Close Button
close = Button(window, text = "Close", width = 12, command = window.destroy)
close.grid(row = 7, column = 3)



# Wait for Events and Update the Graphical User Interface (GUI)
window.mainloop()
