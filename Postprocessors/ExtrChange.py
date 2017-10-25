# ExtrChange script - Change Extruder train from T0 (standard) to T1 (second train)
#
# This script is a quick migration of the ExtrChange plugin for legacy Cura.
# 
# This script is licensed under the Creative Commons - Attribution - Share Alike (CC BY-SA) terms
# Author: Chris & Alina

from ..Script import Script


class ExtrChange(Script):
    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return """{
            "name":"Extruder Change to 2nd Train",
            "key": "ExtrChange",
            "metadata":{},
            "version": 2,
            "settings":
            {

            }
        }"""

    def execute(self, data):
        for index, layer in enumerate(data):
            new_layer = ""
            lines = layer.split("\n")
            for line in lines:
                if line:
                    new_layer += line + "\n"
                    if line.startswith("M190"):
                        new_layer += "\nT1 ;Extruder change by postprocessor\n\n"
                    if line.startswith("M104 S0"):
                        new_layer += "\nT0 ;Extruder reset by postprocessor\n\n"
            data[index] = new_layer
        return data