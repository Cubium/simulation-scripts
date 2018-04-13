# Units are arbitrary as long as you're consistent

volumeUnit = "cm3"
pressureUnit = "atm"

# Boom box's height
boxHeight = 10

# The longest box dimension
boxLength = 20.0

# The dimension corresponding to the boom's width
boxWidth  = 10.0

boomLength    = 500.0
boomWidth     = 5.0
boomThickness = 1.0

boomPressure = 1.0

#------------------#

print "Boom pressure:      ", boomPressure,pressureUnit

boomVolume = boomLength * boomWidth * boomThickness
print "Boom volume:        ", boomVolume,volumeUnit

packedBoomVolume = boomWidth * boxLength * boxHeight

if packedBoomVolume > boomVolume:
    packedBoomVolume = boomVolume

print "Packed boom volume: ",packedBoomVolume,volumeUnit

compressionFactor = packedBoomVolume / boomVolume

print "Compression factor:  " + str(compressionFactor) + "x original boom volume"

packedPressure = (boomPressure * boomVolume) / packedBoomVolume

print "Pressure exerted by packed boom: ",packedPressure,pressureUnit
