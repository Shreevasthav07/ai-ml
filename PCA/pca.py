import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create a sample dataset (4 features)
X = np.array([
    [2.5, 2.4, 1.5, 0.9],
    [0.5, 0.7, 0.9, 0.3],
    [2.2, 2.9, 2.1, 1.7],
    [1.9, 2.2, 1.6, 1.1],
    [3.1, 3.0, 2.9, 2.5],
    [2.3, 2.7, 2.2, 1.9],
    [2.0, 1.6, 1.7, 1.2],
    [1.0, 1.1, 0.8, 0.5],
    [1.5, 1.6, 1.3, 0.9],
    [1.1, 0.9, 1.0, 0.4]
])

# Step 2: Standardize data (mean=0)
X_meaned = X - np.mean(X, axis=0)

# Step 3: Covariance matrix
cov_mat = np.cov(X_meaned, rowvar=False)

# Step 4: Compute eigenvalues and eigenvectors
eigen_values, eigen_vectors = np.linalg.eigh(cov_mat)

# Step 5: Sort eigenvectors by decreasing eigenvalues
sorted_index = np.argsort(eigen_values)[::-1]
eigen_values = eigen_values[sorted_index]
eigen_vectors = eigen_vectors[:, sorted_index]

# Step 6: Select top 2 principal components
n_components = 2
eigenvector_subset = eigen_vectors[:, :n_components]

# Step 7: Transform data
X_reduced = np.dot(X_meaned, eigenvector_subset)

print("Original shape:", X.shape)
print("Reduced shape:", X_reduced.shape)
print("Eigenvalues:", np.round(eigen_values, 3))
print("Explained variance (%):", np.round(eigen_values / np.sum(eigen_values) * 100, 2))

# Step 8: Visualization
plt.figure(figsize=(7,5))
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], color='blue', edgecolor='k')
plt.title("PCA Visualization (2D Projection)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(True)
plt.show()

