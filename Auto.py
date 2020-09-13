#code will be uploaded here
import re
from collections import Counter
import numpy as np
import pandas as pd
from collections import Counter

def process_data(file_name):
    
    words = [] # return this variable correctly

   
    with open(file_name) as f:
        file_name_data = f.read()
    file_name_data=file_name_data.lower()
    words = re.findall(r'\w+',file_name_data)
   
    
    return words
  
word_l = process_data('shakespeare.txt')
vocab = set(word_l)  # this will be your new vocabulary
print(f"The first ten words in the text are: \n{word_l[0:10]}")
print(f"There are {len(vocab)} unique words in the vocabulary.")

def get_count(word_l):
   
    
    word_count_dict = {}  # fill this with word counts
  
#     for word in word_l:
#         if word in word_count_dict:
#             word_count_dict[word]+=1
#         else:
#             word_count_dict[word]=1
    word_count_dict = Counter(word_l)        
   
    return word_count_dict
  
  
word_count_dict = get_count(word_l)
print(f"There are {len(word_count_dict)} key values pairs")
print(f"The count for the word 'thee' is {word_count_dict.get('thee',0)}")
      
      
 def delete_letter(word, verbose=False):
    
    
    delete_l = []
    split_l = []
    
   
#     split_l=[(word[:i],word[i:]) for i in range(len(word)+1)]
#     delete_l=[l+r[1:] for l,r in split_l if r]
    for c in range(len(word)):
        split_l.append((word[:c],word[c:]))
    for a,b in split_l:
        delete_l.append(a+b[1:]) 
  

    if verbose: print(f"input word {word}, \nsplit_l = {split_l}, \ndelete_l = {delete_l}")

    return delete_l
delete_word_l = delete_letter(word="cans",
                        verbose=True)
 
def switch_letter(word, verbose=False):
     
    
    switch_l = []
    split_l = []
    len_word=len(word)
    
    for c in range(len_word):
        split_l.append((word[:c],word[c:]))
    switch_l = [a + b[1] + b[0] + b[2:] for a,b in split_l if len(b) >= 2] 
    
    
    if verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nswitch_l = {switch_l}") 

    return switch_l
   
 switch_word_l = switch_letter(word="eta",
                         verbose=True)
      
      
 def replace_letter(word, verbose=False):
    
    
    letters = 'abcdefghijklmnopqrstuvwxyz'
    replace_l = []
    split_l = []
    rep=[]
   
    
#     split_l=[(word[:i],word[i:]) for i in range(len(word)+1)]
#     replace_set= [letter+l+r[1:] for l,r in split_l if l and r for letter in letters]
#     replace_set=set(replace_set)
#     replace_set.discard("can")
#     for l in letters:
#         a=str(l)
#         for i in range(len(word)):
#             b=str(word[i])
#             c=word.replace(b,a)
#             rep.append(c)
#     replace_set=set(rep)      
#     replace_set.discard("can")
    for c in range(len(word)):
        split_l.append((word[0:c],word[c:]))
    replace_l = [a + l + (b[1:] if len(b)> 1 else '') for a,b in split_l if b for l in letters]
    replace_set=set(replace_l)    
    replace_set.remove(word)
   
    
    # turn the set back into a list and sort it, for easier viewing
    replace_l = sorted(list(replace_set))
    
    if verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nreplace_l {replace_l}")   
    
    return replace_l   
   
 def insert_letter(word, verbose=False):
    
    letters = 'abcdefghijklmnopqrstuvwxyz'
    insert_l = []
    split_l = []
    
   
#     split_l=[(word[:i],word[i:]) for i in range(len(word)+1)]
#     insert_l=[l+letter+r for l,r in split_l for letter in letters]
    for c in range(len(word)+1):
        split_l.append((word[0:c],word[c:]))
    insert_l = [ a + l + b for a,b in split_l for l in letters]
   

    if verbose: print(f"Input word {word} \nsplit_l = {split_l} \ninsert_l = {insert_l}")
    
    return insert_l
      
  def edit_one_letter(word, allow_switches = True):
   
    
    edit_one_set = set()
    
   
    edit_one_set.update(delete_letter(word))
    if allow_switches:
        edit_one_set.update(switch_letter(word))
    edit_one_set.update(replace_letter(word))
    edit_one_set.update(insert_letter(word))


    return edit_one_set  
      
      
   def edit_two_letters(word, allow_switches = True):
    
    
    edit_two_set = set()
    
   
    edit_one = edit_one_letter(word,allow_switches=allow_switches)
    for w in edit_one:
        if w:
            edit_two = edit_one_letter(w,allow_switches=allow_switches)
            edit_two_set.update(edit_two)
    
    return edit_two_set
      
    print( [] and ["a","b"] )
print( [] or ["a","b"] )
#example of Short circuit behavior
val1 =  ["Most","Likely"] or ["Less","so"] or ["least","of","all"]  # selects first, does not evalute remainder
print(val1)
val2 =  [] or [] or ["least","of","all"] # continues evaluation until there is a non-empty list
print(val2)
      
def get_corrections(word, probs, vocab, n=2, verbose = False):
    
    
    suggestions = []
    n_best = []
    
    
    suggestions = list((word in vocab and word) or edit_one_letter(word).intersection(vocab) or edit_two_letters(word).intersection(vocab))
    n_best = [[s,probs[s]] for s in list(reversed(suggestions))]
   
    
    if verbose: print("suggestions = ", suggestions)

    return n_best
   
      
     #### TEST YOUR MODEL #### 
 my_word = "hry " 
tmp_corrections = get_corrections(my_word, probs, vocab, 2, verbose=True)
for i, word_prob in enumerate(tmp_corrections):
    print(f"word {i}: {word_prob[0]}, probability {word_prob[1]:.6f}")


print(f"data type of corrections {type(tmp_corrections)}")
      
      
