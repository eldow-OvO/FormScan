# FormScan
A Python-based vulnerability scanner that identifies XSS vulnerabilities in web forms by injecting custom payloads.

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
python xss_scanner.py --url http://example.com/contact
