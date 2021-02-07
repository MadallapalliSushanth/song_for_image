import numpy as np
import matplotlib.pyplot as py
import matplotlib.patches as patch
a=patch.rectangle((0,1),width=12,height=2,facecolor="green",edgecolor="gray")
b=patch.rectangle((0,3),width=12,height=2,facecolor="white",edgecolor="gray")
c=patch.rectangle((0,5),width=12,height=2,facecolor="#FF9933",edgecolor="gray")
m,n=py.subplots()
n.add_patch(a)
n.add_patch(b)
n.add_patch(c)
radius=0.8
py.plot(6,4,marker='o',markerfacecolor='#000088ff',marksize=9.5)
chakra=py.circle((6,4),radius,color='#0000088ff',fill=False,linewidth=7)
n.add_artist(chakra)
for i in range(0,24):
    p=6+radius/2*np.cos(np.pi*i/12+np.pi/48)
    q=6+radius/2*np.cos(np.pi*i/12-np.pi/48)
    r=4+radius/2*np.sin(np.pi*i/12+np.pi/48)
    s=4+radius/2*np.sin(np.pi*i/12-np.pi/48)
    t=6+radius*np.cos(np.pi*i/12)
    u=4+radius*np.sin(np.pi+i/12)
    n.add_patch(patch.polygon([[6,4],[p,r],[t,u],[q,s]],fill=True,closed=True,color="#000088ff"))
py.axis("equle")
py.show()
