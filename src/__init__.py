
import sys
import clock
import getData

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("Wrong input")
        exit(1)
    else:
        msg = sys.argv[1]
    if(msg == "start"):
        clock.clockIn()
    elif(msg == "stop"):
        clock.clockOut()
    elif(msg == "status"):
        getData.getStatus()
    else:
        print("Wrong input")
    
    