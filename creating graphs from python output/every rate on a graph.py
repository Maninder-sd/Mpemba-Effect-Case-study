##temperature vs time graph for all temperatures with
##different colours
## and initial temperatures be golden

import pygame,sys,math
from pygame import *

#Choosing file

raw=open("d2_d3.txt","r")
simple=open("simple_d2_d3.txt","r")
golden=open("simple_d2_d3.txt","r")

every=open("every_d2_d3.txt","w")

files=[raw,simple,every,golden]



#Setting up pygame:
pygame.init()
size=(1000,600)
graph_size = (800,400)
screen = pygame.display.set_mode(size)
gameSurface = pygame.display.get_surface()

white=(255,255,255)
origin=(100,500)

y_axis=(100,100)
x_axis=(900,500)

pix_per_x_unit= (x_axis[0]- origin[0])/100#for temp

max_time= 5000
pix_per_y_unit= (origin[1]-y_axis[1])/max_time

def stc(x,y):
    a= (x-100)//pix_per_x_unit
    b= (500-y)//pix_per_y_unit
    return(a,b)

def cts(a,b):
    x= a*pix_per_x_unit+100
    y= 500-b*pix_per_y_unit
    x=int(x)
    y=int(y)
    return(x,y)


#making the graph axis:




comicsans = pygame.font.SysFont("comicsansms",10)

#Makes x axis and labels:
draw.line(screen, white, origin, x_axis) #x-axis
for x in range (0,101,5):
    draw.rect(screen, white,cts(x,40)+(1,40*2*pix_per_y_unit),0)
    number=comicsans.render(str(x),5,white)
    screen.blit(number,cts(x-1,-50))
    display.update()

#Makes y  axis and labels:
draw.line(screen, white, origin, y_axis) #y-axis
for y in range (0,max_time+5,max_time//10):
    draw.rect(screen, white,cts(-1,y)+(1*2*pix_per_x_unit,2),0)
    number=comicsans.render(str(y),5,white)
    screen.blit(number,cts(-5,y+70))
    display.update()


#Displaying the data:

def colour(temp):
    code=(int(255/100*temp),0,int(255/100*(100-temp)) )
    return(code)

resetted=1
times=[]

##loading the simple data:

## !!!!!!!! BIG ASSUMPTION THAT SIMPLE AND RAW DATA ALIGNED !!!!!!!!!!

total_time=dict()
while(1):
    inter=simple.readline()
    inter=[float(x) for x in inter.split()]
    if (inter==[]):
        break
    total_time[inter[0]]=inter[1]
    

while(1):

    while (1):
        raw_line=raw.readline()
        if (raw_line=="-----------END---------\n"):
            resetted=1
            break


        raw_line=[float(x) for x in raw_line.split()]
        
        if (raw_line==[]):
            break
        if (resetted==1):
            resetted=0
            col=colour(raw_line[1])
            t_time=total_time[raw_line[1]]
            
        draw.circle(screen,col,cts(raw_line[1],t_time-raw_line[0]),1)
        
        every.write(str(raw_line[1])+" "+ str(t_time-raw_line[0])+"\n")
        
        times.append(raw_line[0])
        display.update()
    if (raw_line==[]):
            break

gold=(255,215,0)

while (1):
    raw_line=golden.readline()#format: temp time
    
    raw_line=[float(x) for x in raw_line.split()]#
    if (raw_line==[]):
        break
    draw.circle(screen,gold,cts(raw_line[0],raw_line[1]),3)
 
    display.update()

#drawing the parabola:

def f(x):
    y=-0.8133*x**2 + 103.48*x + 458.69
    return(y)

my_x=0
while (1):
    draw.circle(screen,(0,255,0),cts(my_x,f(my_x)),3)
    my_x+=0.5
    if (my_x>=100):
        break
    display.update()
    
    
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    display.update()


for fi in files:
    fi.close()
