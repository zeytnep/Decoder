def make_dictionary(message_file):
    dictionary_data = {}
    with open(message_file, 'r') as file:
        for line in file:
            number, word = line.split()
            dictionary_data[int(number)] = word

    return dictionary_data


def process_decoder_keys(dictionary_data):

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
    print("This is the main function.")
    dictionary_data = make_dictionary('message.txt')
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
