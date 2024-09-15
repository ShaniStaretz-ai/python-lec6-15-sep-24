# python-lec6-15-sep-24

## learned subjects:

1) loop else:
   In loops, when the condition in the while is TRUE you can add the else and the next action

   example: (see full code in while)
    ```
    while num!=777:
   ....
        if num==0:
            break;
   else: 
        print("well done")
    ```
   usage: if there is a break in the loop, you cannot know what was the exit value, therefore this else help to know
   that the exit value was the value from the while condition and not because of the break in the loop.
2) random numbers:
    * need the random functions from module(library) name 'random' :
     ```   
    import random (will import the entire module) 
   or
   from random import *  
   ```
    * num=randint(a=0,b=3)- make random number between 0,10 including and return it to num
    * randint function: random integer number
    * uniform function: random float number
       ```
       from random import randint, uniform
       num=randint(a=0,b=3) -a=start, b=end including 
       num = uniform(a=0, b=3)
       ```
    * choice function: random from list of options:
       ```
      choose = choice([True,False,"sunday"])
       ```
    * import 2 functions from the same module:
         ```
       from random import randint, uniform
      ```
3) nested loop: 
   * loop within loop: it's a <u>child</u> loop within a <u>parent</u> loop.
   * iterator can be the same parameter, doesn't change the functionality (for now....).

## Extra:

* if you write a constant parameter, that doesn't change, you can write the parameter with all capital letters.

  i.e: PIE:float=3.14