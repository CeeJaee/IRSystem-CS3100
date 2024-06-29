from collections import Counter

def generate_integer():
    return ''.join(str(random.randint(0, 9)) for _ in range(7))

def simulate_game(num_simulations):
    integers = [generate_integer() for _ in range(num_simulations * 5)]
    counts = Counter(integers)
    unique_integers = [int(i) for i in counts if counts[i] == 1]
    
    probabilities = {int_num: unique_integers.count(int_num) / num_simulations for int_num in unique_integers}
    sorted_probabilities = sorted(probabilities.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_probabilities[:5]

if __name__ == "__main__":
    import random
    
    num_simulations = 100000
    top_integers = simulate_game(num_simulations)
    print("Top 5 integers with the best odds of winning:")
    for int_num, probability in top_integers:
        print(f"{int_num}: Probability = {probability:.6f}")
