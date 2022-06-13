import math


def getSection(x, z):
    return math.floor(x / 16), math.floor(z / 16)


def getRegion(x, z):
    section_x, section_z = getSection(x, z)
    return math.floor(section_x / 32), math.floor(section_z / 32)


def getMinRegion(x, z):
    region_x, region_z = getRegion(x, z)
    return region_x * 32, region_z * 32


def getChunkSection(x, z):
    section_x, section_z = getSection(x, z)
    min_region_x, min_region_z = getMinRegion(x, z)
    return abs(abs(section_x) - abs(min_region_x)), abs(abs(section_z) - abs(min_region_z))


def getInChunkPos(x, z):
    return x % 16, z % 16
