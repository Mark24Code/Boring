def replace_str(paragrah,word1,word2):
    tmp = paragrah.split(word1)
    return '%s'%(word2).join(tmp)

print(replace_str('123 44 55 44','44','word2'))