import subprocess

class CommandHandler:
    def get_command_result(self, command):
        print(command)
        complete_command = command.split(" ")

        try:
            if len(complete_command) == 1:
                cmdcheck = subprocess.Popen(command, stdout=subprocess.PIPE)
                output = cmdcheck.stdout.read()
            elif len(complete_command) > 1:
                cmdcheck = subprocess.Popen([complete_command[0], complete_command[1]], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, err = cmdcheck.communicate(b"input data that is passed to subprocess' stdin")
                rc = cmdcheck.returncode
            return output
        except:
            return "Invalid Argument"
    def check_dangerous_command(self, command):
        dangerous_commands = ['rm', 'sudo', 'su', 'mv']
        for danger in dangerous_commands:
            if command == danger:
                return True
        return False    
            
            
