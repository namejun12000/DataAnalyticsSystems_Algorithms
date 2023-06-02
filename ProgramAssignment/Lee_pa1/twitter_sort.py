###
# Twitter Sort
# Author: Nam Jun Lee
# Date: Sept 26th, 2021
###

import sys
import re


# function for read the tweets file
def read_tweets(file):
    records_list = []
    lines = open(file, encoding='UTF-8')
    # map to the information containted in each line of the file
    for line in lines:
        line = line.rstrip()
        # find all line and append to records using regular expression
        if re.findall('', line):
            records_list.append(line)
    return records_list


# function for merges two lists of records
def merge_tweets(lst1, lst2):
    merge_t1 = lst1
    merge_t2 = lst2
    final = merge_t1 + merge_t2
    return final


# function for writes to the file output each record line
def write_tweets(file, lst3):
    wf = open(str(file), 'w', encoding='UTF-8')
    # write all lines
    for i in lst3:
        wf.writelines("%s\n" % i)
    # close file
    wf.close()


def main():
    # main program to prompt
    # input files are read using command line agruments
    file1 = read_tweets(sys.argv[1])
    file2 = read_tweets(sys.argv[2])
    # output file are write using command line arguments
    file3 = sys.argv[3]
    print('Reading files...')
    # file that contained the most tweets
    file1_len = len(file1)
    file2_len = len(file2)
    # if-elif-else statement
    if file1_len > file2_len:
        print("%s contained the most tweets with %d.\n" % (sys.argv[1], file1_len))
    elif file1_len < file2_len:
        print("%s contained the most tweets with %d.\n" % (sys.argv[2], file2_len))
    else:
        print("Both contained the most tweets with %d.\n" % file1_len)

    print('Merging files...')
    # merge two tweets files
    mg_tweet = merge_tweets(file1, file2)
    print('File Merged.\n')
    print('Writing file...')
    # write the tweets output file
    # arrange the tweets according to the date and time.
    write_tweets(file3, mg_tweet)
    print('File written.\n')
    print('Displaying 5 newest tweeters and tweets.')
    # displays the five newest tweets along with the tweeter
    for i in range(5):
        idx = mg_tweet[i].index('" ')
        print(mg_tweet[i][:idx + 1])


if __name__ == '__main__':
    main()
