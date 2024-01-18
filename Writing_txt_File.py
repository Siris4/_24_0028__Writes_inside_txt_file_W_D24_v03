with open("my_file.txt", mode="a") as file:
    contents = file.write("\nanything you want to write here will be appended to the original contant already in the txt file")
    print(contents)
#anything you want to write here
#anything you want to write here