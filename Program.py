import subprocess
import time

def run_program_continuously(program_path):
    while True:
        print("Running the program...")
        # Run the program
        process = subprocess.Popen(['python', r'C:\Users\gowth\Metamask-Selenium-Auto-Import-Mnemonic\chrome3.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        
        # Print the output and error if any
        print("Output:", output.decode())
        print("Error:", error.decode())
        
        # Wait for a certain duration before running the program again
        time.sleep(5)  # Change the duration as needed

if __name__ == "__main__":
    program_path = r'C:\Users\gowth\Metamask-Selenium-Auto-Import-Mnemonic\chrome3.py'  # Replace "your_program.py" with the path to your program
    run_program_continuously(program_path)