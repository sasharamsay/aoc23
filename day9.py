import re


def get_datasets(lines):
    datasets = []
    for line in lines:
        dataset_str = re.split("\s+", line.strip())
        dataset = []
        for i in dataset_str:
            dataset.append(int(i))
        datasets.append(dataset)
    return datasets


def get_history(dataset):
    all_rows = []

    curr_row = dataset
    all_rows.append(curr_row)

    all_zeroes = False

    while not all_zeroes:
        all_zeroes = True
        new_row = []
        for i in range(len(curr_row) - 1):
            new_row.append(curr_row[i + 1] - curr_row[i])
        all_rows.append(new_row)
        curr_row = new_row
        for i in new_row:
            if i != 0:
                all_zeroes = False

    return all_rows


def get_next(all_rows):
    all_rows[-1].append(0)
    prev_row = all_rows[-1]

    for i in reversed(range(len(all_rows) - 1)):  # excluding row of zeroes
        all_rows[i].append(all_rows[i][-1] + prev_row[-1])
        prev_row = all_rows[i]

    return all_rows[0][-1]


def get_prev(all_rows):
    all_rows[-1].insert(0, 0)
    prev_row = all_rows[-1]

    for i in reversed(range(len(all_rows) - 1)):  # excluding row of zeroes
        all_rows[i].insert(0, (all_rows[i][0] - prev_row[0]))
        prev_row = all_rows[i]

    return all_rows[0][0]


def extrapolate(datasets, direction):
    sum_histories = 0

    for dataset in datasets:
        history = get_history(dataset)
        sum_histories += get_next(history) if direction == 'next' else get_prev(history)

    return sum_histories


def day_9(filename):
    datasets = get_datasets(open(filename, 'r').readlines())
    return extrapolate(datasets, 'next')


def day_9_part_2(filename):
    datasets = get_datasets(open(filename, 'r').readlines())
    return extrapolate(datasets, 'prev')
