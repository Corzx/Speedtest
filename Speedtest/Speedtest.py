import speedtest

wifi = speedtest.Speedtest()
wifi.get_best_server()
print("Wifi download speed = {round(wifi.download() / 1000 / 1000, 1)} MB/s")
print("Wifi upload speed = {round(wifi.upload() / 1000 / 1000, 1)} MB/s")
print("Ping = {wifi.results.ping} ms")
