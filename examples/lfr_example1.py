from sbm.sbm import SBM

from lfr.lfr import LFR

model = {}
model['lfr_N'] = 1200  # the number of nodes
model['lfr_tau1'] = 2.2
model['lfr_tau2'] = 2.3
model['lfr_mu'] = 0.35
model['lfr_min_degree'] = 1
model['lfr_min_community'] = 120

output_file = "../outputs/lfr_synthetic_"
output_file += "n{}_tau1{}_tau2{}_mindeg{}_mincom{}.gml".format(model['lfr_N'], model['lfr_tau1'], model['lfr_tau2'], model['lfr_min_degree'], model['lfr_min_community'])

lfr = LFR(model=model)
lfr.build_graph()
g = lfr.get_graph()
lfr.save_graph(output_file)

