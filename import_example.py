#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def rater_loop(data_dirs):
    dfs=[]
    for idir in data_dirs:
        files = glob.glob(idir + '*.csv')
        sub_dfs = []
        for file in files:
            # read in scored file
            df = pd.read_csv(file,header=0)
            # option to spread idea units into 1 per row
            # df = df.set_index(['sub_id','response','para','sent']).stack().str.split(',',expand=True).stack().unstack(-2).reset_index(-1,drop=True).reset_index()
            sub_dfs.append(df)
        # create 1 df from n subject df's
        dfs.append(pd.concat(sub_dfs, ignore_index = True))
    return dfs

bdir = '/dir/dir/'
data_dirs =[bdir + 'wbr_scored/',bdir + 'lia_scored/',bdir + 'reesha_scored/']
dfs= rater_loop(data_dirs)