# Часть 1. TestSuit.
# Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True.
# Напишите соответствующий декоратор к каждому методу (кроме @classmethod), который при значении
# is_frozen = False будет выполнять тесты, а is_frozen = True - пропускать и выводить сообщение
# 'Тесты в этом кейсе заморожены'.
import unittest
from rt_with_exeptions import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):
    is_frozen = True
    # tearDownClass - метод, где выводятся all_results по очереди в столбец.
    @classmethod
    def tearDownClass(cls):
        cls.all_results = []

    # setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который
    # будут сохраняться результаты всех тестов.
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.h_run = Runner('Усэйн', 10)
        self.a_run = Runner('Андрей', 9)
        self.n_run = Runner('Ник', 3)

# tearDownClass - метод, где выводятся all_results по очереди в столбец.
    @classmethod
    def tearDownClass(cls):
        def tearDownClass(cls):
            for i, elem in enumerate(cls.all_results):
                print(f'{i + 1}. {elem}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_tournament(self):
        tournament = Tournament(90, self.h_run, self.n_run)
        results = tournament.start()
        TournamentTest.all_results[1] = results
        self.assertTrue(results[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tournament(self):
        tournament = Tournament(90, self.a_run, self.n_run)
        results = tournament.start()
        TournamentTest.all_results[2] = results
        self.assertTrue(results[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tournament(self):
        tournament = Tournament(90, self.h_run, self.a_run, self.n_run)
        results = tournament.start()
        TournamentTest.all_results[3] = results
        self.assertTrue(results[3] == 'Ник')



class RunnerTest(unittest.TestCase):
    is_frozen = False

# test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у
# этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
    @unittest.skipIf(is_frozen, 'Тесты не заморожены')
    def test_walk(self):
        run_ = Runner('run1')
        for i in range(10):
            run_.walk()
        self.assertEqual(run_.distance, 50)

# test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у
# этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
    @unittest.skipIf(is_frozen, 'Тесты не заморожены')
    def test_run(self):
        run_2 = Runner('run2')
        for _ in range(10):
            run_2.run()
        self.assertEqual(run_2.distance, 100)
# test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз
# у объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте
# метод assertNotEqual, чтобы убедится в неравенстве результатов.
    @unittest.skipIf(is_frozen, 'Тесты не заморожены')
    def test_challenge(self):
        run_3 = Runner('run3')
        run_4 = Runner('run4')
        for _ in range(10):
            run_3.walk()
            run_4.run()
        self.assertNotEqual(run_3.distance, run_4.distance)
# Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.


# Создайте модуль suite_12_3.py для описания объекта TestSuite. Укажите на него переменной
# с произвольным названием.
# Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
# Создайте объект класса TextTestRunner, с аргументом verbosity=2.
# Часть 2. Пропуск тестов.
# Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True.
# Напишите соответствующий декоратор к каждому методу (кроме @classmethod), который при значении
# is_frozen = False будет выполнять тесты, а is_frozen = True - пропускать и выводить сообщение
# 'Тесты в этом кейсе заморожены'.
# Таким образом вы сможете контролировать пропуск всех тестов в TestCase изменением всего одного атрибута.
# Запустите TestSuite и проверьте полученные результаты тестов из обоих TestCase.
# Пример результата выполнения тестов:
# Вывод на консоль:
# test_challenge (tests_12_3.RunnerTest.test_challenge) ... ok
# test_run (tests_12_3.RunnerTest.test_run) ... ok
# test_walk (tests_12_3.RunnerTest.test_walk) ... ok
# test_first_tournament (tests_12_3.TournamentTest.test_first_tournament) ... skipped
# 'Тесты в этом кейсе заморожены'
# test_second_tournament (tests_12_3.TournamentTest.test_second_tournament) ... skipped
# 'Тесты в этом кейсе заморожены'
# test_third_tournament (tests_12_3.TournamentTest.test_third_tournament) ... skipped
# 'Тесты в этом кейсе заморожены'
# ----------------------------------------------------------------------
# Ran 6 tests in 0.000s OK (skipped=3)
