import datetime
try:
    def diff_time():
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        given_time = str(input("Enter time in hh:mm:ss format with colons: "))
        print("Current time: " + str(current_time))
        print("Given time: " + str(given_time))
        hc = int(current_time[:2])
        hg = int(given_time[:2])
        mc = int(current_time[3:5])
        mg = int(given_time[3:5])
        sc = int(current_time[6:])
        sg = int(given_time[6:])
        ct = (hc*60*60)+(mc*60)+(sc)
        gt = (hg*60*60)+(mg*60)+(sg)
        if(gt != ct):
            if(gt > ct):
                diff = gt - ct
            else:
                diff = ct - gt
            
            hour = int(diff/3600)
            m = diff - (hour*3600)
            minute = int(m/60)
            second = m - (minute*60)
            while(second>60):
               minute += 1
               second -=60
               
            print(f"The difference between current time and given time is {hour}:{minute}:{second}")
        elif(gt == ct):
            print("There is no time difference")
    diff_time()
except ValueError:
    print("Enter time in number and in correct format")
except:
    print("Enter correctly")