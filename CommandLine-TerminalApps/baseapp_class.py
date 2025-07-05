# Basic command line app framework
import sys

class App:
    
    def __init__(self):
        pass

    # Checks for end command (standard for command line apps) and closes the app
    def check_for_end_command(self,prompt):
        if prompt.lower().replace(" ","") == "end":
            print("Ended Session.")
            sys.exit()
    

    def run(self):
        pass 


if __name__=="__main__":
    app = App()
    app.run()
