
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('ggplot')

CB91_Pink = '#F3A0F2'
CB91_Blue = '#2CBDFE'
CB91_Green = '#47DBCD'

CB91_Purple = '#9D2EC5'
CB91_Violet = '#661D98'
CB91_Amber = '#F5B14C'

color_list = [CB91_Blue, CB91_Pink, CB91_Green, CB91_Amber,
              CB91_Purple, CB91_Violet]

plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_list)

df = pd.DataFrame({
    'name':['john','mary','peter','jeff','bill','lisa','jose'],
    'age':[23,78,22,19,45,33,20],
    'gender':['M','F','M','M','M','F','M'],
    'state':['california','dc','california','dc','california','texas','texas'],
    'num_children':[2,0,0,3,2,1,4],
    'num_pets':[5,1,0,5,2,2,3]
})

df.plot(kind = 'scatter', x = 'num_children', y = 'num_pets', color = CB91_Pink)

df.plot(kind = 'bar', x = 'name', y = 'age')

plt.clf()
ax = plt.gca()


df.plot(kind = 'line', x = 'name', y = 'num_children', ax = ax)
df.plot(kind = 'line', x = 'name', y = 'num_pets', ax = ax) #color = 'red')

df.groupby(['state','gender']).size().unstack().plot(kind='bar',stacked=True)

