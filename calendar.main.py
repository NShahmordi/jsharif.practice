class Calendar:
    default_months = {1:'Farvardin', 2:'Ordibehesht', 3:'Khordad', 4:'Tir',5:'Mordad',6:'Shahrivar',
                      7:'Mehr',8:'Aban',9:'Azar',10:'Day',11:'Bahman', 12:'Esfand'}
    remains_of_the_leap_year = [1, 5, 9, 13, 17, 22, 26, 30]
    first_time = [1,2,3,4,5,6]
    
    def __init__(self, input_date:str, base_day=0, base_month=0, base_year=0, counter_day =0 
                 , counter_month =0, counter_year=0, day=1, month=0, year=0,name_of_month:str='' ):
        self.input_date = input_date
        self.day = day
        self.month = month
        self.year = year
        self.counter_day = counter_day  
        self.counter_month = counter_month
        self.counter_year = counter_year
        self.base_day = base_day
        self.base_month = base_month
        self.base_year = base_year
        self.name_of_month = name_of_month
        
    def forward_date(self):
        self.number_of_month = 0
        self.__counter_year = 0
        self.minus_two_years = 0

        self.base_year, self.base_month, self.base_day = map(int, self.input_date.split('/'))
        self.counter_day = self.base_day + self.day
        self.counter_month = self.base_month + self.month
        self.counter_year = self.base_year + self.year
        
        while self.counter_day % 6 in Calendar.first_time:
            self.counter_month += self.counter_day // 31 
            self.counter_day %= 31 
        self.counter_month += self.counter_day // 30 
        self.counter_day %= 30
            
        if self.counter_month >= 12:
            self.counter_year += self.counter_month // 12
            self.counter_month %= 12
           
        self.minus_two_years = self.counter_year - self.__counter_year
        while self.minus_two_years:
            self.minus_two_years = self.counter_year - self.__counter_year
            self.__counter_year += 1
            if self.minus_two_years % 33 not in Calendar.remains_of_the_leap_year:
                if self.counter_year == 30 and self.counter_month == 12:
                    self.counter_day -= 1
        for self.number_of_month, self.name_of_month in Calendar.default_months.items():
            if  self.counter_month == self.number_of_month:
                return f'{self.counter_day} of {self.name_of_month} {self.counter_year}'
        return f'{self.counter_day} of {self.name_of_month} {self.counter_year}', self.counter_month  
     
    def backward_date(self):
        self.base_year, self.base_month, self.base_day = map(int, self.input_date.split('/'))
        
        self.counter_day = self.base_day - self.day
        self.counter_month = self.base_month - self.month
        self.counter_year = self.base_year - self.year
        
        while abs(self.counter_month) % 6 in Calendar.first_time:
            if self.counter_day <= 0:
                self.counter_day += 31
                self.counter_month-= 1 
                
        if self.counter_day <= 0:
                self.counter_day += 30
                self.counter_month-= 1 
        if self.counter_month <= 0:
            self.counter_month += 12
            self.counter_year -= 1
            
        for self.number_of_month, self.name_of_month in Calendar.default_months.items():
            if  self.counter_month == self.number_of_month:
                return f'{self.counter_day} of {self.name_of_month} {self.counter_year}'
            
        return self.counter_year, self.base_month, self.counter_day 

C = Calendar('1403/7/11',day=13,month=12,year=3)
print(C.forward_date())
print(C.backward_date())
