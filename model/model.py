import copy

import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self.countryList = DAO.getAllCountries()
        self.countryMap = {}
        for c in self.countryList:
            self.countryMap[c.CCode] = c
        self.grafo = nx.Graph()


    def creaGrafo(self, anno):
        self.grafo.clear()
        listNodi = DAO.getCountryConf(anno)
        #self.grafo.add_nodes_from(listNodi)
        self.grafo.add_nodes_from(self.countryList)
        confini = DAO.getConfini(anno)
        for conf in confini:
            country1 = self.countryMap[conf.cnt1]
            country2 = self.countryMap[conf.cnt2]
            self.grafo.add_edge(country1, country2)

    def trovaNodi(self):
        listaNodi = []
        for n in self.grafo.nodes():
            listaNodi.append(n)
        return listaNodi

    def trovaNumArchiVicini(self, nodo):
        return len(list(self.grafo.neighbors(nodo)))

    def getNumCompConnesse(self):
        return nx.number_connected_components(self.grafo)



    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def getRaggiungibiliTree(self, stato):
        tree = nx.bfs_tree(self.grafo, stato)
        listaNodi = list(tree.nodes)
        listaNodi.remove(stato)
        return listaNodi

    def getRaggiungibiliRecorsive(self, stato):
        visited = []
        self.ricorsione(stato, visited)
        visited.remove(stato)
        return copy.deepcopy(visited)

    def ricorsione(self, stato, visited):
        visited.append(stato)
        for n in self.grafo.neighbors(stato):
            if n not in visited:
                self.ricorsione(n, visited)



