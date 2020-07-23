#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    permutations = []
    options = [["rock"], ["paper"], ["scissors"]]
    def play(played, n):

        # base case
        if n == 0:
            permutations.append(played)
            return
        else:
            # recurse to n - 1 and play the 3 options
            return play(played + options[0], n-1), play(played + options[1], n-1), play(played + options[2], n-1) 

    play([], n)
    return permutations    

      # below are all the false starts i had while working on this

# def rock_paper_scissors(n):
#   # Your code here
#   options = ['rock', 'paper', 'scissors']
#   # all possible combos will be saved here
#   permutations = []

#   def play(played, rounds):
#         if rounds == 0:
#               permutations.append(played)
#               return
#         i = 3
#         while i >= 0:
#               i -= 1
#               played.append(options[i])
#               play(played, rounds - 1)
              

#   play([], n)   
#   return permutations   



# def rock_paper_scissors(n):
      
#     # Your code here
#     options = ['rock', 'paper', 'scissors']
#     # all possible combos will be saved here
#     permutations = []

#     def play(played, n):
#         if n == 0:
#               permutations.append(played)
#         else: 
 
#               round_options = options[:]
              
#               i = 3
#               while i > 0:
#                     if i == 1:
#                           permutations.append(played)
#                     else:
#                           i -= 1
#                           chosen = round_options.pop()
#                           played.append(chosen)
#                           play(played, n - 1)
                  

#     play([], n)   
#     return permutations        

# def rock_paper_scissors(n):
#     permutations = []
#     def play(played, n):
           
#         # base case
#         if n == 0:
              
#             permutations.append[played]
#             return
#         else:
          
#             play(played.append("rock"), n-1)
#             play(played.append("scissors"), n-1)
#             play(played.append("paper"), n-1)

#     play(["rock"], n)
#     play(["paper"], n)
#     play(["scissors"], n)
#     return permutations

    
          


if __name__ == "__main__":
    n = 2  
    print(rock_paper_scissors(n))
  # if len(sys.argv) > 1:
  #   num_plays = int(sys.argv[1])
  #   print(rock_paper_scissors(num_plays))
  # else:
  #   print('Usage: rps.py [num_plays]')