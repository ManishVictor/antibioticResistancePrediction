import os
from Bio import SeqIO
#_____________________________________________________
def making_list_for_folders(in_path):
    folders_lv1 = os.listdir(in_path)
    lof = []
    for folders1 in folders_lv1:
        try:
            expression = ("{}/predictedGenes/predicted-orfs-amino.fasta").format(folders1)
            lof.append(expression)
        except FileNotFoundError:
            continue
    return(lof)
#_____________________________________________________
in_path = '/data/prosjekt/15719-Res-Marine/Project_Work/Project_Wastewater/_4_fARGene/fargene_YtreSandviken_out'
out_path = '/data/prosjekt/15719-Res-Marine/Project_Work/Project_Wastewater/_4_fARGene/fargene_YtreSandviken_out'
#_____________________________________________________
count = 0
model_files = making_list_for_folders(in_path)
#print(model_files)
test = []
for ffiles in model_files:
    header1 = ffiles.split('/')[0]
    if (header1 not in test):
        test.append(header1)
        count = 0
    #print(header1)
    try:
        for Seq in SeqIO.parse(os.path.join(in_path,ffiles),'fasta'):
            #print(Seq.seq)
            count +=1
            with open(os.path.join(out_path,'fargene_YtreSandviken_out_headers.fasta'),'a') as file1:
                file1.write(('>{}_{}_{}\t{}\n').format('YtreSandviken_out',header1,count,Seq.id))
    except (NotADirectoryError,FileNotFoundError):
        continue
