import re
from nltk import sent_tokenize as nltk_tokenize

def my_tokenize(paragraph):
    return paragraph.split('.')

def my_tokenize2(paragraph):
    punct_regex = "[\\.\\?\\!]"
    return re.split(punct_regex, paragraph)



sample_paragraphs = [
  "This is a simple paragraph. It's composed of short sentences I wrote. I like this paragraph quite a bit. Don't you?",
  "I agree with Mr. Wu and Mrs. Jenkins, this is a more difficult paragraph. Even in the U.S.A., approximately 4.5% of paragraphs can be difficult to tokenize. Can you do it?",
  "Does NLTK get tripped up from time to time? Let's look in Apt. #2 for a quick estimation. what about sentences that aren't properly capitalized?"
 ]

 
 def test_tokenizer(tokenizer):
    for para in sample_paragraphs:
        print tokenizer(para)

for tokenizer in [my_tokenize, my_tokenize2, nltk_tokenize]:
    test_tokenizer(tokenizer)