from events.event_bus import EventBus
from agents.traffic_light import TrafficLight
from agents.vehicle_sensor import VehicleSensor
from agents.emergency_handler import EmergencyHandler
from agents.control_center import ControlCenter

def main():
    event_bus = EventBus()
    control_center = ControlCenter()

    # Initialize agents
    traffic_light = TrafficLight(event_bus)
    vehicle_sensor = VehicleSensor(event_bus)
    emergency_handler = EmergencyHandler(event_bus)

    # Simulate events
    traffic_light.change_light("Green")
    vehicle_sensor.detect_traffic(15)
    emergency_handler.handle_emergency()
    vehicle_sensor.detect_traffic(5)

    # Process events
    event_bus.process_events([control_center])

if __name__ == "__main__":
    main()
