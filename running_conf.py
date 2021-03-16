from netmiko import ConnectHandler
import datetime

with open('devices.txt') as d:
    devices = d.read().splitlines()

for ip in devices:
    cisco_device = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'admin',
        'password': 'cisco',
    }
    print('Start connecting to ' + ip)
    connect = ConnectHandler(**cisco_device)

    now = datetime.datetime.now()
    today = str(now.year) + '-' + str(now.month) + '_' + str(now.day)
    devices = today + '_' + ip + '.txt'

    Result = connect.send_command('show running')
    print(Result)

    R = Result.split('\n')
    config = '\n'.join(R)

    with open(devices, 'w') as backup:
        backup.write(config)
        print('configuration_file ' + ip + ' Done Successfully')
    connect.disconnect()
