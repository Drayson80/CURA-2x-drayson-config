#Name: Insert gcode at layer change
#Info: Adds the ability to manually send commands on layer change e.g. for Timelaps trigger.
#Depend: GCode
#Type: postprocess
#
# Created by Wayne Porter
#
from ..Script import Script
class InsertAtLayerChange(Script):
    def __init__(self):
        super().__init__()
    def getSettingDataString(self):
        return """{
            "name": "Insert at layer change",
            "key": "InsertAtLayerChange",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "insert_loc":
                {
                    "label": "When to insert",
                    "description": "Whether to insert code before or after layer change.",
                    "type": "enum",
                    "options": {"before": "Before", "after": "After"},
                    "default_value": "before"
                },
                "gcode_to_add":
                {
                    "label": "GCODE to insert.",
                    "description": "GCODE to add before or after layer change.",
                    "type": "str",
                    "default_value": ""
                }
            }
        }"""
    def execute(self, data):
        in_layer = False
        gcode_to_add = self.getSettingValueByKey("gcode_to_add") + "\n"
        for layer in data:
            # Check that a layer is being printed
            lines = layer.split("\n")
            if ";LAYER:" in lines[0]:
                in_layer = True
            else:
                in_layer = False
            if in_layer:
                index = data.index(layer)
                if self.getSettingValueByKey("insert_loc") == "before":
                    layer = gcode_to_add + layer
                else:
                    layer = layer + gcode_to_add
                data[index] = layer
        return data