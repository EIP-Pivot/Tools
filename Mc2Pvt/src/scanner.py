from asyncio.windows_events import NULL
import nbt.nbt
from src.reader import Reader
import anvil
import json


class SaveEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, nbt.nbt.TAG_String):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


class Scanner:
    save = {}
    x = 0
    y = 0
    z = 0

    def __init__(self, min, max, path) -> None:
        self.save["origin"] = (min[0], min[1], min[2])
        self.x_range = range(min[0], max[0] + 1)
        self.y_range = range(min[1], max[1] + 1)
        self.z_range = range(min[2], max[2] + 1)
        self.path = path
        self.reader = Reader(path)

    def saveScan(self):
        f = open(self.path + "save.json", "w")
        f.write(json.dumps(self.save, cls=SaveEncoder))
        f.close()

    def getNamespace(self, block: anvil.Block):
        if not block.namespace in self.save:
            self.save[block.namespace] = {}
        return self.save[block.namespace]

    def getId(self, block: anvil.Block):
        namespace = self.getNamespace(block)
        if not block.id in namespace:
            namespace[block.id] = []
        return namespace[block.id]
    
    def getX(self):
        x = 0
        try:
            x = self.x_range[self.x]
            self.x += 1
        except IndexError:
            self.z += 1
            self.x = 0
            x = self.x_range[self.x]
        return x
    
    def getY(self):
        y = 0
        try:
            y = self.y_range[self.y]
        except IndexError:
            return None
        return y

    def getZ(self):
        z = 0
        try:
            z = self.z_range[self.z]
        except IndexError:
            self.y += 1
            self.z = 0
            z = self.z_range[self.z]
        return z

    def getNextBlock(self):
        x = self.getX()
        z = self.getZ()
        y = self.getY()
        if y == None:
            return None
        block = self.reader.getBlock(x, y, z)
        return {'block': block, 'x': x, 'y': y, 'z': z}

    def scan(self) -> None:
        while block := self.getNextBlock():
            if block["block"].id != "air":
                        self.getId(block["block"]).append(
                            {'x': block["x"], 'y': block["y"], 'z': block["z"], 'properties': block["block"].properties})
        self.saveScan()