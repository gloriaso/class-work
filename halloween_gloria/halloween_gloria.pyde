def setup():
    size(768,576)
    global tree
    global ghost
    global fence
    global bat
    tree=loadImage("tree.png")
    ghost=loadImage("ghost.png")
    ghost.resize(120,130)
    fence=loadImage("fence.png")
    bat=loadImage("bat.png")
    bat.resize(60,96)


cloud1=100
cloud2=500
ghost1_pos=0
ghost2_pos=-400
bat_xpos=768


def draw():
    background(5, 10, 80)
    noStroke()
    #moon
    fill(85, 105, 252)
    ellipse(200,150,210,210)
    fill(202, 207, 247)
    ellipse(200,150,200,200)
    fill(169, 174, 211,100)
    ellipse(230,160,30,30)
    ellipse(230,130,30,30)
    ellipse(210,230,40,40)
    ellipse(190,130,45,45)
    ellipse(155,90,50,50)
    
    
    #clouds
    global cloud1
    global cloud2
    fill(255)
    if cloud1 >=800:
        cloud1=-200
    cloud1+=1 
    if cloud2>=800:
        cloud2=-200
    cloud2+=0.8
    
    fill(255)
    ellipse(cloud1,130,60,60)
    ellipse(cloud1+30,110,60,60)
    ellipse(cloud1+30,160,60,60)
    ellipse(cloud1+80,110,60,60)
    ellipse(cloud1+80,160,60,60)
    ellipse(cloud1+110,130,60,60)
    ellipse(cloud1+70,130,60,60)
    ellipse(cloud1+40,130,60,60)

    ellipse(cloud2,200,60,60)
    ellipse(cloud2+30,180,60,60)
    ellipse(cloud2+30,230,60,60)
    ellipse(cloud2+80,180,60,60)
    ellipse(cloud2+80,230,60,60)
    ellipse(cloud2+110,200,60,60)
    ellipse(cloud2+70,200,60,60)
    ellipse(cloud2+40,200,60,60)

    #grass
    fill(8,92,54)
    ellipse(width/2,height+50,width+100,200)
    
    #ghost
    global ghost1_pos
    global ghost2_pos
    tint(255,255,255,100)
    image(ghost,ghost1_pos,250)
    if ghost1_pos >=800:
        ghost1_pos=-200
    ghost1_pos+=1.5
    
    image(ghost,ghost2_pos,150)
    if ghost2_pos>=800:
        ghost2_pos=-200
    ghost2_pos+=1.7
        
    
    
    #tree
    tint(0)
    image(tree,0,0,400,600)
    
    #haunted house
    fill(0)
    triangle(500,200,420,280,580,280)
    rect(450,280,100,60)
    triangle(500,300,380,400,620,400)
    quad(430,400,570,400,545,550,455,550)
    fill(242,165,22)
    rect(480,280,40,50)
    rect(475,400,50,60)
    stroke(0)
    strokeWeight(3)
    line(500,280,500,330)
    line(480,305,520,305)
    line(500,400,500,550)
    line(475,430,525,430)
    
    #pumpkin
    noStroke()
    fill(65,102,6)
    rect(315,260,10,30)
    fill(245,150,42)
    ellipse(320,310,60,50)
    fill(74,44,10)
    triangle(305,295,295,310,315,310)
    triangle(335,295,325,310,345,310)
    
    #fence
    image(fence,300,450)
    
    #bat
    global bat_xpos
    image(bat,bat_xpos,60)
    if bat_xpos<=-200:
        bat_xpos=800
    bat_xpos-=3
    
    
    
