from constants import arrow_keys, arrows, arrow_keys_reversed


def move_valid(original_grid, new_grid):
    return original_grid != new_grid


def request_move(valid_moves):
    input_str = 'What\'s the next move? '
    for i in range(4):
        if valid_moves[i]:
            input_str += arrow_keys_reversed[i] + ': ' + arrows[i] + ', '
    input_str += 'q: quit\n'

    next_move_str = input(input_str)
    while next_move_str not in list(arrow_keys.keys()) + ['q'] \
        or (next_move_str != 'q' and
            not valid_moves[arrow_keys[next_move_str]]):
        if input_str[:2] != 'Wr':
            input_str = 'Wrong input. ' + input_str
        next_move_str = input(input_str)

    if next_move_str == 'q':
        return next_move_str
    return arrow_keys[next_move_str]
