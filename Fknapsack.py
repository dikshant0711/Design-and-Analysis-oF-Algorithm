def fracKnapsack(wt,val,W):
    n = len(wt)
    if n == 0:
        return 0
    else:
        maxRatioIndex = -1
        maxRatio = -1
        for i in range(n):
            if val[i]/wt[i] > maxRatio:
                maxRatioIndex = i
                maxRatio = val[i]/wt[i]
    maxVal = maxRatio*W
    return maxVal
   
print("Enter the values :")
val = list(map(int,input().split(' ')))
print("Enter the weights :")
wt = list(map(int,input().split(' ')))
W = int(input("Enter the maximum capacity :"))
print("The answer is :",fracKnapsack(wt, val, W))