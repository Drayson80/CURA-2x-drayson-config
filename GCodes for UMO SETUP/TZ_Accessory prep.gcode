;FLAVOR:RepRap
;G-Gode for preparing UMO as Plotter/DragKnife cutter
;Generated by Drayson
;=======================

G21 ;metric values
G90 ;absolute positioning
M107 ;start with the fan off

M117 Start Laser/Drag Knife Preparation
G28 X0 Y0 ;move X/Y to min endstops
G28 Z0 ;move Z to min endstops

G1 Z170 F9000 ;move Platform down to make space for inserting the Z-Spacer
M117 Please insert Z-spacer
M0 ;pause

M117 Zero Z
G28 Z0 F9000
G1 Z2 ;move x/y to attachement mounting position
G1 X100 Y10 F9000
G1 Z80 F9000
M117 Mount Accessory
M0 ;Pause

M117 Homing X/Y
G28 X0 Y0 F9000
M117 Preparation Done...
M300 S1397 P240
M300 S1760 P240
M300 S2093 P240
M300 S1397 P720
M300 S0 P240
