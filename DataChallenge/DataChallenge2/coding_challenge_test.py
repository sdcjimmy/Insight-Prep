def merge_two_list_helper(list1, list2):
    #NOTE: YOU CAN NOT USE ANY SORTING LIBRARIES
    #YOUR CODE GOES HERE


    return None


#DO NOT CHANGE THIS FUNCTION
def merge_two_list(list1,list2):
    return merge_two_list_helper(list1, list2)


#test cases
def main():
    list1 = [1,3,5]
    list2 = [2,4,6]
    print ("merging [1,3,5] and [2,4,6]......")
    print ("expected result is [1,2,3,4,5,6]")
    print ("your output is {}".format(merge_two_list(list1, list2)))

if __name__ == "__main__":
    main()