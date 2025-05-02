# Evaluation script for MAP@3 and Recall@3 using provided test set
def map_at_k(recommended, relevant, k=3):
    hits = 0
    sum_precisions = 0.0
    for i, item in enumerate(recommended[:k]):
        if item in relevant:
            hits += 1
            sum_precisions += hits / (i + 1)
    return sum_precisions / min(len(relevant), k)

def recall_at_k(recommended, relevant, k=3):
    hits = sum(1 for item in recommended[:k] if item in relevant)
    return hits / len(relevant)

# Example test set and usage
test_queries = [
    {
        "query": "Looking for Java developer assessment",
        "relevant": ["Core Java (Entry Level)"]
    }
]

# Assuming dummy recommendations
recommended = ["Core Java (Entry Level)", "Agile Software Development"]
for test in test_queries:
    print("MAP@3:", map_at_k(recommended, test["relevant"]))
    print("Recall@3:", recall_at_k(recommended, test["relevant"]))