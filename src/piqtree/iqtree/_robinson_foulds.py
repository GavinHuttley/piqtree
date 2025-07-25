"""Python wrappers to RF distances in the IQ-TREE library."""

from collections.abc import Sequence

import cogent3
import numpy as np
from _piqtree import iq_robinson_fould

from piqtree.iqtree._decorator import iqtree_func

iq_robinson_fould = iqtree_func(iq_robinson_fould)


def robinson_foulds(trees: Sequence[cogent3.PhyloNode]) -> np.ndarray:
    """Pairwise Robinson-Foulds distance between a sequence of trees.

    For the given collection of trees, returns a numpy array containing
    the pairwise distances between the trees.

    Parameters
    ----------
    trees : Sequence[cogent3.PhyloNode]
        The sequence of trees to calculate the pairwise Robinson-Foulds
        distances of.

    Returns
    -------
    np.ndarray
        Pairwise Robinson-Foulds distances.

    """
    pairwise_distances = np.zeros((len(trees), len(trees)))
    for i in range(1, len(trees)):
        for j in range(i):
            rf = iq_robinson_fould(str(trees[i]), str(trees[j]))
            pairwise_distances[i, j] = rf
            pairwise_distances[j, i] = rf
    return pairwise_distances
