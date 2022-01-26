Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def __init__(self, name, priority, period, execution_time, last_execution):



self.name = name
self.priority = priority
self.period = period
self.execution_time = execution_time
self.last_execution_time = last_execution



############################################################################
def run(self):
# Update last_execution_time
if(self.name == "pump1") :
log_fifo.append(self.name + " : reading message : " + datetime.datetime.now().strftime("%H:%M:%S"))
print(data_fifo[0])
print("pump1")



elif (self.name == "pump2"):
data_fifo.append(self.name + " : reading message : " + datetime.datetime.now().strftime("%H:%M:%S"))
log_fifo.append(self.name + " : reading message : " + datetime.datetime.now().strftime("%H:%M:%S"))
print("pump2")



elif (self.name == "Machine1"):
print(log_fifo[0])
print("Machine1")



elif:
log_fifo.append(self.name + " : reading message : " + datetime.datetime.now().strftime("%H:%M:%S"))
print("Machine2")

else :
log_fifo.append(self.name + " : reading message : " + datetime.datetime.now().strftime("%H:%M:%S"))
print("TANK")


self.last_execution_time = datetime.datetime.now()
time.sleep(self.execution_time)






####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':




last_execution = datetime.datetime.now()



# Instanciation of task objects

task_list = []
task_list.append(my_task(name="Pump1", priority = 1, period = 5, execution_time = 2, last_execution = last_execution))
task_list.append(my_task(name="Pump2", priority = 1, period = 15, execution_time = 3, last_execution = last_execution))
task_list.append(my_task(name="Machine1", priority = 2, period = 5, execution_time = 5, last_execution = last_execution))
task_list.append(my_task(name="Machine2", priority = 3, period = 5, execution_time = 3, last_execution = last_execution))
task_list.append(my_task(name="TANK", priority = 4, period = , execution_time = , last_execution = last_execution))



while(1):



time_now = datetime.datetime.now()

print("\nScheduler tick : " + time_now.strftime("%H:%M:%S"))



# Find the task with Earliest deadline



task_to_run = None
earliest_deadline = time_now + datetime.timedelta(hours=1) # Init ... not perfect but will do the job
print_out = ""
for current_task in task_list:
current_task_next_deadline = current_task.last_execution_time + datetime.timedelta(seconds=current_task.period)



print("\tAcuel task " + current_task.name + " : " + current_task_next_deadline.strftime("%H:%M:%S"))

if(current_task_next_deadline < earliest_deadline):
earliest_deadline = current_task_next_deadline
task_to_run = current_task
# Start task
task_to_run.run()