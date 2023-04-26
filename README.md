# solver: a quick solver for the New York Times Digits game

## What is it?

This is a simple queue-based approach to solving the [Digits](https://nytimes.com/games/digits) puzzle in the fewest number of steps possible.

## How do I use it?

1. Clone this repository
2. [Install Python 3.9 or newer](https://wsvincent.com/install-python/) using @wsvincent's excellent guide
3. Run: `python solver.py 1 2 3 4 10 25 --target 81` (where the six numbers are the six numbers outlined in a dashed circle and 81 is the big number you're trying to reach)
4. Follow those steps in the NYT game
5. Celebrate your victory (I won't judge)

## Example output

```
$ python3 solver.py 5 11 19 20 23 25 -t 413
Found a solution in 4 steps:
20 ➖ 11 🟰 9
23 ➕ 25 🟰 48
9 ✖️ 48 🟰 432
432 ➖ 19 🟰 413
```

## Testing

I have some minimal tests in `test_solver.py`. Run `python -m unittest` to see if things work after you make changes.

## I think I might have found a bug. How do I get in touch?

Find me on Mastodon: https://takahe.social/@drew

PRs welcome!