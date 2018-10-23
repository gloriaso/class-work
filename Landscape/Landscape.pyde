bear_movement=768
a=0
h=0

import time
def setup():
    global a
    global h
    size(768,576)
    global sky

def sky():
    global a
    global h
    for i in range(30):
        noStroke()
        fromC = color(0, 102, 153)
        toC = color(204, 102, 0)
        colour=lerpColor(fromC,toC,a)
        fill(colour)
        rect(0,h,width,20)
        a+=0.05
        h+=20


def draw():
    sky()
    global cloud
    global bear_movement

    #cloud
    # if cloud >=800:
    #     cloud=-200
    # cloud+=1 
    
    # fill(255)
    # ellipse(cloud,170,60,60)
    # ellipse(cloud+30,150,60,60)
    # ellipse(cloud+30,200,60,60)
    # ellipse(cloud+80,150,60,60)
    # ellipse(cloud+80,200,60,60)
    # ellipse(cloud+110,170,60,60)
    # ellipse(cloud+70,170,60,60)

    #sun
    fill(245, 150, 35)
    ellipse(width/2,height-200,100,100)

    #grass
    fill(5,90,0)
    ellipse(80,height+20,800,400)
    fill(10,100,0)    
    ellipse(400,height+20,700,400)
    fill(20,110,0)
    ellipse(800,height+50,1000,500)
    fill(25,120,15)  
    ellipse(300,height+40,1200,250)
    
    #trees
    fill(3,80,0)
    triangle(750,150,700,250,800,250)
    triangle(750,220,680,330,820,330)
    triangle(100,180,50,280,150,280)
    triangle(100,250,40,330,160,330)
    triangle(100,280,20,380,180,380)
    fill(0,70,0)
    triangle(650,200,600,300,700,300)
    triangle(650,250,580,360,720,360)
    fill(100,60,20)
    rect(635,360,30,70)
    rect(735,330,30,70)
    rect(85,380,30,50)
    
    #tent
    fill(200,105,0)
    triangle(640,380,590,480,690,480)
    fill(170,95,0)
    triangle(640,380,690,480,710,460)
    
    
    #bear
    if bear_movement<-100:
        bear_movement=1000
    bear_movement-=1
    noStroke()
    fill(180,100,40)
    ellipse(bear_movement+20,440,25,25)
    fill(120,70,30)
    ellipse(bear_movement+20,440,15,15)
    fill(180,100,40)
    ellipse(bear_movement,460,60,60)
    ellipse(bear_movement+60,480,80,60)
    rect(bear_movement+30,490,20,50)
    rect(bear_movement+70,490,20,50)
    ellipse(bear_movement-20,469,30,30)
    fill(10,10,0)
    ellipse(bear_movement-34,469,5,5)
    fill(0)
    ellipse(bear_movement-10,455,7,10)
    
   
    
    


        
