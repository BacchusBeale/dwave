import settings
from dimod.reference.samplers import ExactSolver

import dwave_networkx as dnx
from dwave.system import DWaveSampler, EmbeddingComposite

mytoken = settings.apitoken

import networkx as nx
s5 = nx.star_graph(4)
print(s5)

# on local CPU
print("run on local CPU")
x_sampler = ExactSolver()
print(dnx.min_vertex_cover(s5, x_sampler))

# run on DWave QPU
print("run on DWave QPU")
d_sampler = EmbeddingComposite(DWaveSampler(token=mytoken))
print(dnx.min_vertex_cover(s5, d_sampler))
