#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import process utility library 
import psutil
#import time library for delaying execution for 20secs
import time


print('Wait, Watching processes on local computer for each 20 secs')

#get initial number of running process 
ini_pids_count=len(psutil.pids())
ini_cpu_usage=psutil.cpu_percent()
i=1
#create an infinite loop
while i !=0: 
    print('\n\n')
    #delay for 20 secs 
    time.sleep(20)
    #get percentage cpu usage
    cpu_usage=psutil.cpu_percent()
    
    #display the percentage CPU usage
    print(f'{"Percentage CPU usage":26s} : {cpu_usage:6f}\n')
    
    #get all running processes 
    pids=psutil.pids()
    
    #get the total number of pids
    pids_count=len(pids);
    
    #display the total number of running processes 
    print(f'{"Total running processes":26s} : {pids_count:6d}\n')
    
    
    #compare the process 20secs ago to processes running now
    if pids_count > ini_pids_count:
        print(f'There are {pids_count - ini_pids_count} processes running than before\n')
    elif pids_count < ini_pids_count:
        print(f'The Total number of processes reduced by {ini_pids_count - pids_count} than before\n')
    else:
        print(f'There is no change in the number of processes running\n')
    
    #set ini_pids_count to pids_count
    ini_pids_count=pids_count
        
        
    #check if percentage cpu usage has increase by more than 10% in the last 20secs
    if(cpu_usage - ini_cpu_usage >= 10):

    
        #variable to determine if there is a running process
        running_pros_count=0
    
    
        #check which process is using more than 1%
        for i in range(pids_count):
            
            try: 
                #create a process instance for each pid
                p=psutil.Process(pids[i])
        
                #get the details of the process as a dictionary 
                pro_details=p.as_dict(attrs=['name', 'cpu_percent'])
        
                #check if the cpu_percent is over 1%
                if pro_details['cpu_percent'] > 1:
                    #display the process name using more than 1%
                    print(f'{pro_details["name"]} process using more than 1% CPU capacity\n')
                    running_pros_count= running_pros_count+1
                    
            except (NoSuchProcess, ProcessLookupError, NameError):
                print('Error Occured');
                
        if running_pros_count == 0: 
            print('There are no processes using more than 1% CPU capacity\n')
            
    #set the initial cpu usage to the initial cpu usage
    ini_cpu_usage=cpu_usage
    
    


# In[ ]:




