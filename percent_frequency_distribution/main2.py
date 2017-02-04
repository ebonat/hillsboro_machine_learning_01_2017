# -*- coding: utf-8 -*-

# import sys
import os
import time

from frequency_distribution_library import FrequencyDistributionLibrary
import config

def main():
#     set the class object
    frequency_distribution = FrequencyDistributionLibrary()
    
#     set data file
    project_directory_path = frequency_distribution.get_project_directory_path()    
    data_file_name = os.path.join(project_directory_path, config.DATA_FILE)      
    
#     percent frequency distribution by Priority
    image_file_name11 = os.path.join(project_directory_path, config.IMAGE_FILE1)      
    x_axis, y_axis = frequency_distribution.load_x_y_axis_data(data_file_name, config.INPUT1)     
    frequency_distribution.build_bar_chart_vertical(x_axis, y_axis, image_file_name11)

#     percent frequency distribution by Error Message        
    image_file_name2 = os.path.join(project_directory_path, config.IMAGE_FILE2)     
    x_axis, y_axis = frequency_distribution.load_x_y_axis_data(data_file_name, config.INPUT2, config.INPUT1, config.INPUT1_CLASS2)      
    frequency_distribution.build_bar_chart_horizontal(x_axis, y_axis, image_file_name2, config.PLOT_X_LABEL2, config.PLOT_Y_LABEL2, config.PLOT_TITLE2)
    
#     percent frequency distribution by Warning Message        
    image_file_name3 = os.path.join(project_directory_path, config.IMAGE_FILE3)     
    x_axis, y_axis = frequency_distribution.load_x_y_axis_data(data_file_name, config.INPUT2, config.INPUT1, config.INPUT1_CLASS3)      
    frequency_distribution.build_bar_chart_horizontal(x_axis, y_axis, image_file_name3, config.PLOT_X_LABEL3, config.PLOT_Y_LABEL3, config.PLOT_TITLE3)
    
if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print("Program Runtime: " + str(round(end_time - start_time, 1)) + " seconds" + "\n")