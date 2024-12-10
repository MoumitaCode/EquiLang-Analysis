#Project Name = EquiLang
#Author = Moumita Ray
#Starting Date = 12-04-2024
#Ending Date = 12-10-2024

#Import the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Check if the file exists and load the data
def load_data():
    try:
        data = pd.read_csv('data/ELLData.csv')
        print("File loaded successfully!")
        return data
    except FileNotFoundError:
        print("The file was not found. Please check the path.")
        return None

# Main program
def main():
    data = load_data()
    if data is not None:
        print("Please choice what you want an analysis on:")
        print("1. Total English Language Learners in 50 states")
        print("2. Students with disabilities under IDEA in Michigan")
        print("3. Visualizations")
        print("4. Quit")
        
        while True:
            choice = input("Enter your choice (1-4): ")
            if choice == "1":
                total_ELL_learners(data)
            elif choice == "2":
                students_with_disabilities(data)
            elif choice == "3":
                visualizations(data)
            elif choice == "4":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")




# Choice 1: Total English Language Learners in all 50 states
def total_ELL_learners(data):
    total_ELL = data.loc[data['State'] == '50 states, District of Columbia, and Puerto Rico', 'Total Students'].values[0]
    print(f"Total ELLs in 50 states: {str(total_ELL)}")
    print("---------------------------------------------")

# Choice 2: Students with disabilities under IDEA
def students_with_disabilities(data):
    michigan_row = data[data['State'] == 'Michigan']
    
    total_disabilities = michigan_row['Students With Disabilities Served Under IDEA  Number'].values[0]
    disability_percent = michigan_row['Students With Disabilities Served Under IDEA  Percent'].values[0]

    print(f"Total students with disabilities in Michigan: {total_disabilities}")
    print("Percentage of students with disabilities in Michigan: " + str(disability_percent) + "%")
    print("---------------------------------------------")


# Choice 3 Function for visualizations
def visualizations(data):
    while True:
        print("Choose an option:")
        print("1. Bar graph of the number of schools in the top 4 states with most ELL students")
        print("2. Pie chart of percentage of ELL students by race/ethnicity")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":

# Data for bar graph (Top 4 states with most ELL students)
            states = ['California', 'Texas', 'Florida', 'New York']
            ell_students = [1090375, 954145, 290057, 241791]
            number_of_schools = [10121, 8758, 3976, 4873]

            # Bar positions
            x = range(len(states))
            width = 0.4

            # Create the grouped bar graph
            plt.bar([pos - width/2 for pos in x], ell_students, width, label='ELL Students', color='skyblue')
            plt.bar([pos + width/2 for pos in x], number_of_schools, width, label='Number of Schools', color='green')

            # Add labels, title, and legend
            plt.xlabel('State')
            plt.ylabel('Count')
            plt.title('Comparison of ELL Students and Schools in Top 4 States')
            plt.xticks(x, states)
            plt.legend()

            # Show the graph
            plt.show()

        elif choice == "2":
            # Pie chart of ELL students by race/ethnicity
            race_ethnicity = ['White', 'Hispanic/Latino', 'Black', 'Asian', 'Two or more races']
            percentages = [6.5, 76.5, 4.3, 10.6, 0.7]

            # Create the pie chart
            plt.pie(percentages, labels=race_ethnicity, autopct='%1.1f%%', startangle=90)
            plt.title('Total Percentage of ELL Students by Race/Ethnicity')
            plt.axis('equal') 
            plt.show()

#function for exiting the analysis
        elif choice == "3":
            print("Exiting visualization options.")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
main()