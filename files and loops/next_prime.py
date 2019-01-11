def isprime(num):
    if num > 1:
   # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               return False

       return True

 #if input number is less than
 #or equal to 1, it is not prime
    else:
       return False

def next_prime(user_number):
    while True:
        user_number+=1
        if isprime(user_number):
            return user_number

def start_next_prime(num):
    next_value = next_prime(num)
    print(next_value)
    while True:
        user_con = input("Do you want to continue? y/n ")
        user_con = user_con.lower()
        if user_con == 'n' or user_con == 'no':
            break;
        elif user_con == 'y' or user_con == 'yes':
            next_value = next_prime(next_value)
            print(next_value)

        else:
            print('invalid command, enter y or n')
            # break
    return "That ends it!"

replay = True
while replay:
  user_input = input("Enter a number: ")
  try:
    user_input = int(user_input)
    print(start_next_prime(user_input))
    replay = False
  except:
    print('try again with a number')

# handle errors
# perfect square - plus something
# guess number plus random
