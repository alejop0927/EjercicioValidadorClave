# validador.py
from abc import ABC, abstractmethod

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        if len(clave) <= self._longitud_esperada:
            raise ValueError(f"La clave debe tener más de {self._longitud_esperada} caracteres.")

    def _contiene_mayuscula(self, clave):
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave):
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave):
        return any(c.isdigit() for c in clave)

    @abstractmethod
    def es_valida(self, clave):
        pass

class ReglaValidacionGanimedes(Regla, Validacion):
    def __init__(self):
        super().__init__(8)  # Longitud esperada de más de 8 caracteres

    def contiene_caracter_especial(self, clave):
        caracteres_especiales = "@_#$%"
        return any(c in caracteres_especiales for c in clave)

    def es_valida(self, clave):
        self._validar_longitud(clave)
        if not self._contiene_mayuscula(clave):
            raise ValueError("La clave debe contener al menos una letra mayúscula.")
        if not self._contiene_minuscula(clave):
            raise ValueError("La clave debe contener al menos una letra minúscula.")
        if not self._contiene_numero(clave):
            raise ValueError("La clave debe contener al menos un número.")
        if not self.contiene_caracter_especial(clave):
            raise ValueError("La clave debe contener al menos un carácter especial (@, _, #, $, %).")
        return True

class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(6)  # Longitud esperada de más de 6 caracteres

    def contiene_calisto(self, clave):
        count = sum(1 for c in clave if c in "CALISTO")
        return 2 <= count < len("CALISTO")

    def es_valida(self, clave):
        self._validar_longitud(clave)
        if not self._contiene_numero(clave):
            raise ValueError("La clave debe contener al menos un número.")
        if not self.contiene_calisto(clave):
            raise ValueError("La clave debe contener la palabra 'calisto' con al menos dos letras mayúsculas.")
        return True

class Validador:
    def __init__(self, regla):
        self.regla = regla

    def es_valida(self, clave):
        try:
            return self.regla.es_valida(clave)
        except ValueError as e:
            print(f"Error: {e}")
            return False

# Ejemplo de uso
validador_ganimedes = Validador(ReglaValidacionGanimedes())
validador_calisto = Validador(ReglaValidacionCalisto())

clave_ganimedes = "MiClaveGanimedes123@"
clave_calisto = "MiClaveCalisto123CALISTO"

print(validador_ganimedes.es_valida(clave_ganimedes))  # Debe imprimir True
print(validador_calisto.es_valida(clave_calisto))  # Debe imprimir True