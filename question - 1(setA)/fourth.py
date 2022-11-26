from sklearn.preprocessing import LabelEncoder
label_en=LabelEncoder() 

x['sex']=label_en.fit_transform(x['sex'])
x['region']=label_en.fit_transform(x['region'])
x['married']=label_en.fit_transform(x['married'])
x['save_act']=label_en.fit_transform(x['save_act'])
x['current_act']=label_en.fit_transform(x['current_act'])
x['mortgage']=label_en.fit_transform(x['mortgage'])
x['pep']=label_en.fit_transform(x['pep'])

plt.figure(figsize=(20,20))

sns.heatmap(x.corr(),annot=True)
