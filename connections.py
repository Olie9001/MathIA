import numpy as np
import matplotlib.pyplot as plt

def calc_points(ox,oy,scale,num_points):
    px = []
    py = []
    ang=0
    i=0
    da = (np.pi*2)/num_points
    while(i<num_points):
        x = ox + scale*np.cos(ang)
        y = oy + scale*np.sin(ang)
        ang = ang+da
        px.append(x)
        py.append(y)
        i = i+1
    
    return px,py

def draw_circle(plt,ox,oy,scale,num_points,fc,ec):
    px,py = calc_points(ox,oy,scale,num_points)
    plt.fill(px,py,facecolor=fc, edgecolor=ec, zorder=2)

def draw_points(plt,px,py,scale):
    for x,y in zip(px,py):
        draw_circle(plt,x,y,scale,32,'blue','black')
    draw_circle(plt,px[0],py[0],scale,32,'green','black')

def draw_connections(plt,px,py,scale,cc,ix):
    cx = px[ix]
    cy = py[ix]
    for x,y in zip(px,py):
        x1 = [cx,x]
        y1 = [cy,y]
        plt.plot(x1,y1,color=cc,zorder=1)

def draw_all_connections(plt,px,py,scale,c1,c2):
    i = 1
    while i<len(px):
        draw_connections(plt,px,py,scale,c2,i)
        i=i+1
    draw_connections(plt,px,py,scale,c1,0)

plt.figure(figsize=(10, 10))
plt.axis('equal')
px,py = calc_points(0,0,1,23)

draw_points(plt,px,py,0.1)
draw_connections(plt,px,py,0.1,'green',0)
plt.title(f'23 connections',fontsize = 40)
plt.savefig("connections1.png", dpi=300)

plt.cla()
draw_points(plt,px,py,0.1)
draw_all_connections(plt,px,py,0.1,'green','grey')
plt.title(f'253 connections',fontsize = 40)
plt.savefig("connections2.png", dpi=300)