# python3


def build_heap(data, n):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    for i in range(n, 1, -1):
        #print("For: ", data)
        while data[i-1] < data [(i//2)-1]:
            data[i-1], data[(i//2)-1] = data[(i//2)-1], data[i-1]
            swaps.append(((i//2) -1, i-1))
            i = i // 2
            #print("while: ", data)
            if i == 1:
                break

    #print(swaps)            
    return swaps
 

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    text = input("I vai F: ")
    if "I" in text[:1]:
        n = int(input("cipars: "))
        # input from keyboard
        data = list(map(int, input().split()))
    elif "F" in text[:1]:
        filename = "tests/" + input("Fails: ")
        file = open(filename, "r")
        n = int(file.readline())
        data = file.readline()
        data = list(map(int, data.split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data, n)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
