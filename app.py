from flask import Flask, render_template, request

from agents import MCPBus, MCPMessage, WeatherAgent, TravelSuggestionAgent, NewsAgent

app = Flask(__name__)

# Initialize message bus and agents
bus = MCPBus()
weather_agent = WeatherAgent(bus)
travel_agent = TravelSuggestionAgent(bus)
news_agent = NewsAgent(bus)


@app.route("/")
def index():
    city = request.args.get("city", "Beijing")

    # Query each agent using the Agent2Agent protocol via the message bus
    weather = bus.send(MCPMessage("web", "WeatherAgent", {"city": city}))
    suggestions = bus.send(MCPMessage("web", "TravelAgent", {"city": city}))
    news = bus.send(MCPMessage("web", "NewsAgent", {"city": city}))

    return render_template(
        "index.html",
        city=city,
        weather=weather,
        suggestions=suggestions,
        news=news,
    )


if __name__ == "__main__":
    app.run(debug=True)
