from gps import gps

gps = gps()

localZone = gps.getTimeZone()

print("Time zone here is: " + str(localZone))
