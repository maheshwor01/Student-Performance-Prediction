import pickle
import os

model_path = os.path.join(os.path.dirname(__file__), "student_model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

print("Model loaded successfully!")
print(model)
print(type(model))