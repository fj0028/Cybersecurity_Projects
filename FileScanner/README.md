# File Scanner

**FileScanner** is a Python-based tool that scans a given directory and processes specific file types using customizable file processors. 
It's modular, multithreaded, and designed for extensibility — ideal for cybersecurity file triage, analysis tooling, or educational projects.

---

## Features

- Scans a directory for supported file types
- Multi-threaded file processing for performance
- Modular architecture using OOP
- Easily extendable with new file processors
- Command-line interface (CLI) with argparse

---

## Requirements

- Python 3.8+
- Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## Usage
Basic Example
```bash
python file_scanner.py "C:\path\to\your\folder" --types txt pdf
```
This will scan the folder and process .txt and .pdf files using their respective processors

---

## Architecture Overview

- FileScanner: Manages directory walking and dispaches processing jobs
- BaseFileProcessor: Abstract base class for all processors
- Indivdual processors (e.g., TextFileProcessor, PdfFileProcessor) inherit from base and implement process() module
- Uses ThreadPoolExecutor for concurrent file handling

---

## Cybersecurity Relevance

This tool serves as a foundation for file triage tools, useful in:
- Security automation - scanning directories for suspicious or malformed documents
- Incident repsonse - gathering file metadata
- Forensics pipelines - feeding extracted data into other analysis tools

--- 

## Adding a New Processor

To support a new file type:
1. Create a new class that inherits from BaseFileProcessor
2. Implement the process(self, file_path) method
3. Register the new processor in processor_map in file_scanner.py




