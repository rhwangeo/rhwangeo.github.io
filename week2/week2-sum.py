print("---Task1---")
def find_and_print(messages, current_station):
    # 建立捷運站名稱與編號的對應清單
    station_list = {
        "Songshan": 1,
        "NanjingSanmin": 2,
        "Taipei Arena": 3,
        "NanjingFuxing": 4,
        "Zhongshan": 5,
        "Beimen": 6,
        "Ximen": 7,
        "Xiaonamen": 8,
        "ChiangKai-ShekMemorialHall": 9,
        "Guting": 10,
        "TaipowerBuilding": 11,
        "Gongguan": 12,
        "Wanlong": 13,
        "Jingmei": 14,
        "Dapiinglin": 15,
        "Qizhang": 16,
        "Xiaobitan": 16.5,
        "Xindian City Hall": 17,
        "Xindian": 18,
    }
    
    # 將目前站點的名稱轉換為編號
    current_station_num = station_list.get(current_station)
    # print("current_station_num")
    
    # 建立一個字典來存儲人員與距離的對應關係
    people_distance = {}
    for member, message in messages.items():
        for station in station_list:

            if station in message:
                station_num = station_list[station]
                distance = abs(station_num - current_station_num)
                # 人員若在Xiaobitan必須多增加一站的轉乘
                if station== "Xiaobitan" in message:
                    distance += 1
                people_distance[member] = distance
    # print(people_distance)
    # if current_station == "Xiaobitan" or station== "Xiaobitan" in message:
    # 找到距離最接近的人
    closest_person = min(people_distance, key=people_distance.get)
    
    # 確認最終結果
    print(closest_person)

messages = {
    "Leslie": "I'm at home near Xiaobitan station.",
    "Bob": "I'm at Ximen MRT station.",
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Vivian": "I'm at Xindian station waiting for you."
}

find_and_print(messages, "Wanlong")  # print Mary
find_and_print(messages, "Songshan")  # print Copper
find_and_print(messages, "Qizhang")   # print Leslie
find_and_print(messages, "Ximen")     # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian

print("---Task2---")
def book(consultants, hour, duration, criteria):
    # 建立顧問schedule
    for consultant in consultants:
        consultant.setdefault("schedule", [])
    time_on = hour
    time_off = hour + duration

    # 找出有空的顧問
    available_consultants = [consultant 
        for consultant in consultants
            if all(start >= time_off or end <= time_on 
                for (start, end) in consultant["schedule"]
        )]
    if not available_consultants:
        print("No Service")
        return

    # 根據條件選擇顧問
    if criteria == "price":
        chosen_consultant = min(
            available_consultants, 
            key=lambda x: x["price"])
    elif criteria == "rate":
        chosen_consultant = max(
            available_consultants, 
            key=lambda y: y["rate"])
    else:
        print("Invalid criteria")
        return

    # 更新顧問時間表
    chosen_consultant["schedule"].append((time_on, time_off))
    print(chosen_consultant["name"])

consultants = [
    {"name": "John", "rate": 4.5, "price": 1000},
    {"name": "Bob", "rate": 3, "price": 1200},
    {"name": "Jenny", "rate": 3.8, "price": 800}]

book(consultants, 15, 1, "price")  # Jenny
book(consultants, 11, 2, "price")  # Jenny
book(consultants, 10, 2, "price")  # John
book(consultants, 20, 2, "rate")   # John
book(consultants, 11, 1, "rate")   # Bob
book(consultants, 11, 2, "rate")   # No Service
book(consultants, 14, 3, "price")  # John
print("---Task3---")
def func(*data):
    middle_name_count = {}
    names_with_middle_name = {}  # 用來記錄每個中間名對應的名字

    for name in data:
        # 確認中間名
        if len(name) == 5:
            middle_name = name[2]
        elif len(name) == 4:
            middle_name = name[2]
        elif len(name) == 3:
            middle_name = name[1]
        elif len(name) == 2:
            middle_name = name[1]
        else:
            middle_name = ("僅辨識名字長度2-5個字")  # 無法確定中間名時
        # 更新中間名出現次數
        if middle_name:
            if middle_name in middle_name_count:
                middle_name_count[middle_name] += 1
                names_with_middle_name[middle_name].append(name)
            else:
                middle_name_count[middle_name] = 1
                names_with_middle_name[middle_name] = [name]
    # print("中間名出現次數：", middle_name_count)
    # print(middle_name)
    # 印出只出現一次的名字
    # print("只出現一次的名字:")
    one_time_count = 0
    for middle_name, count in middle_name_count.items():
        if count == 1:
            one_time_count += 1
            print(names_with_middle_name[middle_name])
    if one_time_count == 0:
        print("沒有")

func("彭大牆","陳王明雅","吳明") #彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") #林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") #沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆")#夏曼藍波安
print("---Task4---")
def get_number(index):
    print(4*index-5*(int(index//3)))
get_number(1) #4
get_number(5) #15
get_number(10) #25
get_number(30) #70
print("---Task5---")