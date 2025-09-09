# Forward Chaining Example: Healthcare Diagnosis

# Known facts (symptoms)
facts = {
    "cough": True,
    "fatigue": True,
    "temperature": 101.2  # Fahrenheit
}

# Rules with condition as part of facts
rules = [
    {"if": {"temperature": lambda t: t > 100.4, "cough": True}, "then": "flu"},
    {"if": {"temperature": lambda t: t > 102, "fatigue": True, "body_pain": True}, "then": "dengue"},
    {"if": {"cough": True, "sore_throat": True}, "then": "cold"},
    {"if": {"headache": True, "nausea": True}, "then": "migraine"}
]

inferred = set()

def forward_chaining(facts, rules):
    new_inferred = True
    while new_inferred:
        new_inferred = False
        for rule in rules:
            match = True
            for cond, value in rule["if"].items():
                if cond == "temperature":
                    if not value(facts["temperature"]):
                        match = False
                        break
                else:
                    if value and not facts.get(cond, False):
                        match = False
                        break
            if match and rule["then"] not in facts:
                facts[rule["then"]] = True
                inferred.add(rule["then"])
                print(f"Inferred: {rule['then']}")
                new_inferred = True
    return inferred

diagnosis = forward_chaining(facts, rules)
print("\nPossible diagnoses:", diagnosis)
