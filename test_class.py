import unittest
from Car_Dealership import *

class Test_Brand_car(unittest.TestCase):
    def setUp(self):
        self.a = Brand_car('Audi')

    def test_Brand_car_(self):
        aa = 'Audi'
        self.assertEqual(aa, self.a.name)


class Test_Buyer(unittest.TestCase):
    def setUp(self):
        self.a3 = Buyer('Vlasov', 'Andrey', 'Michailovich', '12345', 'Street L, 8', 'Archangelsk', '33', 'man')

    def test_Buyer_(self):
        aa3 = 'Andrey'
        self.assertEqual(aa3, self.a3.name)


class Test_Cars(unittest.TestCase):
    def setUp(self):
        self.a2 = Cars('A4', 'Audi', '2016', 'black', 'drive', 1500000)

    def test_Cars(self):
        aa2 = 'yellow'
        self.assertEqual(aa2, self.a2.color)


class Test_Employee(unittest.TestCase):
    def setUp(self):
        self.a4 = Employee('Fedotov')

    def test_Employee_(self):
        aa4 = 'Au'
        self.assertEqual(aa4, self.a4.surname)


class Test_Car_sale(unittest.TestCase):
    def setUp(self):
        self.a5 = Car_sale('10.11.2022')

    def test_Car_sale_(self):
        aa5 = '10.11.2022'
        self.assertEqual(aa5, self.a5.data)

if __name__=='__main__':
    unittest.main()
