import xml.sax

class GraphMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_element = ""
        self.nodes = {}  # Diccionario para almacenar los nodos: {id: (lat, lon)}
        self.edges = []  # Lista para almacenar las aristas
        self.current_edge = None
        self.lat = None
        self.lon = None
        self.node_id = None
        self.content = ""  # Almacenar contenido temporal de etiquetas
        self.current_key = None  # Almacenar la clave actual del <data>

    def startElement(self, name, attrs):
        self.current_element = name
        self.content = ""  # Limpiar contenido al iniciar un nuevo elemento
        if name == "node":
            # Extraer el ID del nodo
            self.node_id = attrs["id"]
            self.lat = None
            self.lon = None
        elif name == "edge":
            # Iniciar la creación de una arista
            source = attrs["source"]
            target = attrs["target"]
            self.current_edge = (source, target, None)
        elif name == "data" and "key" in attrs:
            # Guardar la clave de data actual para procesar lat y lon
            self.current_key = attrs["key"]

    def endElement(self, name):
        if name == "data" and self.node_id:
            # Almacenar latitud y longitud si los encontramos en el contenido de <data>
            if self.current_key == "d8" and self.content:
                # Clave para la longitud
                try:
                    self.lon = float(self.content)
                except ValueError:
                    pass
            elif self.current_key == "d9" and self.content:
                # Clave para la latitud
                try:
                    self.lat = float(self.content)
                except ValueError:
                    pass

            # Agregar el nodo al diccionario si tenemos lat y lon
            if self.lat is not None and self.lon is not None:
                self.nodes[self.node_id] = (self.lat, self.lon)
                self.lat = None
                self.lon = None
                self.node_id = None

        # Al finalizar de leer una arista, la almacenamos en la lista de aristas
        if name == "edge" and self.current_edge:
            self.edges.append(self.current_edge)
            self.current_edge = None

        self.content = ""  # Limpiar el contenido después de procesarlo

    def characters(self, content):
        # Capturar el contenido de las etiquetas data
        self.content += content.strip()

# Parsear el archivo GraphML
if __name__ == "__main__":
    parser = xml.sax.make_parser()
    handler = GraphMLHandler()
    parser.setContentHandler(handler)
    parser.parse("CR_Capital.xml")

    # Mostrar los nodos y aristas
    print("Nodos:", len(handler.nodes))
    print("Primeros 5 nodos:", list(handler.nodes.items())[:5])
    print("Número de aristas:", len(handler.edges))
    print("Primeras 5 aristas:", handler.edges[:5])

    # Construcción de la lista de adyacencias
    adj_list = {node_id: [] for node_id in handler.nodes}

    for source, target, length in handler.edges:
        if source in adj_list and target in adj_list:
            adj_list[source].append((target, length))
            adj_list[target].append((source, length))  # Si el grafo es bidireccional

    # Mostrar la lista de adyacencias
    print("Lista de adyacencias (primeros 5 nodos):", dict(list(adj_list.items())[:5]))
