__author__ = "Gabriela Benitez"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "gabrielabenitez658@gmail.com"

#----------------------------------------------------------------
# Importaciones
#----------------------------------------------------------------

from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:
    
    #----------------------------------------------------------------
    # Atributos
    #----------------------------------------------------------------
    __cedula = ''
    __nombre = ''
    __mesActual = 0
    
    #----------------------------------------------------------------
    # Asociaciones
    #----------------------------------------------------------------
    
from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT
class simuladorbancario:
    #----------------------------------------------------------------
    # Atributos
    #----------------------------------------------------------------
    __cedula = ''
    __nombre = ''
    
    __cuentacorriente = CuentaCorriente()
    __cuentaahorros = CuentaAhorros ()
    __cdt = CDT()
    
    __mesActual = 0
    
    #----------------------------------------------------------------
    # Metodos
    #----------------------------------------------------------------
    
    method = 'ConsignaCuentaCorriente'
    params = 'monto'
    returns = 'nada'
    Description ='Este metodo consigna un monto a la cuenta corriente'
    def ConsignarCuentaCorriente (self, monto):
    #aqui inicia el monto
    #self.__cuentacorriente.saldo = self._cuentacorriente.saldo + monto 
    #modo no recomendado
        self.__cuentacorriente.ConsignarValor(monto)
    

    
    method = 'DarSaldo'
    params = 'ninguno'
    returns = 'Saldo'
    Description ='Este metodo retorna el saldo'
    def DarSaldo (self):
        return self.__saldo