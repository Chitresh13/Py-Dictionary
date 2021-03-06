import json
from difflib import get_close_matches

data = json.load(open("data.json"))#this locates to json

# main calling function 
def translate(w):
    w = w.lower()#turns to Lowercase
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word didn't exist. Please double check it."
   
# driver code for program
word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
#This Program ends here.
#a book that contains a list of words in alphabetical order and explains their meanings, 
#or gives a word for them in another language; an electronic product giving similar information on a computer, smartphone, 
#etc.: a French-English/English-French dictionary. 
#WELL WELL WELL 
