class Gate:
    def printInfo(self):
        self.refresh()
        if self.inY != None:
            print(f'Type: {self.typeString}\nID: {self.id}\ninX: {self.inX}\ninY: {self.inY}\nout: {self.out}\n')
        else:
            print(f'Type: {self.typeString}\nID: {self.id}\ninX: {self.inX}\nout: {self.out}\n')
    def printInfoColored(self):
        from colorama import Fore; import colorama; colorama.init()
        self.refresh()
        if self.inY != None:
            print(f'{Fore.YELLOW}Type: {self.typeString}\nID: {self.id}{Fore.GREEN if self.inX else Fore.RED}\ninX: {self.inX}\n{Fore.GREEN if self.inY else Fore.RED}inY: {self.inY}{Fore.GREEN if self.out else Fore.RED}\nout: {self.out}{Fore.RESET}\n')
        else:
            print(f'{Fore.YELLOW}Type: {self.typeString}\nID: {self.id}{Fore.GREEN if self.inX else Fore.RED}\ninX: {self.inX}\n{Fore.GREEN if self.out else Fore.RED}out: {self.out}{Fore.RESET}\n')
    def returnInfo(self):
        self.refresh()
        return (self.type,self.mode,self.id,self.inX,self.inY,self.out)
    def setMode(self,mode:str):
        mode = str(mode).lower()
        if mode == 'native': self.mode = mode
        elif mode == 'transistor': self.mode = mode
    def get(self,pin:str):
        pin = str(pin)
        self.refresh()
        if pin == 'inX': return self.inX
        elif pin == 'inY': return self.inY
        elif pin == 'out': return self.out
        else: return -1