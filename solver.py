#!/usr/bin/env python
import argparse
import heapq


def run_operations(
    board: list[int], operations: list[str]
) -> list[tuple[list[int], list[str]]]:
    """Iterate over the board, returning all possible new boards"""
    if len(board) == 1:
        # nothing to do
        return []
    candidates = []
    for index, item in enumerate(board):
        for new_index, new_item in enumerate(board[index + 1 :], start=index + 1):
            # start with addition and multiplication (both commutative)
            candidates.append(
                (
                    board[:index]
                    + board[index + 1 : new_index]
                    + board[new_index + 1 :]
                    + [item + new_item],
                    operations + [f"{item} ➕ {new_item} 🟰 {item + new_item}"],
                )
            )
            candidates.append(
                (
                    board[:index]
                    + board[index + 1 : new_index]
                    + board[new_index + 1 :]
                    + [item * new_item],
                    operations + [f"{item} ✖️ {new_item} 🟰 {item * new_item}"],
                )
            )
            # subtraction must be > 0
            if (sub_result := item - new_item) > 0:
                candidates.append(
                    (
                        board[:index]
                        + board[index + 1 : new_index]
                        + board[new_index + 1 :]
                        + [sub_result],
                        operations + [f"{item} ➖ {new_item} 🟰 {sub_result}"],
                    )
                )
            elif (sub_result := new_item - item) > 0:
                candidates.append(
                    (
                        board[:index]
                        + board[index + 1 : new_index]
                        + board[new_index + 1 :]
                        + [sub_result],
                        operations + [f"{new_item} ➖ {item} 🟰 {sub_result}"],
                    )
                )
            # division must return an integer
            if item > new_item and item % new_item == 0:
                candidates.append(
                    (
                        board[:index]
                        + board[index + 1 : new_index]
                        + board[new_index + 1 :]
                        + [item // new_item],
                        operations + [f"{item} ➗ {new_item} 🟰 {item // new_item}"],
                    )
                )
            elif item < new_item and new_item % item == 0:
                candidates.append(
                    (
                        board[:index]
                        + board[index + 1 : new_index]
                        + board[new_index + 1 :]
                        + [new_item // item],
                        operations + [f"{item} ➗ {new_item} 🟰 {new_item // item}"],
                    )
                )
    return candidates


def run_board(board: list[int], target: int) -> list[str]:
    """Run through all possible combos of the board and find a solution"""
    queue = [
        (0, board, []),
    ]
    heapq.heapify(queue)
    while queue:
        steps, new_board, instructions_done = heapq.heappop(queue)
        if target in new_board:
            return instructions_done
        for newer_board, new_instructions in run_operations(
            new_board, instructions_done
        ):
            heapq.heappush(queue, (steps + 1, newer_board, new_instructions))
    raise ValueError("No solution found! Did you have a typo?")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", type=int, required=True)
    parser.add_argument("board", nargs=6, type=int)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    result = run_board(args.board, args.target)
    print(f"Found a solution in {len(result)} steps:")
    print("\n".join(result))
