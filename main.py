meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "Ayn": "Aynen kelimesinin kısaltılmış hâlidir. Bir cümle bile yazmaya üşenenler, aynen yerine sıkça kullanır.",
            "Ez": "Genelde sosyal medya aleminde kolay, basit ve yapması zorlamayan anlamında kullanılır.",
            }

word = input("Bilmediğin bir kelime varsa buara yaz burda herşey ez):")
if word in meme_dict.keys():

    print(meme_dict[word])
else:
    
    print("Adamım bu çok zor başka kelime seç")
