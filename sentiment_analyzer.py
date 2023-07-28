punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(s):
    for c in s:
        if c in punctuation_chars:
            s= s.replace(c,'')
    return s
    
def get_pos(string):
    ct = 0
    lst_string = string.split()
    for wrd in lst_string:
        wrd = strip_punctuation(wrd)
        if wrd.lower() in positive_words:
            ct+=1
    return ct
    
def get_neg(string):
    ct2 = 0
    lst_string = string.split()
    for wrd in lst_string:
        wrd = strip_punctuation(wrd)
        if wrd.lower() in negative_words:
            ct2+=1
    return ct2
    
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        negative_words.append(lin.strip())
        
f1 = open('twitter_data.csv','r')
f2 = open('resulting_data.csv','w')
f2.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')
for lin in f1.readlines()[1:]:
    wrds = lin.split(',')
    retweets = wrds[1]
    replies = wrds[2].strip()
    p_score = get_pos(wrds[0])
    n_score = get_neg(wrds[0])
    net_score = p_score - n_score
    f2.write('{},{},{},{},{}\n'.format(retweets,replies,p_score,n_score,net_score))
