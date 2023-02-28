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