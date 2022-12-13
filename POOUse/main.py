from Classes import Escritor
from Classes import Caneta

c = Caneta('bick')
e = Escritor('João')
e.ferramenta = c
c.escrever()