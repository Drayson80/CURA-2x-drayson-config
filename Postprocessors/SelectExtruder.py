#!/usr/bin/env python

#Name: Select Extruder 15.01
#Info: Adjusts the used extruder for a single material print
#Help: SelectExtruder
#Depend: GCode
#Type: postprocess
#Param: ExtruderNo(int:0) Extruder to be used (0: 1st ex., 1: 2nd ex.)

# Written by Stefan Heule, Dim3nsioneer@gmx.ch
# This script is licensed under the Creative Commons - Attribution - Share Alike - Non Commercial (CC BY-SA-NC) 3.0 terms
#
# Hacked for Cura 2.x by Da Hai Zhu - appologies to the original author
# Handles up to 10 extruders (0-9) - should last another year, maybe...
# 2017-04-24
# version 2.5.0

from ..Script import Script
import re

class SelectExtruder(Script):
    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return """{
            "name":"Select Extruder",
            "key": "SelectExtruder",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "ext_Num": 
                {
                    "label": "Extruder Number (0 - n)",
                    "description": "0 = 1st, 1 = 2nd, etc...",
                    "unit": "",
                    "type": "int",
                    "default_value": 0
                }
            }
        }"""


    def execute(self, data):
        extNum = self.getSettingValueByKey("ext_Num")
        for layer in data:
            index = data.index(layer)
            lines = layer.split("\n")
            for line in lines:
                if "M109" in line: #look for M109 command (heat up and wait)
                    layer = layer.replace(line, re.sub("M109.+(S\d+)","M109 T%d \g<1>\nT%d\n" % (int(extNum),int(extNum)),line))
                elif "M104" in line: #look for M104 command (temperature change)
                    layer = layer.replace(line, re.sub("M104.+(S\d+)","M104 T%d \g<1>\nT%d\n" % (int(extNum),int(extNum)),line))
                elif re.search("T\d",line) and "M200" not in line:
                    layer = layer.replace(line, re.sub("T\d","T%d\n" % int(extNum),line))
            data[index] = layer
        return data
