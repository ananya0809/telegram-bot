import subprocess

class CommandHandler:
    def get_command_result(self, command):
        print(command)
        try:
            cmdcheck = subprocess.Popen(command, stdout=subprocess.PIPE)
            output = cmdcheck.stdout.read()
            return output
        except:
            return "Invalid Argument"
    def check_dangerous_command(self, command):
        dangerous_commands = ['pwd']
        for danger in dangerous_commands:
            if command == danger:
                return True
        return False    
            
            
