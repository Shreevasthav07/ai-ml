import pandas as pd
import math


data = pd.read_csv("buy_computer.csv")


def entropy(df, target_attr):
    values = df[target_attr].unique()
    entropy_val = 0
    total = len(df)
    for val in values:
        p = len(df[df[target_attr]==val]) / total
        entropy_val -= p * math.log2(p) if p > 0 else 0
    return entropy_val


def info_gain(df, attr, target_attr):
    total_entropy = entropy(df, target_attr)
    values = df[attr].unique()
    subset_entropy = 0
    total = len(df)
    for val in values:
        subset = df[df[attr]==val]
        weight = len(subset)/total
        subset_entropy += weight * entropy(subset, target_attr)
    gain = total_entropy - subset_entropy
    return gain

def id3(df, target_attr, attributes):
    
    if len(df[target_attr].unique()) == 1:
        return df[target_attr].iloc[0]
    
    
    if len(attributes) == 0:
        return df[target_attr].mode()[0]  
    
    gains = {attr: info_gain(df, attr, target_attr) for attr in attributes}
    best_attr = max(gains, key=gains.get)
    
    tree = {best_attr: {}}
    
    for val in df[best_attr].unique():
        subset = df[df[best_attr]==val]
        new_attrs = [a for a in attributes if a != best_attr]
        tree[best_attr][val] = id3(subset, target_attr, new_attrs)
    
    return tree

def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree
    attribute = list(tree.keys())[0]
    subtree = tree[attribute]
    value = sample.get(attribute)
    if value in subtree:
        return predict(subtree[value], sample)
    else:
        return None


attributes = list(data.columns)
attributes.remove('buys_computer')
tree = id3(data, 'buys_computer', attributes)

print("Generated Decision Tree:")
print(tree)

new_sample = {
    'age': 'youth',
    'income': 'medium',
    'student': 'yes',
    'credit_rating': 'fair'
}

predicted_class = predict(tree, new_sample)
print("\nNew Sample:", new_sample)
print("Predicted Class:", predicted_class)



