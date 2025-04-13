
# Pan Card PDF Password Cracker

A simple Python script that uses [pdfcrack](https://pdfcrack.sourceforge.net/) to brute-force the password of a PDF file. By default, it generates a wordlist of possible dates (in the format MMDDYYYY) that might serve as the PDF password.

> **Important**: This tool should only be used on files you have permission to test. Misuse could lead to legal consequences. The author is not responsible for any misuse or damage caused by this tool.

---

## Features

- Automatically generates a date-based wordlist using Python’s [exrex](https://pypi.org/project/exrex/) library (covering years 1930–2099 by default).
- Uses [pdfcrack](https://pdfcrack.sourceforge.net/) to attempt unlocking the PDF.
- Supports both Linux and Windows.

---

## Prerequisites

1. **Python 3**  
   Make sure you have Python 3 installed.

2. **pdfcrack**  
   - **Linux**:  
     Install via your package manager. For example, on Debian/Ubuntu:
     ```bash
     sudo apt-get update
     sudo apt-get install pdfcrack
     ```
   - **Windows**:  
     The `pdfcrack.exe` already present in windows folder.
---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/sangleshubham/Pan-Card-Password-Cracker.git
   ```
2. Navigate into the cloned repository:
   ```bash
   cd Pan-Card-Password-Cracker
   ```
3. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Verify `pdfcrack` is installed by running on linux:
   ```bash
   pdfcrack --help
   ```
   If it’s not installed or not recognized, install or place `pdfcrack.exe` in the `windows/` folder as needed.

---

## Usage

Run the script:
   ```bash
   python3 script.py <PDF_Filename.pdf>
   ```

**Example**:
```bash
python3 script.py secret_pan_card.pdf
```

- The script will generate a file named `wordlist` in the current directory.
- It will then call `pdfcrack` with the generated wordlist to try to unlock the PDF.
- Once the process finishes, it prints the total time taken for the cracking attempt.

---

## How It Works

1. **Generate the Wordlist**  
   The script uses a regular expression to generate all possible dates in the format `MMDDYYYY` (for example, `02141995`). This is done using `exrex.generate()` with the pattern:
   ```
   ((0[0-9])|(1[0-2]))((0[1-9])|(1[0-9])|(2[0-9])|(3[0-2]))((19[3-9][0-9])|(20[012][0-9]))
   ```

2. **Crack the PDF**  
   - On **Linux**, it calls `pdfcrack` directly.  
   - On **Windows**, it calls `pdfcrack.exe` in the `windows/` directory.

3. **Track Execution Time**  
   It measures how long the cracking attempt takes and prints the total duration.

---

## Modifying the Wordlist Logic

If you want to adjust the date range or pattern:

1. Open the script in a text editor.
2. Locate this line:
   ```python
   data = list(exrex.generate(r'((0[0-9])|(1[0-2]))((0[1-9])|(1[0-9])|(2[0-9])|(3[0-2]))((19[3-9][0-9])|(20[012][0-9]))'))
   ```
3. Adjust the regex to meet your needs (e.g., to handle narrower or broader date ranges).

---

## Contributing

1. Fork the repo.
2. Create a new feature branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request describing the changes.

---

## License

This project is licensed under the [MIT License](LICENSE). You can freely modify and distribute it. See the [LICENSE](LICENSE) file for details.

---

### Disclaimer

Use this script only on PDFs you own or have explicit permission to test. The author is not responsible for any misuse or damages caused by this tool. Always comply with your local laws and regulations.
