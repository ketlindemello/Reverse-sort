import operator
import pickle
def main():
    # Files
    f = open('alice_in_wonderland.txt', 'r')
    ranked_words_list = rank_words(f)
    f.close()

    alice_in_wonderland_frequency = open('alice_in_wonderland_frequency.txt', 'w')
 
        # Save the results to File
    for w in list(ranked_words_list):
        line = ' '.join(str(x) for x in w)
        alice_in_wonderland_frequency.write(line + '\n')   
    alice_in_wonderland_frequency.close()
    
##        print(w[0],"-->", w[1])

def rank_words(f):

    word_dict = {} 
    words = [] 
    for line in f:
        list_of_words = line.split()



        list_of_char = ['!', '.', ',', ':', '-', '', '`', ';', ')', '(', '*', '"', "?'", "'", '?', '""', ']', '[', "'", '"', '_']
        for w in list_of_words:
            w = ''.join((elem for elem in w if elem not in list_of_char))
            words.append(w.lower()) # Add Word to List
        
 
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1


    output_file = open('alice_wonderland.dat', 'wb')
    pickle.dump(word_dict, output_file)
    output_file.close()


    input_file = open('alice_wonderland.dat', 'rb')
    pb = pickle.load(input_file)
    print(pb)
    input_file.close()

            
        #sort the dictionary and return a list of Tuples
        
    return sorted(word_dict.items(), reverse=True, \
                    key=operator.itemgetter(1))

 
if __name__ == '__main__':
    main()
