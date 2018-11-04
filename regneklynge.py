from rack import Rack
from node import Node


class Regneklynge:

    def __init__(self, noderPerRack):
        self._noderPerRack = noderPerRack
        self._regneklynge = []

    def settInnNode(self, node):
        if len(self._rack) < 16:
            self._rack.append(node)
        elif len(self._rack) >= 16:
            

    def antProsessorer(self):
        pass


    def noderMedNokMinne(self, paakrevdMinne):
        pass


    def antRacks(self):
        pass
