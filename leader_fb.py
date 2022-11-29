from itertools import cycle, count
        
        
 #current leading solution from stack overflow: 14.2MiB/s
 #https://codegolf.stackexchange.com/questions/215216/high-throughput-fizz-buzz
def derailleur(counter, carousel):
    if not carousel:
        return counter
    return carousel

def main():
    carousel = cycle([0,0,'Fizz',0,'Buzz','Fizz',0,0,'Fizz','Buzz',0,'Fizz',0,0,'FizzBuzz'])
    counter = count(1)
    f = map(print, map(derailleur, counter, carousel))
    for _ in range(10000000):
        next(f)

main()

#maxwallace@MaxBook2 ~/b/c/p/ultrafb> python3 ultrafb.py | pv -c > /dev/null                                      (ultrafb)
#64.9MiB 0:00:06 [9.37MiB/s] [            <=>                                                                              ]