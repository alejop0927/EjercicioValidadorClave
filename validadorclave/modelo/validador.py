# TODO: Implementa el código del ejercicio aquí

# validador.py
from abc import ABC, abstractmethod

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        if len(clave) <= self._longitud_esperada:
            raise ValueError(f"La clave debe tener más de {self._longitud_esperada} caracteres.")

    @abstractmethod
    def es_valida(self, clave):
        pass