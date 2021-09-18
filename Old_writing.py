import time

words={
    'crucial':'極めて重要な',
    'subseqent':'その後の',
    'devise':'考案する',
    'strain':'負担',
    'distinct':'明確な',
    'incorporate':'取り入れる',
    'eliminate':'なくす',
    'retain':'記憶する，維持する',
    'disturb':'邪魔する不安にさせる'
}
print('単語の意味を教える')
while True:
    word=input('単語を入力してくれめんす>>>')
    if word=='ok':
        print('good bye')
        break
    elif word in words:
        # リストの中のキーにアクセス
        print(words[word]+'>>っていう意味\n')
    else:
        print('分からん')
        meaning=input('意味を教えてくれ>>>')
        while not meaning:
            meaning=input('意味を教えてくれ>>>')
        words[word]=meaning
        print('記憶中...')
        time.sleep(3)

