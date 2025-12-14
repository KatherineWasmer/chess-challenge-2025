import pandas as pd 

# Download the file from https://database.lichess.org/#puzzles

def parse_lichess_csv(your_file_zst, keeps, output_file_name): 
  """
  Unzips the current database of Lichess puzzles (12/13/25 has around 5.6M puzzles!) and converts it into a readable csv format for data analysis. 

  Parameters:
  your_file_zst -- the .zst file you downloaded
  keeps -- a list of variables to keep in your new file. Options are as follows: 
  PuzzleId, FEN, Moves, Rating, RatingDeviation, Popularity, NbPlays, Themes, GameUrl, OpeningTags
  output_file_name -- your new file name for the exported .csv file 
  """
  df = pd.read_csv(your_file_zst, compression='zstd')
  puzzles = df[[keeps]]
  puzzles.to_csv(puzzles, index=False)
