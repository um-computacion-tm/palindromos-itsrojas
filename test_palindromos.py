import unittest

from palindromos import palindromos

class TestPalindromos(unittest.TestCase):
    def test_palindromos_simple(self):
        result = palindromos('neuquen')
        self.assertEqual(result, 'es palindromo')
    
    def test_palindromos_2_simple(self):
        result = palindromos('esteban')
        self.assertEqual(result, 'no es palindromo')

    def test_palindromos_3_simple(self):
        result = palindromos('reconocer')
        self.assertEqual(result, 'es palindromo')



if __name__ == '__main__':
    unittest.main()