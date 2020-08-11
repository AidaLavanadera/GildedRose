# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_update_sulfuras(self):
        items = [Item('Sulfuras, Hand of Ragnaros', 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        correct = {'sell_in': 0, 'quality': 80}
        self.assertEquals(items[0].quality, correct['quality'])
        self.assertEquals(items[0].sell_in, correct['sell_in'])

    def test_update_agedbrie(self):
        items = [Item('Aged Brie', 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        correct = {'sell_in': 1, 'quality': 1}
        self.assertEquals(items[0].quality, correct['quality'])
        self.assertEquals(items[0].sell_in, correct['sell_in'])

    def test_update_conjured(self):
        items = [Item('Conjured Mana Cake', 3, 6),
                 Item('Conjured Mana Cake', 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        correct = {'sell_in': 2, 'quality': 4}
        self.assertEquals(items[0].quality, correct['quality'])
        self.assertEquals(items[0].sell_in, correct['sell_in'])
        correct = {'sell_in': -1, 'quality': 6}
        self.assertEquals(items[1].quality, correct['quality'])
        self.assertEquals(items[1].sell_in, correct['sell_in'])

    def test_update_backstage(self):
        items = [Item('Backstage passes to a TAFKAL80ETC concert', 15, 20),
                 Item('Backstage passes to a TAFKAL80ETC concert', 10, 49),
                 Item("Backstage passes to a TAFKAL80ETC concert", 5, 49),
                 Item('Backstage passes to a TAFKAL80ETC concert', 10, 10),
                 Item("Backstage passes to a TAFKAL80ETC concert", 5, 10),
                 Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)
                 ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        correct = {'sell_in': 14, 'quality': 21}
        self.assertEquals(items[0].quality, correct['quality'])
        self.assertEquals(items[0].sell_in, correct['sell_in'])
        correct = {'sell_in': 9, 'quality': 50}
        self.assertEquals(items[1].quality, correct['quality'])
        self.assertEquals(items[1].sell_in, correct['sell_in'])
        correct = {'sell_in': 4, 'quality': 50}
        self.assertEquals(items[2].quality, correct['quality'])
        self.assertEquals(items[2].sell_in, correct['sell_in'])
        correct = {'sell_in': 9, 'quality': 12}
        self.assertEquals(items[3].quality, correct['quality'])
        self.assertEquals(items[3].sell_in, correct['sell_in'])
        correct = {'sell_in': 4, 'quality': 13}
        self.assertEquals(items[4].quality, correct['quality'])
        self.assertEquals(items[4].sell_in, correct['sell_in'])
        correct = {'sell_in': -1, 'quality': 0}
        self.assertEquals(items[5].quality, correct['quality'])
        self.assertEquals(items[5].sell_in, correct['sell_in'])

    def test_update_anythingelse(self):
        items = [Item('+5 Dexterity Vest', 10, 20),
                 Item('Elixir of the Mongoose', 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        correct = {'sell_in': 9, 'quality': 19}
        self.assertEquals(items[0].quality, correct['quality'])
        self.assertEquals(items[0].sell_in, correct['sell_in'])
        correct = {'sell_in': -1, 'quality': 8}
        self.assertEquals(items[1].quality, correct['quality'])
        self.assertEquals(items[1].sell_in, correct['sell_in'])


if __name__ == '__main__':
    unittest.main()
