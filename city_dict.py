import pandas

info = list()

# convert the data from the original excel form into a data structure that will be extensively used in this program
# The output is a python dictionary in the form of
# {'city_name_1': {'province': 'province_name', '本土': case#, '无症状': case#},...,'city_name_n':{...}}
def create_dict():
    global info
    excel = pandas.read_excel('./covid_frame[872].xlsx')
    city_dict = excel.to_dict('records')
    dict = {}
    for element in city_dict:
        dict[element['city']] = {'province' : element['province'] , '本土' : 0 , '无症状':0}
        element.pop('city', None)
        element.pop('province', None)
    # universal information such as city codes and province codes are stored into the info variable
    info = city_dict
    return dict

# due to the unpredictable nature of data_fetching on new cases for provinces, a function is supplied to calculate
# the total cases for each province by summing up the cases of each city/district
def province_add(dict):
    city_list = dict.keys()
    native = 0
    asymptomatic = 0
    for city_name in city_list:
        native += dict[city_name]['本土']
        asymptomatic += dict[city_name]['无症状']
        if city_name == dict[city_name]['province']:
            dict[city_name]['本土'] = native
            dict[city_name]['无症状'] = asymptomatic
            native = 0
            asymptomatic = 0


# this function transforms the data structure described above into a list of dictionaries that can be directory exported
# as an Excel file
def dict_out(dict_list):
    out = list()
    cities = list(dict_list[0][1].keys())
    props = list(dict_list[0][1].values())
    for i in range(len(cities)):
        out_dict = {'code': info[i]['code'], 'city': cities[i], 'province_code': info[i]['province_code'],
                    'province': props[i]['province']}
        for date, dic in dict_list:
            out_dict[date + "_本土"] = dic[cities[i]]['本土']
            out_dict[date + "_无症状"] = dic[cities[i]]['无症状']
        out.append(out_dict)
    return out

# exporting into excel form
def out_excel(dict):
    data = pandas.DataFrame(dict)
    print(data)
    data.to_excel(r'./covid.xlsx', index=False, header=True)