# Separate into boom mats
# Air can be compressed, mats cant

# Units are arbitrary as long as you're consistent

volumeUnit = "cm3"
pressureUnit = "atm"

boxHeight = 2.0
boxLength = 7.0
boxWidth  = 3.0

boomLength     = 90.0
innerBoomWidth = 1.8
outerBoomWidth = 2.0

teflonThickness     = 0.01
fibreGlassThickness = 0.01

airVolume = 30.0

unpackedBoomPressure = 1.0

#------------------#

outer = 2.0 * teflonThickness     * boomLength * innerBoomWidth
mid   = 2.0 * fibreGlassThickness * boomLength * innerBoomWidth
inner = 2.0 * teflonThickness     * boomLength * innerBoomWidth

materialVolume = outer + mid + inner

packedAirVolume = (boxHeight * innerBoomWidth * boxLength) - materialVolume

packedAirPressure = (unpackedBoomPressure * airVolume) / packedAirVolume

if packedAirVolume < 0:
    print "No BOOM ROOM for specified parameters"
    exit()

print "Uncompressed air volume:  ",airVolume,volumeUnit
print "Uncompressed air pressure:",unpackedBoomPressure,pressureUnit
print "Compressed air volume:    ",packedAirVolume,volumeUnit
print "Compressed air pressure:  ",packedAirPressure,pressureUnit
