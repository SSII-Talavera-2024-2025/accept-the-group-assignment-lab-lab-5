# Problema.py
import heapq
from Estado import Estado  # Importamos la clase Estado
from leerxml import cargar_adyacencias  # Importamos la función cargar_adyacencias

class ProblemaBusqueda:
    def __init__(self, archivo_grafo):
        self.adyacencias, self.costo_arista = self.cargar_grafo(archivo_grafo)

        # Verificación de los datos cargados
        print("Lista de adyacencias:", dict(list(self.adyacencias.items())[:5]))  # Muestra los primeros 5 nodos
        print("Costos de aristas:", dict(list(self.costo_arista.items())[:5]))    # Muestra los primeros 5 costos

    def cargar_grafo(self, archivo_grafo):
        return cargar_adyacencias(archivo_grafo)

    def heuristica(self, estado):
        # La heurística puede ser el número de nodos pendientes por visitar
        return len(estado.pendientes)
    

    def buscar_ruta(self, nodo_inicial, nodos_objetivo):
        estado_inicial = Estado(nodo_actual=nodo_inicial, pendientes=nodos_objetivo)
        frontera = []
        visitados = set()
        heapq.heappush(frontera, (0, estado_inicial, []))  # (costo_estimado, estado, camino)

        while frontera:
            costo_actual, estado, camino = heapq.heappop(frontera)

            if estado.id_estado() in visitados:
                continue
            
            visitados.add(estado.id_estado())
            camino_actualizado = camino + [estado.nodo_actual]
            
            if estado.es_objetivo():
                return camino_actualizado  # Ruta completa al alcanzar el objetivo

            for accion, nuevo_estado, costo in estado.generar_sucesores(self.adyacencias, self.costo_arista):
                if nuevo_estado.id_estado() not in visitados:
                    costo_nuevo = costo_actual + costo + self.heuristica(nuevo_estado)
                    heapq.heappush(frontera, (costo_nuevo, nuevo_estado, camino_actualizado))

        return None  # Ruta no encontrada

# Ejecución de ejemplo
if __name__ == "__main__":
    archivo_grafo = 'CR_Capital.xml'
    problema = ProblemaBusqueda(archivo_grafo)
    nodo_inicial = '1'
    nodos_objetivo = ['11', '40', '50', '300']  # Nodos a visitar    
    print("Nodo inicial:", nodo_inicial)
    print("Nodos objetivo:", nodos_objetivo)

    # Verificar que el nodo inicial y los objetivos están en el grafo
    if nodo_inicial not in problema.adyacencias:
        print(f"El nodo inicial {nodo_inicial} no está en el grafo.")
    if any(objetivo not in problema.adyacencias for objetivo in nodos_objetivo):
        print("Algunos nodos objetivo no están en el grafo.")

    ruta = problema.buscar_ruta(nodo_inicial, nodos_objetivo)
    print("Ruta óptima encontrada:", ruta)