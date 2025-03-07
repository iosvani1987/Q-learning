# Q-Learning Grid Navigation

This project implements a Q-Learning agent that navigates a grid to reach a goal position. The agent learns optimal paths through reinforcement learning, using a reward system defined within the grid.

## Project Structure

- **src/notebooks/00-support.ipynb**: Contains the implementation of the `Grid` and `QLearningAgent` classes.
- **src/main.py**: The main script to run the Q-Learning agent.
- **models/**: Directory where the Q-Learning model is defined.
- **domain/**: Directory containing the grid environment.

## Requirements

- Python 3.x
- NumPy

## Setup

1. **Clone the repository**:
   ```bash
   git clone git@github.com:iosvani1987/Q-learning.git
   cd Q-learning
   ```

2. **Install dependencies**:
   Make sure you have Python and NumPy installed. You can install NumPy using pip:
   ```bash
   pip install -r requirements.txt
   ```

   3. **Directory Structure**:
      Ensure your directory structure looks like this:
      ```
      project-root/
      ├── src/
          ├── notebooks/
          │   └── 00-support.ipynb
          └── main.py
          │
          ├── models/
          │   └── q_learning.py
          └── domain/
              └── grid.py
      ```

## Usage

1. **Run the Q-Learning Agent**:
   Execute the main script to train the agent and test its pathfinding capabilities:
   ```bash
   python src/main.py
   ```

2. **Test the Agent**:
   The agent will start from a random position and attempt to reach the goal. The path taken by the agent will be printed to the console.

## Customization

- **Grid Size and Goal**: You can modify the grid size and goal position in the `Grid` class instantiation within the notebook or main script.
- **Agent Parameters**: Adjust learning rate (`alpha`), discount factor (`gamma`), and exploration parameters (`epsilon`, `epsilon_decay`, `epsilon_min`) in the `QLearningAgent` class to experiment with different learning behaviors.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## Contact

For questions or feedback, please contact `Iosvani More` at `iosvani1987@gmail.com`.
