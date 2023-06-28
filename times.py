class time(object):
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
    
    def __str__(self):
        return f"{self.hour:>2}:{self.minute:0>2}"
    
    def __add__(self, __o: object):
        if not isinstance(__o, time):
            raise Exception(f"time object connot be add with {__o.__class__}.")
        up = 0
        minute = self.minute + __o.minute
        if minute>=60:
            up = minute // 60
            minute = minute % 60
        hour = self.hour + __o.hour + up
        return time(hour, minute)
    
    def __sub__(self, __o: object):
        if not isinstance(__o, time):
            raise Exception(f"time object connot be sub with {__o.__class__}.")
        sub = 0
        minute = self.minute - __o.minute
        if minute<0:
            sub = abs(minute // 60)
            minute = minute + 60 * sub
        hour = self.hour - __o.hour - sub
        return time(hour, minute)
    
    def __eq__(self, __o: object):
        if not isinstance(__o, time):
            raise Exception(f"time object connot be compare with {__o.__class__}.")
        return self.hour==__o.hour and self.minute==__o.minute
    
    def __ne__(self, __o: object):
        if not isinstance(__o, time):
            raise Exception(f"time object connot be compare with {__o.__class__}.")
        return self.hour!=__o.hour or self.minute!=__o.minute
    
    def __lt__(self, __o: object):
        if not isinstance(__o, time):
            raise Exception(f"time object connot be compare with {__o.__class__}.")
        return self.hour<__o.hour or (self.hour==__o.hour and self.minute<__o.minute)
    
    def __le__(self, __o: object):
        if not isinstance(__o, time):
            raise Exception(f"time object connot be compare with {__o.__class__}.")
        return self.hour<__o.hour or (self.hour==__o.hour and self.minute<=__o.minute)
    
    def __gt__(self, __o: object):
        if not isinstance(__o, time):
            raise Exception(f"time object connot be compare with {__o.__class__}.")
        return self.hour>__o.hour or (self.hour==__o.hour and self.minute>__o.minute)
    
    def __ge__(self, __o: object):
        if not isinstance(__o, time):
            raise Exception(f"time object connot be compare with {__o.__class__}.")
        return self.hour>__o.hour or (self.hour==__o.hour and self.minute>=__o.minute)
