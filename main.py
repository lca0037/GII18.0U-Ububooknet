# -*- coding: utf-8 -*-

#from src import personaje
from tst import testUnitarios
from src import modelo, personaje
import unittest
#import unittest 

#testUnitarios.testUnitarios()
#testUnitarios.unittest.main()

runner = unittest.TextTestRunner()
result = runner.run(unittest.makeSuite(testUnitarios.testUnitarios))
