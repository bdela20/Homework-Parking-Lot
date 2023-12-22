class ParkingGarage:
    def __init__(self, max_tickets, max_parking_spaces):
        self.tickets = list(range(1, max_tickets + 1))
        self.parking_spaces = list(range(1, max_parking_spaces + 1))
        self.current_ticket = {}

    def take_ticket(self):
        if self.tickets:
            ticket_number = self.tickets.pop(0)
            parking_space = self.parking_spaces.pop(0)
            self.current_ticket = {'ticket_number': ticket_number, 'parking_space': parking_space, 'paid': False}
            print(f"Ticket #{ticket_number} issued. Park in space #{parking_space}")

    def pay_for_parking(self):
        if self.current_ticket and not self.current_ticket['paid']:
            amount = input("Enter the amount to pay: ")
            if amount:
                print(f"Ticket #{self.current_ticket['ticket_number']} has been paid. You have 15 minutes to leave.")
                self.current_ticket['paid'] = True
            else:
                print("Payment cancelled.")

    def leave_garage(self):
        if self.current_ticket and self.current_ticket['paid']:
            print("Thank you, have a nice day!")
            self.tickets.append(self.current_ticket['ticket_number'])
            self.parking_spaces.append(self.current_ticket['parking_space'])
            self.current_ticket = {}
        elif self.current_ticket and not self.current_ticket['paid']:
            payment = input("Please pay for your ticket before leaving. Enter the amount to pay: ")
            if payment:
                print("Thank you, have a nice day!")
                self.current_ticket['paid'] = True
                self.tickets.append(self.current_ticket['ticket_number'])
                self.parking_spaces.append(self.current_ticket['parking_space'])
                self.current_ticket = {}
            else:
                print("Payment cancelled.")

# Example usage
max_tickets = 10
max_parking_spaces = 10
garage = ParkingGarage(max_tickets, max_parking_spaces)

while True:
    action = input("Enter action (take/pay/leave/quit): ").lower()
    
    if action == 'take':
        garage.take_ticket()
    elif action == 'pay':
        garage.pay_for_parking()
    elif action == 'leave':
        garage.leave_garage()
    elif action == 'quit':
        print("Goodbye!")
        break
    else:
        print("Invalid action. Please enter take/pay/leave/quit.")


        
