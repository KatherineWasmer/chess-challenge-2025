import pandas as pd 
import requests
import urllib.parse
import chess
import chess.engine
from stockfish import Stockfish

# Download the file from https://database.lichess.org/#puzzles

def parse_lichess_zst(your_file_zst, keeps, output_file_name): 
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
  puzzles.to_csv(output_file_name, index=False)

def get_first_n_lines(your_file, n_lines, output_file_name):
  df = pd.read_csv(your_file, nrows=n_lines)
  df.to_csv(output_file_name, index=False)

def get_all_legal_moves(my_fen):
    """Returns a list of all legal moves that can be parsed into a json format
    for LLM prompting."""
    board = chess.Board(my_fen)
    moves = board.legal_moves
    uci_lm_list = []
    for m in moves:
        uci_lm_list.append(board.uci(m))
    return uci_lm_list

def format_input(fen, legal_moves):
    """This function formats the FEN and LegalMoves 
    columns from the data frame into a JSONL-friendly 
    format."""
    return (
        f"FEN: {fen}\n"
        f"Legal moves: {', '.join(legal_moves)}"
    )

def get_best_move(fen):
    stockfish = Stockfish(path="/opt/homebrew/bin/stockfish")
    stockfish.set_fen_position(fen)
    stockfish.set_skill_level(20) # most important param for accuracy 
    return (stockfish.get_best_move())

def format_output(best_move):
    """This function returns a text-based output 
    from the BestMove column, allowing the LLM to fine 
    tune data."""
    return (
        f"<uci_move>{best_move}</uci_move>"
    )