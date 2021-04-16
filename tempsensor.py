
---
- name: Test the Pi from tower
  hosts: 10.0.0.233
  tasks:
    - name: Get the temperature
      command: "python3 /home/pi/SunFounder/Python/18_thermistor.py"
