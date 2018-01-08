import sympy
import math



class SampleProbability:
    def __init__(self, data_size, sample_size, violation):
        self.data_size = data_size
        self.sample_size = sample_size
        self.violation = violation

    def max_unique_prob(self, sample_violation):
        first = sympy.binomial(self.violation, sample_violation)
        sigma = 0
        for j in range(self.sample_size - 2 * sample_violation + 1):
            sigma += sympy.binomial(self.violation - sample_violation, j) * math.pow(2, j) * sympy.binomial(
                self.data_size - 2 * self.violation, self.sample_size - 2 * sample_violation - j)
        p = first * sigma / sympy.binomial(self.data_size, self.sample_size)

        return p

    def min_unique_prob(self, sample_violation):
        n_i = (1 + math.sqrt(1 + 8 * sample_violation)) / 2
        if n_i.is_integer():
            k = math.ceil((1 + math.sqrt(1 + 8 * self.violation)) / 2)
            p = sympy.binomial(k, n_i) * sympy.binomial(self.data_size - k,
                                                        self.sample_size - n_i) / sympy.binomial(
                self.data_size, self.sample_size)
            return p
        return 0

# # Primial test
#
# sp = SampleProbability(6, 4, 3)
# i = 3
# print "min is :"
# print sp.min_unique_prob(i)
# print "max is :"
# print sp.max_unique_prob(i)


