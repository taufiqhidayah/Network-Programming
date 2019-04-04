import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-prime", type=int,help="increase output verbosity")
parser.add_argument("-sum", type=int,help="increase output verbosity")



args = parser.parse_args()
answer = args.square**2
jwb = args.square /args.square

if args.prime == 2:
    print "the square of {} equals {}".format(args.square, jwb)
elif args.prime == 1:
    print "{}^2 == {}".format(args.square, jwb)
elif args.sum:
    print "{}== {}".format(args.square, answer)
