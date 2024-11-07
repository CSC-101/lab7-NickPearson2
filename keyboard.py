import convert
def gather_numbers()->list[float]:
    list = []
    while True:
        num = input("Enter a number: ")
        if(num.lower() == "done"):
            break
        num = convert.str_to_float(num)
        if (num != None):
            list.append(num)
        else:
            print("Please enter a valid number.")
    return list
if __name__ == '__main__':
    list = gather_numbers()
    total = 0
    for num in list:
        total+=num
    print(total)