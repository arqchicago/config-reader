import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# config.getint: to read integer parameters
print(f'integers')
print(f'> parameter 1 = {config.getint("integer_vars", "parameter1")}')
print(f'> parameter 2 = {config.getint("integer_vars", "parameter2")}')
print(f'> parameter 3 = {config.getint("integer_vars", "parameter3")}')
print(f'> parameter 4 = {config.getint("integer_vars", "parameter4")}\n')

# config.getfloat: to read floating point parameters
print(f'floats')
print(f'> parameter 1 = {config.getfloat("float_vars", "parameter1")}')
print(f'> parameter 2 = {config.getfloat("float_vars", "parameter2")}')
print(f'> parameter 3 = {config.getfloat("float_vars", "parameter3")}')
print(f'> parameter 4 = {config.getfloat("float_vars", "parameter4")}')

# config.get: to read string parameters
# config.getboolean: to read boolean parameters

#with open('config.ini', 'w') as config_file:
#    config.write(config_file)