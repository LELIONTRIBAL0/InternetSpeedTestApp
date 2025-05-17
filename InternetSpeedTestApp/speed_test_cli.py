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

def perform_speed_test():
    st = speedtest.Speedtest()
    console = Console()
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task(description="Searching for best server...", total=None)
        best_server = st.get_best_server()
    console.print(f"[bold green]✅ Best Server:[/bold green] {best_server['host']} in {best_server['name']}, {best_server['country']}")
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task(description="Measuring download speed...", total=None)
        download_speed_mbps = st.download() / 1_000_000
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task(description="Measuring upload speed...", total=None)
        upload_speed_mbps = st.upload() / 1_000_000
    ping_ms = st.results.ping
    result_link = st.results.share()
    return {
        "download": download_speed_mbps,
        "upload": upload_speed_mbps,
        "ping": ping_ms,
        "server": best_server,
        "result_link": result_link
    }

def main():
    console = Console()
    console.print(Panel("[bold cyan]Internet Speed Test CLI[/bold cyan]", expand=False))
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
    result_table = Table(title="Speed Test Results", show_header=True, header_style="bold green")
    result_table.add_column("Metric", style="dim")
    result_table.add_column("Value")
    result_table.add_row("Download", f"{results['download']:.2f} Mbps")
    result_table.add_row("Upload", f"{results['upload']:.2f} Mbps")
    result_table.add_row("Ping", f"{results['ping']:.2f} ms")
    console.print(result_table)
    console.print(f"[bold blue]Share your results:[/bold blue] {results['result_link']}")

if __name__ == "__main__":
    main()

