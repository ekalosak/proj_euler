class tree:

    def __init__(self, par, val = None):
        self.par = par
        if par: par.addChild(self)
        self.childs = []
        self.val = val

    def addChild(x):
        self.childs.append(x)

    def getChilds():
        return self.childs

    def removeChild(x):
        try:
            self.childs.remove(x)
            return True
        except ValueError as e:
            return False
