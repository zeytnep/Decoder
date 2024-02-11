def make_dictionary(message_file):
    # Initialize an empty dictionary to store number-word pairs
    dictionary_data = {}
    try:
        # Open the specified file in read mode
        with open(message_file, 'r') as file:
            for line in file:
                number, word = line.split()
                dictionary_data[int(number)] = word
    except FileNotFoundError:
        # Handle the case where the specified file is not found
        print("File not found.")
    except IOError:
        # Handle other I/O errors
        print("Error reading the file.")
    except Exception as e:
        # Handle unexpected errors
        print("An unexpected error occurred:", str(e))

    return dictionary_data


def process_decoder_keys(dictionary_data):
    
    # Determine the number of pairs in the dictionary
    num_pairs = len(dictionary_data)
    # Initialize the list of specific counts
    specific_counts = []

    x = 1
    y = 2
    specific_counts.append(x)

    while x < num_pairs:
        x = x + y 
        specific_counts.append(x)
        y = y + 1
        if x+y > num_pairs:
            break
    return specific_counts

# Main function /entry point
def main():
    # Prompting the user to input a file name
    filename = input("Please enter the file name: ").strip()

    dictionary_data = make_dictionary(filename)
    decoder_key_list = process_decoder_keys(dictionary_data);
    decoded_message = ""

    if not decoder_key_list:
        #Error handling
        print("The list is empty")
    else:
        for num in decoder_key_list:
            if num in dictionary_data:
                decoded_message += dictionary_data[num] + " "

    print(decoded_message)

# Call the main function
main()
