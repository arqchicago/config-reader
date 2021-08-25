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
print(f'> parameter 4 = {config.getfloat("float_vars", "parameter4")}\n')

# config.get: to read string parameters
print(f'strings')
print(f'> parameter 1 = {config.get("string_vars", "parameter1")}')
print(f'> parameter 2 = {config.get("string_vars", "parameter2")}')
print(f'> parameter 3 = {config.get("string_vars", "parameter3")}')
print(f'> parameter 4 = {config.get("string_vars", "parameter4")}\n')

# config.getboolean: to read boolean parameters
print(f'booleans')
print(f'> parameter 1 = {config.getboolean("boolean_vars", "parameter1")}')
print(f'> parameter 2 = {config.getboolean("boolean_vars", "parameter2")}')
print(f'> parameter 3 = {config.getboolean("boolean_vars", "parameter3")}')
print(f'> parameter 4 = {config.getboolean("boolean_vars", "parameter4")}\n')

# config.get: to read lists
print(f'lists')
string_list = config.get("lists", "list1")
string_list = string_list.split(',')
print(f'> string list = {string_list}')

float_list = config.get("lists", "list2")
float_list = [float(x) for x in float_list.split(',')]
print(f'> float list = {float_list}')

bool_list = config.get("lists", "list3")
bool_list = [True if x in 'True' else False for x in bool_list.split(', ')]
print(f'> bool list = {bool_list}\n')


# config._sections to read sections as python dictionary
config2 = configparser.ConfigParser()
config2.read('config2.ini')
config_sections = config2._sections

print(f'reading config sections as a dictionary')
print(f'> integers = {config_sections["integer_vars"]}')
print(f'> floats = {config_sections["float_vars"]}')
print(f'> strings = {config_sections["string_vars"]}')
print(f'> booleans = {config_sections["boolean_vars"]}')

#with open('config.ini', 'w') as config_file:
#    config.write(config_file)