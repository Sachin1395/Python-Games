result = []
candies=[2,3,5,1,3]
extraCandies=3
def fn():
    for x in range(len(candies)):
        candies[x] += extraCandies
        if candies[x] == max(candies):
            result.append("true")
        elif candies[x] < max(candies):
            result.append("false")
        candies[x] -= extraCandies
    return result
print(fn())