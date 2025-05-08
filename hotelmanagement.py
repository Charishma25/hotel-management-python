class Customer:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.phone = ""
        self.from_date = ""
        self.to_date = ""
        self.payment_advance = 0.0
        self.booking_id = 0


class Room:
    def __init__(self):
        self.type = ''
        self.stype = ''
        self.ac = ''
        self.roomNumber = 0
        self.rent = 0
        self.status = 0
        self.cust = Customer()

    def add_room(self, rno):
        self.roomNumber = rno
        self.ac = input("Type AC/Non-AC (A/N): ")
        self.type = input("Type Comfort (S/N): ")
        self.stype = input("Type Size (B/S): ")
        self.rent = int(input("Daily Rent: "))
        self.status = 0
        print("Room Added Successfully!")

    def display_room(self):
        print(f"\nRoom Number: {self.roomNumber}")
        print(f"Type AC/Non-AC (A/N): {self.ac}")
        print(f"Type Comfort (S/N): {self.type}")
        print(f"Type Size (B/S): {self.stype}")
        print(f"Rent: {self.rent}")


class HotelMgnt:
    def __init__(self):
        self.rooms = []

    def check_in(self):
        rno = int(input("Enter Room number: "))
        room = next((r for r in self.rooms if r.roomNumber == rno), None)
        if not room:
            print("Room not found!")
            return

        if room.status == 1:
            print("Room is already Booked")
            return

        room.cust.booking_id = int(input("Enter booking id: "))
        room.cust.name = input("Enter Customer Name (First Name): ")
        room.cust.address = input("Enter Address (only city): ")
        room.cust.phone = input("Enter Phone: ")
        room.cust.from_date = input("Enter From Date: ")
        room.cust.to_date = input("Enter To Date: ")
        room.cust.payment_advance = float(input("Enter Advance Payment: "))
        room.status = 1
        print("Customer Checked-in Successfully")

    def get_available_rooms(self):
        available = False
        for room in self.rooms:
            if room.status == 0:
                room.display_room()
                available = True
        if not available:
            print("All rooms are reserved")

    def search_customer(self, pname):
        found = False
        for room in self.rooms:
            if room.status == 1 and room.cust.name.lower() == pname.lower():
                print(f"Customer Name: {room.cust.name}")
                print(f"Room Number: {room.roomNumber}")
                found = True
        if not found:
            print("Person not found.")

    def check_out(self, room_num):
        room = next((r for r in self.rooms if r.status == 1 and r.roomNumber == room_num), None)
        if not room:
            print("Room not found or not booked!")
            return
        days = int(input("Enter Number of Days: "))
        bill_amount = days * room.rent
        print("\n######## CheckOut Details ########")
        print(f"Customer Name: {room.cust.name}")
        print(f"Room Number: {room.roomNumber}")
        print(f"Address: {room.cust.address}")
        print(f"Phone: {room.cust.phone}")
        print(f"Total Amount Due: {bill_amount}")
        print(f"Advance Paid: {room.cust.payment_advance}")
        print(f"Total Payable: {bill_amount - room.cust.payment_advance}")
        room.status = 0

    def guest_summary_report(self):
        if not any(room.status == 1 for room in self.rooms):
            print("No Guest in Hotel!!")
        else:
            for room in self.rooms:
                if room.status == 1:
                    print(f"\nCustomer First Name: {room.cust.name}")
                    print(f"Room Number: {room.roomNumber}")
                    print(f"Address (only city): {room.cust.address}")
                    print(f"Phone: {room.cust.phone}")
                    print("-" * 40)

    def manage_rooms(self):
        while True:
            print("\n### Manage Rooms ###")
            print("1. Add Room")
            print("2. Search Room")
            print("3. Back to Main Menu")
            opt = input("Enter Option: ")

            if opt == '1':
                rno = int(input("Enter Room Number: "))
                if any(room.roomNumber == rno for room in self.rooms):
                    print("Room Number is already present. Please enter a unique number.")
                else:
                    new_room = Room()
                    new_room.add_room(rno)
                    self.rooms.append(new_room)
            elif opt == '2':
                rno = int(input("Enter Room Number: "))
                room = next((r for r in self.rooms if r.roomNumber == rno), None)
                if room:
                    print("Room is Reserved" if room.status == 1 else "Room is Available")
                    room.display_room()
                else:
                    print("Room not found.")
            elif opt == '3':
                break
            else:
                print("Please enter a valid option.")


def main():
    hm = HotelMgnt()
    while True:
        print("\n######## Hotel Management #########")
        print("1. Manage Rooms")
        print("2. Check-In Room")
        print("3. Available Rooms")
        print("4. Search Customer")
        print("5. Check-Out Room")
        print("6. Guest Summary Report")
        print("7. Exit")

        opt = input("Enter Option: ")
        if opt == '1':
            hm.manage_rooms()
        elif opt == '2':
            if not hm.rooms:
                print("No rooms available. Please add rooms first.")
            else:
                hm.check_in()
        elif opt == '3':
            if not hm.rooms:
                print("No rooms available. Please add rooms first.")
            else:
                hm.get_available_rooms()
        elif opt == '4':
            if not hm.rooms:
                print("No rooms available. Please add rooms first.")
            else:
                pname = input("Enter Customer Name: ")
                hm.search_customer(pname)
        elif opt == '5':
            if not hm.rooms:
                print("No rooms available. Please add rooms first.")
            else:
                rno = int(input("Enter Room Number: "))
                hm.check_out(rno)
        elif opt == '6':
            hm.guest_summary_report()
        elif opt == '7':
            print("THANK YOU! FOR USING THE SOFTWARE")
            break
        else:
            print("Please enter a valid option.")


if __name__ == "__main__":
    main()
