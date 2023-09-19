#230724 Datacamp - Data Manipulation with Pandas
import pandas as pd
#先建立表格
Penguins = pd.DataFrame({
'Name':['Nunu','Nono','Nope Nope','mini Pen','Big Pen'],
'Color':['blue','blue','blue','blue','blue'],
'Height(cm)':[15,12,10,8,8],
'Weight(kg)':[5,3,2,1,1],
'Nationality':['Japan','Japan','Japan','the Philippines','the Philippines'],
'Address':['USA','USA','Taiwan','USA','USA'],
'Date of Birth':['2018-11-10','2022-01-24','2022-02-25','2023-01-01','2023-01-01']
})
#print(Penguins)

#sort
print(Penguins.sort_values(['Height(cm)','Weight(kg)'], ascending=[True, True]))
#subset multiple columns
print(Penguins[['Name','Color']])
print(Penguins[Penguins['Date of Birth']>'2021-01-01'])
print(Penguins[Penguins['Weight(kg)']==1])
is_Japan = Penguins['Nationality'].isin(['USA','Japan'])
print(is_Japan)
#new columns
Penguins['Height(m)'] = Penguins['Height(cm)']/100
Penguins['bmi'] = Penguins['Weight(kg)']/Penguins['Height(m)']**2
Penguins['bmi'] = Penguins['bmi'].round(2)
print(Penguins)
bmi_less_than_200 = Penguins['bmi']<200
print(bmi_less_than_200)
#oldest penguin
print(Penguins['Date of Birth'].min())
#使用agg: 自製statistics公式
def pct30(column):
    return column.quantile(0.3)
print(Penguins[['Weight(kg)','Height(m)']].agg(pct30))

#drop duplicate items
Penguins_flying_class = pd.DataFrame({
'class_date':['2023-05-01','2023-05-01','2023-05-07','2023-05-07','2023-05-21','2023-05-22','2023-05-14','2023-05-15','2023-05-14'],
'Name':['Nunu','Nono','Nunu','Nono','Nope Nope','Nunu','Nope Nope','Nono','Nono'],
'attendence':['y','y','n','y','y','n','y','y','n']})
Penguins_flying_class.drop_duplicates(subset='class_date')

#count
print(Penguins_flying_class['attendence'].value_counts(sort=True))
##groupby,跑不出來因為我們資料不夠
#print(Penguins.groupby('Nationality')['Height(cm)'].agg([min,max,sum]))

#pivot table，不確定其實用性

#set a column as the index, index的重要性: make subsetting simpler
Penguins_index = Penguins.set_index('Name')
##remove the index
#print(Penguins_index.reset_index(drop=True))
#取特定列!gotcha!但要設置index才能這樣切!
print(Penguins_index.loc[['Nono','Big Pen']])
#visualizing our data!
import matplotlib.pyplot as plt
Penguins.plot(x='Name', y='bmi',kind='bar', xlabel='Penguin\'s name', ylabel='bmi', title= 'bmi for Beblo\'s penguins')
plt.show()
#看有無missing data
Penguins.isna()
#看各欄位(variable)有無missing data
print(Penguins.isna().any())
#remove missing data
Penguins.dropna()
#replace missing values with sth
Penguins.fillna(0)

#merge: inner join (如果要merge更多，on='col')\.merge(...!)
print(Penguins.merge(Penguins_flying_class, on = 'Name', suffixes='_1'))
#merge: merge vertically
print(pd.concat([Penguins,Penguins_flying_class]))
#select data with .query
print(Penguins.query('bmi >200'))
#unpivot: .melt(),表示把結合在一起的表格們打開

#計算特定欄位的數目
print(Penguins.value_counts('Nationality'))
#validate各欄位的data type
print(Penguins.dtypes)
#update data type,跑不出來, 試用新data: Book
#print(Penguins['Date of Birth'].astype(int))

#看某欄位有沒有特定的字
print(Penguins['Name'].str.contains('Nunu'))