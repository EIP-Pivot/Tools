import json
import copy
import random
import sys

scene = {
    "components": [],
    "name": "NatouLeBabtou",
    "scripts": [],
    "systems": [
        "Physics System"
    ]
}

renderObject = {
    "RenderObject": {
        "materialIndex": "",
        "pipelineID": "",
        "transform": {
            "rotation": [
                0.0,
                0.0,
                0.0
            ],
            "scale": [
                1.0,
                1.0,
                1.0
            ]
        }
    }
}

gravity = {"Gravity": {
                "force": [
                    0.0,
                    0.0,
                    0.0
                ]
            }
}


rigidBody = { "RigidBody": {
                "acceleration": [
                    0.0,
                    0.0,
                    0.0
                ],
                "velocity": [
                    0.0,
                    0.0,
                    0.0
                ]
            }
}

def replacePos(origin, x, y, z):
        return x - origin[0], y - origin[1], z - origin[2]

def saveScene():
    f = open("NatouLeBabtou.json", "w")
    f.write(json.dumps(scene))
    f.close()

f = open(sys.argv[1], "r")
save = json.loads(f.read())
origin = save["origin"]

blockCount = 0
for id, details in save["minecraft"].items():
    for pos in details:
        x, y, z = replacePos(origin, pos["x"], pos["y"], pos["z"])
        render = copy.deepcopy(renderObject)
        render["RenderObject"]["meshID"] = id
        render["RenderObject"]["transform"]["position"] = [x, y, z]
        render["Tag"] = { "name": "block" + str(blockCount) }
        render["Gravity"] = {
                "force": [
                    0.0,
                    random.uniform(-10.0, -1.0),
                    0.0
                ]
            }
        render["RigidBody"] = {
                "acceleration": [
                    0.0,
                    0.0,
                    0.0
                ],
                "velocity": [
                    random.uniform(-20.0, 20.0),
                    random.uniform(10.0, 20.0),
                    random.uniform(-20.0, 20.0)
                ]
            }
        scene["components"].append(render)
        blockCount += 1

print(blockCount)
saveScene()