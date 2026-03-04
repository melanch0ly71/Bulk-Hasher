import hashlib
import argparse

def hash_text(text, algorithm):
    text = text.strip().encode('utf-8')
    
    if algorithm == "md5":
        return hashlib.md5(text).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(text).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(text).hexdigest()
    elif algorithm == "sha512":
        return hashlib.sha512(text).hexdigest()
    else:
        raise ValueError("Unsupported algorithm")

def main():
    parser = argparse.ArgumentParser(description="Bulk Text to Hash Converter")
    parser.add_argument("-i", "--input", required=True, help="Input file path")
    parser.add_argument("-o", "--output", required=True, help="Output file path")
    parser.add_argument("-a", "--algorithm", required=True,
                        choices=["md5", "sha1", "sha256", "sha512"],
                        help="Hash algorithm")

    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as infile, \
         open(args.output, "w", encoding="utf-8") as outfile:
        
        for line in infile:
            hashed = hash_text(line, args.algorithm)
            outfile.write(hashed + "\n")

    print("Hashing completed successfully.")

if __name__ == "__main__":
    main()