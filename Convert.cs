using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using System.Linq;
using System.Diagnostics;

namespace CsharpTest
{
    class Convert
    {
        static void Main(string[] args)
        {
            if (args.Length != 1)
            {
                Console.WriteLine("Usage: Move a csv file to this exe file.");
                Console.ReadKey();
                return;
            }

            string OUTNAME = args[0] + "_out.csv";

            // 読み込み
            var words = new List<string>();
            var means = new List<string[]>();
            using (var r = new StreamReader(args[0]))
            {
                string line;
                while ((line = r.ReadLine()) != null)
                {
                    line = line.Replace(';', ',');
                    string[] seps = { "///" };
                    string[] ss = line.Split(seps, StringSplitOptions.None)
                        .Select(s => s.TrimEnd()).ToArray();

                    // 発音記号が複数あるときは前の means に追加する
                    if (ss.Length < 2)
                    {
                        string[] m = means.Last();
                        means.RemoveAt(means.Count - 1);
                        m[0] += " " + ss[0];
                        means.Add(m);
                        continue;
                    }
                    Debug.Assert(ss.Length == 2);

                    string word = ss[0];
                    string[] seps2 = { "\\" };
                    string[] mean = ss[1].Split(seps2, StringSplitOptions.None)
                        .Select(s => s.Trim()).ToArray();
                    words.Add(word);
                    means.Add(mean);
                }
            }
            Debug.Assert(words.Count == means.Count);

            // 書き込み
            using (var writer = new StreamWriter(OUTNAME, false, Encoding.UTF8))
            {
                foreach (var i in words.Zip(means, Tuple.Create))
                {
                    string word = i.Item1;
                    string mean = String.Join("<br>", i.Item2);
                    writer.WriteLine(word + ";" + mean);
                }
            }
            Console.WriteLine(OUTNAME + " was created.");
            Console.ReadKey();
        }
    }
}
