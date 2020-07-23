from timezonefinder import TimezoneFinder


class gps:
    __coords = {}
    # Below are dummy coordinates for testing
    __coords["lat"], __coords["lng"] = 38.897565, -77.036596

    def __init__(self):
        # Initialise GPS
        self.tzf = TimezoneFinder()

    def updateCoords(self):
        # Get coords from GPS device
        return

    def getCoords(self):
        # Return coords
        return self.__coords

    def getTimeZone(self):
        coords = self.getCoords()
        timezone = self.tzf.timezone_at(lng=coords["lng"], lat=coords["lat"])
        return timezone
