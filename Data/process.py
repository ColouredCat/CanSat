
def proc_value(v):
    #remove trailing newline
    lst = list(v)
    lst.pop(-1)
    v = ''.join(lst)
    #return number rounded to 2 d.p
    try:
        n = round(float(v), 2)
        return n
    except ValueError:
        #if data si invalid return none
        return None

def proc_file(f):
    #look through lines in file
    rssi, tmp, prs, rec, sen = [], [], [], [], []
    for line in f.readlines():
        line = line.split(":")

        #sort data into lists based on type
        if "RSSI" in line[0]:
            rssi.append(proc_value(line[-1]))
        if "Time Recived" in line[0]:
            rec.append(proc_value(line[-1]))
        if "Sent" in line[0]:
            sen.append(proc_value(line[-1]))
        if "Temperature" in line[0]:
            tmp.append(proc_value(line[-1]))
        if "Pressure" in line[0]:
            prs.append(proc_value(line[-1]))

    return rssi, tmp, prs, rec, sen

def main():
    f = open("log", 'r+')

    #get data to plot
    rssi, tmp, prs, rec, sen = proc_file(f)
            
    print(rssi, rec)
    f.close()

if __name__ == "__main__":
    main()