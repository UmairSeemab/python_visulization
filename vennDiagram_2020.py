from matplotlib_venn import venn2, venn2_circles
from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

file=open('study_data_3.csv',"r")
studies=file.readlines()
file.close()
inchi_ccle=[]
inchi_gdsc=[]
inchi_ctrpv2=[]
cell_ccle=[]
cell_gdsc=[]
cell_ctrpv2=[]


for i in range(1,len(studies)):  
    print(i)
    studies[i]=studies[i].replace("\n","")         
    studies[i]=studies[i].replace('"','')     
    studies[i]=studies[i].split(";")
    if studies[i][2]=='ccle':
        inchi_ccle.append(studies[i][1])
        cell_ccle.append(str(studies[i][0]))
    elif studies[i][2]=='gdsc':
        inchi_gdsc.append(studies[i][1])
        cell_gdsc.append(str(studies[i][0]))
    elif studies[i][2]=='ctrpv2':
        inchi_ctrpv2.append(studies[i][1])
        cell_ctrpv2.append(str(studies[i][0]))

#inchi_ccle=sorted(set(inchi_ccle), key=inchi_ccle.index)  # get unique values out of list
#cell_ccle=sorted(set(cell_ccle), key=cell_ccle.index)
#inchi_gdsc=sorted(set(inchi_gdsc), key=inchi_gdsc.index)
#cell_gdsc=sorted(set(inchi_gdsc), key=inchi_gdsc.index)

#inchi_ctrpv2=sorted(set(inchi_ctrpv2), key=inchi_ctrpv2.index)
#cell_ctrpv2=sorted(set(inchi_ctrpv2), key=inchi_ctrpv2.index)

#lst1 = ["gene1", "gene2", "gene3", "gene4", "gene5", "gene6", "gene7", "gene8", "gene9", "gene10"]
#lst2 = ["gene0", "gene1", "gene2", "gene3", "gene8", "gene9", "gene10", "gene11", "gene12", "gene13"]
#lst3 = ["gene0", "gene4", "gene5", "gene8", "gene9", "gene10", "gene11", "gene13", "gene14", "gene15", "gene16"]
fig, axs = plt.subplots(constrained_layout=True)


inchi_venn=venn3([set(inchi_ccle), set(inchi_gdsc), set(inchi_ctrpv2)], set_labels = ('CCLE', 'GDSC', 'CTRPv2'))
plt.title('A) Overlapping compounds',fontsize=18)

for text in inchi_venn.set_labels:
    text.set_fontsize(18)
for x in range(len(inchi_venn.subset_labels)):
    if inchi_venn.subset_labels[x] is not None:
        inchi_venn.subset_labels[x].set_fontsize(18)

# fig.savefig('Overlapping_compounds.png',dpi=300, orientation='portrait',  transparent=False)
# plt.show()
#len(intersection(lst1, lst2))
#cell_venn=venn3(subsets=(104,163,254,25,34,71, 112), set_labels = ('CCLE', 'GDSC', 'CTRPv2'))

#cell_venn=venn3([set(cell_ccle), set(cell_gdsc), set(cell_ctrpv2)], set_labels = ('CCLE', 'GDSC', 'CTRPv2'))
#cell_venn=venn3([set(inchi_ccle), set(inchi_gdsc), set(inchi_ctrpv2)], set_labels = ('CCLE', 'GDSC', 'CTRPv2'))

# plt.title('B) Overlapping cell lines',fontsize=18)
# for text in cell_venn.set_labels:
#     text.set_fontsize(18)
# for x in range(len(cell_venn.subset_labels)):
#     if cell_venn.subset_labels[x] is not None:
#         cell_venn.subset_labels[x].set_fontsize(18)

fig.savefig('Overlapping_compounds.jpg',dpi=600, orientation='portrait',  transparent=False)

plt.show()
