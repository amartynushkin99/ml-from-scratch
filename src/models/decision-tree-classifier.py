class MyTreeClf:
    def __init__(self, max_depth=5, min_samples_split=2, max_leafs=20):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.max_leafs = max_leafs

    def __str__(self):
        return (f"MyTreeClf class: max_depth={self.max_depth}, "
                f"min_samples_split={self.min_samples_split}, "
                f"max_leafs={self.max_leafs}")

    __repr__ = __str__