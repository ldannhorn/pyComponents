from gate_xor import XorGate
from gate_and import AndGate
class HalfAdder():
    def __init__(self,id:str):
        self.type = 'HalfAdder'
        self.id = str(id)
        self.inX = False
        self.inY = False
        self.outS = False
        self.outC = False
        self.mode = 'native'
        self.refresh()
    
    def setInput(self,inputID:str,state:bool):
        inputID = str(inputID)
        state = bool(state)
        if inputID == 'inX': self.inX = state
        elif inputID == 'inY': self.inY = state
        self.refresh()
    
    def setMode(self,mode:str):
        mode = str(mode).lower()
        if mode == 'native': self.mode = mode
        elif mode == 'transistor': self.mode = mode
    
    def get(self, pin:str):
        pin = str(pin)
        if pin == 'inX': return self.inX
        elif pin == 'inY': return self.inY
        elif pin == 'outS': return self.outS
        elif pin == 'outC': return self.outC

    def refresh(self):
        self.typeString = f'{self.type}@{self.mode}'
        self.inX = bool(self.inX)
        self.inY = bool(self.inY)
        self.outS = bool(self.outS)
        self.outC = bool(self.outC)
        if self.mode == 'native':
            if bool.__xor__(self.inX,self.inY):
                self.outS = True
                self.outC = False
            elif bool.__and__(self.inX,self.inY):
                self.outS = False
                self.outC = True
            else:
                self.outS = False
                self.outC = False
        elif self.mode == 'transistor':
            gXor = XorGate('gXor')
            gAnd = AndGate('gAnd')
            gXor.setMode('transistor')
            gAnd.setMode('transistor')
            gXor.setInput('inX', self.inX)
            gXor.setInput('inY', self.inY)
            gAnd.setInput('inX', self.inX)
            gAnd.setInput('inY', self.inY)
            self.outS = gXor.get('out')
            self.outC = gAnd.get('out')
    
    def printInfoColored(self):
        from colorama import Fore; import colorama; colorama.init()
        self.refresh()
        print(f'{Fore.YELLOW}Type: {self.typeString}\nID: {self.id}{Fore.GREEN if self.inX else Fore.RED}\ninX: {self.inX}\n{Fore.GREEN if self.inY else Fore.RED}inY: {self.inY}{Fore.GREEN if self.outS else Fore.RED}\noutS: {self.outS}{Fore.RESET}\n{Fore.GREEN if self.outC else Fore.RED}outC: {self.outC}{Fore.RESET}\n')


if __name__ == '__main__':
    adder = HalfAdder('adder')

    print('--- NATIVE ---')

    adder.printInfoColored()

    adder.setInput('inX', True)
    adder.printInfoColored()

    adder.setInput('inX', False)
    adder.setInput('inY', True)
    adder.printInfoColored()

    adder.setInput('inX', True)
    adder.printInfoColored()

    print('--- TRANSISTOR ---')

    adder.setMode('transistor')

    adder.setInput('inX', False)
    adder.setInput('inY', False)
    adder.printInfoColored()

    adder.setInput('inX', True)
    adder.printInfoColored()

    adder.setInput('inX', False)
    adder.setInput('inY', True)
    adder.printInfoColored()

    adder.setInput('inX', True)
    adder.printInfoColored()