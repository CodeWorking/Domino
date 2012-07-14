
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



class Jugador():
    """
    """

    def __init__(self, n,t):
        """
        Crear un Jugador
        Arguments:
        - `nombre`: El nombre del jugador
        - `fichas`: Numero de fichas
        - `tipo`  : Tipo de

        """
        self.nombre = n
        self.fichas = []
        self.tipo = t

    def __unicode__(self):
        return "(%s, %s, %s)" % (self.nombre, self.fichas, self.tipo)

class Domino():
    def __init__(self, nummayor, numjugadores):
        """
        nummayor: el numero mayor de las fichas
        numjugadores: numero de participantes del juego
        fichasrobar: numero de fichas que sobran
        """
        self.nummayor = 0
        self.jugadores = [Jugador()]
        self.fichasrobar = []
        self.turno = 0
        self.tablero = Tablero()
        self.crearFichas()
        self.crearJugadores()
        self.repartirFichas()

    def crearFichas():
        for x in range(self.nummayor):
            for j in range(x, self.nummayor):
                self.fichasrobar.append(Ficha(x,j))         
        
    
    def __unicode__(self):
        return "(%s, %s)" & (self.nummayor, self.numjugadores)