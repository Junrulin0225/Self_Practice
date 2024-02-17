import pandas as pd
Airlines = pd.read_csv('C:/Users/candy850225/Desktop/python練習資料/airlines_final.csv')

#先觀察
# print(Airlines['dest_region'].value_counts())
# print(Airlines['dest_size'].value_counts())
# print(Airlines['dest_region'].unique())
# print(Airlines['dest_size'].unique())

#處理大寫
Airlines['dest_region'] = Airlines['dest_region'].str.lower()
#取代
Airlines['dest_region'] = Airlines['dest_region'].replace({'eur':'europe'})

#處理空格
Airlines['dest_size'] = Airlines['dest_size'].str.strip()

print(Airlines['dest_region'].unique())
print(Airlines['dest_size'].unique())

