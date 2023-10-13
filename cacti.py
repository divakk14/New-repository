def cacti_number(plot):
    # Get the dimensions of the plot
    rows = len(plot)
    columns = len(plot[0])
    
    
    count_n_of_cacti = 0
    for i in range(rows):
        for j in range(columns):
            if plot[i][j] == 0:
                # Check if the adjacent blocks are empty
                adjacent_empty = True
                if i > 0 and plot[i-1][j] == 1:
                    adjacent_empty = False
                if j > 0 and plot[i][j-1] == 1:
                    adjacent_empty = False
                if i < rows-1 and plot[i+1][j] == 1:
                    adjacent_empty = False
                if j < columns-1 and plot[i][j+1] == 1:
                    adjacent_empty = False
                if i > 0 and j > 0 and plot[i-1][j-1] == 1:
                    adjacent_empty = False
                if i > 0 and j < columns-1 and plot[i-1][j+1] == 1:
                    adjacent_empty = False
                if i < rows-1 and j > 0 and plot[i+1][j-1] == 1:
                    adjacent_empty = False
                if i < rows-1 and j < columns-1 and plot[i+1][j+1] == 1:
                    adjacent_empty = False
                
                if adjacent_empty:
                    count_n_of_cacti += 1
    
    return count_n_of_cacti