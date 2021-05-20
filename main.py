import torch
import json
# Applying the zeros function and
# storing the resulting tensor in 't'
testdic = {"2386759.jpg": {"height": 500, "width": 350, "depth": 3, "object": {"1": {"category": "shirt", "bbox": [1,2,3,4]}}}}
print(type(1))
with open("./ffuck.json","w") as f:
    json.dump(testdic, f)