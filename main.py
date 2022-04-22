import os
import sys

def main():
  
    input_path = os.environ["INPUT_PATH"]

    print(input_path)

    message = '1'
  

    print(f"::set-output name=warnings::{message}")

    sys.exit(0)


if __name__ == "__main__":
    main()