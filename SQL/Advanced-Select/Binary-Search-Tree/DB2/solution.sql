
/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/
select N,
case
when (P is null) then 'Root'
when N IN (select P from BST) then 'Inner'
else 'Leaf'
end

from BST
order by 1;
        
