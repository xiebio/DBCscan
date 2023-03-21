import re
class taxid:

    def __init__ (self, nodes_dmp):
        self.pare = {}
        self.node = nodes_dmp
        self.readnode()

    def readnode(self):
        with open(self.node) as fp:
            for line in fp.readlines():
                line = line.strip()
                a,b,_ = line.split('\t|\t',2)
                self.pare[a] = b

    def is_sub(self, taxid_small, taxid_big):
        taxid_small = str(taxid_small)
        taxid_big = str(taxid_big)
        if taxid_small == taxid_big: return True
        while (taxid_small != '1'):
            if taxid_small in self.pare:
                taxid_small = self.pare[taxid_small]
                if taxid_small == taxid_big: return True
            else:
                return taxid_small
        return False
