def single_root_words(root_word, *other_words):
    same_words=[]
    for i in range(len(other_words)):
        if root_word.upper() in other_words[i].upper():
            same_words.append(other_words[i])
        else:
            if other_words[i].upper() in root_word.upper():
                same_words.append(other_words[i])
            else:
                continue
    print(*same_words)
single_root_words('мир',"Мировой","Шикарный","Мирный","Архивный","ир")
single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
