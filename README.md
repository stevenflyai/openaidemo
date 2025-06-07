# openaidemo

This demo shows a simple multi-agent system with a small web UI. It uses a
message bus implementing a basic MCP/Agent2Agent style protocol so agents can
communicate. Three agents are included:

- **WeatherAgent** – returns mock weather data
- **TravelAgent** – suggests sights to see
- **NewsAgent** – provides short news headlines

The UI displays their responses side by side. The default city is Beijing but
any city present in the mock data may be specified using the `city` query
parameter.

## Running

1. Install Flask:
   ```bash
   pip install Flask
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Open `http://localhost:5000/` in your browser and optionally change the
   city using the input box.
