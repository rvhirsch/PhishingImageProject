import sklearn

from sklearn.datasets import load_breast_cancer

# load dataset
data = load_breast_cancer()

# organize data
label_names = data['target_names']
lables = data['target']
feature_names = data['feature_names']
features = data['data']

print(label_names)
print(labels[0])
print(feature_names[0])
print(features[0])
