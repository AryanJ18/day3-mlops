from dataloader import load_data
from preprocess import preprocess_data
from train import train_model
from evaluate import evaluate_model
import joblib

data = load_data()

X_train, X_test, y_train, y_test = preprocess_data(data)
model = train_model(X_train, y_train)
accuracy = evaluate_model(model, X_test, y_test)
joblib.dump(model, "model.pkl")
print(f"Model Accuracy :{accuracy:.2f}")