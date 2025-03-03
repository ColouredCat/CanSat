
def proc_value(v):
    #remove trailing newline
    lst = list(v)
    lst.pop(-1)
    v = ''.join(lst)
    #return number rounded to 2 d.p
    return round(float(v), 2)


def main():
    f = open("log", 'r+')

    #look through lines in file
    rssi, tmp, prs, rec, sen = [], [], [], [], []
    for line in f.readlines():
        line = line.split(":")

        #sortd data into lists based on type
        if "RSSI" in line[0]:
            rssi.append(proc_value(line[-1]))
        elif "Time Recived" in line[0]:
            rec.append(proc_value(line[-1]))
        elif "Sent" in line[0]:
            sen.append(proc_value(line[-1]))
        elif "Temperature" in line[0]:
            tmp.append(proc_value(line[-1]))
        elif "Pressure" in line[0]:
            prs.append(proc_value(line[-1]))

            
    print(rssi, rec)


    f.close()

if __name__ == "__main__":
    main()