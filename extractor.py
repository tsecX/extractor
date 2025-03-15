import re
import argparse
import time

def extract_usernames(text, extract_type):
    if extract_type == "emails":
        pattern = re.compile(r'\b[A-Za-z]+\.[A-Za-z]+@[\w\.]+\b')
    elif extract_type == "usernames":
        pattern = re.compile(r'\b[A-Za-z]+\.[A-Za-z]+\b')
    else:
        print("\033[91m[x]Error: Invalid extract_type. Choose 'emails' or 'usernames'.\033[0m")
        exit(1)
    
    matches = pattern.findall(text)
    return matches

def main():
    try:
        parser = argparse.ArgumentParser(description="Extract usernames or valid emails from a file.")
        parser.add_argument("input_file", help="Path to the input file")
        parser.add_argument("output_file", help="Path to the output file")
        parser.add_argument("--type", choices=["emails", "usernames"], required=True, help="Specify extraction type: 'emails' or 'usernames'")
        args = parser.parse_args()
        
        with open(args.input_file, "r", encoding="utf-8") as file:
            text = file.read()
        
        extracted_data = extract_usernames(text, args.type)
        
        with open(args.output_file, "w", encoding="utf-8") as file:
            for item in extracted_data:
                file.write(item + "\n")
        
        print("[*]Extracting data...")
        time.sleep(1)
        print(f"\033[92m[+]Extracted {len(extracted_data)} {args.type} and saved to {args.output_file}\033[0m")
    except FileNotFoundError:
        print("\033[91m[x]Error: The specified input file does not exist.\033[0m")
    except PermissionError:
        print("\033[91m[x]Error: Permission denied when accessing files.\033[0m")
    except Exception as e:
        print(f"\033[91m[!]An unexpected error occurred: {e}\033[0m")

if __name__ == "__main__":
    main()
