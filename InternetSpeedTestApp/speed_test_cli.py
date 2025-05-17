import speedtest
import socket
import requests
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel

def get_local_ip():
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
        return local_ip
    except Exception:
        return "Unavailable"

def get_external_ip_and_isp():
    try:
        response = requests.get("https://ipinfo.io/json", timeout=5)
        data = response.json()
        ip = data.get("ip", "N/A")
        org = data.get("org", "N/A")
        city = data.get("city", "N/A")
        country = data.get("country", "N/A")
        return ip, org, city, country
    except Exception:
        return "N/A", "N/A", "N/A", "N/A"

from datetime import datetime
DOWNLOAD_DIVISOR = 1_000_000
UPLOAD_DIVISOR = 1_000_000

def perform_speed_test():
    st = speedtest.Speedtest()
    try:
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
            progress.add_task(description="Searching for best server...", total=None)
            best_server = st.get_best_server()
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
            progress.add_task(description="Measuring download speed...", total=None)
            download_speed_mbps = st.download() / DOWNLOAD_DIVISOR
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
            progress.add_task(description="Measuring upload speed...", total=None)
            upload_speed_mbps = st.upload() / UPLOAD_DIVISOR
        ping_ms = st.results.ping
        result_link = st.results.share()
        test_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {
            "download": download_speed_mbps,
            "upload": upload_speed_mbps,
            "ping": ping_ms,
            "server": best_server,
            "result_link": result_link,
            "test_time": test_time
        }
    except Exception as e:
        err = str(e)
        if '403' in err:
            err = 'Speedtest servers are blocking this client (HTTP 403). Try using a VPN or a different network.'
        return {"error": err}

def main():
    console = Console()
    console.print(Panel("[bold cyan]Internet Speed Test CLI[/bold cyan]", expand=False))
    while True:
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
            progress.add_task(description="Retrieving network details...", total=None)
            local_ip = get_local_ip()
            external_ip, isp, city, country = get_external_ip_and_isp()
        table = Table(title="Network Details", show_header=True, header_style="bold magenta")
        table.add_column("Type", style="dim")
        table.add_column("Value")
        table.add_row("Local IP", local_ip)
        table.add_row("External IP", external_ip)
        table.add_row("ISP", isp)
        table.add_row("Location", f"{city}, {country}")
        console.print(table)
        results = perform_speed_test()
        if 'error' in results:
            console.print(f"[bold red]Speed test failed:[/bold red] {results['error']}")
            retry = console.input("[bold yellow]Do you want to retry? (y/n): [/bold yellow]").strip().lower()
            if retry == 'y':
                continue
            else:
                return
        result_table = Table(title="Speed Test Results", show_header=True, header_style="bold green")
        result_table.add_column("Metric", style="dim")
        result_table.add_column("Value")
        result_table.add_row("Download", f"{results['download']:.2f} Mbps")
        result_table.add_row("Upload", f"{results['upload']:.2f} Mbps")
        result_table.add_row("Ping", f"{results['ping']:.2f} ms")
        result_table.add_row("Server", f"{results['server']['name']}, {results['server']['country']}")
        result_table.add_row("ISP", isp)
        result_table.add_row("Test Time", results['test_time'])
        console.print(result_table)
        console.print(f"[bold blue]Share your results:[/bold blue] {results['result_link']}")
        # Optional: Export to file
        save = console.input("[bold yellow]Save results to file? (y/n): [/bold yellow]").strip().lower()
        if save == 'y':
            with open('speedtest_results.txt', 'a', encoding='utf-8') as f:
                f.write(f"Test Time: {results['test_time']}\n")
                f.write(f"Local IP: {local_ip}\nExternal IP: {external_ip}\nISP: {isp}\nLocation: {city}, {country}\n")
                f.write(f"Download: {results['download']:.2f} Mbps\nUpload: {results['upload']:.2f} Mbps\nPing: {results['ping']:.2f} ms\n")
                f.write(f"Server: {results['server']['name']}, {results['server']['country']}\n")
                f.write(f"Share Link: {results['result_link']}\n")
                f.write("-"*40 + "\n")
            console.print("[green]Results saved to speedtest_results.txt[/green]")
        break

if __name__ == "__main__":
    main()

