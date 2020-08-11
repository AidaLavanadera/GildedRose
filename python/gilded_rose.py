# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if "sulfuras" in str(item.name).casefold():
                # This is a special case, both price and date no need to be modified, set it to 80 for dealing with
                # possible wrong data entry.
                item.quality = 80
            else:
                # For the rest of the items, selldate must be updated
                item.sell_in = item.sell_in - 1
                if "aged brie" in str(item.name).casefold() or "backstage" in str(item.name).casefold():
                    # For theses cases, quality goes up at least 1 point
                    item.quality = item.quality + 1
                    if "backstage" in str(item.name).casefold():
                        # Handling specific backstage cases after first increment
                        item.quality = item.quality + 1 if item.sell_in <= 10 else item.quality
                        item.quality = item.quality + 1 if item.sell_in <= 5 else item.quality
                        item.quality = 0 if item.sell_in < 0 else item.quality
                else:  # The remaining items decrease in quality
                    item.quality = item.quality - 1 if item.sell_in > 0 else item.quality - 2
                    if "conjured" in str(item.name).casefold():
                        # If item is conjured, update price again for double speed
                        item.quality = item.quality - 1 if item.sell_in > 0 else item.quality - 2
                # For all the remaining items quality cannot be higher than 50
                item.quality = 50 if item.quality > 50 else item.quality


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
