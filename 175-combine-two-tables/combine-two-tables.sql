# Write your MySQL query statement below
select Person.firstName, Person.lastName , Address.city, Address.state
from Person
left Join Address ON Person.personID = Address.personID