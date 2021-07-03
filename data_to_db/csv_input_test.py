import csv

'''
@param:
    input_file='all_csv_merged.csv'
    output_file='all_csv_merged_new.csv'
@read_me:
    all_csv_merged.csv must be in the same directory as this python script
    all_csv_merged_new.csv is created into the same directory as this python script
'''


def main(input_file,output_file):
    print("Main")
    with open(input_file,'r') as in_csv, open(output_file,'w') as out_csv:
        reader = csv.reader(in_csv)
        writer = csv.writer(out_csv, delimiter = ',',lineterminator='\n' )
        count = 0

        for r in reader:
            """"if (r[3] == "2020") or (r[3] == "1960") or (r[3] == ""):
                continue
            else:
                writer.writerow(r)
                continue"""
            if (r[3]) == "NA":
                r[3] = "NaN"


            if r[4] == "NA":
                r[4] = "NaN"

            if r[5] == "NA":
                r[5] = "NaN"

            if r[6] == "NA":
                r[6] = "NaN"

            if r[7] == "NA":
                r[7] = "NaN"

            if r[8] == "NA":
                r[8] = "NaN"


            writer.writerow(r)



    return 0


main('all_csv_merged.csv', 'all_csv_merged_new.csv')




"""if __name__ == "__main__":
    main('all_csv_merged.csv', 'all_csv_merged_new.csv')"""
