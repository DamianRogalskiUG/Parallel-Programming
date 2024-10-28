import sys
import os
import re

def main_func(beginning_filename, searched_word):
    word_count = 0
    children_pid = []
    try:
        with open(beginning_filename, "r") as file:
            for line in file:
                input_match = re.match(r'\\input\{(.+)\}', line.strip())
                if input_match is not None:
                    included_filename = input_match.group(1)
                    pid = os.fork()
                    if pid == 0:
                        count = main_func(included_filename, searched_word)
                        sys.exit(count)
                    else:
                        children_pid.append(pid)
                else:
                    word_count += len(re.findall(r'\b' + re.escape(searched_word) + r'\b', line))

    except FileNotFoundError:
        print("error")

    for pid in children_pid:
        pid, status = os.waitpid(pid, 0)
        word_count += os.WEXITSTATUS(status)

    return word_count



if __name__ == "__main__":
    first_file_name = sys.argv[1]
    searched_word = sys.argv[2]
    main_func(first_file_name, searched_word)
    total_count = main_func(first_file_name, searched_word)
    print(f"Liczba wystąpień słowa '{searched_word}': {total_count}")
