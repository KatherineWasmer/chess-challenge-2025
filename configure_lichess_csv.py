import pandas as pd 
import chess
import chess.engine
from stockfish import Stockfish

# Download the file from https://database.lichess.org/#puzzles

def get_all_legal_moves(my_fen):
    """Returns a list of all legal moves that can be parsed into a json format
    for LLM prompting."""
    board = chess.Board(my_fen)
    moves = board.legal_moves
    uci_lm_list = []
    for m in moves:
        uci_lm_list.append(board.uci(m))
    return uci_lm_list

stockfish = Stockfish(
    path="/opt/homebrew/bin/stockfish",
    parameters={
        "Skill Level": 20,
        "Threads": 1,
        "Hash": 256,
    }
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

def get_puzzle_themes(data: pd.DataFrame, theme: str, nrows: int) -> pd.DataFrame:
    """Extracts n rows of a certain puzzle theme type. 
    """
    return data[data["Themes"].str.contains(theme)].head(nrows)

def extract_jsonl_from_data(data: pd.DataFrame, fileName: str):
    # drop duplicate fens 
    data = data.drop_duplicates()
    data["LegalMoves"] = data["FEN"].apply(get_all_legal_moves)
    data["input"] = (
        "FEN: " + data["FEN"].astype(str) +
        "\nLegal Moves: " + data["LegalMoves"].apply(lambda x: ", ".join(x))
    )
    data["BestMove"] = data["FEN"].apply(get_best_move)
    data["instruction"] = "Select the best move for this position from the set of legal moves, and briefly provide a reason for your choice."
    data["output"] = data["BestMove"].apply(format_output)
    data[["instruction", "input", "output"]].to_json(
        fileName,
        orient="records",
        lines=True,
        force_ascii=False
    )

def get_json_from_fen_csv(csv_file: str, json_file_name: str): 
    data = pd.read_csv(csv_file, header=None)
    extract_jsonl_from_data(data, json_file_name)

