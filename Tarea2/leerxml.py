# leerxml.py
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
        elif name == 'edge':
            source = attrs.get('source')
            target = attrs.get('target')
            length = attrs.get('length', 1)  # Usa longitud 1 como valor por defecto si no está especificada
            if source and target:
                self.edges.append((source, target, float(length)))  # Convertir longitud a flotante

    def endElement(self, name):
        pass

    def characters(self, content):
        pass

def cargar_adyacencias(archivo_xml):
    handler = GraphMLHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(archivo_xml)

    adyacencias = {}
    costo_arista = {}

    for source, target, length in handler.edges:
        if source not in adyacencias:
            adyacencias[source] = []
        adyacencias[source].append(target)
        costo_arista[(source, target)] = length

    return adyacencias, costo_arista