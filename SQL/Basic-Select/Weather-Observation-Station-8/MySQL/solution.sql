/*
Enter your query here.
*/

SELECT DISTINCT CITY FROM STATION WHERE SUBSTR(UPPER(CITY),1,1) IN ('A','E','I','O','U') AND SUBSTR(UPPER(CITY),-1,1) IN ('A','E','I','O','U');
