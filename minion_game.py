#!/usr/bin/env python3

original_vowels = list('AEIOU')
with open('test.txt','r') as fi:
    ss = fi.read()

consonants = list(set([x for x in ss if x not in original_vowels]))
vowels =  list(set([x for x in ss if x in original_vowels]))
vowels_c_dict = {v:ss.count(v) for v in vowels}
consonants_c_dict = {c:ss.count(c) for c in consonants}
print('consonanats {} and vowels {} with count'.format(consonants_c_dict,vowels_c_dict))
def occurrences(sub):
    """
    This function count overlapping substring occurrences.
    It takes the string and substring as argument and return the number of time the give substring 
    ocurrent in the string considering overlapping occurrences too.
    """
    string = ss
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count


def substring_builder(char,char_count):
    """
    This function builds a list of non-repeating words that start with vowels and consonants
    It takes base string from which vowels and consonats are extracte and list of vowels or consonants
    It returns list of words that strat with vowel if given list of vowel or consonat characters if given consonant characters
    """
    s=ss
    words=[]
    if char_count>=1:
        for counter in range(char_count):
            print(s)
            temp = ''
            for c in s[s.index(char):]:
                temp=temp+c
                words.append(temp)
            if s.index(char)==0:
                s=s[1:]
            else:
                s=s[:s.index(char)]+s[s.index(char)+1:]
    return {char:list(set(words))}
    # words = []
    # l = len(s)
    # print(letters_list)
    # for i,c in enumerate(letters_list):
    #     for i in range(l+1):
    #         print('index',i,'character',c)
    #         words.append(s[s.index(c):i+1])
    #         print(words)
    #     s=s[0:s.index(c)]+s[s.index(c)+1:]
    #     print(s) 
    # s=''
    # letters_list=[]
    # return list(filter(lambda x:x!='',words))

cons_result = [substring_builder(key,val) for key,val in consonants_c_dict.items()]
vowels_result = [substring_builder(key,val) for key,val in vowels_c_dict.items()]
kevin =sum( {j:occurrences(j) for x in vowels_result for i in x.values() for j in i}.values())
stuart = sum([occurrences(j) for x in cons_result for i in x.values() for j in i])

print(vowels_result)
print(kevin)
# consonant_words = substring_builder(ss,consonants)
# consonant_words_result = sum({word: (occurrences(ss,word)) for word in list(set(consonant_words))}.values())
# #vowel_words = substring_builder(ss,vowels) 
# #vowels_words_result = sum({word: (occurrences(ss,word)) for word in list(set(vowel_words))}.values())
# if kevin > stuart:
#    print('Kevin',kevin)
# else:
#    print('Stuart',stuart)