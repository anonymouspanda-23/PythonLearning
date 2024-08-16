from typing import List

from generic_processor import GenericProcessor


# Pure function, does not and should not depend on anything else.
def multiply_by_2(values: List[float]):
    new_values = []

    for value in values:
        new_values.append(value * 2)

    return new_values


numbers = [1, 2, 3, 4]

# Targets numbers object, then pass in functions for processor to call.
result = GenericProcessor.of(numbers).transform(multiply_by_2).process()
print(result)

# Notice results are the same.
print(result)
