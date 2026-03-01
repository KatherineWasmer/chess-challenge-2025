# Global Chess Challenge - 2025

### ♟️ Overview 

Chess has become "in vogue" again. With the release of the Queen's Gambit on Netflix in 2020, the rise in popularity of chess twitch streamers, and the documentary *Queen of Chess*, many people have gained an interest in this 5,000 year old board game. I started playing chess in 2023, with only a basic understanding of how the pieces moved. Since then, I have continued to improve and even participate in USCF tournaments. 

I learned about this competition through the chess community and thought it would be a fun opportunity to integrate my data science skills with one of my favorite hobbies. This contest asks an important question: can we use an LLM as a personalized chess coach? Although there are many tools to help individuals learn chess (e.g., Stockfish analysis, chess bots, etc.), many of these tools don't explain *why* the best move works. You can learn more about the objectives of the Global Chess Challenge [here](https://github.com/AIcrowd/global-chess-challenge-2025-starter-kit). 

♟️ ACPL 

Average centipawn loss (ACPL): A centipawn equals 1/100 of a pawn. This is a theoretical way of measuring how well an individual plays compared to the best engine move; you lose more centipawns if your move is less accurate. If the move is decent but not the exact engine move, you would only lose a centipawn or two. In a game between two chess grandmasters (GMs), the mean ACPL is around 12. Most classical chess games consist of 40 turns, so this means that a GM played the best engine move 70% of the time, with the other 30% likely being decent moves. 

♟️ FINAL RESULTS 

**Round 1:** 17th place out of 56 teams (ACPL: 89.2) 

**Round 2:** Did not qualify for the final tournament (Baseline ACPL = 71.9; I obtained a minimum ACPL of 84)

You can download my best model from my [HuggingFace page](https://huggingface.co/kgwasmer/aicrowd-best-model). 

### ♟️ Data 

[**LiChess puzzles**](https://database.lichess.org/#puzzles): This data can be used to help train a model to recognize patterns, tactical motifs, and common moves in chess. 

Within the data folder, you will find various subsets of the puzzle dataset, which consists of 5.6 million puzzles. However, this is computationally inefficient for training, so we only need a few thousand points. 

**chess_data_10K.jsonl:** A sample of 10,000 model-response lines used for fine-tuning the data. I initially fine-tuned the model with 1,000 of the data points (only 0.01% of the data), getting an ACPL of 106. I tested to see if increasing the sample size would improve the model. Running my script for 10,000 data points took 30 minutes. Running my function on 500,000 data points (10% of the data) took 25 hours. 

### ♟️ Scripts 

**configure_lichess_csv.py:** This Python script parses the LiChess puzzle data into an interpretable CSV format for data analysis, manipulation, and JSON conversion for LLM prompting. 

