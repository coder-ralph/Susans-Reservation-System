class menu:
    def __init__(self, choice):
        self.choice = choice
        if choice == "A":
            count = 0
            file = open("reservation.txt")
            lines = file.readlines()[1:]
            file.close()
            for line in lines:
                count += 1

            if count == 0:
                print("\\There are no reservations!!\\")
                print()
            else:
                file = open("reservation.txt", "r")
                print(file.read())
                file.close()

        elif choice == "B":
            with open("reservation.txt", "r") as file:
                for last_line in file:
                    pass

            if last_line[0] == "#":
                num = 1
            else:
                num = int(last_line[0]) + 1

            print("\n Please Fill up this Form to make reservation. Thank you!\n")


            name = input("Enter Name: ")
            date = input("Enter Date: ")
            time = input("Enter Time: ")
            adults = int(input("No. of Adults: "))
            children = int(input("No. of Children: "))
            file = open("reservation.txt", "a")
            file.write(f"{num}\t{name}\t{date}\t{time}\t{adults}\t{children}\n")
            file.close()
            print()

        elif choice == "C":
            resnum = input("Enter Reservation number: ")
            file1 = open("reservation.txt", "r")
            lines = file1.readlines()
            file1.close()
            file2 = open("reservation.txt", "w")

            for line in lines:
                if not line.startswith(resnum):
                    file2.write(line)
            file2.close()

        elif choice == "D":
            adults, children, total_adults, total_children, total = 0, 0, 0, 0, 0
            file = open("reservation.txt", "r")
            list_of_lists=[]
            report = ""
            i = 0
            last_line = file.readlines()[-1]

            stripped_line = last_line.strip()
            line_list = stripped_line.split("\t")
            adults += int(line_list[4])
            children += int(line_list[5])
            subtotal = (int(line_list[4]) * 1000) + (int(line_list[5]) * 500)
            total += subtotal
            line_list.append(str(subtotal))
            report += f"LIST NUMBER:{line_list[0]}DATE:{line_list[2]}TIME:{line_list[3]}" \
                f"NAME:{line_list[1]}NO.OF ADULTS:{line_list[4]}NO.OF CHILDREN:{line_list[5]}TOTAL OF:PHP{line_list[6]}"
            
            file.close()

            print()
            print()
            print("                                                                       RESERVATION REPORT")
            print()
            print(report)
            print("Total Number of Adults: ", adults)
            print("Total Number of Children: ", children)
            print("Grand Total: PHP ", total)
            print("---------------------------------------------------------------- RECEIPT OF PAYMENT "
                  "----------------------------------------------------------------")
            print()
            print()

        elif choice == "E":
            import sys
            sys.exit("Thank you!")

        else:
            print("Invalid response. Please try again.")


while True:
    try:
        file = open("reservation.txt", "r")
    except FileNotFoundError:
        file = open("reservation.txt", "w+")
        file.write("#\\Name\\Date\\Time\\Adults\\Children\\")
    file.close()

    print("\\***SUSAN'S VILLA HOTEL RESORT RESERVATION***\\")
    print("Good day, Client! Before you proceed we would like to\n clarify that booking a reservation is needed.\nPlease fill up this form. Thank you!")
    print("ADULTS: PHP 1000\nCHILDREN: PHP500")
    print("Reservation System Menu:")
    print("A. View all Reservations\nB. Make Reservation")
    print("C. Delete Reservation\nD. Generate Report")
    print("E. Exit")

    selection_menu = input('Enter selection: ').upper()
    menu(selection_menu)