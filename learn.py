import gtmodel,argparse

parser = argparse.ArgumentParser(description='learn new texts')
parser.add_argument('filename', type=str, help='Input file to learn')
args = parser.parse_args()
if args.filename != None:
    model = gtmodel.gentext()
    model.init()

    model.learn(args.filename)

    model.save()

    print("Quantity of words", model.allwordsquantity)
