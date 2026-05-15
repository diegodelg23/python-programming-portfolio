if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    scores = [records[idx][1] for idx in range(len(records))]
    min_num = min(scores)
    while min_num in scores:
        scores.remove(min_num)

    second_lowest = min(scores)

    names = []

    for record in records:
        if record[1] == second_lowest:
            names.append(record[0])

    names.sort()

    for name in names:
        print(name)

