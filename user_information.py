def user_statistics(self):
    self.booked_row=int(input('Enter the booked row number: \n'))
    self.booked_column=int(input('Enter the booked column number: \n'))
    if self.list1[self.booked_row-1][self.booked_column-1] == 'B':
        information = self.user_details[(self.booked_row,self.booked_column)]
        print('Name :', information[0])   
        print('Age : ',information[1])
        print('Gender :', information[2]) 
        print('Contact_number :', information[3])
    else:
        print('This seat is not booked till now:)')
        