import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# config.getfloat: to read floating point parameters
print(f'> parameter 1 = {config.getfloat("floats", "parameter1")}')
print(f'> parameter 2 = {config.getfloat("floats", "parameter2")}')
print(f'> parameter 3 = {config.getfloat("floats", "parameter3")}')
print(f'> parameter 4 = {config.getfloat("floats", "parameter4")}')

# config.get: to read string parameters
# config.getboolean: to read boolean parameters
# config.getint: to read integer parameters

#with open('config.ini', 'w') as config_file:
#    config.write(config_file)