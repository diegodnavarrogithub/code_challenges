def valid_sudoku(board) -> bool:
    for row in board:
        ref_nums = []
        for num in row:
            if num != ".":
                if not num in ref_nums:
                    ref_nums.append(num)
                else:
                    return False
    index_r = 0
    index_c = 0
    ref_nums = []
    while index_r < len(board) and index_c < len(board):
        curr_num = board[index_r][index_c]
        if curr_num != ".":
            if not curr_num in ref_nums:
                ref_nums.append(curr_num)
            else:
                return False
        index_r += 1

        if index_r >= len(board):
            index_r = 0
            index_c += 1
            ref_nums = []

    start_v = 0
    end_v = start_v + 3
    start_h = 0
    end_h = start_h + 3
    ref_nums = []
    while True:
        flat = [num for row in board[start_v:end_v] for num in row[start_h:end_h]]
        clean_n_flat = list(filter(clean_helper, flat))
        if len(set(clean_n_flat)) != len(clean_n_flat):
            return False

        start_h += 3
        end_h = start_h + 3
        ref_nums.clear()
        if end_h > len(row):
            start_h = 0
            end_h = start_h + 3
            start_v += 3
            end_v = start_v + 3

        if end_v > len(board):
            break

    return True


def clean_helper(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
