# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
# В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.
# Изменения в классе Runner:
# Появился атрибут speed для определения скорости бегуна.
# Метод __eq__ для сравнивания имён бегунов.
# Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
# Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать
# и список участников.
# Также присутствует метод start, который реализует логику бега по предложенной дистанции.
import unittest
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name
    def __repr__(self):
        return self.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        run_ = Runner('run1')
        for i in range(10):
            run_.walk()
        self.assertEqual(run_.distance, 50)


    def test_run(self):
        run_2 = Runner('run2')
        for _ in range(10):
            run_2.run()
        self.assertEqual(run_2.distance, 100)

    def test_challenge(self):
        run_3 = Runner('run3')
        run_4 = Runner('run4')
        for _ in range(10):
            run_3.walk()
            run_4.run()
        self.assertNotEqual(run_3.distance, run_4.distance)


class TournamentTest(unittest.TestCase):

    # tearDownClass - метод, где выводятся all_results по очереди в столбец.
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    # setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который
    # будут сохраняться результаты всех тестов.
    def setUp(self):
        self.h_run = Runner('Усэйн', 10)
        self.a_run = Runner('Андрей', 9)
        self.n_run = Runner('Ник', 3)


# tearDownClass - метод, где выводятся all_results по очереди в столбец.
    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(f'{i+1}. {elem}')

    def test_first_tournament(self):
        tournament = Tournament(90, self.h_run, self.n_run)
        results = tournament.start()
        TournamentTest.all_results[1] = results
        self.assertTrue(results[2] == 'Ник')

    def test_second_tournament(self):
        tournament = Tournament(90, self.a_run, self.n_run)
        results = tournament.start()
        TournamentTest.all_results[2] = results
        self.assertTrue(results[2] == 'Ник')

    def test_third_tournament(self):
        tournament = Tournament(90, self.h_run, self.a_run, self.n_run)
        results = tournament.start()
        TournamentTest.all_results[3] = results
        self.assertTrue(results[3] == 'Ник')


#
# Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90.
# У объекта класса Tournament запускается метод start, который возвращает словарь в переменную all_results.
# В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results
# (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
# Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
# Усэйн и Ник
# Андрей и Ник
# Усэйн, Андрей и Ник.
# Как можно понять: Ник всегда должен быть последним.
#
# Дополнительно (не обязательно, не влияет на зачёт):
# В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка.
# В результате его работы бегун
# с меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
# Попробуйте решить эту проблему и обложить дополнительными тестами.
# Пример результата выполнения тестов:
# Вывод на консоль:
# {1: Усэйн, 2: Ник}
# {1: Андрей, 2: Ник}
# {1: Андрей, 2: Усэйн, 3: Ник}
#
# Ran 3 tests in 0.001s
# OK
#
# Примечания:
# Ваш код может отличаться от строгой последовательности описанной в задании. Главное - схожая логика работы тестов
# и наличие всех перечисленных переопределённых методов из класса TestCase.