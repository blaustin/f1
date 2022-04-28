class Driver:

    def __init__(self, name, number, lap_times):   
        self.name = name
        self.number = number
        self.lap_times = lap_times
        self.lap_data = []

        self.num_laps = len(lap_times)
        self.fastest_lap_time = min(lap_times)
        self.fastest_lap = lap_times.index(min(lap_times)) + 1
        self.slowest_lap_time = max(lap_times)
        self.slowest_lap = lap_times.index(max(lap_times)) + 1
        self.total_race_time = sum(lap_times)

    def update_lap(self, data):
        self.lap_data.append({
            "lap": data["lap"],
            "position": data["position"],
            "lap_time": data["lap_time"],
            "total_time": data["total_time"],
            "delta_first": data["delta_first"],
            "delta_ahead": data["delta_ahead"],
        })
        