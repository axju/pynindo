from pynindo import api

api.search['rez'].list.count()
print(api.search['rez'].first)
print(api.search['rez'].last)
print(api.search['rez'][1])
