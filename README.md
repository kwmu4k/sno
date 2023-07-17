<img align="right" height="145" src=".meow/snø.svg">

# snø [<img src="https://nukocities.neocities.org/nuko/sets/cat325.gif">](https://nukocities.neocities.org/)

snø is an esolang I've made for Truttle1's 2023 esojam!

It is a 2D, stack-based esolang of which the IP can only go in diagonal directions

To run `main.sn` just type `python snø.py`, if you want to run another file, use `python snø.py path/to/file.sn`

## Commands

The interpreter ignores every other character than these, making them no-op

The IP's (`@`) default direction is bottom left

### IP direction commands

| Arrow | Direction        |
| ----- | ---------------- |
| `/`   | Bottom Left      |
| `\`   | Bottom Right     |
| `§`   | Random           |

### Main commands

| Command | Description                                                                        |
| ------- | ---------------------------------------------------------------------------------- |
| `@`     | IP starting point                                                                  |
| `0`-`F` | Push the corrisponding hex number as an integer                                    |
| `!`     | Pop the last value                                                                 |
| `I`     | Push user input (1 byte)                                                           |
| `O`     | Output the last value to the console then pop it                                   |
| `}`     | Swap the last two values                                                           |
| `$`     | Reverse the whole stack                                                            |
| `:`     | Duplicate the top value                                                            |
| `+`     | Add last two values together, leaving only the result                              |
| `-`     | Subtract last two values together, leaving only the result                         |
| `*`     | Multiply last two values together, leaving only the result                         |
| `\|`     | Divide last two values together, leaving only the result                           |
| `^`     | Raise last two values together, leaving only the result                            |
| `%`     | Modulo last two values together, leaving only the result                           |
| `~`     | NOR bitwise operator (you can make any bitwise operator with this!)                |
| `Y`     | If number is non-zero, set direction to bottom left, set to bottom right otherwise |
| `&`     | End program                                                                        |

snø's arithmetic is NOS × TOS, meaning that it will duplicate the 2nd value on the stack by the last value on the stack

## Example programs

Here are some example programs! There are a lot of them (send help they spawn every single nanosecond I breathe)

### 1-byte cat ![](https://nukocities.neocities.org/nuko/act/cat1.gif)

```sn
    @
   \.
  ..I..
 ....O..
......&..
```

### Demonstration of `Y`

```sn
      @
     \.
    ..I..
   ....Y..
  ....1.0..
 ....O...O..
....&.....&..
```

### Addition calculator

```sn
      @
     \·
    ··I··
   ····I··
  ······+··
 ········O··
··········&··
```

## Weird things

### This code doesn't run

```sn
   .
  @@.
 II...
.......
```

### Unicode input

Take the cat program and now put an unicode character such as 🍊, the output will be "ð"

The IP somehow cannot find the `@` so it just gives up

<p align="center"><img src="https://nukocities.neocities.org/nuko/sets/cat80.gif"></img></p>
