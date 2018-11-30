from datetime import datetime
result=['''10/03/1998''']
pydt=datetime.strptime(result[0].replace(''','''),'%m/%d/%Y%H:%M:%S'):
    print(pydt)
