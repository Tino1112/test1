# Import potrebnih biblioteka
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib


# Učitavanje podataka
file_path = r"C:\Users\User\PycharmProjects\test_zadatak_3\training_data.csv"
data = pd.read_csv(file_path)


# Prikaz prvih nekoliko redaka
print("Prvi redovi učitanih podataka:")
print(data.head())


# Podjela podataka na značajke i ciljne varijable
X = data.iloc[:, :-1]
y = data.iloc[:, -1]


# Podjela podataka na trening (70%) i preostalo (30%)
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)


# Podjela preostalog dijela na testiranje (15%) i validaciju (15%)
X_test, X_val, y_test, y_val = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)


print(f"Training set size: {X_train.shape[0]}")
print(f"Testing set size: {X_test.shape[0]}")
print(f"Validation set size: {X_val.shape[0]}")


# Inicijalizacija RandomForest modela
model = RandomForestClassifier(random_state=42)


# Treniranje modela
model.fit(X_train, y_train)


# Evaluacija na validation skupu
y_pred_val = model.predict(X_val)


# Izvještaj klasifikacije i matrica konfuzije za validation skup
print("Classification Report (Validation Data):")
print(classification_report(y_val, y_pred_val))


print("Confusion Matrix (Validation Data):")
print(confusion_matrix(y_val, y_pred_val))


# Evaluacija na testnom skupu
y_pred_test = model.predict(X_test)


# Izvještaj klasifikacije i matrica konfuzije za testni skup
print("Classification Report (Test Data):")
print(classification_report(y_test, y_pred_test))

print("Confusion Matrix (Test Data):")
print(confusion_matrix(y_test, y_pred_test))

# Spremanje modela
joblib.dump(model, 'random_forest_model.joblib')
print("Model saved as 'random_forest_model.joblib'")
