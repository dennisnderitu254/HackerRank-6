/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT DISTINCT CITY FROM STATION WHERE SUBSTR(UPPER(CITY),1,1) IN ('A','E','I','O','U') AND SUBSTR(UPPER(CITY),-1,1) IN ('A','E','I','O','U');
