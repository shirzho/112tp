from tkinter import *
#root = Tk()
import math
import random
#########################################################################
#########################################################################
### 3D MATH CLASS ####
#########################################################################
#########################################################################

class Math3D(object):
    #set default values to 0
    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = x,y,z

    #rotate about x axis
    def xRotate(self, ang):
        radians = ang*math.pi/90
        y = self.y * math.cos(radians) - self.z *math.sin(radians)
        z = self.y * math.sin(radians) + self.z *math.cos(radians)
        return Math3D(self.x, y,z)

    #rotate about y axis
    def yRotate(self, ang):
        radians = ang*math.pi/90
        z = self.z * math.cos(radians) - self.x *math.sin(radians)
        x = self.z * math.sin(radians) + self.x * math.cos(radians)
        return Math3D(x,self.y, z)

    #rotate about z axis
    def zRotate(self, ang):
        radians = ang*math.pi/90
        x = self.x*math.cos(radians)- self.y * math.sin(radians)
        y = self.x * math.sin(radians) + self.y*math.cos(radians)
        return Math3D(x,y, self.z)

    #transform 3D to 2D using perspective projection
    def givePerspective(self, xLocation, yLocation, width, depth):
        #width of how far you want the shape to be seen
        factor = width / (depth + self.z)
        x = self.x * factor +  xLocation#window_width / 2
        y = self.y * factor + yLocation#window_height / 2
        return Math3D(x,y,1)
#########################################################################
#########################################################################
# DRAWING OUT THE 3D
#########################################################################
#########################################################################
class Make3D(object):
    def __init__(self,data, x, y):
        #self.shape = shape
        #self.color = color
        shape = random.choice(["cube","pyramid", "rectangle", 
            "twisted rectangle"])
        #self.size = 0.1
        if data.mode == "playDepth":
            self.size = 0.1
        else:
            self.size = 0.5

        self.depth = 5
        if shape=="cube":
            self.vertices = [
                    #y,z,x
                    Math3D(-self.size,-self.size,-self.size),
                    Math3D(self.size,-self.size,-self.size),
                    Math3D(self.size,-self.size,-self.size),
                    Math3D(-self.size,-self.size,-self.size),
                    Math3D(-self.size,self.size,self.size),
                    Math3D(self.size,self.size,self.size),
                    Math3D(self.size,-self.size,self.size),
                    Math3D(-self.size,-self.size,self.size)
                    ]
        elif shape=="pyramid":
            self.vertices = [
                    #y,z,x
                    Math3D(-self.size,self.size,-self.size),
                    Math3D(self.size,self.size,-self.size),
                    Math3D(self.size,-self.size,-self.size),
                    Math3D(-self.size,-self.size,-self.size),
                    Math3D(-self.size, self.size, self.size),
                    Math3D(self.size, self.size, self.size),
                    Math3D(self.size,-self.size,self.size),
                    Math3D(-self.size,-self.size,self.size)
                    ]
        elif shape=="twisted rectangle":
            #size = 0.5
            self.vertices = [
                    #y,z,x
                    Math3D(-self.size, -0.5*self.size,-self.size),
                    Math3D(self.size, -0.5*self.size, -self.size),
                    Math3D(self.size, 0.5*self.size, -self.size),
                    Math3D(-self.size, 0.5*self.size,-self.size),
                    Math3D(-self.size, 0.5*self.size, self.size),
                    Math3D(self.size, 0.5*self.size, self.size),
                    Math3D(self.size, -0.5*self.size, self.size),
                    Math3D(-self.size, -0.5*self.size,self.size)
                    ]

        elif shape== "rectangle":
            #size = 0.5
            self.vertices = [
                    #y,z,x
                    Math3D(-self.size, -0.5*self.size,-self.size),
                    Math3D(self.size, -0.5*self.size, -self.size),
                    Math3D(self.size, 0.5*self.size, -self.size),
                    Math3D(-self.size, 0.5*self.size,-self.size),
                    Math3D(-self.size, -0.5*self.size, self.size),
                    Math3D(self.size, -0.5*self.size, self.size),
                    Math3D(self.size, 0.5*self.size, self.size),
                    Math3D(-self.size, 0.5*self.size,self.size)
                    ]

        self.angleX = 10
        self.angleY = 10
        self.angleZ = 10
        self.faces = [(0,1,2,3),(1,5,6,2),(5,4,7,6),
        (4,0,3,7),(0,4,5,1),(3,2,6,7)]
        self.width = data.width
        self.height = data.height
        self.xLocation = x
        self.yLocation = y
        self.color = random.choice(["dark slate blue", "honeydew", 
        "medium turquoise", "indian red", "violet red", "pale green", "cyan",
        "deep pink", "spring green", "dodger blue", "yellow", 
        "orange red", "orange", "blue violet"])
        #self.color
        self.coorList = None

    def run3DCube(self,canvas):
        coorList = []
        for vertex in self.vertices:
            rotatedPoint = vertex.xRotate(self.angleX)
            rotatedPoint = rotatedPoint.yRotate(self.angleY)
            rotatedPoint = rotatedPoint.zRotate(self.angleZ)
            point = rotatedPoint.givePerspective(self.xLocation, 
                self.yLocation, 250, self.depth)
            x = int(point.x)
            y = int(point.y)
            coorList.append(point)
            #draws vertices (dots)
            canvas.create_rectangle(x,y, x+0.5, y+0.5, 
                fill = self.color, width = 0)

        for face in self.faces:
            #draws solid faces of shape

            canvas.create_line(coorList[face[0]].x, coorList[face[0]].y,
                    coorList[face[1]].x, coorList[face[1]].y, fill = self.color)
            canvas.create_line(coorList[face[1]].x, coorList[face[1]].y,
                    coorList[face[2]].x, coorList[face[2]].y, fill = self.color)
            canvas.create_line(coorList[face[2]].x, coorList[face[2]].y,
                    coorList[face[3]].x, coorList[face[3]].y, fill = self.color)
            canvas.create_line(coorList[face[3]].x, coorList[face[3]].y,
                    coorList[face[0]].x, coorList[face[0]].y, fill = self.color)
        
        self.coorList = [coorList[face[0]].x, coorList[face[0]].y, 
            coorList[face[1]].x, coorList[face[1]].y, 
            coorList[face[2]].x, coorList[face[2]].y,
            coorList[face[3]].x, coorList[face[3]].y,
            coorList[face[0]].x, coorList[face[0]].y] 
    #finds greatest and smallest x coordinate in a list of shape coordinates
    def largestXCoor(self):
        currCoor = None
        if self.coorList!=None:
            for coordinate in range (0, len(self.coorList),2):
                if currCoor ==None or self.coorList[coordinate]> currCoor:
                    currCoor = self.coorList[coordinate] 
        if currCoor!=None:
            return currCoor 
    def smallestXCoor(self):
        currCoor = None
        if self.coorList!=None:
            for coordinate in range (0, len(self.coorList),2):
                if currCoor ==None or self.coorList[coordinate]<currCoor:
                    currCoor = self.coorList[coordinate]
        if currCoor!=None: 
            return currCoor 

    def largestYCoor(self):
        currCoor = None
        if self.coorList!=None:
            for coordinate in range (1, len(self.coorList),2):
                if currCoor ==None or self.coorList[coordinate]> currCoor:
                    currCoor = self.coorList[coordinate] 
        if currCoor!=None:
            return currCoor 

    def smallestYCoor(self):
        currCoor = None
        if self.coorList!=None:
            for coordinate in range (1, len(self.coorList),2):
                if currCoor ==None or self.coorList[coordinate]<currCoor:
                    currCoor = self.coorList[coordinate] 
        if currCoor!=None:
            return currCoor 

#########################################################################
#########################################################################
#### FALLING STARS BACKGROUND ####
#########################################################################
#########################################################################

class FallingStars(object):
    def __init__(self, data):
        self.smallStarList=[]
        self.medStarList=[]
        self.largeStarList=[]
        self.moonHoles = []
        self.width = data.width
        self.height = data.height
        self.stars()

    def fallingStars(self, data):
        if data.mode == "playSideScroll" and data.rightArrowPress:
            for i in range(len(self.smallStarList)):
                x,y = self.smallStarList[i]
                self.smallStarList[i] = (x-4, y)
                #if y >=self.height:
                    #y = 10
                if x <= 5:
                    x = self.width - 10
                    self.smallStarList[i] =(x,y)
            for i in range(len(self.medStarList)):
                x,y = self.medStarList[i]
                self.medStarList[i] = (x-4, y)
                #if y >=self.height:
                    #y = 10
                if x <= 5:
                    x = self.width - 10
                    self.medStarList[i]=(x,y)
            for i in range(len(self.largeStarList)):
                x,y = self.largeStarList[i]
                self.largeStarList[i] = (x-4, y)
                #if y >=self.height:
                    #y = 10
                if x <= 5:
                    x = self.width - 10
                    self.largeStarList[i] = (x,y)

        else:
            for i in range(len(self.smallStarList)):
                x,y = self.smallStarList[i]
                self.smallStarList[i] = (x, y+2)
                if y >=self.height:
                    y = 10
                    self.smallStarList[i] =(x,y)

            for i in range(len(self.medStarList)):
                x,y = self.medStarList[i]
                self.medStarList[i] = (x, y+1)
                if y >=self.height:
                    y = 10
                
                    self.medStarList[i]=(x,y)
            for i in range(len(self.largeStarList)):
                x,y = self.largeStarList[i]
                self.largeStarList[i] = (x, y+0.5)
                if y >=self.height:
                    y = 10
                
                    self.largeStarList[i] = (x,y)

    def stars(self):
        for i in range (50):
            x = random.randint(0,self.width)
            y = random.randint(0,self.height)
            self.smallStarList.append((x,y))
        
        for i in range(50):
            x = random.randint(0,self.width)
            y = random.randint(0, self.height)
            self.medStarList.append((x,y))
        
        for i in range(50):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            self.largeStarList.append((x,y))

    def drawMoon(self,canvas):
        canvas.create_oval(50,50, 150,150, 
            fill = "pale goldenrod", width= 0)
        canvas.create_oval(50, 55, 130,145, fill = "light yellow", width=0)
    
    def moonHoles(self,canvas):
        numOfMoonHoles = 10
        for i in range(numOfMoonHoles):
            x= random.randint(60, 130)
            y = random.randint(65,140)
            self.moonHoles.append((x,y))
        

    def drawMoonHoles(self, canvas):
        lis = [(117, 122), (81, 108), (60, 121), (129, 113), 
        (129, 97), (82, 89), (97, 123), (62, 86), (103, 80), (73, 131)]
        for hole in lis:
            x,y = hole
            hol = 5 #random.randint(3,6)
            canvas.create_oval(x-hol, y-hol, x+hol, y+hol, 
            fill = "pale goldenrod", width = 0)
    def drawStars(self, canvas):
        #star sizes
        small = 0.5
        med = 1
        L = 1.3
        for star in self.smallStarList:
            x,y=star
            canvas.create_rectangle(x-small, y-small, 
                x+small, y+small, fill = "white", width = 0)
        for star in self.medStarList:
            x,y=star
            canvas.create_rectangle(x-med, y-med, 
                x+med, y+med, fill = "white", width=0)
        for star in self.largeStarList:
            x,y=star
            canvas.create_rectangle(x-L, y-L, x+L, y+L, fill = "white", width=0)
#########################################################################
#########################################################################
#### CONTROL FOR GAME ####
#########################################################################
#########################################################################
   
def jumpUp(data):
    
    maxJumpHeight = 200
    #only moves y coordinates
    origCenter = 500
    #print("catcoors", data.catCenter[1])
    if data.catCenter[1] > origCenter - maxJumpHeight:
        data.catCenter[1] -= data.speed
        if data.speed >1:
            data.speed -= 1
    #else: #if data.catCenter[1]<=origCenter - maxJumpHeight:
        #print("LALALA")
        #print(data.jump)
    #else:
def jumpDown(data):
    #print("boop")
    if data.catCenter[1] <= 500:
        #print(data.catCenter[1])
        data.catCenter[1]+= 10
    else: 
        data.jumpDown = False
    
#data.jump = False
 
#checks that cat doesn't walk into any shapes
#returns true if clear, false if something is in the way
def stayClear(data):
    for shape in data.shapeList:
        #checks the x coors
        for coor in range(0, len(shape.coorList), 2):
            if not (data.cat.backleg[0]  < shape.coorList[coor] or 
            data.cat.head[8]  > shape.coorList[coor]): #greatestXPointInShape
                #return False
                for coor in range(1, len(shape.coorList), 2):
                    if not (data.cat.backleg[7] < shape.coorList[coor]
                    or data.cat.head[1] > shape.coorList[coor]):
                        return False
                #return False

    return True

def hitByFish(data):
    for shape in data.shapeList:
        if data.fishCenter!= None and shape.coorList!=None:
            if (shape.smallestXCoor()<data.fishCenter[0] < shape.largestXCoor()
            and shape.smallestYCoor()<data.fishCenter[1]<shape.largestYCoor()):
                return True
    return False 

def hitByBlock(data):
    #data.catCenter[1] (+-70)
    #data.catCenter[0] (+-85)
    for shape in data.shapeList:
        if shape.coorList!=None:
            if ((data.catCenter[0]-85<shape.smallestXCoor()<data.catCenter[0]+85 
            or data.catCenter[0]-85<shape.largestXCoor()<data.catCenter[0]+85) 
            and data.catCenter[1]+70>shape.largestYCoor()>data.catCenter[1]-70):
                return True
        
        return False

def catCollideStar(data):
    if data.starOnScreen == True:
        print((data.catCenter[0] - 85 < data.starCenter < 
            data.catCenter[1] + 85))
        if (data.catCenter[0] - 85 < data.starCenter < 
            data.catCenter[0] + 85):
            data.drawText=True
            return True
        
        return False

def initImages(data):
    data.cat1 = PhotoImage(file="whiteCat.gif")
    data.fish = PhotoImage(file="fish.gif")
    data.cat2 = PhotoImage(file="whiteCat1.gif")
    data.catFace = PhotoImage(file="catface.gif")
    data.depthLivesList = []
    data.sideScrollLivesList = []
    heart = PhotoImage(file="heart.gif")
    for hearts in range(3):
        data.depthLivesList.append(heart)
    for hearts in range(3):
        data.sideScrollLivesList.append(heart)
    data.star = PhotoImage(file="star.gif")


def init(data):
    #data.width = width
    #data.height = height
    initImages(data)
    data.background = FallingStars(data)
    data.mode = "startScreen"
    data.depthScore = 0
    data.sideScrollScore = 0
    data.timeCount = 0
    data.timeSoFar = 0
    data.shapeSpeed = 3
    data.depthGameOver = False
    data.sideScrollGameOver = False
    data.shapeList = [] 
    data.size = 0.1
    data.catCenter = [500,500]
    data.fishAppear = False
    data.fishCenter = None
    data.jumpUp = False
    data.jumpDown= False
    data.rightArrowPress = False
    data.speedUp = False
    data.changeSpeed = False
    data.starCenter = random.randint(100,900)
    data.starOnScreen=False
    data.catChange = True
    data.speed = 10
    data.lifeLost = True
    data.drawText = False
    

def mousePressed(event, data):
    
    if (data.mode == "startScreen"): startScreenMousePressed(event, data)
    elif (data.mode == "playDepth"): playDepthMousePressed(event, data)
    elif (data.mode == "playSideScroll"):playSideScrollMousePressed(event, data)
    elif (data.mode == "help"): helpMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == "startScreen"): startScreenKeyPressed(event, data)
    elif (data.mode == "playDepth"):   playDepthKeyPressed(event, data)
    elif (data.mode == "playSideScroll"): playSideScrollKeyPressed(event, data)
    elif (data.mode == "help"):       helpKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "startScreen"): startScreenTimerFired(data)
    elif (data.mode == "playDepth"):   playDepthTimerFired(data)
    elif (data.mode == "playSideScroll"): playSideScrollTimerFired (data)
    elif (data.mode == "help"):       helpTimerFired(data)
    
def redrawAll(canvas, data):
    if (data.mode == "startScreen"): startScreenRedrawAll(canvas, data)
    elif (data.mode == "playDepth"): playDepthRedrawAll(canvas, data)
    elif (data.mode == "playSideScroll"): playSideScrollRedrawAll(canvas,data)
    elif (data.mode == "help"): helpRedrawAll(canvas, data)
    

####################################
# startScreen mode
####################################

def startScreenMousePressed(event, data):
    x = event.x
    y = event.y
    if clickOnPlayDepth(data, x, y):
        init(data)
        data.mode = "playDepth"
    elif clickOnHelp(data, x, y):
        data.mode = "help"
    elif clickOnPlaySideScroll(data,x,y):
        init(data)
        data.mode = "playSideScroll"

#checks if mouse press is within the play depth game button
def clickOnPlayDepth(data, x, y):
    return (data.width/2-250 < x < data.width/2 and 
        data.height/2 +10 < y < data.height/2 +  50)
#checks if mouse press is within the sidescroll button
def clickOnPlaySideScroll(data,x,y):
    return(data.width/2+10 < x < data.width/2 + 310 and 
        data.height/2 + 10 < y < data.height/2 + 50)
#checks if mouse press is within the help button
def clickOnHelp(data,x,y):
    return (data.width/2-130< x <data.width/2 + 130 and
        data.height/2 +60 < y < data.height/2 + 100)

def startScreenKeyPressed(event, data):
    pass

def startScreenTimerFired(data):
    data.background.fallingStars(data)

def startScreenRedrawAll(canvas, data):
    canvas.create_rectangle(0,0, data.width, data.height, fill = "black")
    data.background.drawMoon(canvas)
    data.background.drawMoonHoles(canvas)
    data.background.drawStars(canvas)
    drawScreenButtons(data,canvas)
    #canvas.create_image(data.width/2-200,
        #data.height/2 + 20, image = data.catFace)

#draws all the button options on the start screen
def drawScreenButtons(data, canvas):
    #title
    canvas.create_text(data.width/2, data.height/2-40,
            text="Cat Galactica", font="Helvetica 50 bold", fill = "white")
    #play depth
    canvas.create_rectangle(data.width/2-250, data.height/2 + 10, 
        data.width/2, data.height/2 +50, fill = "red" )
    canvas.create_text(data.width/2-120, data.height/2+30,
            text="Click to Play 3D Mode!", font="Arial 20 bold", fill = "white")
    #play side scroll
    canvas.create_rectangle(data.width/2+10, data.height/2 + 10, 
        data.width/2 + 310, data.height/2 + 50, fill = "red")
    canvas.create_text(data.width/2 + 160, data.height/2 + 30, 
        text="Click to Play Side Scroll Mode!", font = "Arial 20 bold", 
        fill = "white")
    #help
    canvas.create_rectangle(data.width/2-130, data.height/2 + 60, 
        data.width/2 + 130, data.height/2 +100, fill = "red" )
    canvas.create_text(data.width/2, data.height/2+80,
            text="Click Here for Help", font="Arial 20 bold", fill = "white")

####################################
# help mode
####################################

def helpMousePressed(event, data):
    pass

def helpKeyPressed(event, data):
    if event.keysym == "b":
        data.mode = "startScreen"

def helpTimerFired(data):
    data.background.fallingStars(data)

def helpRedrawAll(canvas, data):
    canvas.create_rectangle(0,0, data.width, data.height, fill = "black")
    data.background.drawMoon(canvas)
    data.background.drawMoonHoles(canvas)
    data.background.drawStars(canvas)
    helpInstructions(data,canvas)

#make all game instructions here
def helpInstructions(data, canvas):
    canvas.create_text(data.width/2, data.height/2-40,
        text="How to Play:", font="Arial 26 bold", fill = "white")
    canvas.create_text(data.width/2, data.height/2+50,
        text='''Instructions: use the left and right arrow keys in both modes to move the cat.
        Use space bar to either jump in the side-scrolling game or to shoot fish
        at shapes in 3D mode.''', font="Arial 20", fill = "white")
    canvas.create_text(data.width/2, data.height/2+100,
        text="press 'b' to go back!", font="Arial 20", fill = "white")
    

####################################
# playDepth mode
####################################

def playDepthMousePressed(event, data):
    pass

def playDepthKeyPressed(event, data):
    if event.keysym  == "q":
        data.mode = "startScreen"

    if event.keysym == "space":
        data.fishAppear = True
        data.fishCenter = [data.catCenter[0]+40, data.catCenter[1]-100]

    if event.keysym =="Left":
        data.catCenter[0] -= 20
        if data.catChange==True:
            data.catChange = False
        else: 
            data.catChange = True

    elif event.keysym == "Right":
        data.catCenter[0] += 20
        if data.catChange==True:
            data.catChange = False
        else: 
            data.catChange = True
    

def playDepthTimerFired(data):
    data.background.fallingStars(data)
    data.timeCount += 1
    data.timeSoFar = (data.timerDelay*data.timeCount)/1000
    if data.fishCenter!= None:
        data.fishCenter[1] -=4
    
    if data.depthGameOver==False:
   
        if data.timeSoFar%2 == 0:
            x = random.randint(50, 950)
            data.shapeList.append(Make3D(data, x, 150))
        for shape in data.shapeList:
            shape.angleX += 1
            shape.angleY += 1
            shape.angleZ += 1
        for shape in data.shapeList:
            shape.yLocation += data.shapeSpeed
            if shape.depth > 0.3:
                shape.depth -=0.07

            else: 
                data.shapeList.remove(shape)
                data.depthLivesList.remove(data.depthLivesList[-1])

            if hitByFish(data):
                #print("hit block")
                data.shapeList.remove(shape)
                data.depthScore+= 1
                data.speedUp = False
                data.changeSpeed = True
                data.fishAppear = False
        if data.depthScore!= 0 and data.depthScore%10== 0 and data.changeSpeed:
            data.shapeSpeed+=1
            data.changeSpeed = False
            data.speedUp = True
    else:
        #if game over is true
        if data.timeSoFar%2 == 0:
            pass
        for shape in data.shapeList:
            pass
        for shape in data.shapeList:
            pass
            
    #one method to check if lives are lost
    if data.fishAppear and not hitByFish(data) and data.fishCenter[1] <= 10: 
        data.depthLivesList.remove(data.depthLivesList[-1])
        data.fishAppear = False

    #checks for game over state
    if len(data.depthLivesList)==0:
        data.depthGameOver = True

    if data.depthGameOver:
        #stop everything on screen
        pass
        
            


def playDepthRedrawAll(canvas, data):
    #for point in shape.coorList:
    #    x,y = point
    #    canvas.create_rectangle(x,y, x+2, y+2, fill = "red")
    canvas.create_rectangle(0,0, data.width, data.height, fill = "black")
    data.background.drawMoon(canvas)
    data.background.drawMoonHoles(canvas)
    data.background.drawStars(canvas)
    
    canvas.create_text(data.width-100 , 50,
        text="Score: %d" % (data.depthScore), font="Arial 26 bold", 
        fill = "white")

    for shape in data.shapeList:
        shape.run3DCube(canvas)
       
    x,y = data.catCenter
    if data.catChange == True:
        canvas.create_image(x, y, image=data.cat1)
    elif data.catChange == False:
        canvas.create_image(x,y, image=data.cat2)
    if data.fishAppear:
        canvas.create_image(data.fishCenter[0], 
            data.fishCenter[1], image=data.fish)
    x1,y1 = 670,50
    for heart in data.depthLivesList: 
        canvas.create_image(x1, y1, image=heart)
        x1+=50
    canvas.create_text(data.width/2, 50, text = "press 'q' to quit", 
        font = "Arial 26", fill = "white")
    if data.speedUp ==True:
        color = random.choice(["dark slate blue", "honeydew", 
        "medium turquoise", "indian red", "violet red", "pale green", "cyan",
        "deep pink", "spring green", "dodger blue", "yellow", 
        "orange red", "orange", "blue violet"])
        canvas.create_text(data.width/2, data.height/2,
        text="SPEED UP", font="Arial 50 bold", fill = color)
    if data.depthGameOver:
        canvas.create_text(data.width/2, data.height/2,
        text="GAME OVER", font="Arial 50 bold", fill = "white")


####################################
# playSideScroll mode
####################################
def playSideScrollMousePressed(event, data):
    pass

def playSideScrollKeyPressed(event, data):
    if event.keysym  == "q":
        data.mode = "startScreen"
    if event.keysym == "space":
        data.drawText = False
        data.starCenter=random.randint(100,900)
        data.jumpUp = True
        jumpUp(data)

        #data.fishAppear = True
        #data.fishCenter = [data.catCenter0]+40, data.catCenter[1]-100]
    #for shape in data.shapeList:
        #shape.moveShape(event)
    #if stayClear(data):
    #print(stayClear(data))
    
    #if event.keysym == "Up":         
        #data.catCenter[1] -= 20
        #self.angleX-=3
    #elif event.keysym == "Down":
     #   data.catCenter[1] += 20
        #self.angleX+=3
    elif event.keysym =="Left":
        data.catCenter[0] -= 10
        #self.angleY+=3
    elif event.keysym == "Right":
        if data.starOnScreen:
            data.catCenter[0] +=10
        data.rightArrowPress = True
        if data.catChange==True:
            data.catChange = False
        else: 
            data.catChange = True
        #data.catCenter[0] += 10
    else: data.rightArrowPress = False
    #data.cat.moveCat(event,data)
    

def playSideScrollTimerFired(data):
    if data.jumpUp == True:
        data.speed = 10
        jumpUp(data)
    if data.catCenter[1]<= 300:
        data.jumpUp = False
        data.jumpDown = True
    if data.jumpDown==True:
        jumpDown(data)
    if not data.sideScrollGameOver:
        data.background.fallingStars(data)
        data.timeCount += 1
        data.timeSoFar = (data.timerDelay*data.timeCount)/1000
        if data.fishCenter!= None:
            data.fishCenter[1] -=4
        
        if data.timeSoFar%2 == 0:
            data.sideScrollScore+=1
            data.lifeLost = True
        #print(data.timeSoFar)
        if data.timeSoFar%4 == 0:
           data.shapeList.append(Make3D(data, 900, 530))
        if data.sideScrollScore!= 0 and data.sideScrollScore%7 == 0:
            #print("hello???")
            data.starOnScreen = True
        for shape in data.shapeList:
            shape.angleX += 1
            shape.angleY += 1
            shape.angleZ += 1
            shape.xLocation += -10
            if shape.xLocation <= 5:
                data.shapeList.remove(shape)
    else: 
        pass
    
    for shape in data.shapeList:
        if hitByBlock(data) and data.lifeLost:
            data.sideScrollLivesList.remove(data.sideScrollLivesList[-1]) 
            data.lifeLost = False
    if len(data.sideScrollLivesList)==0:
        data.sideScrollGameOver = True

    if data.starOnScreen and catCollideStar(data):
        print("HELLLOOOOOOOOOO????")
        data.sideScrollScore += 3
        data.starOnScreen = False
        
        


def playSideScrollRedrawAll(canvas, data):
    #for point in shape.coorList:
    #    x,y = point
    #    canvas.create_rectangle(x,y, x+2, y+2, fill = "red")
    canvas.create_rectangle(0,0, data.width, data.height, fill = "black")
    data.background.drawMoon(canvas)
    data.background.drawMoonHoles(canvas)
    data.background.drawStars(canvas)
    
    canvas.create_text(data.width-100 , 50,
        text="Score: %d" % (data.sideScrollScore), 
        font="Arial 26 bold", fill = "white")

    canvas.create_text(data.width/2, 50, text = "press 'q' to quit", 
        font = "Arial 26", fill = "white")
    for shape in data.shapeList:
        shape.run3DCube(canvas)
        #print (shape.coorList)
    #data.cat.drawCat(canvas,"gray")
    x,y = data.catCenter
    #canvas.create_image(x, y, image=data.cat1)
    if data.catChange == True:
        canvas.create_image(x, y, image=data.cat1)
    elif data.catChange == False:
        canvas.create_image(x,y, image=data.cat2)

    x1,y1 = 670,50
    for heart in data.sideScrollLivesList: 
        canvas.create_image(x1, y1, image=heart)
        x1+=50
    
    if data.starOnScreen:
        #print("BOOP")
        canvas.create_image(data.starCenter, 550, image = data.star)

    if data.drawText==True:
        color = random.choice(["dark slate blue", "honeydew", 
        "medium turquoise", "indian red", "violet red", "pale green", "cyan",
        "deep pink", "spring green", "dodger blue", "yellow", 
        "orange red", "orange", "blue violet"])
    
        canvas.create_text(data.width/2, data.height/2, 
        text = "You collected a star!!!", 
        font = "Arial 50", fill = color)
        
        #data.starCenter = random.randint(100, 900)
        
        

    if data.sideScrollGameOver:
        canvas.create_text(data.width/2, data.height/2,
        text="GAME OVER", font="Arial 50 bold", fill = "white")

    


   
#########################################################################
#########################################################################
#### RUN FUNCTION taken from 15 112 site "barebones"
#########################################################################
#########################################################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call 
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 50 # milliseconds
    
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    init(data)
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1000, 600)










