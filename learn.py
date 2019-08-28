import gtlearn,argparse

parser = argparse.ArgumentParser(description='learn new texts')
parser.add_argument('filename', type=str, help='Input file to learn')
args = parser.parse_args()
if args.filename != None:
    model = gtlearn.gentext()
    model.init()

    model.learn(args.filename)

    model.save()
