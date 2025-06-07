class MCPMessage:
    def __init__(self, sender, recipient, content, msg_type="query"):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.msg_type = msg_type


class MCPBus:
    """Simple message bus implementing an MCP-like protocol."""

    def __init__(self):
        self.agents = {}

    def register(self, agent):
        self.agents[agent.name] = agent

    def send(self, message: MCPMessage):
        recipient = self.agents.get(message.recipient)
        if not recipient:
            raise ValueError(f"No recipient {message.recipient}")
        return recipient.handle(message)


class Agent:
    def __init__(self, name, bus: MCPBus):
        self.name = name
        self.bus = bus
        bus.register(self)

    def handle(self, message: MCPMessage):
        raise NotImplementedError


class WeatherAgent(Agent):
    def __init__(self, bus: MCPBus):
        super().__init__("WeatherAgent", bus)
        self.weather_data = {
            "Beijing": "Sunny, 25\u00b0C",
            "Paris": "Cloudy, 18\u00b0C",
            "New York": "Rainy, 10\u00b0C",
        }

    def handle(self, message: MCPMessage):
        city = message.content.get("city", "Beijing")
        return self.weather_data.get(city, "Weather data not available.")


class TravelSuggestionAgent(Agent):
    def __init__(self, bus: MCPBus):
        super().__init__("TravelAgent", bus)
        self.suggestions = {
            "Beijing": [
                "Visit the Great Wall",
                "Explore the Forbidden City",
            ],
            "Paris": [
                "See the Eiffel Tower",
                "Walk along the Seine",
            ],
            "New York": [
                "Check out Times Square",
                "Visit Central Park",
            ],
        }

    def handle(self, message: MCPMessage):
        city = message.content.get("city", "Beijing")
        return self.suggestions.get(city, ["No suggestions available."])


class NewsAgent(Agent):
    def __init__(self, bus: MCPBus):
        super().__init__("NewsAgent", bus)
        self.news = {
            "Beijing": [
                "Beijing hosts international cultural festival",
                "New museum opens in downtown Beijing",
            ],
            "Paris": [
                "Paris Fashion Week kicks off",
                "Local bakery wins national award",
            ],
            "New York": [
                "Marathon brings thousands to NYC",
                "New art exhibition opens at MoMA",
            ],
        }

    def handle(self, message: MCPMessage):
        city = message.content.get("city", "Beijing")
        return self.news.get(city, ["No news available."])
