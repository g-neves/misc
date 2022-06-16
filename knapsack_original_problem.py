import time


# Check if given item can be add to the knapsack
def can_add_item(item_weight, available_weight):
    if item_weight > available_weight:
        return False 
    return True

# Gets the maximum value obtained
def solve_knapsack(values, weights, available_weight, idx=0, memo={}):
    # Check if we came to the end of the list
    if idx >= len(values):
        return 0 

    # If we already have the result in memo, returns it
    if (idx, available_weight) in memo:
        return memo[(idx, available_weight)]

    else:
        # Check the solution without including current item
        without_this_item = solve_knapsack(values, weights, available_weight, idx+1, memo)
        # If we can add the current item
        if can_add_item(weights[idx], available_weight):
            # We add it
            with_this_item = solve_knapsack(values, weights, available_weight-weights[idx], idx+1, memo) + values[idx]

            # And stays with the biggest return
            memo[(idx, available_weight)] = max(without_this_item, with_this_item)

            return memo[(idx, available_weight)]

        # Otherwise we only have the option without this item
        else:
            memo[(idx, available_weight)] = without_this_item

    return memo[(idx, available_weight)]

def get_optimum_items(values, weights, available_weight):
    # Iterates over all items
    for idx, value in enumerate(values):
        weight = weights[idx] # Gets the actual item weight
        # If we can not add the item, just continue
        if not can_add_item(weight, available_weight):
            continue 
    
        # Otherwise, we calculate the profit with and without the item
        profit_with_this_item = solve_knapsack(values, weights, available_weight - weight, idx+1) + value
        profit_without_this_item = solve_knapsack(values, weights, available_weight, idx+1)
        # If the profit with the item is bigger, we add the item to the list and subtract 
        # the weight from the available weight
        if profit_with_this_item > profit_without_this_item:
            yield value 
            available_weight -= weight




if __name__ == '__main__':
    # Weights array
    w_arr = [288, 853, 291, 102, 529, 90, 132, 717, 417, 285]
    # Values array
    v_arr = [321, 942, 339, 31, 463, 149, 50, 745, 395, 377]
    # Weight limit for the knapsack
    maximum_weight = 2000

   
    starting_time = time.time()
    print("Optimum profit:")
    print(solve_knapsack(v_arr, w_arr, maximum_weight))
    print("Items list:")
    print(list(get_optimum_items(v_arr, w_arr, maximum_weight)))
    ending_time = time.time()
    print(f'finished in {ending_time - starting_time} seconds')
    
    assert sum(list(get_optimum_items(v_arr, w_arr, maximum_weight))) == solve_knapsack(v_arr, w_arr, maximum_weight)
    
 

        

