import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tabulate import tabulate


class MenuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SUSAN'S VILLA HOTEL RESORT RESERVATION")

        # Create and configure the main frame
        self.main_frame = tk.Frame(root, padx=20, pady=20)
        self.main_frame.pack()

        # Create labels, buttons, and text box for user interaction
        self.title_label = tk.Label(self.main_frame, text="SUSAN'S VILLA HOTEL RESORT RESERVATION",
                                    font=("Arial", 16, "bold"))
        self.title_label.pack()

        self.menu_label = tk.Label(self.main_frame, text="System Menu:", font=("Arial", 12, "bold"))
        self.menu_label.pack()

        self.button_frame = tk.Frame(self.main_frame)  # Frame to hold the buttons
        self.button_frame.pack()

        self.reservations = []  # List to store reservation data

        self.create_button("A. View all Reservations", self.view_reservations)
        self.create_button("B. Make Reservation", self.make_reservation)
        self.create_button("C. Delete Reservation", self.delete_reservation)
        self.create_button("D. Generate Report", self.generate_report)
        self.create_button("E. Cancel Reservation", self.cancel_reservation)
        self.create_button("F. Exit", self.exit_program)

        self.output_text = ScrolledText(self.main_frame, width=70, height=10, font=("Arial", 10))
        self.output_text.pack()

    def create_button(self, text, command):
        button = tk.Button(self.button_frame, text=text, font=("Arial", 12), command=command)
        button.pack(side=tk.LEFT, padx=5)

    def view_reservations(self):
        self.output_text.delete("1.0", tk.END)
        table_data = []
        for i, reservation in enumerate(self.reservations, start=1):
            reservation_data = [i, *reservation]
            table_data.append(reservation_data)
        table = tabulate(table_data, headers=["No.", "Name", "Date", "Time", "Adults", "Children"], tablefmt="presto")
        self.output_text.insert(tk.END, table)

    def make_reservation(self):
        # Create the make reservation form window
        reservation_window = tk.Toplevel(self.root)
        reservation_window.title("Make Reservation")

        # Create and configure the form frame
        form_frame = tk.Frame(reservation_window, padx=20, pady=20)
        form_frame.pack()

        # Create labels and entry fields for the form
        name_label = tk.Label(form_frame, text="Name:", font=("Arial", 12))
        name_label.grid(row=0, column=0, sticky=tk.W)
        name_entry = tk.Entry(form_frame, font=("Arial", 12))
        name_entry.grid(row=0, column=1)

        date_label = tk.Label(form_frame, text="Date:", font=("Arial", 12))
        date_label.grid(row=1, column=0, sticky=tk.W)
        date_entry = tk.Entry(form_frame, font=("Arial", 12))
        date_entry.grid(row=1, column=1)

        time_label = tk.Label(form_frame, text="Time:", font=("Arial", 12))
        time_label.grid(row=2, column=0, sticky=tk.W)
        time_entry = tk.Entry(form_frame, font=("Arial", 12))
        time_entry.grid(row=2, column=1)

        adults_label = tk.Label(form_frame, text="No. of Adults:", font=("Arial", 12))
        adults_label.grid(row=3, column=0, sticky=tk.W)
        adults_entry = tk.Entry(form_frame, font=("Arial", 12))
        adults_entry.grid(row=3, column=1)

        children_label = tk.Label(form_frame, text="No. of Children:", font=("Arial", 12))
        children_label.grid(row=4, column=0, sticky=tk.W)
        children_entry = tk.Entry(form_frame, font=("Arial", 12))
        children_entry.grid(row=4, column=1)

        # Create the submit button
        submit_button = tk.Button(form_frame, text="Submit", command=lambda: self.execute_reservation(
            reservation_window, name_entry.get(), date_entry.get(), time_entry.get(), adults_entry.get(),
            children_entry.get()
        ))
        submit_button.grid(row=5, column=0, columnspan=2, pady=10)

    def execute_reservation(self, reservation_window, name, date, time, adults, children):
        if not name or not date or not time or not adults or not children:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            adults = int(adults)
            children = int(children)
        except ValueError:
            messagebox.showerror("Error", "Invalid number of adults or children.")
            return

        # Save the reservation data
        reservation_data = [name, date, time, adults, children]
        self.reservations.append(reservation_data)

        messagebox.showinfo("Info", "Reservation is complete.")
        reservation_window.destroy()

    #def delete_reservation(self):
        #self.output_text.delete("1.0", tk.END)
        #self.reservations = []  # Clear all reservations
        #messagebox.showinfo("Info", "All reservations have been deleted.")

    def delete_reservation(self):
        # Create the delete reservation form window
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Reservation")

        # Create and configure the form frame
        form_frame = tk.Frame(delete_window, padx=20, pady=20)
        form_frame.pack()

        # Create labels and entry fields for the form
        number_label = tk.Label(form_frame, text="Reservation Number:", font=("Arial", 12))
        number_label.grid(row=0, column=0, sticky=tk.W)
        number_entry = tk.Entry(form_frame, font=("Arial", 12))
        number_entry.grid(row=0, column=1)

        # Create the submit button
        submit_button = tk.Button(form_frame, text="Submit", command=lambda: self.execute_delete(
        delete_window, number_entry.get()
        ))
        submit_button.grid(row=1, column=0, columnspan=2, pady=10)

    def execute_delete(self, delete_window, number):
        if not number:
            messagebox.showerror("Error", "Please enter the reservation number.")
        return

        try:
            number = int(number)
        except ValueError:
            messagebox.showerror("Error", "Invalid reservation number.")
        return

        if 1 <= number <= len(self.reservations):
            eleted_reservation = self.reservations[number - 1]
            del self.reservations[number - 1]
            messagebox.showinfo("Info", f"Reservation {number} ({deleted_reservation[0]}) has been deleted.")
        else:
            messagebox.showerror("Error", f"Reservation number {number} does not exist.")

        delete_window.destroy()
        self.view_reservations()  # Update the reservations view after deletion

    def generate_report(self):
        self.output_text.delete("1.0", tk.END)
        table_data = []
        for i, reservation in enumerate(self.reservations, start=1):
            reservation_data = [i, *reservation]
            table_data.append(reservation_data)
        table = tabulate(table_data, headers=["No.", "Name", "Date", "Time", "Adults", "Children"], tablefmt="presto")
        self.output_text.insert(tk.END, table)

    def cancel_reservation(self):
        cancel_window = tk.Toplevel(self.root)
        cancel_window.title("Cancel Reservation")
        name_label = tk.Label(cancel_window, text="Enter your name to cancel the reservation:")
        name_label.pack()
        name_entry = tk.Entry(cancel_window)
        name_entry.pack()
        cancel_button = tk.Button(cancel_window, text="Cancel Reservation",
                                  command=lambda: self.execute_cancel(name_entry.get()))
        cancel_button.pack()

    def execute_cancel(self, name):
        # Find and remove the reservation with the given name
        self.reservations = [reservation for reservation in self.reservations if reservation[0] != name]
        messagebox.showinfo("Info", "Reservation cancelled successfully.")
        self.view_reservations()  # Update the reservations view after cancellation

    def exit_program(self):
        result = messagebox.askyesno("Confirmation", "Are you sure you want to exit?")
        if result:
            self.root.destroy()


# Create the main window
root = tk.Tk()
menu_gui = MenuGUI(root)

# Start the application
root.mainloop()