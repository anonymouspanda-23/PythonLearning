from generic_processor import GenericProcessor
from lazy_evaluator import multiply_by_2


def test_lazy_evaluator():
    values = [1, 2, 3, 4]

    result = GenericProcessor.of(values).transform(multiply_by_2).process()
    assert result == [2, 4, 6, 8]
