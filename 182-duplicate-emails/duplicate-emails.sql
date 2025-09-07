# Write your MySQL query statement below
Select email as Email
from Person
group by Email
Having Count(*)>1;