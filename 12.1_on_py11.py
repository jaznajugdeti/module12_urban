# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
# В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.
import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name
    # Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
class RunnerTest(unittest.TestCase):

# test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у
# этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
    def test_walk(self):
        run_ = Runner('run1')
        for i in range(10):
            run_.walk()
        self.assertEqual(run_.distance, 50)

# test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у
# этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
    def test_run(self):
        run_2 = Runner('run2')
        for _ in range(10):
            run_2.run()
        self.assertEqual(run_2.distance, 100)
# test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз
# у объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте
# метод assertNotEqual, чтобы убедится в неравенстве результатов.
    def test_challenge(self):
        run_3 = Runner('run3')
        run_4 = Runner('run4')
        for _ in range(10):
            run_3.walk()
            run_4.run()
        self.assertNotEqual(run_3.distance, run_4.distance)
# Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.

#
# Пункты задачи:
# Скачайте исходный код для тестов.
# Создайте класс RunnerTest и соответствующие описанию методы.
# Запустите RunnerTest и убедитесь в правильности результатов.
# Пример результата выполнения программы:
# Вывод на консоль:
# Ran 3 tests in 0.001s OK
#
# Примечания:
# Попробуйте поменять значения в одном из тестов, результаты