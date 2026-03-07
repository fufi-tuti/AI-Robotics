from vision.detector import Detector
from vision.camera import  Camera
from vision.board import get_boxes,get_cell_index


from game_ai.minimax import playerMove,bestMove,minimax
from game_ai.rules import isThereAMove,isthereAWinner

from robot.kinematics import solve_inverse_kinematics



#diff states of game

#capture board [camera]

def wait_and_capture_board():
   
   cam=Camera()
   cam.Get_current_frame()



#detection 
def detect_peices():

   detect=Detector()
   detect.Get_detect()



#create board
def Create_board(detection):
   
   All_Boxes=get_boxes(detection)

   get_cell_index(All_Boxes)




 

#humans turn , OR YK ?

def Human_turn():
   pass


#decision:  check minimax , rules [ we want rules always to be on ] or after each turn , do ig after minimax ?

#rules alone ? idk minimax?
def decision(board):

   bestMove(board)

   pass
   


   


# give acc cells , use Ai_interface

def get_cell():
   pass


# move_to_target 1- kinematics , 2-motion planning , 3- driver_movement (low level coding )
def move_to_target():

   Movement=solve_inverse_kinematics()
   pass




