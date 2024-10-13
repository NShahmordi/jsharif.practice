class Clock:
    def __init__(self, hour=1, minute=0, second=0, base_second=0, base_minute=0, base_hour=0):
        self.second = second
        self.minute = minute  # Corrected typo here
        self.hour = hour
        self.base_second = base_second
        self.base_minute = base_minute
        self.base_hour = base_hour
        self.counter_second = 0
        self.counter_minute = 0
        self.counter_hour = 0
        self.counter_day = 0
        self.all_seconds = 0
        self.sum_base_time_as_second = 0
        self.sum_time_as_second = 0
        self.minus_time_as_second = 0
    
    def forward_time(self, input_time: str):
        self.base_hour, self.base_minute, self.base_second = map(int, input_time.split(':'))
        
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
            self.counter_day += self.counter_hour // 24
            self.counter_hour %= 24
             
        print("counter day for forward time method:", self.counter_day)
        return f'{str(self.counter_hour).zfill(2)}:{str(self.counter_minute).zfill(2)}:{str(self.counter_second).zfill(2)}'
    
    def backward_time(self, input_time: str):
        self.base_hour, self.base_minute, self.base_second = map(int, input_time.split(':'))
        
        self.sum_base_time_as_second = self.base_second + (self.base_minute * 60) + (self.base_hour * 3600)
        self.sum_time_as_second = self.second + (self.minute * 60) + (self.hour * 3600)
        self.minus_time_as_second = abs(self.sum_base_time_as_second - self.sum_time_as_second)
        
        self.counter_hour = self.minus_time_as_second // 3600
        self.counter_minute = (self.minus_time_as_second % 3600) // 60
        self.counter_second = (self.minus_time_as_second % 3600) % 60
        
        return f'{str(self.counter_hour).zfill(2)}:{str(self.counter_minute).zfill(2)}:{str(self.counter_second).zfill(2)}'

# Example usage
t = Clock(20, 60, 7)
print(t.forward_time('13:12:10'))
print(t.backward_time('13:12:10'))
