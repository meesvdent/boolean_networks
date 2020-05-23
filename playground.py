import numpy as np
from models import Network

n = Network(
    nodes=['a', 'b', 'c'],
    connections=[['a', 'b', 'act'], ['b', 'c', 'act'], ['c', 'a', 'act']],
    init_state=[1, 0, 0]
)

print(n.run_steps())


n.add_node('d')
n.add_node('e')

n.add_connections([['c', 'd', 'act'], ['d', 'e', 'act'], ['e', 'a', 'inh']])

print(n.run_steps())


print(n)