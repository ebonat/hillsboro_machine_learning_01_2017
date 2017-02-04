# -*- coding: utf-8 -*-

import sys
import os
import time

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
#     Frequency Distribution 1 (Vertical Bar Chart) --------------------------------------------------------------------------------------------------------
#     file_path_name = r"C:\Users\Ernest\git\test-code\test-code\src\percent_frequency_distribution\network_activities.csv"
    
#     get project directory path
    project_directory_path = os.path.dirname(sys.argv[0])  

#     define file path name
    file_path_name1 = os.path.join(project_directory_path, "network_activities.csv")  
    
#     define image file path name
    image_path_name1 = os.path.join(project_directory_path, "network_activities.png")  
    
#     get network activity data frame
    df_network_activity1 = pd.read_csv(filepath_or_buffer = file_path_name1, sep = ",")
     
#      get relative frequencies in a pandas serie
    ds_network_activity1 = df_network_activity1["Priority"].value_counts(normalize = True)
#     print(ds_network_activity)
        
#     define the x and y axis’s
#     tip: how to slide a pandas serie (loc, iloc or ix methods)?
    x_axis = []
    y_axis = []
    for x, y in ds_network_activity1.iteritems():
        x_axis.append(x)        
        y_axis.append(y * 100)            
    
#     build and plot the network activity vertical bar chat    
    colors = []
    for x_value in x_axis:
        if x_value == "Error":
            colors.append('r')
        elif x_value == "Warning":
            colors.append('y')
        else:
            colors.append('g')          
    plt.style.use("ggplot")       
    x_pos = np.arange(len(x_axis))         
    rects = plt.bar(x_pos, y_axis, width = 0.7, color = colors, align = "center", alpha = 0.7, label = "Amount of Messages")
    for rect in rects:
        rec_x = rect.get_x()
        rec_width = rect.get_width()        
        rec_height = rect.get_height()  
        height_format = float("{0:.1f}".format(rec_height)) 
        plt.text(rec_x + rec_width / 2, rec_height , str(height_format) + "%", horizontalalignment = "center", verticalalignment = 'bottom')       
    plt.xticks(x_pos, x_axis)   
    plt.xlabel("Priority")
    plt.ylabel("Percent Frequency")      
    plt.title("Priority Message Percent Frequency Distribution")    
    plt.legend(loc = 1)    
    plt.tight_layout()
    plt.savefig(image_path_name1, dpi = 100)
    plt.show()       
    
#     Frequency Distribution 2 (Horizontal Bar Chart) ----------------------------------------------------------------------------------------------------------------
    
#     get project directory path
    file_path_name2 = os.path.join(project_directory_path, "network_activities.csv")  
    
#     define image file path name
    image_path_name2 = os.path.join(project_directory_path, "network_activities2.png")  
    
#     get network activity data frame for priority and message columns
    df_network_activity2 = pd.read_csv(filepath_or_buffer = file_path_name2, sep = ",")

#     group by priority column          
    df_column_group = df_network_activity2.groupby("Priority")    
    
#     get relative frequencies by message column
    ds_network_activity2 = df_column_group["Message"].value_counts(normalize = True)     
   
#     define the x and y axis’s
    x_axis = []
    y_axis = []
    for x, y in ds_network_activity2.iteritems():     
        if x[0] == "Error":
            x_axis.append(x[1])           
            y_axis.append(y * 100)       
            
#    build and plot the network activity horizontal bar chat    
    plt.style.use("ggplot")  
    x_pos = np.arange(len(x_axis))                     
    colors = ["r"]    
    rects = plt.barh(x_pos, y_axis, color = colors, align = "center", alpha = 0.8, label = "Amount of Messages")    
    for rect in rects:    
        rec_y = rect.get_y()
        rec_width = int(rect.get_width())
        rec_height = rect.get_height()        
        plt.text(rec_width - 0.6,  rec_y + rec_height / 2, str(rec_width) + "%", horizontalalignment = "center", verticalalignment = 'bottom')   
    
    plt.yticks(x_pos, x_axis)   
    plt.xlabel("Percent Frequency")
    plt.ylabel("Error Message")      
    plt.title("Error Server Percent Frequency Distribution")    
    plt.legend(loc = 1)    
    plt.tight_layout()
    plt.savefig(image_path_name2, dpi = 100)
    plt.show()             
    
if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print("Program Runtime: " + str(round(end_time - start_time, 1)) + " seconds" + "\n")