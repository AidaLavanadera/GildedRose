# GildedRose

## Process followed
* Created tests for current fucntionality including all edge cases
* Refactor code with current functionality using tests as proof of working
* Added new feature for conjured items
* Updated tests for conjured items


## Notes:

I have not checked for the exact name of the items as previously done, instead I search for specific terms present within the name so the system can be easily scalable and new itemas can be added.

I have made use of the ternary operator quite often. While this does not decrease the code complexity, in my opinion it improves the code's readability.

I have tried to group items with common characteristics (i.e. items that increase in quality versus items that decrease in quality) for more clarity.

SellIn date update and safety check for Quality to not be higher than 50 are performed only once for the relevant cases.

The quality of sulfuras items is unnecesarily re-assigned every day. However this will prevent any wrong data entry.

I think, the code could be made clearer by creating a function or method to increase/decrease the quality that could be invoked as many times as needed. However I was not sure whether this is allowed.

