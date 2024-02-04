import math
# print(math.ceil(1.2))


# def loan_emi(amount,duration,rate,down_payment = 0):
#     loan_amount = amount-down_payment
#     emi = loan_amount*rate*((1+rate)**duration)/(((1+rate)**duration)-1)
#     emi = math.ceil(emi)
#     return emi
# print(loan_emi(1260000,10*12,0.08/12))
'''
def loan_emi(amount,duration,rate,down_payment = 0):
    loan_amount = amount-down_payment
    try:
        emi = loan_amount*rate*((1+rate)**duration)/(((1+rate)**duration)-1)
    except ZeroDivisionError:
        emi = loan_amount/duration
    emi = math.ceil(emi)
    return emi
'''
# emi_with_interest = loan_emi(amount = 100000,duration= 10*12 ,rate=0.09/12)
# print(emi_with_interest)


# emi_without_interest = loan_emi(amount = 100000,duration= 10*12 ,rate=0./12)
# print(emi_without_interest)

# total_interest = (emi_with_interest-emi_without_interest) * 10*12
# print(total_interest)


'''excercise'''

# def cost_of_trip(tickets,hotel,carweekly,days):
#     weeks = math.ceil(days/7)
#     cost = tickets+ (hotel*days)+ (carweekly*weeks)
#     return cost

# no_days = int(input("days:"))
# paris_trip = cost_of_trip(200,20,200,no_days)
# # print(paris_trip)
# london_trip = cost_of_trip(250,30,120,no_days)
# dubai_trip = cost_of_trip(370,15,80,no_days)
# mumbai_trip = cost_of_trip(450,10,70,no_days)

# least_cost = min(paris_trip,london_trip,dubai_trip,mumbai_trip)

# if least_cost == paris_trip:
#     print("Paris")
# elif least_cost == london_trip:
#     print("London")
# elif least_cost == dubai_trip:
#     print("Dubai")
# elif least_cost == mumbai_trip:
#     print("Mumbai")

'''wrong downside'''

# Paris=[200,20,200,'Paris']
# London = [250,30,120,'London']
# Dubai = [370,15,80,'Dubai']
# Mumbai = [450,10,70,'Mumbai']
# Cities = [Paris,London,Dubai,Mumbai]

# def cost_of_trip(flight,hotel_cost,car_rent,num_of_days=0):
#     return flight+(hotel_cost*num_of_days)+(car_rent*math.ceil(num_of_days/7))
# def given_budget(budget,less_days=False):
#     days = 1
#     cost = 0
#     while cost<budget:
#         cost_before = cost
#         try:
#             costs_before = cost
#         except: 
#             costs_before=costs.copy()
#         costs={}
#         for city in Cities:
#             cost = cost_of_trip(city[0],city[1],city[2],days)
#             costs[cost] = city[3]
#         if less_days:
#             cost = max(list(costs.keys()))
#             if cost>=budget:
#                 return costs_before[cost_before],days-1
#         else:
#             cost = min(list(costs.keys()))
#             if cost>= budget:
#                 return costs_before[cost_before],days-1
#         days+=1

# maxxii = given_budget(600)
# print(maxxii)

'''Interaction with OS and filesystem'''

import os
os.getcwd()
# help(os.listdir)
os.listdir('.')
# os.listdir('/usr')
os.makedirs('./data',exist_ok = True)
'data' in os.listdir('.')
os.listdir('./data')


'''retriving data from url using urllib module'''

url1 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt'
url2 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans2.txt'
url3 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans3.txt'
import urllib.request
urllib.request.urlretrieve(url1, './data/loan1.txt')
urllib.request.urlretrieve(url2, './data/loan2.txt')
urllib.request.urlretrieve(url3, './data/loan3.txt')


'''checking the files in the directory'''
# print(os.listdir('./data'))


'''contents in file1'''

file1 = open('./data/loan1.txt','r')
file1_content = file1.read()
# print("file1",file1_content)
file1.close()


'''contents in file2'''

with open('./data/loan2.txt','r') as file2:
    file2_content = file2.read()
    # print("file2",file2_content)


'''contents in file3'''

with open('./data/loan3.txt','r') as file3:
    file3_lines = file3.readlines()
# print("file3",file3_lines)

# file3_lines

'''defining a function to separate header from the data '''

def parse_header(header):
    return header.strip().split(',') #strip is used to remove spaces and newline character
file3_lines[0]
headers = parse_header(file3_lines[0])
# print("headers",headers)


'''defining a function to parse the values of the data'''
def parse_values(data_line):
    values = []
    for item in data_line.strip().split(","):
        if item=="" :
            values.append(0.00)
        else:
            try:
                values.append(float(item))
            except ValueError:
                values.append(item)
    return values
# print(parse_values(file3_lines[1]))
# print(parse_values(file3_lines[2]))


'''creating dictionary of the values and headers '''

# def create_item_dict(values,headers):
#     item_dict = dict(zip(headers,values))
#     return item_dict
# v1 = parse_values(file3_lines[1])
# item1 = create_item_dict(v1,headers)
# print(item1)


'''creating a function to read and form a list of dictionaries containing headers and vaules'''

def read_csv(path):
    result = []
    with open(path,'r') as file:
        file_lines = file.readlines()
    head = parse_header(file_lines[0])
    for item in file_lines[1:]:
        value = parse_values(item)
        dictaa = dict(zip(head,value))
        result.append(dictaa)
    return result

# print(read_csv("./data/loan1.txt"))


'''measures emi'''

def loan_emi(amount,duration,rate,down_payment = 0):
    loan_amount = amount-down_payment
    try:
        emi = loan_amount*rate*((1+rate)**duration)/(((1+rate)**duration)-1)
    except ZeroDivisionError:
        emi = loan_amount/duration
    emi = math.ceil(emi)
    return emi

'''computing emi and addding emi to the loan data'''
def compuṭe_emis(loans):
    for loan in loans:
        emi = loan_emi(loan['amount'],loan['duration'],loan["rate"]/12,loan['down_payment'])
        loan['emi'] = emi


loan2 = read_csv('./data/loan2.txt')
compuṭe_emis(loan2)
# print(loan2)


'''converting data to CSV with emi'''

with open('./data/emi2.txt','w') as file_emi:
    for loan in loan2:

        loner = "{},{},{},{},{}\n".format(
            loan['amount'], 
            loan['duration'], 
            loan['rate'], 
            loan['down_payment'], 
            loan['emi']
        )
        # loner = str(loan['amount'])+str(loan['duration'])+str(loan['rate'])+str(loan['down_payment'])+str(loan['emi'])+"\n"
        file_emi.write(loner)


# print(os.listdir('./data'))
with open("./data/emi2.txt",'r') as f:
    emi2 = f.read()
    # print(emi2)


'''a function that writes the file in CSV format including headers'''

def write_csv(items,path):
      with open(path, 'w') as f:
        # Return if there's nothing to write
        if len(items) == 0:
            return
        
        # Write the headers in the first line
        headers = list(items[0].keys())
        f.write(','.join(headers) + '\n')
        
        # Write one item per line
        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, "")))
            f.write(','.join(values) + "\n")
    # with open(path,'w') as f:
    #     if len(items) ==0:
    #         return
    #     headers = list(items[0].keys)
    #     f.write(','.join(headers),"\n")
    #     for item in items:
    #         value = list(item.values())
    #         f.write(",".join(value),"\n")

# loan3 = read_csv('./data/loan3.txt')

# compuṭe_emis(loan3)
# write_csv(loan3,'./data/emi3.txt')

# with open("./data/emi3.txt",'r') as f:
#     print(f.read())

for i in range(1,4):
    loans = read_csv('./data/loan{}.txt'.format(i))
    compuṭe_emis(loans)
    write_csv(loans, './data/emi{}.txt'.format(i))

# import pandas as pd

# movies_url = "https://gist.githubusercontent.com/aakashns/afee0a407d44bbc02321993548021af9/raw/6d7473f0ac4c54aca65fc4b06ed831b8a4840190/movies.csv"
# urllib.request.urlretrieve(movies_url,"./data/movie.csv")
# movie_dataframe = pd.read_csv("./data//movie.csv")
# print(movie_dataframe)




