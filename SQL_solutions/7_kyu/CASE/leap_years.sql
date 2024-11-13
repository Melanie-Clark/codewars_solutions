/*
In this kata you should simply determine, whether a given year is a leap year or not.
In case you don't know the rules, here they are:

Years divisible by 4 are leap years,
but years divisible by 100 are not leap years,
but years divisible by 400 are leap years.
Tested years are in range 1600 ≤ year ≤ 4000.
*/

SELECT
  YEAR,
  CASE
    WHEN year % 400 = 0 THEN true
    WHEN year % 100 = 0 THEN false
    WHEN year % 4 = 0 THEN true
    ELSE false
  END AS is_leap
FROM years
ORDER BY YEAR;