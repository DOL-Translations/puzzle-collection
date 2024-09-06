import sys

def extract_bytes(output_file, input_file, start_hex, end_hex):
    try:
        start = int(start_hex, 16)
        end = int(end_hex, 16)

        if start >= end:
            print("Error: start position must be less than end position.")
            return
        with open(input_file, 'rb') as infile:
            infile.seek(start)
            data = infile.read(end - start)
        with open(output_file, 'wb') as outfile:
            outfile.write(data)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: extract outputfile inputfile start end")
    else:
        output_file = sys.argv[1]
        input_file = sys.argv[2]
        start_hex = sys.argv[3]
        end_hex = sys.argv[4]
        extract_bytes(output_file, input_file, start_hex, end_hex)
