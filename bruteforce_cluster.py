import string
import hashlib
import os
import ray


def text_to_md5(text):
    encoded_text = hashlib.md5(text.encode())
    return encoded_text.hexdigest()


def generate_text(n, chars):
    if n == 0:
        yield ''
    else:
        pw_list = generate_text(n-1, chars)
        for pw in pw_list:
            for c in chars:
                yield pw + c


@ray.remote
def single_process(initial_text, chars, length, pwd, verbose):
    for i in range(1, length+1):
        print(f"{os.getpid()} is now trying {i} character long")
        for text in generate_text(i, chars):
            combined_text = initial_text + text
            '''
            if verbose:
                print(f"{os.getpid()} of {os.getppid()} is trying {combined_text}\n")
                '''
            if text_to_md5(combined_text) == pwd:
                print(f"The password is {combined_text}")


def main():
    chars = string.ascii_letters + string.digits
    length = 7
    pwd = "16b949fd29d0be4a18dc96f200f027e0"
    verbose = True
    ray.init(address='auto')
    ray.get([single_process.remote(c, chars, length, pwd, verbose) for c in chars])


if __name__ == "__main__":
    main()
