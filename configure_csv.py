import pandas as pd 

lichess_puzzles = "lichess_db_puzzle.csv.zst"

df = pd.read_csv(lichess_puzzles, compression='zstd')
puzzles = df[["PuzzleId", "FEN", "Themes", "GameUrl", "OpeningTags"]]
puzzles.to_csv("lichess_puzzles", index=False)
