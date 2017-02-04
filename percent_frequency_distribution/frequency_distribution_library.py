# -*- coding: utf-8 -*-

import os
import sys
import traceback
import time

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import config

class FrequencyDistributionLibrary(object):
    
    def __init__(self):
        pass
        
    def print_exception_message(self, message_orientation = "horizontal"):
        """
        print full exception message
        :param message_orientation: horizontal or vertical
        :return none
        """
        try:
            exc_type, exc_value, exc_tb = sys.exc_info()            
            file_name, line_number, procedure_name, line_code = traceback.extract_tb(exc_tb)[-1]       
            time_stamp = " [Time Stamp]: " + str(time.strftime("%Y-%m-%d %I:%M:%S %p")) 
            file_name = " [File Name]: " + str(file_name)
            procedure_name = " [Procedure Name]: " + str(procedure_name)
            error_message = " [Error Message]: " + str(exc_value)        
            error_type = " [Error Type]: " + str(exc_type)                    
            line_number = " [Line Number]: " + str(line_number)                
            line_code = " [Line Code]: " + str(line_code) 
            if (message_orientation == "horizontal"):
                print( "An error occurred:{};{};{};{};{};{};{}".format(time_stamp, file_name, procedure_name, error_message, error_type, line_number, line_code))
            elif (message_orientation == "vertical"):
                print( "An error occurred:\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(time_stamp, file_name, procedure_name, error_message, error_type, line_number, line_code))
            else:
                pass                    
        except Exception:
            pass
        
    def get_project_directory_path(self):
        """
        get project directory path from the calling file
        """
        project_directory_path = None
        try:  
            project_directory_path = os.path.dirname(sys.argv[0])            
        except Exception:
            self.print_exception_message()                    
        return project_directory_path
    
    def format_float_number(self, decimal_point, real_value):
        """
        format float numbers with digits
        :param decimal_point:
        :param real_value:
        :return formatted float number
        """
        format_value = 0.0
        try:
            if decimal_point == 1:
                format_value = float("{0:.1f}".format(real_value))
            elif decimal_point == 2:
                format_value = float("{0:.2f}".format(real_value))
            elif decimal_point == 3:
                format_value = float("{0:.3f}".format(real_value))
            elif decimal_point == 4:
                format_value = float("{0:.4f}".format(real_value))
            elif decimal_point == 5:
                format_value = float("{0:.5f}".format(real_value))
            else:
                format_value = float("{0:.3f}".format(real_value))
        except Exception:                                                          
            self.print_exception_message()
        return format_value
    
    def load_x_y_axis_data(self, data_file_name, column_name, group_by_colum = None, column_name_class = None):
        """
        define x and y axis data
        :param data_file_name:
        :param column_name:
        :param group_by_colum:
        :return x and y axis data 
        """
        x_axis = []
        y_axis = []        
        try:    
            data_frame = pd.read_csv(filepath_or_buffer = data_file_name, sep = ",")         
            if (group_by_colum is not None):                
                data_frame = data_frame.groupby(group_by_colum)                                
            data_serie = data_frame[column_name].value_counts(normalize = True)                    
            if (group_by_colum is not None):   
                for x, y in data_serie.iteritems():     
                    if x[0] == column_name_class:
                        x_axis.append(x[1])           
                        y_axis.append(y * 100)   
            else:
                for x, y in data_serie.iteritems():
                    x_axis.append(x)        
                    y_axis.append(y * 100)                            
        except Exception:
            self.print_exception_message()
        return x_axis, y_axis
    
    def build_bar_chart_vertical(self, x_axis, y_axis, image_file_name):
        """
        build vertical bar chart 
        :param x_axis: x axis data
        :param y_axis: y axis data
        :param image_file_name: image file path and name
        :return none
        """
        colors = []
        for x_value in x_axis:
            if x_value == config.INPUT1_CLASS2:
                colors.append('r')
            elif x_value == config.INPUT1_CLASS3:
                colors.append('y')
            else:
                colors.append('g')          
        plt.style.use(config.PLOT_STYLE)       
        x_pos = np.arange(len(x_axis))         
        rects = plt.bar(x_pos, y_axis, width = 0.7, color = colors, align = "center", alpha = 0.7, label = config.PLOT_LEGEND)
        for rect in rects:
            rec_x = rect.get_x()
            rec_width = rect.get_width()        
            rec_height = rect.get_height()  
            height_format = self.format_float_number(1, rec_height)      
            plt.text(rec_x + rec_width / 2, rec_height , str(height_format) + "%", horizontalalignment = "center", verticalalignment = 'bottom')       
        plt.xticks(x_pos, x_axis)   
        plt.xlabel(config.PLOT_X_LABEL1)
        plt.ylabel(config.PLOT_Y_LABEL1)      
        plt.title(config.PLOT_TITLE1)    
        plt.legend(loc = 1)    
        plt.tight_layout()
        plt.savefig(image_file_name, dpi = 100)
        plt.show()       
        
    def build_bar_chart_horizontal(self, x_axis, y_axis, image_file_name, plot_xlabel, plot_ylabel, plot_title):        
        """
         build horizontal bar chart 
        :param x_axis: x axis data
        :param y_axis: y axis data
        :param image_file_name: image file path and name
        :return none
        """
        plt.style.use(config.PLOT_STYLE)  
        x_pos = np.arange(len(x_axis))                     
        colors = ["r"]    
        rects = plt.barh(x_pos, y_axis, color = colors, align = "center", alpha = 0.8, label = config.PLOT_LEGEND)    
        for rect in rects:    
            rec_y = rect.get_y()
            rec_width = int(rect.get_width())
            rec_height = rect.get_height()        
            plt.text(rec_width - 0.6,  rec_y + rec_height / 2, str(rec_width) + "%", horizontalalignment = "center", verticalalignment = 'bottom')           
        plt.yticks(x_pos, x_axis)   
        plt.xlabel(plot_xlabel)
        plt.ylabel(plot_ylabel)      
        plt.title(plot_title)    
        plt.legend(loc = 1)    
        plt.tight_layout()
        plt.savefig(image_file_name, dpi = 100)
        plt.show()             