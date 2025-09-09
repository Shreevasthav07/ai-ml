class BackwardChaining:
    def __init__(self, knowledge_base):
        # Store rules and facts
        self.knowledge_base = knowledge_base

    def infer(self, goal):
        # If the goal is already a known fact, return True
        if goal in self.knowledge_base.get("facts", []):
            return True

        # Check rules to see if goal can be derived
        for rule in self.knowledge_base.get("rules", []):
            if rule["then"] == goal:
                # Recursively infer conditions
                if all(self.infer(condition) for condition in rule["if"]):
                    return True
        return False


# Define knowledge base (facts and rules)
knowledge_base = {
    "facts": ["Crimea Annexation", "NATO Expansion"],  # Known facts
    "rules": [
        {"if": ["Crimea Annexation", "NATO Expansion"], "then": "Russia's Invasion"},
        {"if": ["Russia's Invasion"], "then": "Ukraine-Russia War"},
    ]
}

# Initialize backward chaining system
bc = BackwardChaining(knowledge_base)

# Test backward chaining with a goal
goal = "Ukraine-Russia War"
if bc.infer(goal):
    print(f"The cause of {goal} is inferred from known facts.")
else:
    print(f"The cause of {goal} cannot be inferred.")
