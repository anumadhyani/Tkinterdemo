# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# import tkinter
#
# window = tkinter.Tk()
# window.title("My first GUI program")
# window.minsize(width=500, height=500)
#
# my_label = tkinter.Label("I am a label")

# forces = {0: ["Calm", "Sea like a mirror", "Smoke rises vertically"],
#           1: ["Light air", "Ripples with appearance of scales are formed, without foam crests", "Direction shown by smoke drift but not by wind vanes."],
#           2: ["Light breeze", "Small wavelets still short but more pronounced; crests have a glassy appearance but do not break","Wind felt on face; leaves rustle; wind vane moved by wind."],
#           3: ["Gentle breeze","Large wavelets; crests begin to break; foam of glassy appearance; perhaps scattered white horses","Leaves and small twigs in constant motion; light flags extended."],
#           4: ["Moderate breeze","Small waves becoming longer; fairly frequent white horses","Raises dust and loose paper; small branches moved."],
#           5: ["Fresh breeze","Moderate waves taking a more pronounced long form; many white horses are formed; chance of some spray","Small trees in leaf begin to sway; crested wavelets form on inland waters."],
#           6: ["Strong breeze","Large waves begin to form; the white foam crests are more extensive everywhere; probably some spray","Large branches in motion; whistling heard in telegraph wires; umbrellas used with difficulty."],
#           7: ["High wind, moderate gale, near gale","Sea heaps up and white foam from breaking waves begins to be blown in streaks along the direction of the wind; spindrift begins to be seen","Whole trees in motion; inconvenience felt when walking against the wind."],
#           8: ["Gale, fresh gale","Moderately high waves of greater length; edges of crests break into spindrift; foam is blown in well-marked streaks along the direction of the wind","Twigs break off trees; generally impedes progress."],
#           9: ["Strong/severe gale","High waves; dense streaks of foam along the direction of the wind; sea begins to roll; spray affects visibility","Slight structural damage (chimney pots and slates removed)."],
#           10: ["Storm, whole gale","Very high waves with long overhanging crests; resulting foam in great patches is blown in dense white streaks along the direction of the wind; on the whole the surface of the sea takes on a white appearance; rolling of the sea becomes heavy; visibility affected","Seldom experienced inland; trees uprooted; considerable structural damage."],
#           11: ["Violent storm","Exceptionally high waves; small- and medium-sized ships might be for a long time lost to view behind the waves; sea is covered with long white patches of foam; everywhere the edges of the wave crests are blown into foam; visibility affected","Very rarely experienced; accompanied by widespread damage."],
#           12: ["Hurricane force","The air is filled with foam and spray; sea is completely white with driving spray; visibility very seriously affected","Devastation"]
#           }
#
# Knots1 = [1, 3, 6, 10, 16, 21, 27, 33, 40, 47, 55, 63, 64]
#
# speed = int(input("Enter the speed of the wind in km/h:"))
#
# cons_converter = float(1/1.85)
#
# speed_in_knot = speed*cons_converter
# print(speed_in_knot)
#
# for items in Knots1
#     if speed_in_knot < Knots1[items]:
#     description = forces[0][0]
#     print(description)
#     sea_conditions = forces[0][1]
#     print(sea_conditions)
#     land_conditions = forces[0][2]
#     print(land_conditions)


#Step 1: Convert this speed in knots knowing that 1 knot = 1.852 km/h


#Step 2: Use the Beaufort scale to work out the matching wind force


#Step 3: Display the wind force, description, sea conditions and land conditions corresponding to this wind force


#Step 4: Review the code in step 1 to allow the user to enter the wind speed in the unit of their choice (km/h, mph, knots)
# import tkinter
# from tkinter import *
#
# window = tkinter.Canvas(width=500, height=500)
# window.pack()
#
# my_label = tkinter.Label(text="Argument name")
# my_label.pack()

import requests

resp = requests.get('https://catfact.ninja/fact')
print(type(resp))

# if resp.status_code != 200:
#     # This means something went wrong.
#     raise ApiError('GET /tasks/ {}'.format(resp.status_code))
# for todo_item in resp.json():
#     print('{} {}'.format(todo_item['id'], todo_item['summary']))





# window.mainloop()