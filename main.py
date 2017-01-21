import time
import os
import node_system

try:
    file_name = input('Enter name of file map(including the extension):')
    file = open(file_name, 'r')
    end_node = file.read(2)
    file.read(1)
    length = int(file.read(5))
    connections = eval(file.read(length))
    file.read(1)
    length = int(file.read(5))
    names = eval(file.read(length))
    file.read(1)
    length = int(file.read(5))
    content = eval(file.read(length))
    file.read(1)
    length = int(file.read(5))
    connect_points = eval(file.read(length))
    loaded_map = node_system.Nodes(connections, names, content, connect_points)
    last_command = '>>%s\n\n' % file_name
    while True:
        os.system('cls')
        print(last_command, end='')
        loaded_map.print_info('current')
        command = input('>>')
        last_command = ('>>%s\n\n' % command)
        if command == 'exit':
            break
        else:
            node = command
            if node == end_node:
                if loaded_map.connect(node):
                    while True:
                        print('')
                        time.sleep(1)
            else:
                loaded_map.connect(node)
except NameError:
    input('The file you entered is invalid. Press enter to continue.')
except FileNotFoundError:
    input("We couldn't find a file with the name you entered. Press enter to continue.")
