import random
secret_number = random.randint(1, 10)
total = 0
play_again = "yes"

while play_again == "yes":
        total = 0
        while True:
                if total == 5:
                    print ("No attempts left! You fail.")
                    break
                else: print(f"{5-total} attempts left")


                ans = input("Guess the number 1-10? ")
                if ans == "quit":
                    print("You failed! try again.")
                    print(f"You had {total} attempts!")
                    break

                if ans == "restart":
                    print("hi again")
                    total = 0
                    continue



                ans = int(ans)
                total = total + 1 
                if ans > secret_number:
                    print("too high!")
                elif ans < secret_number:
                    print ("too low!")
                else:
                    print ("Correct!")
                    print(f"You guessed it in {total} attempts!")
                    break    
        play_again = input("would you like to play again?") 
        if play_again == "no":
             break
        else:
             print ("ok!")
             play_again = "yes"




      