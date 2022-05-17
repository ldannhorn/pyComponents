from arithmetic_half_adder import HalfAdder
from gate_or import OrGate
class FullAdder():
    def __init__(self,id:str):
        self.type = 'FullAdder'
        self.id = str(id)
        self.inX = False
        self.inY = False
        self.inC = False
        self.outS = False
        self.outC = False
        self.mode = 'native'
        self.refresh()
    
    def setInput(self,inputID:str,state:bool):
        inputID = str(inputID)
        state = bool(state)
        if inputID == 'inX': self.inX = state
        elif inputID == 'inY': self.inY = state
        elif inputID == 'inC': self.inC = state
        self.refresh()
    
    def setMode(self,mode:str):
        mode = str(mode).lower()
        if mode == 'native': self.mode = mode
        elif mode == 'transistor': self.mode = mode

    def refresh(self):
        self.typeString = f'{self.type}@{self.mode}'
        self.inX = bool(self.inX)
        self.inY = bool(self.inY)
        self.outS = bool(self.outS)
        self.outC = bool(self.outC)
        if self.mode == 'native':
            inTuple = (self.inX,self.inY,self.inC)
            trueCounter = 0
            for value in inTuple:
                if value: trueCounter+=1

            if trueCounter == 1:
                self.outS = True; self.outC = False
            elif trueCounter == 2:
                self.outS = False; self.outC = True
            elif trueCounter == 3:
                self.outS = True; self.outC = True
            else: self.outS = None; self.outC = None


        elif self.mode == 'transistor':
            ha1 = HalfAdder('ha1'); ha1.setMode('transistor')
            ha2 = HalfAdder('ha2'); ha2.setMode('transistor')
            gOr = OrGate('gOr'); gOr.setMode('transistor')

            ha1.setInput('inX', self.inX)
            ha1.setInput('inY', self.inY)
            ha2.setInput('inX', ha1.get('outC'))
            ha2.setInput('inY', self.inC)
            gOr.setInput('inX', ha1.get('outS'))
            gOr.setInput('inY', ha2.get('outS'))
            self.outS = ha2.get('outC')
            self.outC = gOr.get('out')

    
    def printInfoColored(self):
        from colorama import Fore; import colorama; colorama.init()
        self.refresh()
        print(f'{Fore.YELLOW}Type: {self.typeString}\nID: {self.id}{Fore.GREEN if self.inX else Fore.RED}\ninX: {self.inX}\n{Fore.GREEN if self.inY else Fore.RED}inY: {self.inY}\n{Fore.GREEN if self.inC else Fore.RED}inC: {self.inC}\n{Fore.GREEN if self.outS else Fore.RED}outS: {self.outS}{Fore.RESET}\n{Fore.GREEN if self.outC else Fore.RED}outC: {self.outC}{Fore.RESET}\n')


if __name__ == '__main__':
    def boolify(arg:str):
        arg = str(arg).lower()
        if arg == 'true': return True
        elif arg == 'false': return False
        else: return

    adder = FullAdder('adder')

    while True:
        adder.setInput('inX', boolify(input('X: ')))
        adder.setInput('inY', boolify(input('Y: ')))
        adder.setInput('inC', boolify(input('Cin: ')))

        adder.printInfoColored()

        input()

