##time vs temperature graph for all temperatures with
##different colours

import pygame,sys,math
from pygame import *

#Choosing file
raw=open("d3.txt","r")
simple=open("simple_D3.txt","r")



#Setting up pygame:
pygame.init()
size=(1200,600)
graph_size = (1000,500)
screen = pygame.display.set_mode(size)
gameSurface = pygame.display.get_surface()


white=(255,255,255)

#screen.fill((255,255,255))
#display.update()


origin=(100,500)

y_axis=(100,20)
x_axis=(1100,500)

max_time= 5000
pix_per_x_unit= (x_axis[0]- origin[0])/max_time#for temp


pix_per_y_unit= (origin[1]-y_axis[1])/100

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
for x in range (0,max_time+5,max_time//10): 
    draw.rect(screen, white,cts(x,1)+(1,1*2*pix_per_y_unit),0)
    number=comicsans.render(str(x),5,white)
    screen.blit(number,cts(x-30,-2))
    display.update()

#Makes y  axis and labels:
draw.line(screen, white, origin, y_axis) #y-axis
for y in range (0,101,5):
    draw.rect(screen, white,cts(-40,y)+(40*2*pix_per_x_unit,2),0)
    number=comicsans.render(str(y),5,white)
    screen.blit(number,cts(-130,y+2))
    display.update()


#Displaying the data:

def colour(temp):
    code=(int(255/100*temp),0,int(255/100*(100-temp)) )
    return(code)

resetted=1


times=[]

while(1):

    while (1):
        linee=raw.readline()
        if (linee=="-----------END---------\n"):
            resetted=1
            break


        linee=[float(x) for x in linee.split()]
        if (linee==[]):
            break
        if (resetted==1):
            resetted=0
            col=colour(linee[1])
        draw.circle(screen,col,cts(linee[0],linee[1]),1)
        times.append(linee[0])
        display.update()
    if (linee==[]):
            break
    
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    display.update()
