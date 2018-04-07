import csv

# !!! ここを書き換える !!!
INNAME = "level7.csv"
OUTNAME = "level7_out.csv"

def main():
    fname = INNAME
    f = open(fname, "r", encoding="utf-16")

    words, means = [], []
    for line in f:
        out = [x.strip() for x in line.split("///")]

        # 発音記号が複数あるときは前の means に追加する
        if len(out) < 2:
            means[-1][0] += " " + out[0] # -> str
            means[-1] = [x.strip() for x in means[-1][0].split("\\") if len(x)]
            continue

        assert(len(out) == 2)
        word, mean = out
        mean = [x.strip() for x in mean.split("\\") if len(x)]
        words.append(word)
        means.append(mean)

    f.close()
    assert(len(words) == len(means))

    outname = OUTNAME
    with open(outname, "w", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\n")
        for word, mean in zip(words, means):
            # word; mean
            writer.writerow([word, "<br>".join(mean)])

    print("done")


if __name__ == "__main__":
    main()
