import fileinput
import math

#add function to print curves
#maybe non planar printing

class printer:
        
    def __init__(self, filType):
        self.time = 0
        self.xPos = 0
        self.yPos = 0
        self.zPos = 0
        self.ePos = 0
        self.mem = [] * 4

        self.filType = filType
        self.exTemp = 0
        self.bedTemp = 0
        self.output = []
    def __init__ (self, xPos, yPos, zPos, ePos, filType):
        self.xPos = xPos
        self.yPos = yPos
        self.zPos = zPos
        self.ePos = ePos
        self.mem = [] * 4
        self.filType = filType
        self.time = 0
        self.exTemp = 0
        self.bedTemp = 0
        self.output = []
    def setExTemp(self, temp):
        self.exTemp = temp
        self.output.append('M109 ' + temp)
        #M104S 
        #M109 - wait hot end temp

        self.output.append()
    def getTemps(self):
        self.output.append('M105 S')
        #M105 S - gets all temps
        
    def setBedTemp(self, temp):
        self.bedTemp = temp
        self.output.append('M140 S' + str(temp))
        #M140 S - set new temp

    def changeFil(self, filType):
        self.filType = filType
        prevX = self.xPos
        prevY = self.yPos
        prevZ = self.zPos
        #move away from part
        self.move(125, 125, 125, 0, 1000, False)
        #prompt - extrusion
        self.prompt('remove filament')
        #extrude in negative direction
        self.moveExtruder(-100, 1000)
        #prompt - change filament
        self.prompt('load filament')
        #set temperature 
        #extrude new filament forwards
        self.moveExtruder(100, 1000)
        #prompt - new filament loaded continue
        self.prompt('continue print')
        self.output.append('G92 E0')
        self.ePos = 0
        self.move(prevX, prevY, prevZ, 0, 1000, False)
        
    def prompt(self, prompt):
        self.output.append('M117 ' + prompt)
        #prompt for user

    def move(self, xPos, yPos, zPos, exf, speed, relative = True, extrude = True):
        if (relative == True):
            dist = math.sqrt(xPos * xPos + yPos * yPos)
            ePos = dist * exf
            if (extrude == True):
                self.output.append('G1 ' + 'X' + str(self.xPos + xPos) + ' Y' + str(self.yPos + yPos) + ' Z' + str(self.zPos + zPos) + ' E' + str(self.ePos + ePos) + ' F' + str(speed) + '\n')
            else:
                self.output.append('G0 ' + 'X' + str(self.xPos + xPos) + ' Y' + str(self.yPos + yPos) + ' Z' + str(self.zPos + zPos) + ' E' + str(self.ePos + ePos) + ' F' + str(speed) + '\n')
            #update nozzle position
            self.xPos = self.xPos + xPos
            self.yPos = self.yPos + yPos
            self.zPos = self.zPos + zPos
            self.ePos = self.ePos + ePos
        
        else:
            dist = math.sqrt((xPos - self.xPos)**2 + (yPos - self.yPos)**2)
            ePos = dist * exf
            if (extrude == True):
                self.output.append('G1 ' + 'X' + str(xPos) + ' Y' + str(yPos) + ' Z' + str(zPos) + ' E' + str(self.ePos + ePos) + ' F' + str(speed) + '\n')
            else:
                self.output.append('G0 ' + 'X' + str(xPos) + ' Y' + str(yPos) + ' Z' + str(zPos) + ' E' + str(self.ePos + ePos) + ' F' + str(speed) + '\n')
            self.xPos = xPos
            self.yPos = yPos
            self.zPos = zPos
            self.ePos = self.ePos + ePos
                
    def moveExtruder(self, ePos, speed):
            self.output.append('G1 ' + 'X' + str(self.xPos) + ' Y' + str(self.yPos) + ' Z' + str(self.zPos) + 'E ' + str(ePos) + ' F' + str(speed) + '\n')

    def setFil(self, filType):
        self.filType = filType
    def print(self):
        with open('preamble.txt', 'r') as p:
            preamble = p.read()
        with open('endcode.txt', 'r') as e:
            endcode = e.read()
        with open('output.txt', 'w') as f:
            f.write(preamble)
            f.write('\n\n')
            for i in self.output:
                f.write(i)
        
            f.write('\n\n')
            f.write(endcode)
    def zero(self):
        self.output.append('G92')
        #zeros printer using G92 command
    #def ssp(self, layerCount):
        #create pva layer
        #print 50, 100, 150, 200
        #wedges across surface 
        #standardized temp





    
