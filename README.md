
# Chess Outcome Predictor

Predicts the outcomes of chess games based on real data from lichess using random forest

## Results

The model achieved 65% accuracy across three classes (white win, black win, draw)
![Feature Importance](feature_importance.png)

## Key Findings

The biggest factor (most important feature) in determining the outcome of a game was the rating difference between two players. Interestingly, the game length was also a large factor. Openings were not very important, and had very little effect on the outcome of a game. Draws were difficult to predict due to draws being less than 5% of the games in the data set.

## Tech stack
- Python
- pandas
- scikit-learn
- matplotlib



​```zsh

# Clone the repo
git clone https://github.com/KairavT/chess-predictor.git
cd chess-predictor
  
# Set up a virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install pandas scikit-learn matplotlib
  
# Download games.csv from Kaggle and place it in the data/ folder:
# https://www.kaggle.com/datasets/datasnaek/chess
  
# Run the predictor
python3 chess_predictor.py

​```
