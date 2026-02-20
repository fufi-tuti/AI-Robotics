
#checks position of detected , and compare if its in this cell put it .

#take from camera and seperate it into 3 colums and rows 

# use numpy.shape?, frame.shape? 


#if u recieve detection atke frame 

def Get_cell_index(frame,className,x_min,x_max,y_min,y_max): #should i write result from detector.py?
    cell__hight=frame.shape[0]/3      # row
    cell_Width=frame.shape[1]/3 #col


   # boundaryH_0=0*cell__hight
    boundaryH_1=cell__hight
    boundaryH_2=cell__hight*2  
    boundaryH_3=cell__hight*3  


    #boundaryW_0=0*cell_Width  
    boundaryW_1=cell_Width  
    boundaryW_2=cell_Width*2  
    boundaryW_3=cell_Width*3  


    # splitting box into seperate rows and columns

    row1=range(0,boundaryH_1)
    row2=range(boundaryH_1,boundaryH_2)
    row3=range(boundaryH_2,boundaryH_3)


    col1=range(0,boundaryW_1)
    col2=range(boundaryW_1,boundaryW_2)
    col3=range(boundaryW_2,boundaryW_3)

    #computing center of box from inferenece (detector.py)

    x_center=(x_min+x_max)/2
    y_center=(y_min+y_max)/2



    if  (0<=x_center<boundaryH_1):
        row1=range(0,boundaryH_1)
        return row1
        



    #seeing center falls into whch row /col
    
    if x_center in row1:


        return row1
    
    if x_center in row2:

        return row2
    

    if x_center in row2:

        return row2
    


    ##---------------------------##

    if y_center in col1:

        return col1
    
    if y_center in col2:

        return col2
    
    if y_center in col3:

        return col3

    

    return

















#col_1=[0:0+Column_size]   #use slicing ? 
#col_2=[col_1:col_1+Column_size]  
#col_3=[col_2:col_2+Column_size]  

#row_1=[0:0+Row_size]  
#row_2=[row_1:]  
#row_3=[row_2:] 