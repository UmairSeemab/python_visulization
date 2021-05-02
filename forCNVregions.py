################ To draw CNV regions at chromosomes #######################

import matplotlib.pyplot as plt
import numpy as np
file=open('chromosizes.txt',"r")
chrom_sizes=file.readlines()
file.close()

file=open('scRNA_del.txt',"r")
region2=file.readlines()
file.close()

file=open('WGS_del_loose.txt',"r")
region1=file.readlines()
file.close()

Chr_locations=[]
region_loc1=[]
region_loc2=[]


    #region_loc2.append(float(region2[i][2]))

for i in range(len(chrom_sizes)):  
    chrom_sizes[i]=chrom_sizes[i].replace("\n","")          
    chrom_sizes[i]=chrom_sizes[i].split("\t")
    Chr_locations.append(float(chrom_sizes[i][1]))

# Fixing random state for reproducibility


# Example data
plt.rcdefaults()
fig, ax = plt.subplots()
chr_names = ('chr1','chr2','chr3','chr4','chr5','chr6','chr7', 'chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY')
y_pos = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
Chr_locations=np.array(Chr_locations)

region_loc1=np.array(region_loc1)
region_loc2=np.array(region_loc2)

ax.barh(y_pos, Chr_locations,  align='center',color='#FADA5E')
for i in range(len(region1)-1):  
    region1[i]=region1[i].replace("\n","")          
    region1[i]=region1[i].split("\t")
    chr_index=region1[i][0]
    chr_index=float(chr_index[3:len(chr_index)])
    ax.broken_barh([(float(region1[i][1]), float(region1[i][2])-float(region1[i][1]))], (chr_index-0.3, 0.2), facecolors ='tab:blue',zorder=10) 

region1[i+1]=region1[i+1].replace("\n","")          
region1[i+1]=region1[i+1].split("\t")
chr_index=region1[i+1][0]
chr_index=float(chr_index[3:len(chr_index)])
ax.broken_barh([(float(region1[i+1][1]), float(region1[i+1][2])-float(region1[i+1][1]))], (chr_index-0.3, 0.2), facecolors ='tab:blue',zorder=10, label='WGS') 

for i in range(len(region2)-1):  
    region2[i]=region2[i].replace("\n","")          
    region2[i]=region2[i].split("\t")
    chr_index=region2[i][0]
    chr_index=float(chr_index[3:len(chr_index)])
    ax.broken_barh([(float(region2[i][1]), float(region2[i][2])-float(region2[i][1]))], (chr_index+.1, 0.2), facecolors ='tab:red',zorder=10) 
region2[i+1]=region2[i+1].replace("\n","")          
region2[i+1]=region2[i+1].split("\t")
chr_index=region2[i+1][0]
chr_index=float(chr_index[3:len(chr_index)])
ax.broken_barh([(float(region2[i+1][1]), float(region2[i+1][2])-float(region2[i+1][1]))], (chr_index+.1, 0.2), facecolors ='tab:red',zorder=10,label='ScRNA') 


ax.set_yticks(y_pos)
ax.set_yticklabels(chr_names)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Chromosome location')
ax.legend()

#fig.savefig('/Users/rehmanzu/Desktop/Umair/WGS-del_scRNA-del-F-1.jpg',dpi=300, orientation='portrait',  transparent=False )

plt.show()
