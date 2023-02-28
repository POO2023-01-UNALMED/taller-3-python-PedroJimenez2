class Marca:
    def __init__(self,nombre):
        self._nombre = nombre

    def setNombre(self,nom):
        self._nombre = nom

    def getNombre(self):
        return self._nombre
    
class TV:
    _numTV = 0
    def __init__(self,marca,estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        self._control = None
        TV._numTV += 1

    def setMarca(self,marc):
        self._marca = marc

    def setControl(self,contr):
        self._control = contr

    def setPrecio(self,prec):
        self._precio = prec

    def setVolumen(self,vol):
        self._volumen = vol

    def setCanal(self,can):
        if self._estado == True:
            if can >= 1 and can <= 120:
                self._canal = can

    def setEstado(self,estad):
        self._estado = estad

    def setNumTV(self,numt):
        self._numTV = numt

    def getMarca(self):
        return self._marca
    
    def getControl(self):
        return self._control
    
    def getPrecio(self):
        return self._precio
    
    def getVolumen(self):
        return self._volumen
    
    def getCanal(self):
        return self._canal
    
    def getNumTV(self):
        return self._numTV
    
    def getEstado(self):
        return self._estado
    
    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def canalUp(self):
        if self._canal >= 1 and self._canal < 120:
            if self._estado == True:
                self._canal += 1

    def canalDown(self):
        if self._canal > 1 and self._canal <= 120:
            if self._estado == True:
                self._canal -= 1

    def volumenUp(self):
        if self._volumen >= 0 and self._volumen < 7:
            if self._estado == True:
                self._volumen += 1

    def volumenDown(self):
        if self._volumen > 0 and self._volumen <= 7:
            if self._estado == True:
                self._volumen -= 1

class Control:
    def __init__(self):
        self._tv = None

    def turnOn(self):
        self._tv.setEstado(True)

    def turnOff(self):
        self._tv.setEstado(False)

    def canalUp(self):
        self._tv.canalUp()

    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()

    def setCanal(self,canal):
        self._tv.setCanal(canal)

    def enlazar(self,telev):
        self._tv = telev
        telev.setControl(self)

    def setTv(self,t):
        self._tv = t

    def getTv(self):
        return self._tv