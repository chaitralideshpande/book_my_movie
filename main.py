class BookMyMovie:
    from availability import showing_seats
    from seat_booking import buy_ticket
    from user_information import user_statistics
    from revenues import maximum_revenue
    from revenues import showing_stats

    print('\n Welcome to BookMyMovie.COM \n')
    print('\n Lets go and book your entertainment day! \n')

    def menu(self):
        output = True
        while output :
            print('Menu :')
            print('1. Show the seats')
            print('2. Buy a ticket')
            print('3. Statistics')
            print('4. Show booked Tickets User Info')
            print('5. Exit')

            self.input = input('Select option of your choice')
            if self.input.isalpha() == True:
                print('Invalid Option! Please enter a valid choice from the menu: \n')
            else:
                self.input=int(self.input)
                if self.input==1:
                    self.showing_seats()
                elif self.input==2:
                    self.buy_ticket()
                elif self.input==3:
                    self.showing_stats()
                elif self.input==4:
                    self.user_statistics()
                elif self.input==5:
                    output = False
                    self.exit()
                else:
                    print('Invalid Response! Please Try Again ')
                
    def __init__(self):
        self.rows = int(input('Number of rows:\n'))
        self.columns = int(input('Number of seats in each row:\n'))
        self.total_seats = self.rows * self.columns
        self.list1= []
        self.booked_seats_count = 0
        self.current_income = 0
        self.total_income = 0
        self.user_details = {}

        for i in range(self.rows):
            list2=[]
            for j in range(self.columns):
                list2.append('S')
            self.list1.append(list2)
        print(end = ' ')

    def exit(self):
       print('Thanks for visiting Book My Movie') 
     
movie_object = BookMyMovie()
movie_object.menu()


    