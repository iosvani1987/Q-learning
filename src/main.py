from domain.grid import Grid
from models.qlearning import QLearningAgent

def main():
    grid = Grid(size=4, goal=(3, 2))
    agent = QLearningAgent(grid)
    agent.train()
    # Generate a random tuple with maximum values of 3, 3
    start_state = (random.randint(0, 3), random.randint(0, 3))

    path = agent.test_agent(start_state)
    print("Start state:", start_state)
    print("Path followed by the agent:", path)

if __name__ == "__main__":
    main()