import psutil

#set log file 
filename = "log/log"
cur_fd = 1
cur_filename = filename + str(cur_fd) + ".log"
header_str = "usage\tuser\tsystem\tiowait\tidle\n"

# set max size of one log file 
MAX_FILE_SIZE = 10000   # 10000 records for one file

# get user, system, iowait and idle time
def get_time(time1, time2):
    result = []
    result.append(time2[0] - time1[0])
    result.append(time2[2] - time1[2])
    result.append(time2[4] - time1[4])
    result.append(time2[3] - time1[3])
    return result

f = open(cur_filename, 'w')
f.write(header_str)

# set time interval to record cpu_info
TIME_ITERVAL = 60   #one minute
cur_cnt = 0

# the main loop
while True:
    # change another file
    if cur_cnt == MAX_FILE_SIZE:
        f.close()
        cur_cnt = 0
        cur_fd += 1
        cur_filename = filename + str(cur_fd) + ".log"
        f = open(cur_filename, 'w')
        f.write(header_str)

    # get those cpu information 
    cpu_info1 = psutil.cpu_times()
    time = psutil.cpu_percent(interval = TIME_ITERVAL)
    cpu_info2 = psutil.cpu_times()
    cpu_info = get_time(cpu_info1, cpu_info2)

    # log those data
    f.write(str(time) + "\t")
    for cpu_i in cpu_info:
        f.write(str(cpu_i) + "\t")
    f.write("\n")

    cur_cnt += 1
    print cur_filename, cur_cnt, time

f.close()
