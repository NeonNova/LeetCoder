# Write your MySQL query statement below
select name, bonus from employee natural left join bonus where bonus < 1000 or bonus is null