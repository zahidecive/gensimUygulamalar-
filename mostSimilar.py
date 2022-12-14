#Most Similar Example

from gensim.models import KeyedVectors

kelimeVektoru = KeyedVectors.load_word2vec_format('trModel100', binary=True)

def benzerKelimeler():

    anahtarKelime = input("Anahtar Kelime: ").lower()
    print("Anahtar Kelime : "+ str(anahtarKelime))
    oneriler = (kelimeVektoru.most_similar(positive=anahtarKelime))

    print(oneriler)
    for index, oneri in enumerate(oneriler):
        print(index+1, oneri[0])

        for i in range(3):
            onerilenKelime = oneriler[i][0]
            print('https://www.google.com.tr/search?q='+onerilenKelime)


benzerKelimeler()