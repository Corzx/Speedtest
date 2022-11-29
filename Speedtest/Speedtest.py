import speedtest

wifi = speedtest.Speedtest()
wifi.get_best_server()
print(f"Wifi download speed = {round((wifi.download() / 1000 / 1000) / 8, 1)} MB/s")
print(f"Wifi upload speed = {round((wifi.upload() / 1000 / 1000) / 8, 1)} MB/s")
print(f"Ping = {wifi.results.ping} ms")
