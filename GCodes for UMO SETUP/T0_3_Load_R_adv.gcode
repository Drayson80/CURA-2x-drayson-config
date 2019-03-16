; Advanced version of Load-script

G21 			;metric values
G90 			;absolute positioning
T0			;selecting right extruder train
M109 S200.000 	;Heat hotend to 200C for PLA
M107			;Fan Off
G28 X0 Y0 		;Zero X/Y
G28 Z0 			;Zero Z an Min-Endstop
G1 Z30.0 F4000 		;Plattform 30mm down
G92 E0 			;Reset the position of the extruder
G1 E200 F20000		;Retract xxx mm of filament at xxx mm/minute speed
G1 E600 F20000 		;Retract xxx mm of filament at xxx mm/minute speed
G1 E800 F500		;Retract xxx mm of filament at xxx mm/minute speed
G92 E0 			;Reset the position of the extruder
M117 FILAMENT OK 	;Display message on LCD-display to remove the filament
M0 S5		; wait 5sek
M104 S0
M300 S1397 P240
M300 S1760 P240
M300 S2093 P240
M300 S1397 P720
M300 S0 P240
