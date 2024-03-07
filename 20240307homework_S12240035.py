# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

def calculate_circle(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return circumference, area

def main():
    radius = float(input("請輸入圓的半徑："))
    circumference, area = calculate_circle(radius)
    print("圓的周長為：", circumference)
    print("圓的面積為：", area)

if __name__ == "__main__":
    main()

def collect_user_data():
    name = input("請輸入您的姓名：")
    age = int(input("請輸入您的年齡："))
    height = float(input("請輸入您的身高（米）："))
    favorite_color = input("請輸入您喜愛的顏色：")

    user_data = {
        "姓名": name,
        "年齡": age,
        "身高": height,
        "喜愛的顏色": favorite_color
    }

    return user_data

def format_user_data(user_data):
    formatted_data = "{}, {}歲, 身高{}米, 喜愛的顏色是{}。".format(
        user_data["姓名"],
        user_data["年齡"],
        user_data["身高"],
        user_data["喜愛的顏色"]
    )
    return formatted_data

def main():
    user_data = collect_user_data()
    formatted_data = format_user_data(user_data)
    print("用戶的個人資料摘要：", formatted_data)

if __name__ == "__main__":
    main()

def main():
    num = int(input("請輸入一個整數："))

    if num % 2 == 0:
        print("您輸入的數字是偶數。")
    else:
        print("您輸入的數字不是偶數。")

if __name__ == "__main__":
    main()
    
def main():
    try:
        num = int(input("請輸入一個整數："))

        if num % 2 == 0:
            print("您輸入的數字是偶數。")
        else:
            print("您輸入的數字不是偶數。")
    except ValueError:
        print("錯誤：請輸入一個有效的整數。")

if __name__ == "__main__":
    main()
