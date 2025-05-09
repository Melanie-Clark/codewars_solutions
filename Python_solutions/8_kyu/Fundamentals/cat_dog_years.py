"""
I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:

humanYears >= 1
humanYears are whole numbers only
Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that
Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that
"""

def human_years_cat_years_dog_years(human_years):
    first_year = 15
    if human_years >= 2:
        catYears = 24 + (4 * (human_years-2))
        dogYears = 24 + (5 * (human_years-2))
        return [human_years, catYears, dogYears]
    return [human_years, first_year, first_year]