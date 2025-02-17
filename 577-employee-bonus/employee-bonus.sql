# Write your MySQL query statement below
select e.name, Bonus.bonus
from Employee e
left join Bonus on e.empID=Bonus.empID
where bonus < 1000 or bonus is null;
