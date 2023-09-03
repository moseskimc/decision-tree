from decision_tree.base import DecisionTree


class RegressionTree(DecisionTree):

    def __init__(
        self,
        is_target_categorical=False,
        max_depth=None,
        min_samples_split=None,
        min_information_gain=1e-10,
        max_categories=20
    ):
        super().__init__(
            is_target_categorical,
            max_depth,
            min_samples_split,
            min_information_gain,
            max_categories
        )

    # implement regression-specific methods
