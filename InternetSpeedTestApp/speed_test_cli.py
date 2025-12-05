import speedtest
import socket
import requests
import csv  # <-- Added to handle the CSV file
import os   # <-- Added to check if the file already exists
from datetime import datetime  # <-- Added to the timestamp

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

# --- NEW FEATURE ADDED ---
def save_results_csv(data_row):
    """
Saves a data row in a CSV file.
Creates the header if the file does not exist.
    """
    FILENAME = 'speedtest_history.csv'
    
    # Define the headers (columns) of our CSV
    # They correspond to the keys of the 'data_to_save' dictionary in the main() function
    HEADERS = ['timestamp', 'download', 'upload', 'ping', 'isp', 'external_ip', 'result_link']
    
    # 'os.path.isfile' checks if the file already exists.
    # We use this to know if we need to write the header.
    file_exists = os.path.isfile(FILENAME)
    
    try:
    # 'a' means 'append'. This adds to the end of the file without deleting the content.
    # 'newline=""' is important for the csv module to function correctly in Windows.
        with open(FILENAME, 'a', newline='', encoding='utf-8') as f:
            
            # DictWriter is great because it maps dictionaries to CSV rows.
            # Using 'fieldnames=HEADERS' ensures the correct column order.
            writer = csv.DictWriter(f, fieldnames=HEADERS)
            
            # If the file did NOT exist, we write the header.
            if not file_exists:
                writer.writeheader()
            
            # Write the data line (our dictionary)
            writer.writerow(data_row)
        
        print(f"✅ Results saved successfully in {FILENAME}")
    
    except IOError as e:
        print(f"❌ Error saving CSV file: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred while saving: {e}")
# --- END OF NEW FUNCTION ---


def main():
    print("🔍 Starting network details retrieval...\n")
    local_ip = get_local_ip()
    external_ip, isp, city, country = get_external_ip_and_isp()
    print(f"📡 Local IP Address     : {local_ip}")
    print(f"🌐 External IP Address  : {external_ip}")
    print(f"🏢 ISP                : {isp}")
    print(f"📍 Location           : {city}, {country}\n")
    
    results = perform_speed_test()
    
    print("\n📊 Speed Test Results Summary:")
    print(f"⬇️ Download Speed       : {results['download']:.2f} Mbps")
    print(f"⬆️ Upload Speed         : {results['upload']:.2f} Mbps")
    print(f"⏱ Ping                 : {results['ping']:.2f} ms")
    print(f"\n🔗 Share your results with this link: {results['result_link']}")

# --- BLOCK ADDED TO SAVE ---
    print("\n💾 Saving results to history...")
    
    # 1. Obtain the current timestamp in ISO format (default).
    current_timestamp = datetime.now().isoformat()
    
    # 2. Consolidate all the data we want to save into a dictionary.
    #    The keys (e.g., 'timestamp') MUST MATCH the HEADERS of the save_results_csv function.
    data_to_save = {
        'timestamp': current_timestamp,
        'download': results['download'],  # We saved the "raw" (float) value for analysis.
        'upload': results['upload'],      # Same
        'ping': results['ping'],          # Same
        'isp': isp,
        'external_ip': external_ip,
        'result_link': results['result_link']
    }
    
    # 3. Call the new function to save.
    save_results_csv(data_to_save)
   # --- END OF ADDED BLOCK ---

if __name__ == "__main__":
    main()
