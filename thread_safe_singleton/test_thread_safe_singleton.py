from thread_safe_singleton import Person


class NonSingleton:
    pass


def test_singleton():
    name = "name"
    age = 99
    assert Person(name, age) is Person(name, age)


def test_non_singleton():
    assert NonSingleton() is not NonSingleton()
