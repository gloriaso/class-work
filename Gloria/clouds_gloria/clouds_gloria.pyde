cloud1=0
cloud2=120
dog_movement=768
sky=0.11

import time
def setup():
    size(768,576)
    line(0,0,600,600)


def draw():
    global cloud1
    global cloud2
    global dog_movement
    global sky
    
    #sky
    noStroke()
    fromC = color(0, 102, 153)
    toC = color(204, 102, 0)
    interA = lerpColor(fromC, toC, .05)
    interB = lerpColor(fromC, toC, .10)
    interC = lerpColor(fromC,toC,.15)
    interD = lerpColor(fromC,toC,.2)
    interE = lerpColor(fromC, toC,.25)
    interF = lerpColor(fromC, toC,.3)
    interG = lerpColor(fromC,toC,.35)
    interH = lerpColor(fromC,toC,.4)
    interI = lerpColor(fromC, toC, .45)
    interJ = lerpColor(fromC, toC, .5)
    interK = lerpColor(fromC,toC,.55)
    interL = lerpColor(fromC,toC,.6)
    interM = lerpColor(fromC, toC,.65)
    interN = lerpColor(fromC, toC,.7)
    interO = lerpColor(fromC,toC,.75)
    interP = lerpColor(fromC,toC,.8)

    fill(fromC)
    rect(0, 0, width,20)
    fill(interA)
    rect(0,20,width,20)
    fill(interB)
    rect(0,40,width,20)
    fill(interC)
    rect(0,60,width,20)
    fill(interD)
    rect(0,80, width,20)
    fill(interE)
    rect(0,100,width,20)
    fill(interF)
    rect(0,120,width,20)
    fill(interG)
    rect(0,140,width,20)
    fill(interH)
    rect(0,160, width,20)
    fill(interI)
    rect(0,180,width,20)
    fill(interJ)
    rect(0,200,width,20)
    fill(interK)
    rect(0,220,width,20)
    fill(interL)
    rect(0,240, width,20)
    fill(interM)
    rect(0,260,width,20)
    fill(interN)
    rect(0,280,width,20)
    fill(interO)
    rect(0,300,width,20)
    fill(interP)
    
    #clouds
    if cloud1 >=800:
        cloud1=-200
    if cloud2 >=800:
        cloud2=-200
    cloud1+=1
    cloud2+=0.5
    noStroke()
    fill(255,255,255)
    
    #cloud 1
    ellipse(cloud1,80,60,60)
    ellipse(cloud1+30,60,60,60)
    ellipse(cloud1+30,110,60,60)
    ellipse(cloud1+80,60,60,60)
    ellipse(cloud1+80,110,60,60)
    ellipse(cloud1+110,80,60,60)
    ellipse(cloud1+70,80,60,60)
    
    #cloud 2
    ellipse(cloud2,170,60,60)
    ellipse(cloud2+30,150,60,60)
    ellipse(cloud2+30,200,60,60)
    ellipse(cloud2+80,150,60,60)
    ellipse(cloud2+80,200,60,60)
    ellipse(cloud2+110,170,60,60)
    ellipse(cloud2+70,170,60,60)
    
    #grass
    fill(50,180,25)
    rect(0,height-200,768,height)
    
    
    
    fill(180,100,40)
    dog=createShape(GROUP)
    head=createShape(ELLIPSE,0,0,60,60)
    body=createShape(ELLIPSE,60,30,80,60)
    leg1=createShape(RECT,30,40,20,50)
    leg2=createShape(RECT,70,40,20,50)
    ear=createShape(ELLIPSE,20,5,20,50)
    ear.setFill(color(120,70,30))
    dog.addChild(head)
    dog.addChild(body)
    dog.addChild(ear)
    dog.addChild(leg1)
    dog.addChild(leg2)

    dog_movement-=3
    translate(dog_movement,450)
    shape(dog)
    
    if dog_movement<=-500:
        dog_movement=800
    


    
    


    
        

    
        

    
    


    
        

    
        
