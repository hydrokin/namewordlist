import itertools

def generate_wordlist(length):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'

    if length % 2 != 0:
        print("Uyarı: Verilen uzunluk çift bir sayı olmalıdır.")
        return

    wordlist = []

    total_permutations = len(vowels) ** (length // 2) * len(consonants) ** (length // 2)
    processed_permutations = 0

    with open("wordlist.txt", "w") as file:
        for vowel_permutation in itertools.permutations(vowels, length // 2):
            for consonant_permutation in itertools.permutations(consonants, length // 2):
                word = ''.join(''.join(pair) for pair in zip(consonant_permutation, vowel_permutation))
                wordlist.append(word)
                file.write(word + "\n")

                processed_permutations += 1
                progress_percentage = (processed_permutations / total_permutations) * 100
                print(f"İşlem tamamlandı: %{progress_percentage:.2f}", end='\r')

    print("\nKelime listesi 'wordlist.txt' dosyasına kaydedildi.")

    return wordlist

if __name__ == "__main__":
    word_length = int(input("Oluşturulacak kelime uzunluğunu girin (çift bir sayı): "))

    if word_length % 2 == 0:
        wordlist = generate_wordlist(word_length)
    else:
        print("Uyarı: Verilen uzunluk çift bir sayı olmalıdır.")
