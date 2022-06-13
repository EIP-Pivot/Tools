import anvil
import src.utils as utils


class Reader:
    regions = {}
    chunks = {}

    def __init__(self, path):
        self.path = path

    def getRegionFile(self, x, z):
        region_x, region_z = utils.getRegion(x, z)
        file = self.path + "r.{x}.{z}.mca"
        return file.format(x=region_x, z=region_z)

    def getRegion(self, x, z) -> anvil.Region:
        region = utils.getRegion(x, z)
        if not region in self.regions:
            try:
                self.regions[region] = anvil.Region.from_file(
                    self.getRegionFile(x, z))
            except FileNotFoundError:
                error = "File for region {x}, {z} not found"
                print(error.format(x=region[0], z=region[1]))
                exit(1)
        return self.regions[region]

    def getChunk(self, x, z) -> anvil.Chunk:
        region = self.getRegion(x, z)
        chunk = utils.getChunkSection(x, z)
        if not chunk in self.chunks:
            self.chunks[chunk] = anvil.Chunk.from_region(
                region, chunk[0], chunk[1])
        return self.chunks[chunk]

    def getBlock(self, x, y, z) -> anvil.Block:
        chunk = self.getChunk(x, z)
        x, z = utils.getInChunkPos(x, z)
        return chunk.get_block(x, y, z)
