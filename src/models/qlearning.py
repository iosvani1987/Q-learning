import numpy as np
import random
from domain.grid import Grid

class QLearningAgent:
    def __init__(self, grid, alpha=0.1, gamma=0.9, epsilon=1.0, epsilon_decay=0.995, epsilon_min=0.01, episodes=1000):
        self.grid = grid
        self.actions = [(-1, -1), (-1, 0), (-1, 1),  # King's moves
                        (0, -1),          (0, 1),
                        (1, -1),  (1, 0), (1, 1),
                        (0, 0)]  # NOP (No Operation)
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.episodes = episodes
        self.Q = np.zeros((grid.size, grid.size, len(self.actions)))

    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.randint(0, len(self.actions) - 1)  # Exploration
        else:
            return np.argmax(self.Q[state])  # Exploitation

    def move(self, state, action):
        row, col = state
        dr, dc = self.actions[action]
        new_row, new_col = row + dr, col + dc
        # Check grid boundaries using the Grid class
        if self.grid.is_within_bounds((new_row, new_col)):
            return (new_row, new_col)
        else:
            return state  # Do not move if out of grid

    def train(self):
        for episode in range(self.episodes):
            state = (random.randint(0, self.grid.size - 1), random.randint(0, self.grid.size - 1))  # Random initial state
            done = False

            while not done:
                action = self.choose_action(state)
                next_state = self.move(state, action)
                reward = self.grid.rewards[next_state]

                # Update Q-table
                self.Q[state][action] += self.alpha * (reward + self.gamma * np.max(self.Q[next_state]) - self.Q[state][action])

                # Check if goal is reached
                if next_state == self.grid.goal:
                    done = True

                state = next_state

            # Epsilon decay
            self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)

    def test_agent(self, start_state):
        state = start_state
        path = [state]
        while state != self.grid.goal:
            action = np.argmax(self.Q[state])
            state = self.move(state, action)
            path.append(state)
        return path
