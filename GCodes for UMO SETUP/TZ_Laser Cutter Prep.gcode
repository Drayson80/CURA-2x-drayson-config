; Prepare UMO for Laser Head

G21        ;metric values
G90        ;absolute positioning
M107       ;start with the fan off

M117 Start Laser Prep
G28 X0 Y0  ;move X/Y to min endstops
G28 Z0     ;move Z to min endstops


G1 Z2 F9000
G1 X100 Y10
M117 Move Platform down
G1 Z170
M117 INSERT FOCUS TOOL
M0 ;Pause

M117 Zero Z for Laser
G28 Z0
M117 Mount Laser
M0 ;Pause

M117 Homing X/Y
G28 X0 Y0 F9000
M117 Preparation Done

