# Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
# В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:
# Уровень - INFO
# Режим - запись с заменой('w')
# Название файла - runner_tests.log
# Кодировка - UTF-8
# Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.
from  rt_with_exeptions import Runner, Tournament
import unittest
import logging
logging.basicConfig(level=logging.INFO, filemode= 'w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s')

# Дополните методы тестирования в классе RunnerTest следующим образом:
# test_walk:
# Оберните основной код конструкцией try-except.
# При создании объекта Runner передавайте отрицательное значение в speed.
# В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
# В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением
# "Неверная скорость для Runner".
class RunnerTest(unittest.TestCase):

    @unittest.skipIf(False, 'пропуск')
    def test_walk(self):
        try:

            run_ = Runner('run1', -5)
            for i in range(10):
                run_.walk()
                self.assertEqual(run_.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as exc:
            logging.warning("Неверная скорость для Runner", exc_info=exc)

    # test_run:
    # Оберните основной код конструкцией try-except.
    # При создании объекта Runner передавайте что-то кроме строки в name.
    # В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
    # В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING
    # с сообщением "Неверный тип данных для объекта Runner".
    @unittest.skipIf(False, 'пропуск')
    def test_run(self):
        try:

            run_2 = Runner('run2', -1)
            for _ in range(10):
                run_2.run()
                self.assertEqual(run_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except ValueError as exc:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=exc)

    @unittest.skipIf(False, 'пропуск')
    def test_challenge(self):
        run_3 = Runner('run3')
        run_4 = Runner('run4')
        for _ in range(10):
            run_3.walk()
            run_4.run()
        self.assertNotEqual(run_3.distance, run_4.distance)

