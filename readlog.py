# Function to convert keylog file to readable format
def convert_log_to_readable(log_file, output_file):
    with open(log_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        for line in lines:
            key = line.strip().replace("'", "")
            if key.startswith("Key."):
                key = key.split(".")[1].upper()
            f.write(key + " ")

# Convert the keylog.txt to readable_log.txt
convert_log_to_readable('keylog.txt', 'readable_log.txt')
