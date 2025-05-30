![alt text](https://github.com/eldow-OvO/FormScan/blob/main/FormScan.png "Logo")

FormScan is a Python-based vulnerability scanner that identifies XSS vulnerabilities in web forms by injecting custom payloads.

## 🚀 Features
- Auto-detects and scans all forms on a given page
- Injects XSS payloads into input fields
- Supports both reflected and DOM-based XSS (with Selenium)
- Outputs clean vulnerability reports (CSV/JSON)
- Customizable payload list

## 📸 Demo
![demo](assets/demo.gif)

## 🧪 Example Usage
```bash
python formscan.py --url http://example.com/contact
```

## 🔧 Requirements
- Python 3.x
- requests
- beautifulsoup4
- selenium
- colorama
- tqdm

Install them with:
```bash
pip install -r requirements.txt
```

## 📂 Output
```text
[+] Vulnerable URL: http://example.com/contact
[+] Payload: <script>alert(1)</script>
[+] Input Field: message
```

## 📚 Future Plans
- Add CSRF detection
- Auto-exploit builder
- Save reports in HTML format

## 📜 License
MIT

## 🙌 Contribute
Pull requests are welcome! Let's make security better together.
