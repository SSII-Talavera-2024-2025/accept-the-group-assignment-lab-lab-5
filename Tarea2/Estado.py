# Estado.py
import hashlib

class Estado:
    def __init__(self, nodo_actual, pendientes):
        self.nodo_actual = nodo_actual
        self.pendientes = sorted(pendientes)  # Ordenar para mantener consistencia

    def __str__(self):
        return f"({self.nodo_actual},{self.pendientes})"

    def id_estado(self):
        # Genera un hash MD5 único para cada estado
        estado_str = str(self)
        return hashlib.md5(estado_str.encode()).hexdigest()

    def es_objetivo(self):
        # Verifica si es el estado objetivo (sin pendientes)
        return len(self.pendientes) == 0

    def generar_sucesores(self, adyacencias, costo_arista):
        sucesores = []
        for destino in sorted(adyacencias.get(self.nodo_actual, [])):
            # Actualiza los nodos pendientes si el destino es uno de ellos
            if destino in self.pendientes:
                nuevos_pendientes = [nodo for nodo in self.pendientes if nodo != destino]
            else:
                nuevos_pendientes = self.pendientes[:]
        
            nuevo_estado = Estado(destino, nuevos_pendientes)
            accion = f"{self.nodo_actual}->{destino}"  # Definir la acción aquí para evitar el error
            costo = costo_arista.get((self.nodo_actual, destino), 1)  # Coste por defecto 1
        
            sucesores.append((accion, nuevo_estado, costo))
        
        return sucesores

    def __lt__(self, other):
        # Comparar estados basándose en el nodo actual y los pendientes
        return (self.nodo_actual, self.pendientes) < (other.nodo_actual, other.pendientes)