import unittest

def palindromos(palabra):
    palindromo = palabra[::-1]
    if palindromo == palabra:
        return 'es palindromo'
    else:
        return 'no es palindromo'
    

if __name__ == '__main__':
    unittest.main()