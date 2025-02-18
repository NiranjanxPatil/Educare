import torch
import torch.nn as nn
import torch.optim as optim
import random
import numpy as np
import pygame
from collections import deque

# Simple DQN model
class DQN(nn.Module):
    def __init__(self):
        super(DQN, self).__init__()
        # Updated input size to match the new screen resolution (800x800)
        self.fc1 = nn.Linear(800 * 800 * 3, 128)
        self.fc2 = nn.Linear(128, 3)

    def forward(self, x):
        x = x.view(x.size(0), -1)  # Flatten input
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Pong environment (simplified)
class PongGame:
    def __init__(self):
        self.width = 800  # Updated size
        self.height = 800  # Updated size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.reset()

    def reset(self):
        self.score = 0
        self.done = False
        return np.random.randn(self.height, self.width, 3)

    def step(self, action):
        next_state = np.random.randn(self.height, self.width, 3)
        reward = random.random()
        self.done = random.random() > 0.95
        return next_state, reward, self.done

    def render(self):
        pygame.display.update()

# DQN Training function
def train_dqn():
    env = PongGame()
    model = DQN()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.MSELoss()

    memory = deque(maxlen=10000)
    epsilon = 0.1
    gamma = 0.99
    batch_size = 32
    target_update = 10
    num_episodes = 2000

    for episode in range(num_episodes):
        state = np.array(env.reset())
        state = torch.FloatTensor(state).unsqueeze(0)  # Add batch dimension
        done = False
        total_reward = 0

        while not done:
            if random.random() < epsilon:
                action = random.choice([0, 1, 2])
            else:
                with torch.no_grad():
                    q_values = model(state)
                action = torch.argmax(q_values).item()

            next_state, reward, done = env.step(action)
            next_state_tensor = torch.FloatTensor(next_state).unsqueeze(0)

            memory.append((state, action, reward, next_state_tensor, done))
            state = next_state_tensor
            total_reward += reward

            if len(memory) > batch_size:
                batch = random.sample(memory, batch_size)
                states, actions, rewards, next_states, dones = zip(*batch)

                states = torch.stack(states)
                actions = torch.tensor(actions).unsqueeze(1)
                rewards = torch.tensor(rewards).unsqueeze(1)
                next_states = torch.stack(next_states)
                dones = torch.tensor(dones).unsqueeze(1)

                current_q_values = model(states).gather(1, actions)
                next_q_values = model(next_states).max(1)[0].unsqueeze(1)

                target_q_values = rewards + gamma * next_q_values * (1 - dones.float())

                loss = criterion(current_q_values, target_q_values)

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

        if episode % target_update == 0:
            print(f'Episode {episode}, Total Reward: {total_reward}')
            env.render()

        if episode % 500 == 0:
            torch.save(model.state_dict(), f"dqn_pong_{episode}.pth")

if __name__ == "__main__":
    pygame.init()
    train_dqn()
