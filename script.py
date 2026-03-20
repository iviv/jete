import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--text', required=True)
parser.add_argument('--choice', required=True)
args = parser.parse_args()

print(f"Text input: {args.text}")
print(f"Choice input: {args.choice}")

# your logic here
