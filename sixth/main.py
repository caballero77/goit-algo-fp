def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']

    return selected_items, total_calories


def dynamic_programming(items, budget):
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]

    item_list = list(items.items())

    for i in range(1, len(items) + 1):
        for w in range(1, budget + 1):
            item_name, item_details = item_list[i - 1]
            if item_details['cost'] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - item_details['cost']] + item_details['calories'])
            else:
                dp[i][w] = dp[i - 1][w]

    w = budget
    n = len(items)
    selected_items = []

    while n > 0 and w > 0:
        if dp[n][w] != dp[n - 1][w]:
            item_name, item_details = item_list[n - 1]
            selected_items.append(item_name)
            w -= item_details['cost']
        n -= 1

    return selected_items, dp[len(items)][budget]


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 160

print("Greedy:")
greedy_result = greedy_algorithm(items, budget)
print(f"Selected meals: {greedy_result[0]}")
print(f"Total caloric content: {greedy_result[1]}")

print()
print("Dynamic:")
dp_result = dynamic_programming(items, budget)
print(f"Selected meals: {dp_result[0]}")
print(f"Total caloric content: {dp_result[1]}")

