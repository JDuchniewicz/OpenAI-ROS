import matplotlib.pyplot as plt
import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help="the name of file with the results", required=True)
    args = parser.parse_args()

    data = []
    with open(args.f, 'r') as f:
        data = list(json.load(f).items())

    # decode the results file
    scores = data[3][1]
    plt.style.use('ggplot')
    plt.xlabel("Episodes")
    plt.ylabel("Score")
    plt.plot(scores)
    plt.show()

if __name__ ==  "__main__":
    main()
