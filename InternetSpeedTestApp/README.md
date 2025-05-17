# Internet Speed Test App

## Features
- CLI and GUI versions of an internet speed test application.
- Uses `speedtest-cli` to measure download, upload speeds and ping.
- Modern CLI UI with [rich](https://github.com/Textualize/rich): colored panels, tables, and progress spinners.
- Displays local and external IP, ISP, and location.
- Shows server info, test time, and allows saving results to a file.
- Friendly error handling and retry option if the test fails.

## How to Use

### Install Requirements
```powershell
pip install -r requirements.txt
```

### Run CLI Version
```powershell
python speed_test_cli.py
```

### CLI Features
- See network details (local IP, external IP, ISP, location)
- See speed test results in a formatted table (download, upload, ping, server, ISP, test time)
- Retry the test if it fails
- Optionally save results to `speedtest_results.txt`

### Run GUI Version
```powershell
python speed_test_gui.py
```
