def get_memory_score(input_nums):
    
    invalid = False
    invalid_inputs = []
    
    for n in input_nums:
        if(isinstance(n, int) != True):
            invalid = True
            invalid_inputs.append(n)
    
    if(invalid):
        print("Please enter a valid input list.\nInvalid inputs detected:", invalid_inputs)
        return
    
    memory = []
    score = 0
    
    for n in input_nums:
        
        if(n in memory):
            score += 1
        
        else:
            if(len(memory) == 5):
                memory.pop(0)
                memory.append(n)
            else:
                memory.append(n)
    
    print("Score:", score)
    return


input_nums =  [3, 4, 1, 6, 3, 3, 9, 0, 0, 0]

get_memory_score(input_nums)