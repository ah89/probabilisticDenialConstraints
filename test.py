from probability import SampleProbability
import matplotlib.pyplot as plt

class Test:

    def prob_hist(self, samaple_size, number_of_violations_in_data, data_size):

        sp = SampleProbability(data_size, samaple_size, number_of_violations_in_data)
        x = []
        pmax = []
        pmin = []
        max_p_point = [0, 0]
        min_p_point = [0, 0]
        for i in range(0, samaple_size):
            x.append(i)
            max_p = sp.max_unique_prob(i)
            pmax.append(max_p)
            if max_p_point[1] < max_p:
                max_p_point = [i, max_p]

            min_p = sp.min_unique_prob(i)
            pmin.append(min_p)
            if min_p_point[1] < min_p:
                min_p_point = [i, min_p]

        fig = plt.figure(111)
        plt.title("Probability of max and min unique")
        plt.ylabel("Probability")
        plt.xlabel("number of violation in sample")
        plt.scatter(x, pmax, label='Max unique tuple')
        plt.scatter(x, pmin, label='Min unique tuple')
        leg = plt.legend(loc='upper right', ncol=2, mode="expand", shadow=True, fancybox=True)
        leg.get_frame().set_alpha(0.3)
        plt.grid(True)
        plt.show()

    def max_probability_point(self, samaple_size, number_of_violations_in_data, data_size):

        x = []
        pmax = []
        pmin = []
        for sam in xrange(0,samaple_size,100):
            x.append(sam)
            sp = SampleProbability(data_size, sam, number_of_violations_in_data)
            max_p_point = 0
            min_p_point = 0
            max_min_point = 0
            max_max_point = 0
            for i in range(sam):
                max_p = sp.max_unique_prob(i)
                if max_p_point < max_p:
                    max_p_point = max_p
                    max_max_point = i

                min_p = sp.min_unique_prob(i)
                if min_p_point < min_p:
                    min_p_point = min_p
                    max_min_point = i
            pmax.append(max_max_point)
            pmin.append(max_min_point)

        fig = plt.figure(111)
        plt.title("Probability of max and min unique")
        plt.ylabel("Violation likelihood in sample")
        plt.xlabel("Sample size")
        plt.scatter(x, pmax, label='Max unique tuple')
        plt.scatter(x, pmin, label='Min unique tuple')
        leg = plt.legend(loc='upper right', ncol=2, mode="expand", shadow=True, fancybox=True)
        leg.get_frame().set_alpha(0.3)
        plt.grid(True)
        plt.show()

    def best_sample_size(self, data_size):
        x = []
        pmax = []
        # pmin = []
        for number_of_violations in range(1,data_size/2):
            for sam in xrange(1, data_size):
                sp = SampleProbability(data_size, sam, number_of_violations)
                max_p_point = 0
                min_p_point = 0
                max_min_point = 0
                max_max_point = 0
                for i in range(1, sam):
                    max_p = sp.max_unique_prob(i)
                    if max_p_point < max_p:
                        max_p_point = max_p
                        max_max_point = i

                    # min_p = sp.min_unique_prob(i)
                    # if min_p_point < min_p:
                    #     min_p_point = min_p
                    #     max_min_point = i

                if (max_max_point * 1.0 / data_size) - (2.0 * number_of_violations / (data_size * (data_size - 1))) < 0.01 and max_max_point != 0:
                    x.append(number_of_violations)
                    pmax.append(max_max_point)

        fig = plt.figure(111)
        plt.title("Best sample size for given violaation in data size =" + str(data_size))
        plt.xlabel("Violation likelihood in sample")
        plt.ylabel("Sample size")
        plt.scatter(x, pmax, label='Max unique tuple')
        # leg = plt.legend(loc='upper right', ncol=2, mode="expand", shadow=True, fancybox=True)
        # leg.get_frame().set_alpha(0.3)
        plt.grid(True)
        plt.show()

test = Test()
sample_size = 1000
number_of_violations_in_data = 500
data_size = 1000
# test.prob_hist(sample_size, number_of_violations_in_data, data_size)
test.max_probability_point(sample_size, number_of_violations_in_data, data_size)
# test.best_sample_size(data_size)