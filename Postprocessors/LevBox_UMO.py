# Leveling Box script - adds leveling box around bed of Ultimaker Original
#
# This script is a quick hack of the ExtrChange plugin for legacy Cura.
#
# This script is licensed under the Creative Commons - Attribution - Share Alike (CC BY-SA) terms
# Author: Christian Eberl

from ..Script import Script


class LevBox_UMO(Script):
    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return """{
            "name":"Bed Leveling Box for UMO",
            "key": "LevBox_UMO",
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
                    if line.startswith(";LAYER_COUNT:"):
                        new_layer += "\n\n;Leveling Round START\nG0 F3600 X6.269 Y5.303 Z0.3\n;TYPE:SKIRT\nG1 F1800 X6.656 Y4.977 E0.00952\nG1 X7.089 Y4.716 E0.01903\nG1 X7.557 Y4.526 E0.02853\nG1 X8.05 Y4.413 E0.03804\nG1 X8.52 Y4.378 E0.04691\nG1 X198.502 Y4.379 E3.62058\nG1 X199.006 Y4.419 E3.63009\nG1 X199.497 Y4.538 E3.63959\nG1 X199.964 Y4.732 E3.6491\nG1 X200.394 Y4.998 E3.65861\nG1 X200.777 Y5.328 E3.66812\nG1 X201.103 Y5.715 E3.67764\nG1 X201.364 Y6.148 E3.68715\nG1 X201.554 Y6.616 E3.69665\nG1 X201.667 Y7.109 E3.70617\nG1 X201.702 Y7.579 E3.71503\nG1 X201.702 Y197.56 E7.28868\nG1 X201.662 Y198.064 E7.29819\nG1 X201.543 Y198.555 E7.30769\nG1 X201.349 Y199.022 E7.31721\nG1 X201.083 Y199.452 E7.32672\nG1 X200.753 Y199.835 E7.33623\nG1 X200.366 Y200.161 E7.34575\nG1 X199.933 Y200.422 E7.35526\nG1 X199.465 Y200.612 E7.36476\nG1 X198.972 Y200.725 E7.37427\nG1 X198.502 Y200.76 E7.38314\nG1 X8.52 Y200.76 E10.9568\nG1 X8.016 Y200.72 E10.96631\nG1 X7.525 Y200.601 E10.97582\nG1 X7.058 Y200.407 E10.98533\nG1 X6.628 Y200.141 E10.99484\nG1 X6.245 Y199.811 E11.00435\nG1 X5.919 Y199.424 E11.01387\nG1 X5.658 Y198.991 E11.02338\nG1 X5.468 Y198.523 E11.03288\nG1 X5.355 Y198.03 E11.0424\nG1 X5.32 Y197.56 E11.05126\nG1 X5.32 Y7.578 E14.62493\nG1 X5.36 Y7.074 E14.63444\nG1 X5.479 Y6.583 E14.64394\nG1 X5.673 Y6.116 E14.65345\nG1 X5.939 Y5.686 E14.66296\nG1 X6.269 Y5.303 E14.67247\nG1 F1500 E8.17247\nG0 F3600 X8.099 Y7.158\nG0 X8.725 Y7.783\nG0 X8.911 Y7.869\nG0 X8.911 Y7.769\n;TYPE:WALL-OUTER\nG1 F1500 E14.67247\nG1 F1800 X198.111 Y7.769 E18.23143\nG1 X198.311 Y7.769 E18.23519\nG1 X198.311 Y196.978 E21.79432\nG1 X198.311 Y197.369 E21.80168\nG1 X198.111 Y197.369 E21.80544\nG1 X8.911 Y197.369 E25.36439\nG1 X8.711 Y197.369 E25.36816\nG1 X8.711 Y196.978 E25.37551\nG1 X8.711 Y7.769 E28.93464\nG1 X8.911 Y7.769 E28.9384\nG0 F3600 X9.111 Y7.769\nG0 X8.911 Y7.778\nG92 E0 ;zero the extruded length\n;Leveling Round END\n\n"
            data[index] = new_layer
        return data
