import sys
import statistics as stats
def analyze_cat_shelter(file_path):
#to keep track of statistics    
    correct_cat_entries = 0
    intruding_cat_doused = 0
    total_time_correct_cat = 0
    correct_cat_visit = []
    try:
        with open(file_path, 'r') as file:# open the file for reading
            for line in file: #iterates each line in the file
                parts= line.strip().split(',')
                if len(parts)==1:  #Terminates the loop when END is encountered
                    break
                cat_name, entry_time, departure_time = parts
                
                #convert entry and departure time into integers
                entry_time = int(entry_time)
                departure_time = int(departure_time)
                
                max_duration = 0
                min_duration = float("inf") #used to compare shortest duration
                
                #to check if the cat is the correct cat(OURS)
                if cat_name == "OURS":
                    correct_cat_entries += 1
                    total_time_correct_cat += (departure_time - entry_time)
                    correct_cat_visit.append(departure_time - entry_time)
                    
                else:
                    #if it is an intrding cat ,increament the count
                    intruding_cat_doused += 1
        
        #calculation
        avg_duration = round(stats.mean(correct_cat_visit))
        max_duration = max(correct_cat_visit)
        min_duration = min(correct_cat_visit)
        hours = total_time_correct_cat // 60
        mins = total_time_correct_cat % 60
        
        
        #displaying results
        print("\nLog File Analysis")
        print("="*40)
        print(f"\nTotal number of times the correct cat entered: {correct_cat_entries}")
        print(f"\nThe numbers of times intruding cats have been doused with water: {intruding_cat_doused}")
        print(f"\nThe total time spent in the house by the correct cat: {hours} hours {mins} minutes")
        print(f"\nAverage duration of each visit by the correct cat: {avg_duration} minutes")
        print(f"\nDuration of the longest visit by the correct cat: {max_duration} minutes ")
        print(f"\nDuration of the shortest visit by the correct cat: {min_duration} minutes")
    
    except FileNotFoundError:
        print(f"The file '{file}' was not found.")

if len(sys.argv)!=2:
    print("Missing command line argument")
else:
    #calling the function
    analyze_cat_shelter(sys.argv[1])