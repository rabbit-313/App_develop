import logging


logging.basicConfig(level=logging.INFO, filename='example.log', format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    sum = 0
    answer = "y"
    while answer != "n":
        num_input = int(input("Enter number: "))
        sum += num_input
        logging.info("The sum of input is {}".format(sum))
        print("Do you want to continue? (y/n)")
        answer = input()
if __name__ == "__main__":
    main()
