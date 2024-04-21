#抓取檔案,確認可抓取到資料來源
import urllib.request as request
import json
url_1="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
url_2="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"
with request.urlopen(url_1) as response1:
    data_1=json.load(response1) #資料類型為字典"dict"
with request.urlopen(url_2) as response2:
    data_2=json.load(response2) #資料類型為字典"dict"
#print(data_1)
#print(data_2)
# 讀取檔案
spot_list=data_1["data"]["results"] #資料類型為清單"list"
MRT_list=data_2["data"] #資料類型為清單"list"
#print(spot_list)
#print(MRT_list)
# 將MRT_list轉換成以SERIAL_NO為key的字典
data2_dict = {item["SERIAL_NO"]: item for item in MRT_list}
#print(data2_dict)
# # 合併spot_list和MRT_list
merged_data = []
for item in spot_list:
    serial_no = item["SERIAL_NO"]
    if serial_no in data2_dict:
        item.update(data2_dict[serial_no])
        merged_data.append(item)
# 整理filelist,取第一個.jpg檔案
for spot_list2 in merged_data:
     first_image_url_modify=spot_list2["filelist"].lower().split(".jpg")[0]
     # print(first_image_url_modify)
     first_image_url=first_image_url_modify+".jpg"
    # print(first_image_url)
     spot_list2["first_image_url"]=first_image_url
# print(merged_data)
with open("spot.csv","w",encoding="utf-8-sig") as file:
    for spot in merged_data:
        # print(spot["stitle"],spot["address"][5:8],spot["longitude"],spot["latitude"],spot["first_image_url"])
        file.write(spot["stitle"]+","+spot["address"][5:8]+","+spot["longitude"]+","+spot["latitude"]+","+spot["first_image_url"]+"\n")