/*
Enter your query here.
*/
SELECT ROUND(SQRT(POWER(MAX(LONG_W) - MAX(LAT_N),2)+POWER(MIN(LONG_W) - MIN(LAT_N),2)),4) FROM STATION;
