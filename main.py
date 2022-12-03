import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


'''get data one by one'''


URL = os.getenv('URL')
while True:
    id = input("enter the id for fetching data or enter '0000' to exit : ")
    if id == '0000':
        break
    else:
        response = requests.get(f"{URL}={id}")
        if response.status_code == 200:
            values = response.json()
            apps_data = values['apps']
            filtered_data = []
            for val in apps_data:
                if 'vajro_version' in val:
                    val['vajro_version']['id']=id
                    filtered_data.append(val['vajro_version'])
            if filtered_data:
                try:
                    df = pd.DataFrame(filtered_data)
                    df = df.set_index('id')
                    writer = pd.ExcelWriter(f'{id}.xlsx')
                    df.to_excel(writer)
                    writer.save()
                except:
                    print(f"something wrong when handling data with id {id}, please try again")
            else:
                print(f"no data in {id}")


#'''combine all excel into one'''

# import os
# import glob
# path = os.getcwd()
# file_list = glob.glob(path + "/*.xlsx")
# excl_list = []
 
# for file in file_list:
#     excl_list.append(pd.read_excel(file))
# excl_merged = pd.DataFrame()
 
# for excl_file in excl_list:
#     excl_merged = excl_merged.append(
#       excl_file, ignore_index=True)
# excl_merged.to_excel('total.xlsx', index=False)


#==============================================================================================================


#'''get data one by one'''

# def get_data(data):
#     filtered_data = []
#     for i in data:
#         response = requests.get(f"url{i}")
#         if response.status_code == 200:
#             values = response.json()
#         apps_data = values['apps']
#         for val in apps_data:
#             if 'vajro_version' in val:
#                 val['vajro_version']['id']=i
#                 filtered_data.append(val['vajro_version'])
#     return filtered_data              
# result= get_data([33079,33078,16074])
# df = pd.DataFrame(result)
# df = df.set_index('id')
# writer = pd.ExcelWriter('data.xlsx')
# df.to_excel(writer)
# writer.save()