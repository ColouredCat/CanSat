
import matplotlib.pyplot as plt

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

def plot_data(data, label, title):
    #generte x axis
    x = range(len(data))

    #enable everything for the graph
    plt.plot(x, data)
    plt.xlabel("Time")
    plt.ylabel(label)
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    f = open("log", 'r+')

    #get data to plot
    rssi, tmp, prs, rec, sen = proc_file(f)

    plot_data(rssi, "Signal strength", "Recieved Signal Strength Indication over time")
    plot_data(tmp, "Temperature (deg. C)", "Temperature over time")
    plot_data(prs, "Pressure", "Pressure over time")
    plot_data(rec, "Pressure", "Pressure over time")
            
    print(rssi, tmp, prs)
    f.close()

if __name__ == "__main__":
    main()