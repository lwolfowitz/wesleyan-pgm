import json
import sys

sys.path.append("../")
from libpgm.nodedata import NodeData
from libpgm.graphskeleton import GraphSkeleton
from libpgm.discretebayesiannetwork import DiscreteBayesianNetwork

nd = NodeData()
skel = GraphSkeleton()
nd.load("../tests/unittestdict.txt")
skel.load("../tests/unittestdict.txt")

# topologically order graphskeleton
skel.toporder()

# load bayesian network
bn = DiscreteBayesianNetwork(skel, nd)

# sample 
result = bn.randomsample(10)

# output - toggle comment to see
#print json.dumps(result, indent=2)

skel.load("../mywork/leetestlib.txt")
response = raw_input("Choose v: ")
print skel.getparents(response)