from pykakasi import kakasi
kakasi = kakasi()

def text2InstaDmSmiling(text):
    EMOJI = '^_^'
    little_dashes = "ゔがぎぐげござじずぜぞだぢづでどばびぶべぼ"
    little_dashes_conv = "うかきくけこさしすせそたちつてとはひふへほ"
    little_circle = "ぱぴぷぺぽ"
    little_circle_conv = "はひふへほ"
    small_letter = "ぁぃぅぇぉゃゅょっ"
    small_letter_conv = "あいうえおやゆよつ"
    
    little_dashes_dict = {}
    for i in range(len(little_dashes)):
        little_dashes_dict[little_dashes[i]] = little_dashes_conv[i] + EMOJI
        
    little_circle_dict = {}
    for i in range(len(little_circle)):
        little_circle_dict[little_circle[i]] = little_circle_conv[i] + EMOJI

    small_letter_dict = {}
    for i in range(len(small_letter)):
        small_letter_dict[small_letter[i]] = small_letter_conv[i] + EMOJI
    
    kakasi.setMode('J', 'H') 
    kakasi.setMode('K', 'H')

    conv = kakasi.getConverter()
    text_hiragana = conv.do(text)
    
    text_hiragana = text_hiragana.translate(str.maketrans(little_dashes_dict))
    text_hiragana = text_hiragana.translate(str.maketrans(little_circle_dict))
    text_hiragana = text_hiragana.translate(str.maketrans(small_letter_dict))
    return text_hiragana

if __name__ == "__main__":
    text = "ユーチューブチャンネル「ekkyu.com」。チャンネル登録お願いします！"
    text_instaDmSmiling = text2InstaDmSmiling(text)
    print(text_instaDmSmiling)