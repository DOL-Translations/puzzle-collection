import sys

def extract_bytes(output_file, input_file, start_hex, end_hex):
    try:
        # Convert start and end from hex to integers
        start = int(start_hex, 16)
        end = int(end_hex, 16)
        
        # Check if start is less than end
        if start >= end:
            print("Error: start position must be less than end position.")
            return
        
        # Open the input file in binary mode and read the specified range
        with open(input_file, 'rb') as infile:
            infile.seek(start)  # Move to the start position
            data = infile.read(end - start)  # Read the specified range of bytes

        # Write the extracted data to the output file
        with open(output_file, 'wb') as outfile:
            outfile.write(data)
        
        print(f"Successfully extracted bytes from {start_hex} to {end_hex} into {output_file}")
    
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
