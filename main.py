# for parsing XML
import xml.etree.ElementTree as ET
# importing our Graph class
from way import Way
from node import Node
from graph import Graph
from random import randint

def create_graph(filename, g):
    tree = ET.parse(filename)
    root = tree.getroot()
    for item in root:
        if item.tag == 'node':
            node = Node(item.get('id'), float(item.get("lat")), float(item.get("lon")), randint(5000, 10000))
            g.add_node(node)
        if item.tag == 'way':
            id = item.get("id")
            nodes = []
            name = ""
            for subitem in item:
                if subitem.tag == "nd":
                    nodes.append(g.get_node(subitem.get("ref")))
                if subitem.tag == 'tag' and subitem.get('k') == 'name':
                    name = subitem.get('v')
                    break
            way = Way(id, name, nodes)
            g.add_way(way)

def aStarSearch(start_node, end_node):
    pass
            
def main():
    g = Graph()
    create_graph("map.osm", g)
    print(g)

if __name__ == '__main__':
    main()
