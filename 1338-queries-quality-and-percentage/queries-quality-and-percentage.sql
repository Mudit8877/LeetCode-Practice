# Write your MySQL query statement below
select query_name, 
round(sum(q.rating/q.position)/count(*),2) as quality,
round(avg(if(rating<3,1,0))*100,2) as poor_query_percentage
from Queries q
group by query_name