import subprocess
import sys

def main():
    try:
        # Run the command: python -m LaylaRobot
        subprocess.run([sys.executable, "-m", "LaylaRobot"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to execute 'python -m LaylaRobot'. {e}")
        sys.exit(1)

if name == "main":
    main()
