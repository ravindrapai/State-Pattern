class State:
    def insertQuarter(self):
        raise "State.insertQuarter - not overwritten"
    
    def ejectQuarter(self):
        raise "State.ejectQuarter - not overwritten"

    def turnCrank(self):
        raise "State.turnCrank - not overwritten"

    def dispenseGumBall(self):
        raise "State.dispenseGumBall - not overwritten"

class OutOfGumBalls(State):

    def __init__(self,newGum):
        self.gumBall = newGum

    def insertQuarter(self):
        self.ejectQuarter()
       
    def ejectQuarter(self):
        print "Out of GumBalls"

    def turnCrank(self):
        print "Out of GumBalls"

    def dispenseGumBall(self):
        print "Out of GumBalls"

class NoQuarter(State):

    def __init__(self,newGum):
        self.gumBall = newGum

    def insertQuarter(self):
        print "You inserted a Quarter"
        self.gumBall.setState(self.gumBall.getHasQuarterState())

    def ejectQuarter(self):
        print "You havent inserted a Quarter"

    def turnCrank(self):
        print "You turned the crank , but there is no Quarter"

    def dispenseGumBall(self):
        print "You need to pay first"

class HasQuarter(State):

    def __init__(self,newGum):
        self.gumBall = newGum

    def insertQuarter(self):
        print "Wait. You already inserted a Quarter"

    def ejectQuarter(self):
        print "Wait. Ejecting the Quarter"
        self.gumBall.setState(self.gumBall.getNoQuarterState())

    def turnCrank(self):
        print "You turned the crank"
        self.gumBall.setState(self.gumBall.getSoldState())

    def dispenseGumBall(self):
        print "Please turn the crank "

class SoldState(State):

    def __init__(self,newGum):
        self.gumBall = newGum

    def insertQuarter(self):
        print "Wait. You already inserted a Quarter"

    def ejectQuarter(self):
        print "Sorry. You already turned crank"

    def turnCrank(self):
        print "You are already turned the crank"

    def dispenseGumBall(self):
        self.gumBall.releaseBall()
        if self.gumBall.getCount() > 0:
           self.gumBall.setState(self.gumBall.getNoQuarterState())
        else:
           print "Sold Out !!!.No Gum Balls!!!"
           self.gumBall.setState(self.gumBall.getSoldOutState())

class GumBallMachine:

      def __init__(self,n=0):
         self.count = n
         self.out = OutOfGumBalls(self)
         self.sold = SoldState(self)
         self.quarter = HasQuarter(self)
         self.noQ = NoQuarter(self)
         if self.count > 0:
            self.state =  self.noQ
         else:
            self.state = self.out
            self.count = 0

      def getNoQuarterState(self):
          return self.noQ

      def getSoldOutState(self):
          return self.out

      def getHasQuarterState(self):
          return self.quarter

      def getSoldState(self):
          return self.sold

      def setState(self,nextState):
          self.state = nextState

      def getCount(self):
          return self.count

      def releaseBall(self):
          if self.count != 0:
             self.count = self.count - 1
          print "Gum ball is rolling out"

      def insertQuarter(self):
          self.state.insertQuarter()

      def ejectQuarter(self):
          self.state.ejectQuarter()

      def turnCrank(self):
          self.state.turnCrank()

      def dispenseGumBall(self):
          self.state.dispenseGumBall()

def Main():
    # 3 gum balls loaded
    gum = GumBallMachine(3)
    #doing every operation twice
    gum.insertQuarter()
    gum.insertQuarter()
    gum.turnCrank()
    gum.turnCrank()
    gum.dispenseGumBall()
    gum.dispenseGumBall()
    #doing everything sane
    gum.insertQuarter()
    gum.turnCrank()
    gum.dispenseGumBall()
    #repeating again
    gum.insertQuarter()
    gum.turnCrank()
    gum.dispenseGumBall()
    #out of stock, so invalid operation
    gum.insertQuarter()
    gum.turnCrank()
    gum.dispenseGumBall()

if __name__ == '__main__':
   Main()
