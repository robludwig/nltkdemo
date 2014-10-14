from nltk import word_tokenize as nltk_tokenize

def my_tokenize(sentence):
    return sentence.split()
    
def compare_tokenizer_results(sentence):
    my_result = my_tokenize(sentence)
    nltk_result = nltk_tokenize(sentence)
    
    if len(my_result) == len(nltk_result):
        print "same result!"
    else:
        print "different results:"
        for mine, nltks in zip(my_result, nltk_result):
            print "\t{}\t{}".format(mine, nltks)

sample_sentences = [
    "This is a relatively easy sentence",
    "This is a sentence you wouldn't think about possibly.",
    "However, NLTK is particular about punctuation.",
]

for sentence in sample_sentences:
    compare_tokenizer_results(sentence)
    print "\n\n\n"
