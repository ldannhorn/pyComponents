from gate import Gate
class XorGate(Gate):
    def __init__(self,id:str):
        self.type = 'XorGate'
        self.id = str(id)
        self.inX = False
        self.inY = False
        self.out = False
        self.mode = 'native'
        self.refresh()
    def refresh(self):
        self.typeString = f'{self.type}@{self.mode}'
        if self.mode == 'native' or 'transistor':               ### transistor not possible at the moment
            self.mode = 'transistor'
            if self.inX and self.inY: self.out=False
            elif self.inX and not self.inY: self.out=True
            elif self.inY and not self.inX: self.out=True
            elif not self.inX and not self.inY: self.out=False
            else: self.out=None
        elif self.mode == 'transistor':
            pass
    def setInput(self,inputID:str,state:bool):
        inputID = str(inputID); state = bool(state)
        if inputID == 'inX': self.inX=state
        elif inputID == 'inY': self.inY=state
        self.refresh()