from nltk import word_tokenize, pos_tag

tags = {
    #nltk.help.upenn_tagset()
'N' : "noun",
'J' : "adjective",
'V' : "verb",
'D' : "determiner"
}

def tag_sentence(sentence):
    return pos_tag(word_tokenize(sentence))


def read_tagged_sentence(tag_list):
    for tag_pair in tag_list:
        explanation = ""
        if tags.get(tag_pair[1][0]):
            explanation = "which is a {}".format(tags[tag_pair[1][0]])
        print "{0} is a {1} {2}".format(tag_pair[0], tag_pair[1], explanation)


