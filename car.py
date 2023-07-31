from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery, carrigan_tire, octoprime_tire):
        self.engine = engine
        self.battery = battery
        self.carrigan_tire = carrigan_tire
        self.octoprime_tire = octoprime_tire

    def needs_service(self):
        return self.engine.needs_service() or 
            self.battery.needs_service() or
            self.carrigan_tire.needs_service() or
            self.octoprime_tire.needs_service()
