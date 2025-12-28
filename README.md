# chess-challenge-2025
These are the resources used for my fine-tuned LLM for AI Crowd's Global Chess Challenge. 

### configure_lichess_csv.py 

This Python script parses the downloaded LiChess puzzle files (found at https://database.lichess.org/#puzzles) into an interpretable CSV format for data analysis, manipulation, and JSON conversion for LLM prompting. Currently, LiChess has a sample of 5.6 million puzzles. 

### chess_data_10K.jsonl 

A sample of 10,000 model-response lines used for fine-tuning the data. I initially fine-tuned the model with 1,000 of the data points (only 0.01% of the data), getting an ACPL of 106. I tested to see if increasing the sample size would improve the model. 
