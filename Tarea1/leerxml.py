import xml.sax

class GraphMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def startElement(self, name, attrs):
        if name == 'node':
            node_id = attrs.get('id')
            if node_id:
                self.nodes[node_id] = {}
                print(f"Node added: {node_id}")  # Mensaje de depuración
        elif name == 'edge':
            source = attrs.get('source')
            target = attrs.get('target')
            length = attrs.get('length', 1)  # Asumiendo que la longitud es 1 si no está especificada
            if source and target:
                self.edges.append((source, target, length))
                print(f"Edge added: {source} -> {target} (length: {length})")  # Mensaje de depuración

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