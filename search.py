import sha
import sys
import getpass

if len(sys.argv) >= 2:
    password = " ".join(sys.argv[1:])
else:
    password = getpass.getpass("Give a password to check for: ")

sha_object = sha.new(password)
upper_hash = sha_object.hexdigest().upper()
print("SHA-1 hash: %s" % upper_hash)
upper_hash_len = len(upper_hash)

with open("pwned-passwords-ordered-by-count.txt") as f:
    for line in f:

        if line.startswith(upper_hash):
            line = line.strip()
            print("Seen %s times" % line.split(":")[1])
            break
