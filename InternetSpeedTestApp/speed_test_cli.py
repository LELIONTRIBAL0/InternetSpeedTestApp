import speedtest
import socket
import requests

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
    print("🔎 Searching for the best speedtest server based on ping...")
    best_server = st.get_best_server()
    print(f"✅ Best Server Found: {best_server['host']} located in {best_server['name']}, {best_server['country']}\n")
    print("⚡ Measuring download speed...")
    download_speed_mbps = st.download() / 1_000_000
    print("⚡ Measuring upload speed...")
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
    print("🔍 Starting network details retrieval...\n")
    local_ip = get_local_ip()
    external_ip, isp, city, country = get_external_ip_and_isp()
    print(f"📡 Local IP Address     : {local_ip}")
    print(f"🌐 External IP Address  : {external_ip}")
    print(f"🏢 ISP                  : {isp}")
    print(f"📍 Location             : {city}, {country}\n")
    results = perform_speed_test()
    print("\n📊 Speed Test Results Summary:")
    print(f"⬇️ Download Speed       : {results['download']:.2f} Mbps")
    print(f"⬆️ Upload Speed         : {results['upload']:.2f} Mbps")
    print(f"⏱ Ping                 : {results['ping']:.2f} ms")
    print(f"\n🔗 Share your results with this link: {results['result_link']}")

if __name__ == "__main__":
    main()

