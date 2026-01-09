import os
cp = '/data/prosjekt/15719-Res-Marine/Project_Work/Holen_Hospital/Holen_in_Apr/Sample_16-2023-645/fARGene'  # Remember to make changes here #
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
        os.system(('rm -rf {}').format(os.path.join(cp,files,'_dblast.tsv')))
        run_file = os.listdir(os.path.join(cp,files))
        for each in run_file:
            #try:
            if('predictedNamesChnged.fasta' in each):
                file_run = str(each)
        #for ffiles in ['predictedGenes/predicted-orfs-amino.fasta']:
        try:
            os.system(('diamond \
                blastp \
                --threads {thrd_count} \
                --db {path_to_nrDB} \
                --out {out_filename} \
                --outfmt 6 qseqid qtitle qstrand qlen qstart qend qseq sallseqid stitle slen sstart send evalue pident nident mismatch gapopen gaps \
                --query {path_query_file} \
                --evalue 0.00005 \
                --query-cover 90 \
                --quiet \
                --header \
                --max-target-seqs 1').format(thrd_count = 256, path_to_nrDB = '/data/prosjekt/15719-Res-Marine/database/NR_DB/nr.dmnd', \
                               out_filename= os.path.join(cp,files,'_dblast.tsv'), \
                               path_query_file = os.path.join(cp,files,file_run)))
        except:
            continue


