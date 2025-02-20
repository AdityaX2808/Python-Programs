def find_zero_sum_triplets(arr):
    n = len(arr)
    triplet = []

    #Brute force to calculate the triplets
    for i in range(n - 2):              #iteration from 0 element to 5 element
        for j in range(i + 1 , n - 1):  #iteration from 1 element to 6 element
            for k in range(j + 1 , n):  #iteration from 2 element to 7 element
                if arr[i] + arr[j] + arr[k] == 0:
                    triplets = [arr[i] , arr[j] , arr[k]]
                    if triplets not in triplet:
                        triplet.append(triplets)

    return (triplet)

#User input for the array
#map(int) object converts the string into integer and list() converts map objects to list
arr = list(map(int , input("Enter the array: ").split()))   

#using the function to find triplet
triplet = find_zero_sum_triplets(arr)

#If triplet are found print it or else show no output
if triplet:
    print("Triplets that sum to 0 are: ")
    for triplets in triplet:
        print(triplets)
else:
    print("There exist no such triplet")        