import speedtest
import socket
import requests

def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "Unavailable"

def get_external_ip_and_isp():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        return data.get("ip", "N/A"), data.get("org", "N/A"), data.get("city", "N/A"), data.get("country", "N/A")
    except:
        return "N/A", "N/A", "N/A", "N/A"

def main():
    print("🔍 Getting network details...\n")
    local_ip = get_local_ip()
    external_ip, isp, city, country = get_external_ip_and_isp()

    print(f"📡 Local IP Address     : {local_ip}")
    print(f"🌐 External IP Address  : {external_ip}")
    print(f"🏢 ISP                  : {isp}")
    print(f"📍 Location             : {city}, {country}\n")

    st = speedtest.Speedtest()

    print("🔎 Finding best server...")
    best = st.get_best_server()
    print(f"✅ Best Server Found: {best['host']} ({best['name']}, {best['country']})\n")

    print("⚡ Testing download speed...")
    download_speed = st.download() / 1_000_000

    print("⚡ Testing upload speed...")
    upload_speed = st.upload() / 1_000_000

    ping = st.results.ping

    print("\n📊 Speed Test Results:")
    print(f"⬇️ Download Speed       : {download_speed:.2f} Mbps")
    print(f"⬆️ Upload Speed         : {upload_speed:.2f} Mbps")
    print(f"⏱ Ping                 : {ping:.2f} ms")

    print(f"\n🔗 Result Share Link     : {st.results.share()}")

if __name__ == "__main__":
    main()
