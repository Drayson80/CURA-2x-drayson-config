
M117 Preparing for ATOMIC PULL
G21 		;metric values
G90		;absolute positioning
T1		; selecting left extruder train
M109 S190	; set extruder to 190 and wait
M106 S255	; set fan to max
M109 S100	; set extruder to 100
M106 S0		; set fan off
M300 S300 P1000   ; beep
M117 Wait and PULL...
M0 S10		; wait 10sek
M104 S0		; extuder at 0
T0		; selecting right extruder train
M300 S300 P1000   ; beep