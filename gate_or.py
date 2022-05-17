from logic_transistor import Transistor
from gate import Gate
class OrGate(Gate):
    def __init__(self,id:str):
        self.type = "OrGate"
        self.id = str(id)
        self.inX = False
        self.inY = False
        self.out = False
        self.mode = 'native'
        self.refresh()
    def refresh(self):
        self.typeString = f'{self.type}@{self.mode}'
        if self.mode == 'native':
            if self.inX or self.inY: self.out = True
            else: self.out = False
        elif self.mode == 'transistor':
            t1 = Transistor('t1')
            t2 = Transistor('t2')
            t1.setInput('base', self.inX)
            t1.setInput('collector',True)
            t2.setInput('base', self.inY)
            t2.setInput('collector', True)
            self.out = t1.emitter or t2.emitter
    def setInput(self,inputID:str,state:bool):
        inputID = str(inputID); state = bool(state)
        if inputID == 'inX': self.inX=state
        elif inputID == 'inY': self.inY=state
        self.refresh()