from Bio import SeqIO
import pandas as pd
import os

def convert(seq):
    if type(seq) != str:
        raise TypeError("传入的文件名称必须为字符串")
    meta = []
    sequence = []
    label = []
    i = 0
    for seq_record in SeqIO.parse(seq, "fasta"):
        meta.append(str(seq_record.id))
        sequence.append(str(seq_record.seq))
        i = 1 + i
        label.append(int(i))
        # print(sequence)
        df = pd.DataFrame(data={'Meta': meta, 'SequenceID': sequence, 'Label': label})  # 转换后的文件的表头
        print(df)

        # 数据存入csv
        df.to_csv(seq[:-6] + ".csv", sep=',', index=False)  # 转换后的文件

# convert(Fasta 文件位置)
# 会自动将转化后的结果保存到 CSV 文件里面