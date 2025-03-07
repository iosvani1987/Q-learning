class Grid:
    def __init__(self, size, goal):
        self.size = size
        self.goal = goal
        self.rewards = np.zeros((size, size))
        self.rewards[goal] = 100  # High reward at the goal cell

    def is_within_bounds(self, position):
        row, col = position
        return 0 <= row < self.size and 0 <= col < self.size