import subprocess
import sys

def main():
    try:
        # Run the command: python -m BotD
        subprocess.run([sys.executable, "-m", "BotD"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to execute 'python -m BotD'. {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
