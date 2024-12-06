import unittest
import tests_12_3

run_walk_ST = unittest.TestSuite()
run_walk_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
run_walk_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_walk_ST)
