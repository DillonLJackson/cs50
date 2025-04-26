def main():

    # open file path
    with open("USPopulation.txt", "r") as file:
        population_list = [int(line.strip()) for line in file]
    # create list of years for dict
    year = list(range(1950, 1990+1))
    # create dict using zip function
    year_population = dict(zip(year, population_list))
    # find sum of population by indexing
    changes = []
    for i in range(1, len(year)):
        change = year_population[year[i]] - year_population[year[i-1]]
        changes.append(change)
    # calculate average
    average_change = sum(changes) / len(changes)
    # display average
    print(f"The average annual change in population during the time period is {average_change:,.2f}")
    # identify changes in population
    change_per_year = []
    for i in range(1, len(year)):
        year_previous = year[i-1]
        year_curr = year[i]
        change = year_population[year_curr] - year_population[year_previous]
        # make changes into list
        change_per_year.append(change)
    # find max and min changes in list
    max_changes = max(change_per_year)
    min_changes = min(change_per_year)
    # index back into list to find number year
    max_index = change_per_year.index(max_changes)
    min_index = change_per_year.index(min_changes)
    # index back into years to print years
    print(f"The year with the greatest increase in population was {year[max_index]+1}")
    print(f"The year with the smallest increase in population was {year[min_index]+1}")
    

    #wth was that
main()