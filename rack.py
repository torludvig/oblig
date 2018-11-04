from node import Node


class Rack:

    def __init__(self):
        self._rack = []

    def settInn(self, node):
        self._rack.append(node)


    def getAntNoder(self):
        return len(self._rack)


    def antProsessorer(self):
        antallPros = 0
        for node in self._rack:
            antallPros += node.antProsessorer
        return antallPros


    def noderMedNokMinne(self, paakrevdMinne):
        antallNoderMedNokMinne = 0
        for node in self._rack:
            antallNoderMedNokMinne += node.nokMinne(paakrevdMinne)
