from pynindo import api

print(api('charts', 'youtube', 'small'))
print(api.charts['youtube']['small'])
print(api['charts']['youtube']['small'])
