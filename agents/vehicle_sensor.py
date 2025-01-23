from events.event import HighTrafficEvent, ClearTrafficEvent

class VehicleSensor:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def detect_traffic(self, vehicle_count):
        if vehicle_count > 10:
            print(f"High traffic detected with {vehicle_count} vehicles!")
            event = HighTrafficEvent(vehicle_count)
        else:
            print(f"Traffic is clear with {vehicle_count} vehicles.")
            event = ClearTrafficEvent(vehicle_count)
        self.event_bus.emit(event)
