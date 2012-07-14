

class Ficha():
    """
    """

    def __init__(self, a, b):
        """
        Crear una Ficha
        Arguments:
        - `a`: El primer lado de la ficha
        - `b`: El segundo lado de la ficha
        """
        self.lado1 = a
        self.lado2 = b

    def __unicode__(self):
        return "(%s, %s)" % (self.lado1, self.lado2)




class Tablero():
    def __unicode__(self):
        return "Tablero"
