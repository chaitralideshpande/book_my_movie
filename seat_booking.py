def buy_ticket(self):
    a = int(input('Enter the row number:\n'))
    b = int(input('Enter the column number:\n'))
    if self.list1[a-1][b-1] =='B':
        print('This seat is already booked! Please choose another seat.')
        self.menu()
    elif self.total_seats <= 60 :
        self.price = 10
        print('Ticket price per person is $10. Are you sure to continue? Yes / No')
    elif a < self.rows / 2 :
        self.price = 10
        print('Ticket price per person is $10. Are you sure to continue? Yes / No')
    elif a > self.rows / 2 :
        self.price = 8
        print('Ticket price per person is $8. Are you sure to continue? Yes / No')
    self.reply = input()

    if self.reply =='Yes' or self.reply == 'yes':
        dict1={}
        Name = input('Please enter your name :\n')
        Age = input('Please enter your age: \n')
        Gender = input ('Please select your gender, M / F / Other')
        Contact_number=input('Enter your contact number:\n')
        self.row1 = a - 1
        self.column1 = b - 1
        self.list1[self.row1][self.column1] = 'B'
        self.booked_seats_count = self.booked_seats_count + 1 
        self.current_income=self.current_income + self.price

        dict1[(self.row1+1), (self.column1+1)] = list((Name , Age , Gender , Contact_number , self.price))
        self.user_details.update(dict1)
        print('Hurray...You have a confirm seat now!!')
    else:
        print('Your booking cannot be processed! Please try again!!')