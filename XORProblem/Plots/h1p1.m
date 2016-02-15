clear all
hold on
x=-2:.2:2;
[X,Y] = meshgrid(x);
a=1; b=1; c=-2; d=-0.5;
Z=(-d- a * X - b * Y)/c;
surf(X,Y,Z)
shading flat
xlabel('Input Layer x1'); ylabel('Input Layer x2'); zlabel('Hidden Layer h1')
scatter3(0,0,0,'filled','MarkerFaceColor',[0 .75 .75])
scatter3(0,1,0,'filled','filled','MarkerFaceColor',[0 .25 .25])
scatter3(1,0,0,'filled','filled','MarkerFaceColor',[0 .25 .25])
scatter3(1,1,1,'filled','MarkerFaceColor',[0 .75 .75])
view(-30,10)