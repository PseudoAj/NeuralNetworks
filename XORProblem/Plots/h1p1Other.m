%%
syms x y;
hold on;
% Add xy axis to above function plot.
% line([x1 ; x2],[y1 ; y2])
% where line goes from (x1,y1) to (x2,y2)
line([-10 ; 10],[0 ; 0], 'color', 'black', 'LineStyle',':');
line([0 ; 0],[-10 ; 10], 'color', 'black', 'LineStyle',':');