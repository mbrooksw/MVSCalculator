import numpy as np


def mean_value(np_matrix):
    meanX = np_matrix.mean().tolist()
    mean0 = np_matrix.mean(0).tolist()
    mean1 = np_matrix.mean(1).tolist()
    meanV = [mean0, mean1, meanX]
    return meanV


def var_value(np_matrix):
    variX = np_matrix.var().tolist()
    vari0 = np_matrix.var(0).tolist()
    vari1 = np_matrix.var(1).tolist()
    varValue = [vari0, vari1, variX]
    return varValue


def std_value(np_matrix):
    stdX = np_matrix.std().tolist()
    std0 = np_matrix.std(0).tolist()
    std1 = np_matrix.std(1).tolist()
    stdValue = [std0, std1, stdX]
    return stdValue


def max_value(np_matrix):
    maxX = np_matrix.max().tolist()
    max0 = np_matrix.max(0).tolist()
    max1 = np_matrix.max(1).tolist()
    maxValue = [max0, max1, maxX]
    return maxValue


def min_value(np_matrix):
    minX = np_matrix.min().tolist()
    min0 = np_matrix.min(0).tolist()
    min1 = np_matrix.min(1).tolist()
    minValue = [min0, min1, minX]
    return minValue


def sum_value(np_matrix):
    sumX = np_matrix.sum().tolist()
    sum0 = np_matrix.sum(0).tolist()
    sum1 = np_matrix.sum(1).tolist()
    sumValue = [sum0, sum1, sumX]
    return sumValue


def calculate(list):

    if len(list) != 9:
        # check if the length of list is greater than or less than 9
        # raise an error if length of list is not equal to 9
        raise ValueError("List must contain nine numbers.")
    else:
        # create the dictionary to be returned
        calculation = dict(
            mean="", variance="", standarddeviation="", max="", min="", sum=""
        )
        # convert list to numpy matrix
        np_matrix = np.array(list).reshape(3, 3)

        # calculate & assign the valeus for the keys in the dictionary
        calculation["mean"] = mean_value(np_matrix)
        calculation["variance"] = var_value(np_matrix)
        calculation["standarddeviation"] = std_value(np_matrix)
        calculation["max"] = max_value(np_matrix)
        calculation["min"] = min_value(np_matrix)
        calculation["sum"] = sum_value(np_matrix)

    return calculation
