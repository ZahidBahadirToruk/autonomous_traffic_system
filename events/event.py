class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload

class LightChangedEvent(Event):
    def __init__(self, color):
        super().__init__("LightChanged", {"color": color})

class HighTrafficEvent(Event):
    def __init__(self, count):
        super().__init__("HighTraffic", {"count": count})

class ClearTrafficEvent(Event):
    def __init__(self, count):
        super().__init__("ClearTraffic", {"count": count})

class EmergencyVehicleEvent(Event):
    def __init__(self):
        super().__init__("EmergencyVehicleApproaching", {})
