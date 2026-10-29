'''
## Single level inheritance
class car:
    def __init__(self,windows,doors,engine_type):
        self.window=windows
        self.doors=doors
        self.engine_type=engine_type
    def car_details(self):
        print(f"Car has {self.window} windows, \n{self.doors} doors and engine type is {self.engine_type}")
class tesla(car):
    def __init__(self,windows,doors,engine_type,is_autopilot):
        super().__init__(windows,doors,engine_type)
        self.is_autopilot=is_autopilot
    def is_autopilot_enabled(self):
        if self.is_autopilot:
            print("Autopilot is enabled")
        else:
            print("Autopilot is not enabled")



tesla1=tesla(4,4,"electric",True)
tesla1.is_autopilot_enabled()
tesla1.car_details()

'''
## Multiple inheritance
class car:
    def __init__(self,engine_type,is_engine_on):
        self.engine_type=engine_type
        self.is_engine_on=is_engine_on
    def start_engine(self):
        if self.is_engine_on:
            print("Engine is already on")
        else:
            self.is_engine_on=True
            print("Engine started")
    def stop_engine(self):
        if not self.is_engine_on:
            print("Engine is already off")
        else:
            self.is_engine_on=False
            print("Engine stopped")
    def get_engine_status(self):
        return self.is_engine_on
class autopilot:
    def __init__(self,is_autopilot,speed):
        self.is_autopilot=is_autopilot
        self.speed=speed
    def enable_autopilot(self):
        if self.is_autopilot:
            print("Autopilot is already enabled")
        else:
            self.is_autopilot=True
            print("Autopilot enabled")
    def disable_autopilot(self):
        if not self.is_autopilot:
            print("Autopilot is already disabled")
        else:
            self.is_autopilot=False
            print("Autopilot disabled")
    def get_autopilot_status(self):
        return self.is_autopilot
class smartcar(car,autopilot):
    def __init__(self,engine_type,is_engine_on,is_autopilot,speed,brand,model):
        car.__init__(self,engine_type,is_engine_on)
        autopilot.__init__(self,is_autopilot,speed)
        self.brand=brand
        self.model=model
    def display_car_info(self):
        print(f"Car brand is {self.brand}, model is {self.model}")
    def show_all_status(self):
        print(f"Engine status: {'On' if self.is_engine_on else 'Off'}")
        print(f"Autopilot status: {'Enabled' if self.is_autopilot else 'Disabled'}")
        print(f"Current speed: {self.speed} km/h")

s=smartcar("electric",False,True,60,"Tesla","Model S")
s.display_car_info()
s.show_all_status()
    
