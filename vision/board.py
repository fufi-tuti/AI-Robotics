
#checks position of detected , and compare if its in this cell put it .

#take from camera and seperate it into 3 colums and rows 

# use numpy.shape?, frame.shape? 


#if u recieve detection atke frame 

def Get_cell_index(frame,className,x_min,x_max,y_min,y_max): #should i write result from detector.py?
   
    h,w=frame.shape[:2]
    cell__height=h/3      # row
    cell_Width=w/3       #col




    #calc center of infered box 
    x_center=(x_min+x_max)/2
    y_center=(y_min+y_max)/2

    #ex : How many times does 300 fully fit inside 650?

    '''
        How many groups of this size fit inside this amount?

        And the number of full groups = the index.
    '''''

    row=int(x_center//cell_Width)
    col=int(y_center//cell__height)


    row=min(max(row,0),2)
    col=min(max(col,0),2)

    return row,col
