import csv
import time

full_list = [["time","Avg_I_L1","Min_I_L1","Max_I_L1","Avg_I_L2","Min_I_L2","Max_I_L2","Avg_I_L3","Min_I_L3","Max_I_L3","Avg_U_L1","Min_U_L1","Max_U_L1","Avg_U_L2","Min_U_L2","Max_U_L2","Avg_U_L3","Min_U_L3","Max_U_L3","Avg_b_charge","Min_b_charge","Max_b_charge","Avg_P","Min_P","Max_P","Avg_Q","Min_Q","Max_Q"]]

order = ["L1MWI","L1MII","L1MAI",
         "L2MWI","L2MII","L2MAI",
         "L3MWI","L3MII","L3MAI",
         "L1MWU","L1MIU","L1MAU",
         "L2MWU","L2MIU","L2MAU",
         "L3MWU","L3MIU","L3MAU",
         "MWBATT_LADESTAND","MIBATT_LADESTAND","MABATT_LADESTAND",
         "MWP", "MIP", "MAP",
         "MWQ", "MIQ", "MAQ",
]

def open_write(path):
    dated_dictionary = {}
    with open(path) as folder:
        for line in folder:
            split_line = line.split(";")
            split_line[0] += " " + split_line[1]
            split_line.pop(1)
            if split_line[0] not in dated_dictionary:
                dated_dictionary[split_line[0]] = [split_line]
            else : 
                dated_dictionary[split_line[0]].append(split_line)
    return dated_dictionary

def check_for_condition(dated_dictionary, output):
    for date in dated_dictionary:
        list_with_data = [None] * len(order)
        for data in dated_dictionary[date]:
            temp1 = data[1][-7:-5] + data[1][:2] + data[1][-9]
            temp2 = data[1][:2] + data[1][-5]
            temp3 = data[1][:2] + data[1][-18:-4]
            if temp1 in order:
                list_with_data[order.index(temp1)] = data[-1].strip()
            elif temp2 in order:
                list_with_data[order.index(temp2)] = data[-1].strip()
            elif temp3 in order:
                list_with_data[order.index(temp3)] = data[-1].strip()
        list_with_data.insert(0, data[0])
        form_print(list_with_data, dated_dictionary, output)

def form_print(list_with_data, dated_dictionary, output):
    full_list.append(list_with_data)
    if len(full_list) == len(dated_dictionary)+1:
        write(full_list, output)
    
def write(line, output):
    with open(output, mode="a", newline="") as finall_input:
        csv_writer = csv.writer(finall_input, delimiter=";")
        csv_writer.writerows(line)

def main():
    path = input("Enter the data input root path -->")
    output = input("Enter the data output root path -->")
    start_time = time.time()
    dated_dictionary = open_write(path)
    check_for_condition(dated_dictionary, output)
    stop_time = time.time()
    print(stop_time - start_time)

if __name__ == '__main__':
    main()