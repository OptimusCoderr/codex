import numpy as np

def calculate(list):
   
    if len(list) == 9:
        #Convert list to numpy array
        array_1 = np.array(list)
        array_3 = np.array(list).reshape((3, 3))


        #_______SUM______
        #sum of rows
        row_sum = np.sum(array_3, axis=0)
        #sum of columns
        column_sum = np.sum(array_3, axis=1)
        #sum of flattened
        flattened_sum = np.sum(array_1)


        #_____MINIMUM______
        #MIN OF ROWS
        row_min = np.min(array_3, axis=0)
        #MIN OF columns
        column_min = np.min(array_3, axis=1)
        #MIN OF FLATTENED
        flattened_min = np.min(array_1)


        #______MAXIMUM_____
        #MAX OF ROWS
        row_max = np.max(array_3, axis=0)
        #MAX OF columns
        column_max = np.max(array_3, axis=1)
        #MAX OF FLATTENED
        flattened_max = np.max(array_1)


        #_______STANDARD DEVIATION______
        #STANDARD DEVIATION OF ROWS
        row_std = np.std(array_3, axis=0)
        #STANDARD DEVIATION OF COLUMNS
        column_std = np.std(array_3, axis=1)
        #STANDARD DEVIATION OF FLATTENED
        flattened_std = np.std(array_1)



        #______VARIANCE______
        #VARIANCE OF ROWS
        row_var = np.var(array_3, axis=0)
        #VARIANCE OF COLUMNS
        column_var = np.var(array_3, axis=1)
        #VARIANCE OF FLATTENED
        flattened_var = np.var(array_1)
        


        #___MEAN____
        #MEAN OF ROWS
        row_mean = np.mean(array_3, axis=0)
        #MEAN OF COLUMNS
        column_mean = np.mean(array_3, axis=1)
        #MEAN OF FLATTENED
        flattened_mean = np.mean(array_1)

                        

    else:
        print(ValueError, "List must contain nine numbers.")

    calculations = {
  'mean': [row_mean, column_mean, flattened_mean],
  'variance': [row_var, column_var, flattened_var],
  'standard deviation': [row_std, column_std, flattened_std],
  'max': [row_max, column_max, flattened_max],
  'min': [row_min, column_min, flattened_min],
  'sum': [row_sum, column_sum, flattened_sum]
    }







    return calculations