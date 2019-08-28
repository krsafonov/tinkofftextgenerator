import gtmodel, argparse, random

model = gtmodel.gentext()
model.init()

parser = argparse.ArgumentParser(description='Generate new text')
parser.add_argument('length', type=int)
args = parser.parse_args()

if args.length > 0:
    print("Сгенерирована последовательность на основе", model.allwordsquantity, "слов")
    word = model.get_random_word()
    first_word = word[0].upper() + word[1:]
    print(first_word,end = " ")
    for i in range(args.length-1):
        word = model.data[word].random()
        print(word, end = " ")
