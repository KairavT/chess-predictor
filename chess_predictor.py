import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt


# Features using pandas
df = pd.read_csv('data/games.csv')

df['rating_diff'] = df['white_rating'] - df['black_rating']

df['result'] = df['winner'].map({'white':0,'black':1,\
                                'draw':2}) 

df['rated'] = df['rated'].astype(int)

df['opening_category'] = df['opening_eco'].str[0]

df = pd.get_dummies(df, dtype=int, drop_first = True, columns = ['opening_category'])

feature_list = ['white_rating', 'black_rating',\
                 'rating_diff', 'turns', 'rated', 'opening_ply']\
      + [col for col in df.columns if col.startswith('opening_category_')]

X = df[feature_list]
y = df['result']

# Model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.20, random_state=123
)

model = RandomForestClassifier(n_estimators = 100, random_state=123)

model.fit(X_train, y_train)
predictions = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")
print(classification_report(y_test, predictions))


#Feature vs Importance matplotlib
feat_importance = pd.DataFrame(
    {
        "Feature":feature_list,
        "Importance": model.feature_importances_
    }
).sort_values(by='Importance', ascending = True)

print(feat_importance)

plt.figure(figsize=(10, 6))
plt.barh(feat_importance["Feature"], feat_importance["Importance"])
plt.title("Importance of Features in Random Forest Chess Game Predictor")
plt.xlabel("Importance")
plt.tight_layout()
plt.savefig('feature_importance.png')
plt.show()