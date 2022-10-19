import torch
from torch import nn
import torch.nn.functional as F

class MLP(nn.Module):
    def __init__(self, num_observations, num_actions, seed=42, layers=(64, 64)):
        """
         Initialize parameters and build model.
        Params
        =======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            fc1_unit (int): Number of nodes in first hidden layer
            fc2_unit (int): Number of nodes in second hidden layer
        """
        super().__init__()
        self.seed = torch.manual_seed(seed)
        self.inputs = nn.Linear(num_observations, layers[0])
        self.layer1 = nn.Linear(layers[0], layers[1])
        self.layer2 = nn.Linear(layers[1], num_actions)

    def forward(self, x):
        """
        Build a network that maps state -> action values.
        """
        x = F.relu(self.inputs(x))
        x = F.relu(self.layer1(x))
        x = self.layer2(x)
        return x
