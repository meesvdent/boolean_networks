import numpy as np


class BoolNet:

    def __init__(self, nodes=list(), connections=list(), init_state=np.array([])):
        self.nodes = self.create_node_dict(nodes)
        self.connections = self.create_connection_matrix(nodes)
        self.add_connections(connections)
        self.init_state = init_state
        self.state = np.array(init_state, dtype=int)

    def __str__(self):
        return f'Nodes:\n ' \
               f'{self.nodes} \n' \
               f'\n' \
               f'Connections: \n' \
               f'{self.connections}'

    def create_node_dict(self, nodes):
        node_dict = {}
        i = 0
        for node in nodes:
            node_dict[node] = i
            i += 1
        return node_dict

    def create_connection_matrix(self, nodes):
        connection_matrix = np.zeros((len(nodes), len(nodes)), dtype=int)
        return(connection_matrix)

    def add_connections(self, new_connections):
        for connection in new_connections:
            from_index = self.nodes[connection[0]]
            to_index = self.nodes[connection[1]]
            if connection[2] == 'act':
                effect = 1
            elif connection[2] == 'inh':
                effect = -1

            self.connections[from_index, to_index] = effect

    def add_node(self, name):
        add_column = np.zeros((self.connections.shape[0], 1))
        self.connections = np.hstack([self.connections, add_column])
        add_row = np.zeros((1, self.connections.shape[1]))
        self.connections = np.vstack([self.connections, add_row])
        self.nodes[name] = self.connections.shape[0] - 1
        self.state = np.concatenate([self.state, [0]])

    def run_steps(self, state_array=None, n_steps=100, step=0):

        if state_array is None:
            state_array = np.array([self.state], dtype=int)

        multiplied = np.dot(self.state, self.connections)
        self.state = (multiplied > 0).astype(int)

        if step == n_steps or (state_array == self.state).all(1).any():
            return np.vstack([state_array, self.state])

        state_array = np.vstack([state_array, self.state])
        state_array = self.run_steps(state_array=state_array, n_steps=n_steps, step=step+1)
        return state_array

