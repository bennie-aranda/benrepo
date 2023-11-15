def main():
    while True:
        print("choose a number?")
        x = int(input())

        if x > 2:
            print(x, " is greater than 2!")

        elif x < 2: 
            print(x, " is less than 2!")
        
        else: 
            print(x, " is equal to ", x)

        restart = input("Do you want to run the program again? (y/n)")
        if restart.lower() != 'y':
            print("thank you for playing along!")
            print("")
            break
     
if __name__ == "__main__":
    main()   
