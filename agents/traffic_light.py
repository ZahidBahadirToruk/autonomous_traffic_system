from events.event import LightChangedEvent

class TrafficLight:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def change_light(self, color):
        print(f"Traffic light changed to {color}")
        event = LightChangedEvent(color)
        self.event_bus.emit(event)
