import random

import nltk
from nltk.corpus import names

male_names = names.words('male.txt')
female_names = names.words('female.txt')

tagged_male_names = [(name, 'male') for name in male_names]
tagged_female_names = [(name, 'female') for name in female_names]

all_tagged_names = tagged_male_names + tagged_female_names

def gender_feature1(name):
    last_letter = name[-1]
    return {
        'last_letter' : last_letter
    }

def gender_feature2(name):
    last_letter = name[-1]
    last_two_letters = name[-2:]
    length = len(name)
    return {
        'last_letter' : last_letter,
        'last_two_letters' : last_two_letters,
        'length' : length
    }

def build_tagged_names(name_list, feature_function):
    tag_list = [(feature_function(name), classd) for (name, classd) in name_list]
    return tag_list
    
def divide_tagged_set(tagged_set):
    set_length = len(tagged_set)/2
    random.shuffle(tagged_set)
    return tagged_set[set_length:], tagged_set[:set_length]

def train_classifier(training_set):
    return nltk.NaiveBayesClassifier.train(training_set)
    
def test_classifier(classifier, test_set, feature_function):
    hits = 0
    for test in test_set:
        expected = classifier.classify(feature_function(test[0]))
        actual = test[1]
        print "tested {} thought it was {} and it was {}. got it right?  {}".format(test[0], expected, actual, (expected == actual))
        if expected == actual:
            hits = hits + 1
    print "accuracy: {}% ".format(100 * (float(hits)/len(test_set)))


feature_function = gender_feature1
training_set_untagged, test_set_untagged = divide_tagged_set(all_tagged_names)
test_set = build_tagged_names(test_set_untagged, feature_function)
training_set = build_tagged_names(training_set_untagged, feature_function)
name_classifier = train_classifier(training_set)






