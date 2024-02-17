# Datacamp EDA

# import pandas as pd
# Books = pd.read_csv('C:/Users/candy850225/Desktop/python練習資料/clean_books.csv')

# #validate the data type
# print(Books.dtypes)
# #update data type (可以填入float, int, str, category, datetime)
# print(Books['year'].astype(int))
# #validate categorical data
# print(Books['genre'].isin(['Non Fiction','Fiction']))
# #沒有包含在category中的標成true
# ~Books['genre'].isin(['Non Fiction','Fiction'])
# #過濾出特定category的: Non Fiction以及Fiction
# print(Books[Books['genre'].isin(['Non Fiction','Fiction'])])
# #agg: aggregate functions acorss a dataframe  
# print(Books.groupby('genre')['rating'].agg(['max', 'min']).head())
# #specify agg for columns: 使用dic (欄位: statistics方法)
# dic = {'rating':['min', 'max'], 'year': 'median'}
# print(Books.agg(dic))
# #新增新欄位
# print(Books.groupby('genre').agg(
#     mean_rating = ('rating', 'mean'),
#     median_rating = ('rating','median')
# ))

# #check missing data
# print(Books.isna().sum())
#no missing data so let's use new data!
import pandas as pd
#加入parse把資料型態改成datetime
Divorce = pd.read_csv('C:/Users/candy850225/Desktop/python練習資料/divorce.csv')


#check missing data
print(Divorce.isna().sum())
#先設置missing value最多數目
#若小於，可以直接drop!無傷大雅
threshold = len(Divorce) * 0.05
print(threshold)
columns_to_drop = Divorce.columns[Divorce.isna().sum() <= threshold] 
print(columns_to_drop)
#drop missing values
print(Divorce.dropna(subset = columns_to_drop, inplace = True))
#若大於，用statistics去取代
Divorce = Divorce['num_kids'].fillna(Divorce['num_kids'].median())
#就沒有missing values了!
print(Divorce.isna().sum())


#看data中有無特定的字，跑不出來
#Divorce['education_man'].str.contains('Secondary'|'Professional')
#取代，跑不出來
#Divorce['marriage_date'].str.replace('/','')
#移除單個字或是符號
#Divorce['marriage_date'].str.strip('$')

#上述parse_dates也可以改成pd.to_datetime
pd.to_datetime(Divorce['marriage_date'])
#只取年、月、日
Divorce['marriage_month'] = Divorce['marriage_date'].dt.month

#.duplicates(subset= list of col we want to look for dup , keep= )
#.drop_duplicates(subset= list of col we want to look for dup , keep=   ,inplace= 是否要drop dup,答TorF)
