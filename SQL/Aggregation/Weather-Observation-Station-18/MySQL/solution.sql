/*
Enter your query here.
*/
SELECT ROUND(ABS((MAX(LONG_W) - MIN(LONG_W)))+ABS((MAX(LAT_N)-MIN(LAT_N))),4) FROM STATION;
