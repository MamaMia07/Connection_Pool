Task: create your own simple solution

What should be implemented:

- allocate 5 database connections at application startup

- connection limit control (pool can maintain max 100 connections to the database

- the pool should be checked regularly and inactive connections above the starting limit should be deleted

- connections during which an error occurred should be deleted, a new one should be created in their place

Create tool to test this library.
