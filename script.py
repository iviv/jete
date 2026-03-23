import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--text', required=True)
parser.add_argument('--choice', required=True)
args = parser.parse_args()

print(f"Text input: {args.text}")
print(f"Choice input: {args.choice}")
print("hello, world!")

# your logic here

print("checking pipeline stages!")

print("checking if it works when i'm not paying attention!")


