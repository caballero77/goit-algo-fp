import random
import matplotlib.pyplot as plt


def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)


def monte_carlo_simulation(num_rolls):
    sums = {i: 0 for i in range(2, 13)}
    for _ in range(num_rolls):
        roll_sum = roll_dice()
        sums[roll_sum] += 1

    probabilities = {k: (v / num_rolls) * 100 for k, v in sums.items()}
    return probabilities


def analytical_probabilities():
    return {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67,
        8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }


def plot_results(monte_carlo_probs, analytical_probs):
    sums = list(range(2, 13))

    plt.figure(figsize=(12, 6))
    plt.bar([x - 0.2 for x in sums], monte_carlo_probs.values(), width=0.4, label='Monte Carlo', align='center')
    plt.bar([x + 0.2 for x in sums], analytical_probs.values(), width=0.4, label='Analytic', align='center')

    plt.xlabel('Sum')
    plt.ylabel('Probability (%)')
    plt.title('Difference between Monte Carlo and Analytical probabilities for rolling two dice')
    plt.legend()
    plt.xticks(sums)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


def print_table(monte_carlo_probs, analytical_probs):
    print("Sum | Monte Carlo (%) | Analytic (%) | Diff (%)")
    print("----|-----------------|--------------|---------")
    for i in range(2, 13):
        mc = monte_carlo_probs[i]
        an = analytical_probs[i]
        diff = abs(mc - an)
        print(f"{i:3d} | {mc:15.2f} | {an:12.2f} | {diff:8.2f}")


num_rolls = 1000000
monte_carlo_probs = monte_carlo_simulation(num_rolls)
analytical_probs = analytical_probabilities()

print(f"Iterations: {num_rolls}")
print_table(monte_carlo_probs, analytical_probs)
plot_results(monte_carlo_probs, analytical_probs)