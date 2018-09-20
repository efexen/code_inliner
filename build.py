import re
import sys

MATCH_REGEX = re.compile('{{(.+\..+)}}')

def readFileContents(filename):
    with open(filename, "r") as datafile:
        return datafile.read()

def processLine(line):
    match = re.match(MATCH_REGEX, line)

    if match:
        return re.sub(MATCH_REGEX, readFileContents(match.group(1)), line)
    else:
        return line

def main():
    if len(sys.argv) < 3:
        print("Usage: python " + __file__ + " <input_file> <output_file>")
        return

    fname = sys.argv[1]
    outname = sys.argv[2]

    contents = ''.join([processLine(line) for line in open(fname, 'r')])

    with open(outname, 'w') as outfile:
        outfile.write(contents)

main()
