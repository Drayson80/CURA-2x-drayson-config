
G21        ;metric values
G90        ;absolute positioning
M107       ;start with the fan off
M117	   Start Leveling - Homing X/Y
G28 X0 Y0  ;move X/Y to min endstops

M117 Start Extended Bed Leveling


M117 Front Left
G1 X42 Y15 F9000
G28 Z0     ;move Z to min endstops

M0 ;Pause

M117 Front Right
G1 Z5.0 F180 ;move the platform down
G1 X148 Y15 F9000
G1 Z0.0 F180 ;touch print head to bed

M0 ;Pause

M117 Back Middle
G1 Z5.0 F180 ;move the platform down
G1 X95 Y180 F9000
G1 Z0.0 F180 ;touch print head to bed

M0 ;Pause


G00 Z10.0 F180 ;move the platform down

M117 Extended Front Left
G1 X15 Y15 F9000
G1 Z0.0 F180 ;touch print head to bed

M0 ;Pause

M117 Extended Front Right
G1 Z5.0 F180 ;move the platform down
G1 X175 Y15 F9000
G1 Z0.0 F180 ;touch print head to bed

M0 ;Pause

M117 Extended Middle
G1 Z5.0 F180 ;move the platform down
G1 X95 Y97.5 F9000
G1 Z0.0 F180 ;touch print head to bed

M0 ;Pause

M117 Homing X/Y
G00 Z10.0 F180 ;move the platform down
G28 X0 Y0 F9000
M117 Leveling Done
G00 Z20.0 F180 ;move the platform down

;make some noise
M300 S1397 P240
M300 S1760 P240
M300 S2093 P240
M300 S1397 P720
M300 S0 P240