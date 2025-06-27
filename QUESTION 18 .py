# Question 18: Abstract Class: Farm Task
import abc
class FarmTask(abc.ABC):
    @abc.abstractmethod
    def execute(self):
        pass
class PloughingTask(FarmTask):
    def execute(self, field):
        print(f"Executing ploughing on Field {field}")
class SowingTask(FarmTask):
    def execute(self, field, crop):
        print(f"Executing sowing of {crop} on Field {field}")
ploughing = PloughingTask()
sowing = SowingTask()
print("Question 18:")
ploughing.execute("A")
sowing.execute("B", "Maize")
print("-" * 20)
