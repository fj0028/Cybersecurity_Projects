import os
import glob
from abc import ABC, abstractmethod

#Prompts user to input path
directory = input("Enter directory to scan: ")

#Checks if path is valid
if not os.path.isdir(directory):
    print("Error: Invalid directory path. Please enter a valid folder.")
    exit()

#Base Class
class FileProcessor(ABC):
    @abstractmethod
    def process(self, file_path: str):
        #Process given file
        pass

#Main class
class FileScanner:
    def __init__(self, directory: str, processor: FileProcessor):
        self.directory = directory
        self.processor = processor
    
    def scan(self):
        #Scans directory and processes each file"
        if not os.path.exists(self.directory):
            raise FileNotFoundError(f"Directory '{self.directory}' not found.")

        for root, _, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                self.processor.process(file_path)


class TextFileProcessor(FileProcessor):
    def process(self, file_path: str):
        if file_path.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                pass

#Searches for keywords in files
suspicious_files = []
for filename in file_list:
    try:
        with open(filename, 'r', errors='ignore') as file:
            for line_number, line in enumerate(file, 1):
                if any(keyword in line for keyword in keywords):
                    suspicious_files.append((filename, line_number, line.strip()))

    except FileNotFoundError:
        print(f"Error: File {filename} not found \n")
    except Exception as e:
        print(f"An error occured while opening {filename}: {e}\n")

#Saves results to a summary report
report_path = os.path.join(directory, "summary_report.txt")
with open(report_path, 'w') as f:
    for file, line_num, text in suspicious_files:
        f.write(f"File: {file}, Line {line_num}: {text}\n")

print(f"Scanning complete. Found {len(suspicious_files)} suspicious entries.")
print(f"Report saved at: {report_path}")