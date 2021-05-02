import numpy as np
import matplotlib.pylab as plt


X_ticks=[]
fig, ax = plt.subplots(constrained_layout=True)

Activity_types = ( 'IC50', 'Ki', 'Kd', 'EC50','AC50','Potency','Inhibition', 'Activity', 'Other')
y_pos = np.arange(len(Activity_types))
number = [1153137, 674982,76116, 154434, 109449, 2958414,459944,254147, 238057 ]

plt.bar(y_pos, number, align='center', alpha=0.5)
plt.xticks(y_pos, Activity_types)
#plt.ylabel('Endpoint measurements (in millions)')
plt.title('Distribution of bioactivity types')
#ax.ticklabel_format(style='sci',scilimits=None, axis='y') 
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xticks(rotation=90)

ax.ticklabel_format(style='sci',axis='y')

ax.set_ylim([0,3000000])
#plt.show()

#plt.bar(x, mone
#plt.xticks(x, ('Bill', 'Fred', 'Mary', 'Sue'))

ax.set_ylabel('Endpoint measurements (in millions)')
#axs.set_xlabel('% Shared target space')


fig.savefig('Bioactivity_types_distribution.jpeg',dpi=900, orientation='portrait',  transparent=False)

plt.show()