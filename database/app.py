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



# Create Frontend Interface Window
window = Tk()



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



# Create Frontend Interface Buttons

# View All Entries Button
view = Button(window, text = "View All Entries", width = 12)
view.grid(row = 2, column = 3)

# Search for Entry Button
search = Button(window, text = "Search for Entry", width = 12)
search.grid(row = 3, column = 3)

# Add Entry Button
add = Button(window, text = "Add Entry", width = 12)
add.grid(row = 4, column = 3)

# Update Entry Button
update = Button(window, text = "Update Entry", width = 12)
update.grid(row = 5, column = 3)

# Delete Entry Button
delete = Button(window, text = "Delete Entry", width = 12)
delete.grid(row = 6, column = 3)

# Close Button
close = Button(window, text = "Close", width = 12)
close.grid(row = 7, column = 3)



# Wait for Events and Update the Graphical User Interface (GUI)
window.mainloop()
