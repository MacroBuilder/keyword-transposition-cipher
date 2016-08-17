import string

n = int(input())

for _ in range(n):
    ''' Take codeword input, delete duplicate letters '''
    k = [str(i).upper() for i in input().strip()]
    keyword = []
    for i in k:
        if i not in keyword:
            keyword.append(i)
    del k
    re_key = [i for i in keyword]
    num_key = [string.ascii_uppercase.index(i) for i in keyword]
    
    ''' Take cipher text input, build list of lists of cipher word characters '''
    pre_cipher = [str(i) for i in input().split()]
    cipher_list = []
    for i in pre_cipher:
        cipher_list.append([str(j) for j in i])
        
    ''' Alphabet list excluding letters present in keyword '''
    abc = []
    for i in string.ascii_uppercase:
        if i not in keyword:
            abc.append(i)
            
    ''' Split 'abc' into chunks the size of the codeword, append any remaining
        characters, and insert 'keyword' at index zero '''
    abc_split = []
    i, q = 0, len(keyword)
    for _ in range(len(abc) // len(keyword)):
        abc_split.append(abc[i:q])
        i += len(keyword)
        q += len(keyword)
    abc_split.append(abc[q - len(keyword)::])
    abc_split.insert(0, keyword)
    
    ''' Group new sublists by indices, i.e. new sublist at index zero
        is list of all previous subindex zeros '''
    shuffle = []
    while len(abc_split) > 0:
        while any(len(item) < 1 for item in abc_split):
            for thing in abc_split:
                if len(thing) < 1:
                    abc_split.remove(thing)
        shuffle.append([abc_split[index].pop(0) for index in range(len(abc_split))])
    ''' The above leaves an empty list tagged on the end '''
    shuffle.remove(shuffle[-1])
    
    ''' Zip 'num_key' and 'shuffle' and convert to list() to create zip obj instance...
        sorted() works by first element of zipped tuples automatically '''
    ordered_shuffle = sorted(list(zip(num_key, shuffle)))
    re_shuffle = [i[1] for i in ordered_shuffle]
    
    ''' Construct full (old) ascii_upper alphabet list, as well as new cipher-bet '''
    new_alpha = []
    for i in re_shuffle:
        for j in i:
            new_alpha.append(j)
    old_alpha = [i for i in string.ascii_uppercase]

    ''' Convert cipher text to original text '''
    cipher = []
    for i in cipher_list:
        cipher.append([new_alpha.index(j) for j in i])
    orig_text = []
    for i in cipher:
        orig_text.append([old_alpha[j] for j in i])

    ''' Output formatting '''
    final = []
    for index in range(len(orig_text)):
        final.append(''.join(i for i in orig_text[index]))
    print(' '.join(i for i in final))
    
