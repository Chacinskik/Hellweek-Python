#Day 7 - Area calculator

"""
Calculates area of the figures contained in target .txt file. Assumes that first item
of the line is the name of the figure and values are separated by ','.
"""

from CalculateArea import *


file = "figures.txt"

def create_report(file):
    with open(file, encoding = 'utf-8') as f:
        report = ''
        for index, line in enumerate(f):
            line_as_list = line.split(",")
            figure_name = line_as_list[0]
            line_as_list = [float(item.strip()) for item in line_as_list[1:]] #converts all to float excluding first item of the line
            line_as_list.insert(0, figure_name)
            try:
                if "kwadrat" in line_as_list[0]: #square
                    result = CalculateArea.square(line_as_list[1])
                    report += f'Area of {line_as_list[0]} (line {index+1}): {result}\n'
                elif "trojkat" in line_as_list[0]: #triangle
                    result = CalculateArea.triangle(line_as_list[1], line_as_list[2])
                    report += f'Area of {line_as_list[0]} (line {index+1}): {result}\n'
                elif "trapez" in line_as_list[0]: #trapeze
                    result = CalculateArea.trapeze(line_as_list[1], line_as_list[2], line_as_list[3])
                    report += f'Area of {line_as_list[0]} (line {index+1}): {result}\n'
                elif "kolo" in line_as_list[0]: #circle
                    result = CalculateArea.circle(line_as_list[1])
                    report += f'Area of {line_as_list[0]} (line {index+1}): {result}\n'
                else:
                    result = f'Program cannot handle the entered figure: {line_as_list[0]} (line {index+1})\n'
                    report += result
                
            except IndexError:
                print("File does not contain sufficient information.")
                return None
    print(report)


create_report(file)