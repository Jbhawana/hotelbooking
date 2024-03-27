
import tkinter as tk
from tkinter import messagebox
# import pymysql
window = tk.Tk()
window.title("Hotel Booking System")



# Function to book a room
def book_room():
    guest_name = guest_name_entry.get()
    check_in_date = check_in_date_entry.get()
    check_out_date = check_out_date_entry.get()
    room_price = room_price_entry.get()
    room_type = room_type_var.get()


    messagebox.showinfo("Booking Confirmation", "Room booked successfully!")
    # clear_entries()

# Function to clear entry fields
def clear_entries():
    guest_name_entry.delete(0, tk.END)
    check_in_date_entry.delete(0, tk.END)
    check_out_date_entry.delete(0, tk.END)
    room_price_entry.delete(0, tk.END)
    room_type_var.set(room_types[0])

# Create labels and entry widgets
guest_name_label = tk.Label(window, text="Guest Name:")
guest_name_entry = tk.Entry(window)

check_in_date_label = tk.Label(window, text="Check-in Date:")
check_in_date_entry = tk.Entry(window)

check_out_date_label = tk.Label(window, text="Check-out Date:")
check_out_date_entry = tk.Entry(window)

room_price_label = tk.Label(window, text="Room Price:")
room_price_entry = tk.Entry(window)

room_type_label = tk.Label(window, text="Room Type:")
room_types = ["Single", "Double", "Suite"]
room_type_var = tk.StringVar(window)
room_type_var.set(room_types[0])
room_type_option_menu = tk.OptionMenu(window, room_type_var, *room_types)

# Create a Book Room button
book_button = tk.Button(window, text="Book Room", command=book_room)


# Place widgets on the window
guest_name_label.grid(row=0, column=0)
guest_name_entry.grid(row=0, column=1)

check_in_date_label.grid(row=1, column=0)
check_in_date_entry.grid(row=1, column=1)

check_out_date_label.grid(row=2, column=0)
check_out_date_entry.grid(row=2, column=1)

room_price_label.grid(row=3, column=0)
room_price_entry.grid(row=3, column=1)

room_type_label.grid(row=4, column=0)
room_type_option_menu.grid(row=4, column=1)

book_button.grid(row=5, column=0, columnspan=2)




# Start the tkinter main loop
window.mainloop()
