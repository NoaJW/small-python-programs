# Qns: https://inventwithpython.com/bigbookpython/project3.html

# Pattern from https://inventwithpython.com/bitmapworld.txt
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""

print("Enter the message to display with the bitmap.")
while True: 
  msg = input("> ")
  # Validate that msg cannot be empty 
  if msg == "":
    print("Message cannot be empty")
    continue
  else: 
    break

index_ptr = 0 
max_index = len(msg) - 1

# Split bitmap into individual lines in a list
lines = bitmap.splitlines()

for line in lines[2:-1]: 
  # Convert string to list to change it, since string is immutable
  line_list = list(line)

  for index in range(len(line_list)): 
    if line_list[index] == '*':
      line_list[index] = msg[index_ptr]
      index_ptr = (index_ptr + 1) % (max_index + 1)   # Increment the index_ptr. If it exceeds max_index, go back to the start (index 0)

  # Use concatenation and assign new string to line variable 
  line = ''.join(line_list)  

  print(line)

