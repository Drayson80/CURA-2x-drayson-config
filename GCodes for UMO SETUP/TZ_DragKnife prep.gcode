;FLAVOR:RepRap
;G-Gode for preparing UMO as Plotter/DragKnife cutter
;Generated by Drayson
;=======================

G21             ;metric values
G90             ;absolute positioning
M107            ;start with the fan off

M117 Prepare for plotting
G28 X0 Y0       ;move X/Y to min endstops
G28 Z0          ;move Z to min endstops

G1 Z80 F9000    ;make some space for inserting the Z-Spacer
M117 Insert Z-Spacer
M0              ;pause
M117 Zero Z again
G28 Z0
G0 Z80
G1 X100 Y10     ;move x/y to attachement mounting position
M117 Mount DragKnife
M0
M117 Homing X/Y
G28 X0 Y0
M117 Ready for plotting...