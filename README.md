# Multiple Encoding Vector
A Python reimplementation of the Multiple Encoding Vector, a sequence comparison method by [Li et al 2017](https://www.nature.com/articles/s41598-017-12493-2)

## Pre-requisites
You need to have Python3, Numpy and Pandas installed.

## Usage

You can produce the MEV distance matrix from input sequence by the following command format.

```
python3 mev.py <input_file_name> <output_file_name>
```
A sample command would be:
```
python3 mev.py input.fasta dist.csv
```

## Reference

Li, Y., He, L., Lucy He, R., and Yau, S. S.-T. (2017). A novel fast vector method for
genetic sequence comparison. Sci. Rep., 7(1), 12226.


