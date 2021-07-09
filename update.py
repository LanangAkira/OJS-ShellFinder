import os
print("\n\033[32;1mUpdating Wordlist...\n\n\033[0m")
os.system('mv wordlist.txt wordlist_lama.txt')
os.system('wget https://raw.githubusercontent.com/LanangAkira/OJS-ShellFinder/main/wordlist.txt --no-check-certificate')
print("\033[32;1mUpdate Wordlist Success\n\033[0m")
