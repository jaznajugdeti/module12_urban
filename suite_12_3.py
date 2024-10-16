import unittest
from test_12__3 import TournamentTest, RunnerTest

# Создайте объект класса TextTestRunner, с аргументом verbosity=2.


# Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True.
# # Напишите соответствующий декоратор к каждому методу (кроме @classmethod), который при значении
# # is_frozen = False будет выполнять тесты, а is_frozen = True - пропускать и выводить сообщение
# # 'Тесты в этом кейсе заморожены'.
test_run_suite = unittest.TestSuite()
test_run_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test_run_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_run_suite)