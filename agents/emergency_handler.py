from events.event import EmergencyVehicleEvent

class EmergencyHandler:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def handle_emergency(self):
        print("Emergency vehicle approaching!")
        event = EmergencyVehicleEvent()
        self.event_bus.emit(event)
