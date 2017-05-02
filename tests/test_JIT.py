from Statistical_Computation import Original
import unittest
import numpy as np
import random

class Test_jit_k_means_pp(unittest.TestCase):
    X = []
    N=200
    k=3
    ell = 2
    
    def simulate_data(self):
        self.X = []
        n = float(self.N)/self.k
        for i in range(self.k):
            c = (random.uniform(-1,1), random.uniform(-1,1))
            s = random.uniform(0.05,0.15)
            x = []
            while len(x) < n:
                a,b = np.array([np.random.normal(c[0],s),np.random.normal(c[1],s)])
                # Continue drawing points from the distribution in the range [-1,1]
                if abs(a) and abs(b)<1:
                    x.append([a,b])
            self.X.extend(x)
        self.X = np.array(self.X)[:self.N]

        
    def test_jit_k_means_pp(self):
        self.simulate_data()
        clusters = Original.scalable_k_means_pp(self.X,self.k,self.ell)
        self.assertEqual(len(clusters), self.k)


if __name__ == '__main__':
    unittest.main()