import unittest
from tarefa_controller import *
from tarefa_model import Tarefa

class Teste(unittest.TestCase):
    
    def teste_cadastrar_tarefa(self):
        self.assertEqual(cadastrar_tarefa(),True)



if __name__ == '__main__':
    unittest.main()