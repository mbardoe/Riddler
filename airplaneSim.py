__author__ = 'mbardoe'
import random

class airplane(object):
    def __init__(self, numSeats):
        self.numSeats = numSeats

    def getInLine(self):
        self.passengers =range(self.numSeats)
        random.shuffle(self.passengers)

    def getOnPlane(self):
        openSeats=range(self.numSeats)
        self.seats=self.numSeats*[-1]
        firstSeat=random.randint(0,self.numSeats-1)
        #print str(firstSeat)
        self.seats[firstSeat]=0
        openSeats.pop(openSeats.index(firstSeat))
        for i in range(1,self.numSeats):
            #print str(openSeats)
            if self.seats[self.passengers[i]]==-1:
                self.seats[self.passengers[i]]=i
                openSeats.pop(openSeats.index(self.passengers[i]))
            else:
                newSeat=random.choice(openSeats)
                self.seats[newSeat]=i
                openSeats.pop(openSeats.index(newSeat))

    def sim(self):
        self.getInLine()
        self.getOnPlane()
        #for i in range(self.numSeats):
        #    print ("Passenger "+ str(i) +" wanted to sit in "+str(self.passengers[i]) +" and sat in "+str(self.seats.index(i)))
        if self.passengers[self.numSeats-1]==self.seats.index(self.numSeats-1):
            return 1
        else:
            return 0

    def multiSim(self,numSims=1000):
        successes=0
        for n in range(numSims):
            successes+=self.sim()
        return float(successes)/float(numSims)


if __name__ == "__main__":
    ap=airplane(100)
    print str(ap.multiSim(20000))


