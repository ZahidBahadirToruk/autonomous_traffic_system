class ControlCenter:
    def handle(self, event):
        if event.name == "LightChanged":
            print(f"Control Center: Traffic light changed to {event.payload['color']}.")
        elif event.name == "HighTraffic":
            print(f"Control Center: Handling high traffic with {event.payload['count']} vehicles.")
        elif event.name == "ClearTraffic":
            print("Control Center: Traffic is clear.")
        elif event.name == "EmergencyVehicleApproaching":
            print("Control Center: Prioritizing emergency vehicle.")
