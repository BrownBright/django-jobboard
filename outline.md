job 
-title
-location
-jobtybe
-description
-Vacancy
-Salary
-catgory
-exper




--apply job 
--post job



Blog:
-title
-description
-created_at
-catgory
-tags
-author



--search
--comment
--recent posts





relations :
    - one to many  [author - posts]
    - many to many [users  - groups]
    - one to one   [user   - profile]



static files : [front end]
meida files  : [uploaded files]