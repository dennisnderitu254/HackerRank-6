/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT CONVERT(DECIMAL(18,4), SUM(LAT_N)) FROM Station WHERE LAT_N > 38.7880 and LAT_N < 137.2345;
