import unittest
import Treed

class TestRecipeIngestion(unittest.TestCase):
    def testNameIngestion(self):
        recipe = Treed.ingest('tests/fixtures/recipe.cson')

        self.assertEquals(recipe['name'], 'Foo Pie')
