"""
    英辞郎
"""

import csv

def format_string(s):
    """cp932 の文字が含まれてるとエラーになるので取り除く(発音記号とか)
    けどいらなくなった
    """
    UNICODE = "utf-8"
    return s.encode(UNICODE, "ignore").decode(UNICODE)


def main():
    fname = "level1.txt"
    f = open(fname, "r", encoding="utf-16")

    cnt = 0
    words, means = [], []
    for line in f:
        out = [x.strip() for x in line.split("///")]

        # 発音記号が複数あるときは前の means に追加する
        if len(out) < 2:
            means[-1][0] += " " + out[0] # -> str
            means[-1] = [x.strip() for x in means[-1][0].split("\\") if len(x)]
            #break
            continue

        assert(len(out) == 2)
        word, mean = out
        mean = [x.strip() for x in mean.split("\\") if len(x)]
        words.append(word)
        means.append(mean)
        
        cnt += 1
        #if cnt > 5: break

    f.close()

    assert(len(words) == len(means))
    print("")

    #for word, mean in zip(words, means):
    #    #if word != "live": continue
    #    print(word)
    #    print(mean)

    outname = "level1.csv"
    with open(outname, "w", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\n")
        for word, mean in zip(words, means):
            # word; mean
            writer.writerow([word, "<br>".join(mean)])

    print("done")



if __name__ == "__main__":
    main()
