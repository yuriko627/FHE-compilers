import concrete
from concrete import fhe

def add(x, y):
    return x + y

compiler = fhe.Compiler(add, {"x": "encrypted", "y": "clear"})

# input set is a collection representing the typical inputs to the function
# you have to pass input set to a compiler when you compile the fucntion to a circuit
# input set is used to determine the bit widths and shapes of the variables within the function
# input set should be iterable tuples of the same length as the number of arguments of the function being compiled
inputset = [(2, 3)]
circuit = compiler.compile(inputset)

x = 4
y = 4

clear_evaluation = add(x, y)

# encrypt_run_decrypt: implemented as circuit.decrypt(circuit.run(circuit.encrypt(*args)))
# so it does everything at once
homomorphic_evaluation = circuit.encrypt_run_decrypt(x, y)

print(x, "+", y, "=", clear_evaluation, "=", homomorphic_evaluation)