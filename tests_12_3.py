import unittest
import runner
import runner_and_tournament as r_t


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_obj = runner.Runner('Someone')
        for i in range(10):
            test_obj.walk()
        self.assertEqual(50, test_obj.distance)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test_obj = runner.Runner('Someone')
        for i in range(10):
            test_obj.run()
        self.assertEqual(100, test_obj.distance)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_obj_1 = runner.Runner('First')
        test_obj_2 = runner.Runner('Second')
        for i in range(10):
            test_obj_1.walk()
            test_obj_2.run()
        print(f'First distance: {test_obj_1.distance}')
        print(f'Second distance: {test_obj_2.distance}')
        self.assertNotEqual(test_obj_1.distance, test_obj_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(cls.all_results[i])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.usain = r_t.Runner('Usain', 10)
        self.andrey = r_t.Runner('Andrey', 9)
        self.nick = r_t.Runner('Nick', 3)
        self.usain_2 = r_t.Runner('Usain_2', 10)  # для теста на работу кода при равных speed

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_heat(self):
        t = r_t.Tournament(90, self.usain, self.andrey)
        TournamentTest.all_results['first_heat'] = t.start()
        last_runner = max(TournamentTest.all_results['first_heat'].keys())
        self.assertTrue(TournamentTest.all_results['first_heat'][last_runner] == 'Andrey')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_heat(self):
        t = r_t.Tournament(90, self.andrey, self.nick)
        TournamentTest.all_results['second_heat'] = t.start()
        last_runner = max(TournamentTest.all_results['second_heat'].keys())
        self.assertTrue(TournamentTest.all_results['second_heat'][last_runner] == 'Nick')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_heat(self):
        t = r_t.Tournament(90, self.usain, self.andrey, self.nick)
        # t = r_t.Tournament(90, self.andrey, self.nick, self.usain)  # самый быстрый финиширует вторым
        TournamentTest.all_results['third_heat'] = t.start()
        last_runner = max(TournamentTest.all_results['third_heat'].keys())
        self.assertTrue(TournamentTest.all_results['third_heat'][last_runner] == 'Nick')

#  Дополнительные тесты на выявление логических ошибок в методе start тестируемого кода:
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_equal_time(self):
        t1 = r_t.Tournament(90, self.andrey, self.usain)
        t2 = r_t.Tournament(90, self.usain, self.andrey)
        self.assertEqual(t1.start(), t2.start(), 'Проверить, одинаково ли "время" бегунов на дистанции')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_equal_speed(self):
        t1 = r_t.Tournament(90, self.usain, self.usain_2)
        t2 = r_t.Tournament(90, self.usain_2, self.usain)
        self.assertEqual(t1.start(), t2.start(), 'Как должен работать код при равных speed?')


if __name__ == '__main__':
    unittest.main()
