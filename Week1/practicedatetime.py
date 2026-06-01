# import datetime
# x = datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.strftime("%H:%M:%S:%A"))


from datetime import datetime
now = datetime.now()
print(now.strftime("%H:%M:%S:%A"))