# Catherine Morgan, Roger T Webb, Mathew J Carr, Evangelos Kontopantelis, Carolyn A Chew-Graham, Nav Kapur, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"R054z00","system":"readv2"},{"code":"2I16.00","system":"readv2"},{"code":"G732100","system":"readv2"},{"code":"G732.00","system":"readv2"},{"code":"R054.00","system":"readv2"},{"code":"G732200","system":"readv2"},{"code":"G731100","system":"readv2"},{"code":"G732000","system":"readv2"},{"code":"C107.12","system":"readv2"},{"code":"G732400","system":"readv2"},{"code":"G732300","system":"readv2"},{"code":"R054000","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('peripheral-vascular-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["peripheral-vascular-gangrene---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["peripheral-vascular-gangrene---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["peripheral-vascular-gangrene---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
