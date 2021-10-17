# A Fizz-Buzz approach using generators and avoiding modulo operations because - why not!

def gen_fizz(freq):
    '''Generates freq-1 numbers followed by a "fizz" '''
    num = 0
    while True:
        for _ in range(freq-1):
            num += 1
            yield num
        num += 1 # even if we don't output the number, we still need to increment
        yield "fizz"


def gen_buzz(freq_fizz, freq):
    '''Generates freq - 1 outputs of the fizz generator, followed by a "buzz" '''
    fizz = gen_fizz(freq_fizz)
    while True:
        for _ in range(freq-1):
            yield next(fizz)
        _ = next(fizz)  # don't yield, but still generate
        yield "buzz"
        

def gen_fizzbuzz(freq_fizz, freq_buzz):
    '''Generates freq - 1 outputs of the buzz generator, followed by a "fizzbuzz" '''
    buzz = gen_buzz(freq_fizz, freq_buzz)
    while True:
        for _ in range(freq_fizz * freq_buzz - 1):
            yield next(buzz)
        _ = next(buzz) # don't yield, but still generate
        yield "fizzbuzz"
        
        
if __name__=="__main__":
    fizz_frequency = 3
    buzz_frquency = 5
    rounds = 100
    fizzbuzz = gen_fizzbuzz(fizz_frequency, buzz_frquency)
    for _ in range(rounds):
        print(next(fizzbuzz))
        