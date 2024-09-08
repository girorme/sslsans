# 🔒 SSL Certificate SANs Extractor

This simple tool helps you extract domains from certs using **Subject Alternative Names (SANs)**

## 🔧 Requirements
- Python 3.x

## 🛠️ Installation
Clone the repo and navigate to the project directory:

```bash
git clone https://github.com/yourusername/ssl-cert-sans-extractor.git
cd ssl-cert-sans-extractor
```

## ⚡ Usage

### Basic Example
To fetch the SANs for a given host (e.g., `example.com`), run:

```bash
python3 sslsans.py --hostname https://example.com
```

### Specifying a Port
By default, it connects over port 443, but you can specify a different port if needed:

```bash
python3 sslsans.py --hostname https://example.com --port 8443
```

### Output Formats
You can specify the output format as either `text` or `json`.

#### Text Output (default):
```bash
python3 sslsans.py --hostname https://example.com --output text
```

#### JSON Output:
```bash
python3 sslsans.py --hostname https://example.com --output json
```

### Example Output

#### Text:
```
example.com
www.example.com
api.example.com
```

#### JSON:
```json
["example.com", "www.example.com", "api.example.com"]
```

LICENSE
```
MIT
```
