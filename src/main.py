from src.state import wait_and_capture_board,detect_peices,Create_board,Human_turn,decision,get_cell,move_to_target


frame=wait_and_capture_board()

Detection=detect_peices(frame)

Board=Create_board(Detection)

Decisison=decision(Board)

