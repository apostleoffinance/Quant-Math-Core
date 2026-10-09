from returns import simple_return
from compounding import compound_value

print(simple_return(110, 100))     # 0.10
print(simple_return(90, 100))      # -0.10
print(compound_value(100, 0.10, 3))  # 133.10
print(compound_value(1000, 0.05, 10))  # 1628.89...