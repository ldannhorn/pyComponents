from logic_transistor import Transistor
from gate import Gate
class AndGate(Gate):
    def __init__(self,id:str):
        self.type = 'AndGate'
        self.id = str(id)
        self.inX = False
        self.inY = False
        self.out = False
        self.mode = 'native'
        self.refresh()
    def refresh(self):
        self.typeString = f'{self.type}@{self.mode}'
        if self.mode == 'native':
            if self.inX and self.inY: self.out = True
            else: self.out = False
        elif self.mode == 'transistor':
            t = Transistor('t')
            t.setInput('base',self.inX)
            t.setInput('collector',self.inY)
            self.out = t.emitter
    def setInput(self,inputID:str,state:bool):
        inputID = str(inputID); state = bool(state)
        if inputID == 'inX': self.inX=state
        elif inputID == 'inY': self.inY=state
        self.refresh()