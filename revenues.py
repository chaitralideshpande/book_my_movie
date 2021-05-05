def maximum_revenue(self):
    if self.total_seats <= 60:
        self.total_income = self.total_seats * 10
    elif self.total_seats > 60:
        c = int(self.rows/2)*10
        d = (int(self.rows)- int(self.rows/2))* int(self.columns) * 8
        self.total_income = c + d
        return self.total_income

def showing_stats(self):
    print('Number of purchased tickets' , self.booked_seats_count)
    self.percent_of_booking = (self.booked_seats_count/self.total_seats)*100
    print('Percentage of booking is', self.percent_of_booking,'%')
    print('Current Income is $' , self.current_income)
    revenue = self.maximum_revenue()
    print('Total possible income is $' , self.total_income)