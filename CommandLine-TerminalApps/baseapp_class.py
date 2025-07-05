# Basic command line app framework

class App:
    
    def __init__(self):
        pass

    # Checks for end command (standard for command line apps)
    def check_for_end_command(self,prompt):
        if prompt.lower().replace(" ","") == "end":
            print("Ended Session.")
            return True
        return False
    

    def run(self):
        pass 


if __name__=="__main__":
    app = App()
    app.run()
