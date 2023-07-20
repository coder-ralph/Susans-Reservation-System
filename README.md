# SUSAN'S VILLA HOTEL RESORT RESERVATION

Welcome to Susan's Villa Hotel Resort Reservation system! This reservation system allows you to book and manage hotel reservations. The system has a simple graphical user interface (GUI) and a console-based menu that provides various functionalities for managing reservations.

## How to Run the Program

To run the reservation system, make sure you have Python installed on your computer. The GUI-based part of the system is implemented in `main.py`, while the console-based part is implemented in `gui.py`. Follow these steps to run the program:

1. Make sure you have installed the required packages. You can install them using `pip`:

```bash
pip install tkinter tabulate
```

2. Save the `main.py` and `gui.py` files to a folder on your computer.

3. Open a terminal or command prompt and navigate to the folder containing the two files.

4. Run the program by executing `main.py`:

```bash
python main.py
```

5. The program will start, and you will see the main menu with various options for managing reservations.

## Main Features

### Graphical User Interface (GUI)

The GUI-based part of the program (`main.py`) provides a user-friendly interface for interacting with the reservation system. The GUI window displays the title of the system and a menu with buttons for different actions:

1. View all Reservations: Displays a table of all current reservations.
2. Make Reservation: Allows you to create a new reservation by filling in the required information in a separate window.
3. Delete Reservation: Provides a form to enter the reservation number and delete the corresponding reservation.
4. Generate Report: Displays a summary report of the most recent reservation.
5. Cancel Reservation: Provides a form to enter your name and cancel the reservation associated with it.
6. Exit: Closes the application.

### Console-based Menu (gui.py)

The console-based part of the program (`gui.py`) offers similar functionality to the GUI-based part but is implemented with a menu that appears in the terminal or command prompt. The console menu provides the following options:

1. View all Reservations: Shows a table of all current reservations in the console.
2. Make Reservation: Prompts you to fill in the required reservation details in the console to create a new reservation.
3. Delete Reservation: Asks for a reservation number and deletes the corresponding reservation from the list.
4. Generate Report: Displays a summary report of the most recent reservation in the console.
5. Exit: Exits the console-based reservation system.

## Data Storage

The reservation data is stored in a text file named `reservation.txt`. The data is organized in tab-separated columns representing the reservation number, name, date, time, number of adults, and number of children. Each new reservation is appended to the end of the file.

## Note

The two parts of the program (`main.py` and `gui.py`) implement similar functionalities using different user interfaces. You can choose to use either the GUI-based part for a more interactive experience or the console-based part for a simpler text-based interaction.

Please note that this reservation system is a basic example and does not handle advanced scenarios, such as data validation or concurrent access. Additional features and error handling could be added to enhance the system's functionality and robustness.

Feel free to fork the code and build your own customized version of Hotel Reservation System!