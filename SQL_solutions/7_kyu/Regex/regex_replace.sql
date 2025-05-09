/*
You are given a table named repositories, format as below:

** repositories table schema **

project
commits
contributors
address
The table shows project names of major cryptocurrencies, their numbers of commits and contributors and also a random donation address ( not linked in any way :) ).

Your job is to remove all numbers in the address column and replace with '!', then return a table in the following format:

** output table schema **

project
commits
contributors
address
Case should be maintained.

*/

SELECT 
  project, 
  commits, 
  contributors, 
  REGEXP_REPLACE(address, '[0-9]', '!', 'g') AS address -- 'g' global flag replaces all occurrences not just 1
FROM repositories AS r