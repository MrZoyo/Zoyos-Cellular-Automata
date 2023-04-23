import numpy as np
import matplotlib.pyplot as plt


def rule_generator(rule_number, k):
    rule_binary = np.array([int(x) for x in format(rule_number, f"0{int(np.log2(k ** 3))}b")])
    rule = np.zeros((k, k), dtype=int)
    for i in range(k):
        for j in range(k):
            rule[i, j] = rule_binary[i * k + j]
    return rule


def cellular_automaton(steps, width, rule_number, k, initial_state=None):
    if initial_state is None:
        initial_state = np.zeros(width, dtype=int)
        initial_state[width // 2] = 1

    rule = rule_generator(rule_number, k)
    grid = np.zeros((steps, width), dtype=int)
    grid[0, :] = initial_state

    for i in range(1, steps):
        for j in range(1, width - 1):
            grid[i, j] = rule[grid[i - 1, j - 1], grid[i - 1, j]]

    return grid


def main():
    steps = int(input("Enter the number of steps: "))
    width = int(input("Enter the width: "))
    rule_number = int(input("Enter the rule number (Wolfram notation): "))
    k = int(input("Enter the number of states (k): "))

    grid = cellular_automaton(steps, width, rule_number, k)

    fig, ax = plt.subplots()
    ax.imshow(grid, cmap="gray_r", aspect="auto")
    ax.set_title(f"1D Cellular Automaton\nRule {rule_number}, k={k}, Steps={steps}, Width={width}")
    ax.set_xlabel("Cell Index")
    ax.set_ylabel("Timestep")

    ax.set_xticks(np.arange(-0.5, width - 1, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, steps - 1, 1), minor=True)

    ax.set_xticks(np.arange(0, width, 1))
    ax.set_yticks(np.arange(0, steps, 1))

    ax.set_xticklabels(np.arange(1, width + 1, 1))
    ax.set_yticklabels(np.arange(1, steps + 1, 1))

    ax.grid(True, which='minor', color='lightgrey', linewidth=0.5)
    ax.set_axisbelow(True)

    plt.show()


if __name__ == "__main__":
    main()
