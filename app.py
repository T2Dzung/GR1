from cpm import *
from estimated_resource_smoothing import *
from burgess_procedure import *

def main():
    cor = 'correlations.csv'
    dur = 'duration.csv'
    res = 'resources.csv'

    cpm = None
    node_matrix = None
    result = []

    cpm = CPM()
    cpm.find_all_activity_informations(cor, dur, res, 8)
    node_matrix = cpm.get_node_matrix()
    # print(node_matrix)

    # ==== Estimated Method ===== #
    estimatedSmoothing = EstimatedResourceSmoothing(node_matrix)
    estimatedSmoothing.estimate_optimal_schedule()

    # # ==== Burgess Procedure ===== #
    burgessProcedure = BurgessProcedure(node_matrix)
    burgessProcedure.estimate_optimal_schedule()
  

main()

    