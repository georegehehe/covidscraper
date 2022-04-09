# the keywords are indicators of important information that ensues
top_keyword = ("新增确诊","新增无症状")
l2_keyword = "本土"

# define functions to pinpoint the specific area of text which contains related information
# 本土确诊: if no keywords found, then return an empty string to avoid error
def locate_positive(txt):
    if top_keyword[0] in txt:
        new_normal = txt.split(top_keyword[0], 1)[1]
    else:
        return ""
    if l2_keyword in new_normal and "(" in new_normal and ")" in new_normal:
        new_native = new_normal.split(l2_keyword, 1)[1].split("（", 1)[1].split("）", 1)[0]
        return new_native
    else:
        return ""

# 本土无症状: if no keywords found, then return an empty string to avoid error
def locate_asymptomatic(txt):
    if top_keyword[1] in txt:
        new_normal = txt.split(top_keyword[1], 1)[1]
    else:
        return ""
    if l2_keyword in new_normal and "(" in new_normal and ")" in new_normal:
        new_native = new_normal.split(l2_keyword, 1)[1].split("（", 1)[1].split("）", 1)[0]
        return new_native
    else:
        return ""

# given that txt contains needed information, determine the number of cases for each city
def analyzer(txt, dict, mode):
    if mode == '本土':
        txt = locate_positive(txt)
    else:
        txt = locate_asymptomatic(txt)
    # separate txt by province
    province_list = txt.split("；")
    city_list = dict.keys()
    # go through all keys(cities) in the dictionary, check if the name appears in the text section related to its province,
    # fetch the next number after the city name as the new-case number; if no such number exists, that means the city
    # contains all the cases within the province; find that number by locating the first number in the text section
    for city in city_list:
        for province in province_list:
            if city in province:
                city_case = province.split(city, 1)[1]
                try:
                    city_case_num = first_num(city_case)
                except ValueError:
                    city_case_num = first_num(province)
                dict[city][mode] = city_case_num

# a simple function to locate the first occurrence of a number in a string
def first_num(txt):
    num_str = ""
    first = False
    for char in txt:
        if char.isdigit():
            num_str += char
            first = True
        else:
            if first:
                return int(num_str)
    return int(num_str)

