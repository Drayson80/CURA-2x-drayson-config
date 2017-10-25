# LevRound script - adds leveling circle around bed
#
# This script is a quick hack of the ExtrChange plugin for legacy Cura.
#
# This script is licensed under the Creative Commons - Attribution - Share Alike (CC BY-SA) terms
# Author: Christian Eberl

from ..Script import Script


class LevBox_UM2(Script):
    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return """{
            "name":"Bed Leveling Box for UM2",
            "key": "LevBox_UM2",
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
                        new_layer += "\n\n;Leveling Round START\nG0 F3600 X9.344 Y15.444 Z0.3\nG1 F1500 X9.777 Y15.183 E0.06067\nG1 X10.245 Y14.993 E0.12128\nG1 X10.738 Y14.88 E0.18198\nG1 X11.208 Y14.845 E0.23853\nG1 X211.19 Y14.846 E24.23637\nG1 X211.694 Y14.886 E24.29704\nG1 X212.185 Y15.005 E24.35767\nG1 X212.652 Y15.199 E24.41835\nG1 X213.082 Y15.465 E24.47903\nG1 X213.465 Y15.795 E24.53969\nG1 X213.791 Y16.182 E24.60041\nG1 X214.052 Y16.615 E24.66108\nG1 X214.242 Y17.083 E24.72169\nG1 X214.355 Y17.576 E24.78239\nG1 X214.39 Y18.046 E24.83895\nG1 X214.39 Y208.027 E47.63667\nG1 X214.35 Y208.531 E47.69734\nG1 X214.231 Y209.022 E47.75796\nG1 X214.037 Y209.489 E47.81864\nG1 X213.771 Y209.919 E47.87932\nG1 X213.441 Y210.302 E47.93999\nG1 X213.054 Y210.628 E48.00071\nG1 X212.621 Y210.889 E48.06138\nG1 X212.153 Y211.079 E48.12199\nG1 X211.66 Y211.192 E48.18268\nG1 X211.19 Y211.227 E48.23924\nG1 X11.208 Y211.227 E72.23708\nG1 X10.704 Y211.187 E72.29775\nG1 X10.213 Y211.068 E72.35837\nG1 X9.746 Y210.874 E72.41906\nG1 X9.316 Y210.608 E72.47973\nG1 X8.933 Y210.278 E72.5404\nG1 X8.607 Y209.891 E72.60112\nG1 X8.346 Y209.458 E72.66179\nG1 X8.156 Y208.99 E72.7224\nG1 X8.043 Y208.497 E72.7831\nG1 X8.008 Y208.027 E72.83965\nG1 X8.008 Y18.045 E95.63749\nG1 X8.048 Y17.541 E95.69816\nG1 X8.167 Y17.05 E95.75879\nG1 X8.361 Y16.583 E95.81947\nG1 X8.627 Y16.153 E95.88015\nG1 X8.957 Y15.77 E95.94081\nG1 X9.344 Y15.444 E96.00153\nG10\nG0 F3600 X11.413 Y17.34\nG0 X11.413 Y18.25\nG0 X11.63 Y18.336\nG0 X11.63 Y18.236\nG11\nG1 F1800 X210.767 Y18.236 E119.89797\nG1 X210.999 Y18.236 E119.92581\nG1 X210.999 Y207.444 E142.63077\nG1 X210.999 Y207.836 E142.67781\nG1 X210.767 Y207.836 E142.70565\nG1 X11.63 Y207.836 E166.60209\nG1 X11.399 Y207.836 E166.62981\nG1 X11.399 Y207.444 E166.67685\nG1 X11.399 Y18.236 E189.38181\nG1 X11.63 Y18.236 E189.40953\nG0 F3600 X11.83 Y18.236\nG0 X11.63 Y18.244\n\nG92 E0 ;zero the extruded length\n;Leveling Round END\n\n"
            data[index] = new_layer
        return data
