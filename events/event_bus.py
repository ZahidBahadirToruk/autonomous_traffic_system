communication_queue = []

class EventBus:
    def emit(self, event):
        communication_queue.append(event)
        print(f"Event {event.name} emitted!")

    def process_events(self, handlers):
        while communication_queue:
            event = communication_queue.pop(0)
            for handler in handlers:
                handler.handle(event)
