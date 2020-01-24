def interface():
    choice = 0
    #while choice != 9:
    while True:
        print("Cholesterol Calculator")
        print("Options: ")
        print(" 9 - Quit")
        choice = input("Enter your option: ")
        if choice == '9':
            return
        
if __name__ == "__main__":
    interface()