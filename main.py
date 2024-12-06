#Project Name = EquiLang
#Author = Moumita Ray
#Starting Date = 12-04-2024
#Ending Date = 

#Import the libraries
import pandas as pd
import matplotlib.pyplot as plt


#Check if the file exists
def load_data(data):
    try:
        file = open('data/Analysis.csv', 'r')
        print("File opened successfully!")

    except FileNotFoundError:
        print("The file was not found.")
    
    else:
       
        print("No errors occurred during file opening.")
        file.close()

# Call the function
load_data('Analysis.csv')
























# Function for user-driven analysis
def analyze_data(data):

    print("Please choose an option for analysis:")
    print("1. Total Students by Race/Ethnicity")
    print("2. Percentage of Students with Disabilities")
    print("3. Visualization Options")
    choice = input("Enter your choice (1, 2, or 3): ").strip()

#Show answer to user's input 
#if else statements
    if choice == "1":
        for race in ['American Indian or Alaska Native', 'Asian', 'Hispanic or Latino', 'Black or African American', 'White', 'Native Hawaiian or Other Pacific Islander', 'Two or more races']:
            column_name = race + ' Number'
            if column_name in data.columns:
                total = data[column_name].sum()
                print("Total", race, "students:", total)
            else:
                print("Column not found:", column_name)
