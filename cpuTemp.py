from gpiozero import CPUTemperature
import time
cpu = CPUTemperature()
while True:
	if cpu.temperature > 80: 
		print(str(cpu.temperature)+"This shit is too hot!!")
	else:
		print(cpu.temperature)
	time.sleep(2)
