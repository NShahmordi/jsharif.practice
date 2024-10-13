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

class Clock:
    def __init__(self,input_time:str, hour=1, minute=0, second=0, base_second=0, base_minute=0, base_hour=0,counter_day_for_forward_time_method=0):
        self.input_time = input_time
        self.second = second
        self.minute = minute
        self.hour = hour
        self.counter_day_for_forward_time_method = counter_day_for_forward_time_method
        
        self.base_second = base_second
        self.base_minute = base_minute
        self.base_hour = base_hour
        
        self.counter_second = 0
        self.counter_minute = 0
        self.counter_hour = 0
        self.counter_day = 0
        
        self.sum_base_time_as_second = 0
        self.sum_time_as_second = 0
        self.minus_time_as_second = 0
    
    def forward_time(self):
        self.base_hour, self.base_minute, self.base_second = map(int, self.input_time.split(':'))
        self.counter_second = self.base_second + self.second
        self.counter_minute = self.base_minute + self.minute
        self.counter_hour = self.base_hour + self.hour
        
        if self.counter_second >= 60:
            self.counter_minute += self.counter_second // 60
            self.counter_second %= 60
            
        if self.counter_minute >= 60:
            self.counter_hour += self.counter_minute // 60
            self.counter_minute %= 60
            
        if self.counter_hour >= 24:
            self.counter_day_for_forward_time_method += self.counter_hour // 24
            self.counter_hour %= 24
             
        print("counter day for forward time method:", self.counter_day_for_forward_time_method)
        return f'{str(self.counter_hour)}:{str(self.counter_minute)}:{str(self.counter_second)}'
    
    
    def backward_time(self):
        self.base_hour, self.base_minute, self.base_second = map(int,self.input_time.split(':'))
        
        self.sum_base_time_as_second = self.base_second + (self.base_minute * 60) + (self.base_hour * 3600)
        self.sum_time_as_second = self.second + (self.minute * 60) + (self.hour * 3600)
        self.minus_time_as_second = abs(self.sum_base_time_as_second - self.sum_time_as_second)
        
        self.counter_hour = self.minus_time_as_second // 3600
        self.counter_minute = (self.minus_time_as_second % 3600) // 60
        self.counter_second = (self.minus_time_as_second % 3600) % 60
        
        return f'{self.counter_hour}:{self.counter_minute}:{self.counter_second}'

class Time(Calendar, Clock):
    def __init__(self, input_date: str, input_time: str, day=1, month=0, year=0, hour=1, minute=0, second=0):
        Calendar.__init__(self, input_date, day=day, month=month, year=year)
        Clock.__init__(self, input_time, hour=hour, minute=minute, second=second)
    
    def balance_time_and_date(self):
        self.forward_date()
        self.forward_time()
        if self.counter_day_for_forward_time_method > 0:
            self.counter_day += 1
        if self.counter_hour == 23 and self.counter_minute == 59 and self.counter_second == 59:
            self.counter_day-= 1
        for self.number_of_month, self.name_of_month in Calendar.default_months.items():
            if  self.counter_month == self.number_of_month:
                return f'{self.counter_day} of {self.name_of_month} {self.counter_year}'          
obj = Time('1403/7/11', '13:12:11', day=13, month=12, year=3, hour=20, minute=5, second=50)

print('for backward time:',obj.backward_time()) 
print('for forward time:',obj.forward_time()) 
print('for forward date:',obj.forward_date())
print('for backward date:',obj.backward_date())
print('balance date and time:',obj.balance_time_and_date())  
