
# Internet Speed Test App 🌐⚡

![GitHub release](https://img.shields.io/github/release/LELIONTRIBAL0/InternetSpeedTestApp.svg) ![License](https://img.shields.io/badge/license-MIT-blue.svg)

Welcome to the **Internet Speed Test App**! This application provides a quick, simple, and open-source way to check your internet performance. Unlike online browser-based tools, this app gives you direct access to vital metrics such as download and upload speeds, ping (latency), ISP and external IP address, and a link to share your Speedtest.net results.

---

## 🚀 New CLI Features (2025)

- Modern CLI UI with [rich](https://github.com/Textualize/rich): colored panels, tables, and progress spinners
- Displays local and external IP, ISP, and location before the test
- Shows server info and test time in the results table
- Friendly error handling and retry option if the test fails
- Option to save results to a file (`speedtest_results.txt`) after a successful test
- Code cleanup and improved structure

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)


## Features

- **Download Speed**: Measure how fast data can be downloaded from the internet.
- **Upload Speed**: Check how quickly data can be sent to the internet.
- **Ping (Latency)**: Determine the response time of your internet connection.
- **ISP Information**: Get details about your Internet Service Provider.
- **External IP Address**: Find out your public IP address.
- **Result Sharing**: Easily share your Speedtest.net results with a link.
- **Modern CLI UI**: Beautiful output with colors, tables, and spinners (see above)
- **Retry and Save**: Retry failed tests and save results to a file

## Installation

To install the **Internet Speed Test App**, follow these steps:

1. **Download the latest release** from [here](https://github.com/LELIONTRIBAL0/InternetSpeedTestApp/releases). Make sure to choose the appropriate version for your operating system.
2. **Extract the files** if necessary.
3. **Run the application** by executing the main script in your terminal or command prompt.


## Usage

Once you have installed the app, you can start testing your internet speed.

### Run CLI Version
```powershell
python InternetSpeedTestApp/speed_test_cli.py
```

#### CLI Features
- See network details (local IP, external IP, ISP, location)
- See speed test results in a formatted table (download, upload, ping, server, ISP, test time)
- Retry the test if it fails
- Optionally save results to `speedtest_results.txt`

### Run GUI Version
```powershell
python InternetSpeedTestApp/speed_test_gui.py
```

For more details, refer to the [Releases](https://github.com/LELIONTRIBAL0/InternetSpeedTestApp/releases) section.

## Technologies Used

The **Internet Speed Test App** is built using the following technologies:

- **Python**: The primary programming language used for development.
- **Requests**: A library for making HTTP requests to gather data.
- **Socket**: Used for network connections and operations.
- **Speedtest-cli**: A command-line interface for testing internet speed.
- **Modular Design**: The app follows a modular design for easy updates and enhancements.

## Contributing

We welcome contributions to improve the **Internet Speed Test App**! If you want to contribute, please follow these steps:

1. **Fork the repository**: Click the "Fork" button at the top right of this page.
2. **Create a new branch**: Use a descriptive name for your branch.
3. **Make your changes**: Implement your features or fixes.
4. **Submit a pull request**: Describe your changes and why they are needed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, feel free to reach out:

- **GitHub**: [LELIONTRIBAL0](https://github.com/LELIONTRIBAL0)
- **Email**: [your_email@example.com](mailto:your_email@example.com)

## Conclusion

The **Internet Speed Test App** offers a straightforward way to measure your internet performance. With its easy-to-use interface and essential features, it stands out as a reliable tool for anyone looking to assess their connection speed. Download the latest version from the [Releases](https://github.com/LELIONTRIBAL0/InternetSpeedTestApp/releases) section and start testing today!

Feel free to explore, contribute, and enhance this open-source project!