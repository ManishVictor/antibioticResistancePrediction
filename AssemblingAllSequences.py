import os
#from Bio import SeqIO
pwd = os.getcwd()
for files in ['aminoglycoside_model_a_out',\
                  'aminoglycoside_model_b_out',\
                  'aminoglycoside_model_c_out',\
                  'aminoglycoside_model_d_out',\
                  'aminoglycoside_model_e_out',\
                  'aminoglycoside_model_f_out',\
                  'aminoglycoside_model_g_out',\
                  'aminoglycoside_model_h_out',\
                  'aminoglycoside_model_i_out',\
                  'class_a_out',\
                  'class_b_1_2_out',\
                  'class_b_3_out',\
                  'class_c_out',\
                  'class_d_1_out',\
                  'class_d_2_out',\
                  'erm_type_a_out',\
                  'erm_type_f_out',\
                  'mph_out',\
                  'qnr_out',\
                  'tet_efflux_out',\
                  'tet_enzyme_out',\
                  'tet_rpg_out']:
    lof = os.listdir(os.path.join(pwd,files))
    for each in lof:
        if('retrieved-contigs.fasta' in each):
            with open(os.path.join(pwd,files,each),'r') as f1:
                rdf1 = f1.readlines()
            for every in rdf1:
                with open('All_predictted.fasta','a') as f2:
                    f2.write(every)