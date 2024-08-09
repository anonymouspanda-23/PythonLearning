import threading


class Person:
    __instance = None
    __initialized = False
    __lock = threading.Lock()

    def __new__(cls, name: str, age: int):
        # Check if class has instance.
        if cls.__instance is None:
            # Acquire thread lock.
            with cls.__lock:
                # Check if class has instance as it might
                # have been created by another thread already.
                if cls.__instance is None:
                    print("Creating new instance of Person.")
                    cls.__instance = super(Person, cls).__new__(cls)
                    cls.__initialized = False

        return cls.__instance

    def __init__(self, name: str, age: int):
        if not self.__initialized:
            with self.__lock:
                if not self.__initialized:
                    print("Initializing new instance of Person.")
                    self.name: str = name
                    self.age: int = age
                    self.__initialized = True


# Function to be executed by each thread
def create_singleton(name, age):
    instance = Person(name, age)
    print(f"Instance ID: {id(instance)}, Name: {instance.name}, Age: {instance.age}")
    return instance


# Create a list to store threads
threads = []
instance_ids = []

# Start multiple threads
for i in range(10):
    thread = threading.Thread(
        target=lambda: instance_ids.append(
            create_singleton(
                f"Name_{i}",
                20 + 1
            )
        )
    )

    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# After all threads complete, verify that only one instance was created
print(f"Total instances created: {len(set(id(instance_id) for instance_id in instance_ids))}")
