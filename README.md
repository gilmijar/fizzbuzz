# fizzbuzz
The not-so-boring solution to the FizzBuzz puzzle.

As the FizzBuzz rules call for starting from 1, we can mentally translate the divisibility requirements to nth multiple requrement, e.g. "every number divisible by 3" becomes "every 3rd number"  
We divide the nth-expression generationinto 3 responsibility tiers. the "3-multiple" Fizz tier, The "5-multiple" Buzz tier and the "15-multiple" FizzBuzz tier.
We creeate 3 generators, one for each tier.  
The first generator keeps track if integers (or the index of the FizzBuzz expression form the start) and returns (technically yields) either the number or the word "fizz", according to rules.  
The other tiers yield either the previous tier's value, or their assigned word: "buzz" and "fizzbuzz", respectively.  


This way we have some fun with generators and we circumvent the need for modulo operations.
