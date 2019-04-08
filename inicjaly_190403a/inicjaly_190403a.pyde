def setup():
    size (400, 400)
    textSize(120)
    textAlign(CENTER)
    background(255,255,255)
    global c
    global b
    c =('FFFFFFFF')
    b =('FF000000')
def draw():
    global c
    global b
    if keyPressed == True:
        fill(0)
        if key == 'V' or key == 'v':
           text('V', width/2+60, height/2)
        if mousePressed and keyCode==RIGHT:
            fill(255,0,0)
            text('V', width/2+60, height/2)
    else:     
        if mousePressed:
         fill(0,255,0)
         text('S',width/2-60, height/2)
        if mousePressed and keyCode==LEFT:
         fill(0,0,255)
         text('S',width/2-60, height/2)
    if hex(get(mouseX,mouseY)) == c:
     fill(255,0,255)
     text('S',width/2-60, height/2)
    else: 
        if hex(get(mouseX,mouseY)) == b:
         fill(0,255,255)
         text('V',width/2+60, height/2) 
   
