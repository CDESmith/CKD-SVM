import loader as l
import check as ch
import prepare as p

DATASET_FILE='ckd_data.csv'

dataset=l.loadDataset(DATASET_FILE)

p.prepare(dataset)