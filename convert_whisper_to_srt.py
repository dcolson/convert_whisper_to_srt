import sys

def convert_format(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        lines = infile.readlines()
        counter = 1
        for line in lines:
            if '-->' in line:
                outfile.write(f"{counter}\n")
                line = line.strip()[1:-1]
                start_time = '00:' + line[0:9]
                end_time = '00:' + line[14:23]
                start_time = start_time.replace('.', ',')
                end_time = end_time.replace('.', ',')
                text = line[26:]
                outfile.write(f"{start_time} --> {end_time}\n")
                outfile.write(text.strip() + '.' +'\n\n')
                counter += 1

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] + '.srt'

    convert_format(input_file, output_file)
