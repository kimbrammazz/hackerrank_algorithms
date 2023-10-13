def migratoryBirds(arr):
    # Write your code
    print(arr)
    birds = [0, 0, 0, 0, 0, 0, 0]
    for i in arr:
        print(birds[i])
        birds[i] += 1

    return birds.index(max(birds))
