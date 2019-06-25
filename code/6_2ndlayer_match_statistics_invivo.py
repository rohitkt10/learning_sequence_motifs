from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os, sys
import numpy as np
import pandas as pd
import helper

#------------------------------------------------------------------------------------------------

arid3 = ['MA0151.1', 'MA0601.1', 'PB0001.1']
cebpb = ['MA0466.1', 'MA0466.2']
fosl1 = ['MA0477.1']
gabpa = ['MA0062.1', 'MA0062.2']
mafk = ['MA0496.1', 'MA0496.2']
max1 = ['MA0058.1', 'MA0058.2', 'MA0058.3']
mef2a = ['MA0052.1', 'MA0052.2', 'MA0052.3']
nfyb = ['MA0502.1', 'MA0060.1', 'MA0060.2']
sp1 = ['MA0079.1', 'MA0079.2', 'MA0079.3']
srf = ['MA0083.1', 'MA0083.2', 'MA0083.3']
stat1 = ['MA0137.1', 'MA0137.2', 'MA0137.3', 'MA0660.1', 'MA0773.1']
yy1 = ['MA0095.1', 'MA0095.2']

motifs = [[''],arid3, cebpb, fosl1, gabpa, mafk, max1, mef2a, nfyb, sp1, srf, stat1, yy1]
motifnames = [ '','arid3', 'cebpb', 'fosl1', 'gabpa', 'mafk', 'max', 'mef2a', 'nfyb', 'sp1', 'srf', 'stat1', 'yy1']

#----------------------------------------------------------------------------------------------------

# 2nd layer of cnn-1
model_name = 'cnn_1'
num_trials = 5
results_qvalue = []
results_match_fraction = []
results_match_any = []
results_coverage = []
for trial in range(num_trials):

    # save path
    results_path = os.path.join('../results', 'invivo_'+str(trial))
    save_path = os.path.join(results_path, 'conv_filters')

    trial_match_any = []
    trial_qvalue = []
    trial_match_fraction = []
    trial_coverage = []
    for trial in range(num_trials):
        file_path = os.path.join(save_path, model_name+'_2ndlayer', 'tomtom.txt')
        best_qvalues, best_match, min_qvalue, match_fraction  = helper.match_hits_to_ground_truth(file_path, motifs, size=128)
        trial_qvalue.append(min_qvalue)
        trial_match_fraction.append(match_fraction)
        trial_coverage.append((len(np.where(min_qvalue != 1)[0])-1)/12)
        
        df = pd.read_csv(os.path.join(file_path), delimiter='\t')
        trial_match_any.append(len(np.unique(df['#Query ID']))/128)

    results_qvalue.append(trial_qvalue)
    results_match_fraction.append(trial_match_fraction)
    results_match_any.append(trial_match_any)
    results_coverage.append(trial_coverage)
results_qvalue = np.array(results_qvalue)
print("%s &  %.3f$\pm$%.3f &  %.3f$\pm$%.3f  \\\\"%(model_name, 
                                              np.mean(results_match_any), 
                                              np.std(results_match_any),
                                              np.mean(results_match_fraction), 
                                              np.std(results_match_fraction) ) )



# 2nd layer of cnn-1-3
model_name = 'cnn_1_3'
num_trials = 5
results_qvalue = []
results_match_fraction = []
results_match_any = []
results_coverage = []
for trial in range(num_trials):

    # save path
    results_path = os.path.join('../results', 'invivo_'+str(trial))
    save_path = os.path.join(results_path, 'conv_filters')

    trial_match_any = []
    trial_qvalue = []
    trial_match_fraction = []
    trial_coverage = []
    for trial in range(num_trials):
        file_path = os.path.join(save_path, model_name+'_2ndlayer', 'tomtom.txt')
        best_qvalues, best_match, min_qvalue, match_fraction  = helper.match_hits_to_ground_truth(file_path, motifs, size=128)
        trial_qvalue.append(min_qvalue)
        trial_match_fraction.append(match_fraction)
        trial_coverage.append((len(np.where(min_qvalue != 1)[0])-1)/12)
        
        df = pd.read_csv(os.path.join(file_path), delimiter='\t')
        trial_match_any.append(len(np.unique(df['#Query ID']))/128)

    results_qvalue.append(trial_qvalue)
    results_match_fraction.append(trial_match_fraction)
    results_match_any.append(trial_match_any)
    results_coverage.append(trial_coverage)
results_qvalue = np.array(results_qvalue)
print("%s &  %.3f$\pm$%.3f &  %.3f$\pm$%.3f  \\\\"%(model_name, 
                                              np.mean(results_match_any), 
                                              np.std(results_match_any),
                                              np.mean(results_match_fraction), 
                                              np.std(results_match_fraction) ) )



# 3rd layer of cnn-1-3
model_name = 'cnn_1_3'
num_trials = 5
results_qvalue = []
results_match_fraction = []
results_match_any = []
results_coverage = []
for trial in range(num_trials):

    # save path
    results_path = os.path.join('../results', 'invivo_'+str(trial))
    save_path = os.path.join(results_path, 'conv_filters')

    trial_match_any = []
    trial_qvalue = []
    trial_match_fraction = []
    trial_coverage = []
    for trial in range(num_trials):
        file_path = os.path.join(save_path, model_name+'_3rdlayer', 'tomtom.txt')
        best_qvalues, best_match, min_qvalue, match_fraction  = helper.match_hits_to_ground_truth(file_path, motifs, size=128)
        trial_qvalue.append(min_qvalue)
        trial_match_fraction.append(match_fraction)
        trial_coverage.append((len(np.where(min_qvalue != 1)[0])-1)/12)
        
        df = pd.read_csv(os.path.join(file_path), delimiter='\t')
        trial_match_any.append(len(np.unique(df['#Query ID']))/128)

    results_qvalue.append(trial_qvalue)
    results_match_fraction.append(trial_match_fraction)
    results_match_any.append(trial_match_any)
    results_coverage.append(trial_coverage)
results_qvalue = np.array(results_qvalue)
print("%s &  %.3f$\pm$%.3f &  %.3f$\pm$%.3f  \\\\"%(model_name, 
                                              np.mean(results_match_any), 
                                              np.std(results_match_any),
                                              np.mean(results_match_fraction), 
                                              np.std(results_match_fraction) ) )


