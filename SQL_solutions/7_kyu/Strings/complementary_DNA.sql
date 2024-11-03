/*
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA
"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
*/

SELECT dna, REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(dna, 'A', '1'), 'T', 'A'), '1', 'T'), 'C', '2'), 'G', 'C'), '2', 'G') AS res
FROM dnastrand

-- Refactored:
SELECT dna, TRANSLATE(dna, 'ATCG', 'TAGC') AS res
FROM dnastrand

