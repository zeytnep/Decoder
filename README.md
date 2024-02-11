
This script reads an encoded message from a .txt file and returns its decoded version as a string.
The function can process an input file with the following format:
3 love
6 computers
2 dogs
4 cats
1 I
5 you
In this file, each line contains a number followed by a word. The task is to decode a hidden message based on the arrangement of these numbers into a "pyramid" structure. The numbers are placed into the pyramid in ascending order, with each line of the pyramid having one more number than the line above it. The smallest number is 1, and the numbers increase consecutively, like so:
  1
 2 3
4 5 6
The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line (in this example, 1, 3, and 6). All the other words are ignored. So for the example input file above, the message words are:
1: I
3: love
6: computers

---------------------------

Summary:
This Python script performs the following tasks:

1/Reading a file and creating a dictionary:

2/The make_dictionary function reads data from a specified file, where each line contains a pair of numbers and words separated by whitespace. It creates a dictionary where the numbers serve as keys and the corresponding words serve as values.
Generating a list of specific counts:
The process_decoder_keys function takes the created dictionary and generates a list of specific counts based on the number of pairs in the dictionary.

3/Main function:
~The main function serves as the entry point of the script.~
•It prompts the user to input a file name.
•It calls make_dictionary to create a dictionary from the provided file, process_decoder_keys to obtain a list of specific counts.
•It generates a decoded message by iterating over the decoder key list and retrieving the corresponding words from the dictionary.
•If the decoder key list is empty, it prints an error message (terminal).
