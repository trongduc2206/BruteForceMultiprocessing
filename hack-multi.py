import hashlib
import itertools
import multiprocessing


def hack():
    user = 'bolormaa'
    salt = 'cd124a4d388c17e3'
    hashed_pw = 'd873d3ac8c8450ef6e35a4b8acc649dd'

    alphanumeric = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for length in range(1, 9):
        # for guess in itertools.product(numeric, repeat=length):
        print("length ", length)
        for guess in itertools.product(alphanumeric, repeat=length):
            guess = ''.join(guess)
            # print(' guess: ' + guess)
            string = "potPlantSalt" + guess + salt
            byte_string = bytes(string, 'ascii')
            b = hashlib.sha256(byte_string).hexdigest()
            if b[0:32] == hashed_pw:
                print("-------------------- Success: user " + user + " has pw " + guess)
                return


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pool.map(hack(), range(0, 10))
    pool.close()
