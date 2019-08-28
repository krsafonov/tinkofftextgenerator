import gtlearn, argparse, random

model = gtlearn.gentext()
model.init()

parser = argparse.ArgumentParser(description='Videos to images')
parser.add_argument('length', type=int)
args = parser.parse_args()

if args.length > 0:
    word = random.choice(list(model.data.keys()))
    print(word, end = " ")
    for i in range(args.length-1):
        word = random.choice(list(model.data[word]))
        print(word, end = " ")
