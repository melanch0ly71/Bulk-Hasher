# Bulk-Hasher
Hashes large and complex .txt files in bulk quickly and efficiently 
STEP 1 : Once you install bulkhasher.py and the wordlist rockyou.txt, simply transfer them to the same folder and open bash terminal (powershell, cmd) in that folder. 
STEP 2 : write the following piece of code in the terminal : _python bulkhasher.py -i rockyou.txt -o hashedfile.txt -a sha256_
If you have another dictionary or text file rather than rockyou.txt then enter that file's name but make sure its in the same directory and after -a write your desired hashing algorithm such as **md5, sha12, sha256, sha512**.
