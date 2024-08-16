class GenericProcessor:
    def __init__(self, target_supplier):
        self.target_supplier = target_supplier
        self.transformations = []

    # Factory method (simple and clear).
    @staticmethod
    def of(target):
        return GenericProcessor(lambda: target)

    def transform(self, transformation):
        # Add transformations.
        self.transformations.append(transformation)
        return self

    def process(self):
        # Process all transformations.
        result = self.target_supplier()

        for transformation in self.transformations:
            result = transformation(result)

        return result
