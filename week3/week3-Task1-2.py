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
# 合併spot_list和MRT_list
merged_data = []
for item in spot_list:
    serial_no = item["SERIAL_NO"]
    if serial_no in data2_dict:
        item.update(data2_dict[serial_no])
        merged_data.append(item)
# 重新建立一個以捷運站為 key，對應值為該站點的景點清單的字典
attractions_by_mrt = {}
for attraction in merged_data:
    mrt_station = attraction.get("MRT")
    attraction_name = attraction.get("stitle")
        # 確認該景點有捷運站資訊
    if mrt_station not in attractions_by_mrt:
            attractions_by_mrt[mrt_station] = []
        # 將景點加入對應的捷運站清單中
    attractions_by_mrt[mrt_station].append(attraction_name)
# print(attractions_by_mrt)
# 轉CSV
with open("mrt.csv","w",encoding="utf-8-sig") as file:
    for mrt_station, attractions in attractions_by_mrt.items():
        attractions_str = ",".join(attractions)
        # print(f"{mrt_station},{attractions_str}")
        file.write(f"{mrt_station},{attractions_str}"+"\n")