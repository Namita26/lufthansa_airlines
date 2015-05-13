# lufthansa_airlines
Problem :

Write code to find out issues regarding page navigation. Your task is to test all internal and external links and confirm whether there are broken links or orphan pages in the application and if the links work properly.

 

Task Description:
  Phase 1:
     Go to http://www.lufthansa.com/online/portal/lh/ua/homepage
    Fetch the urls in the website recursively, query each url and and check if it returns status - 200 (OK) or 401 (page not available) or (500) internal server error.
    You may limit the recursion depth to 2 levels.

Phase 2:
    Create a Django App
    Save the tuple (link, status, time_of_verification) in database. Here time_of_verification is the time when the status was checked (200 / 401 OR 500)

Phase 3:
    Create a view/function  which returns all the URLS on the basis of the status of the page asked  i.e if user requests for all the links with status 200, the function will return a JSON as follows,

  { result : ["http://www.lufthansa.com/online/portal/lh/ua/homepage" , "http://www.lufthansa.com/online/portal/lh/ua/homepage/t1", http://www.lufthansa.com/online/portal/lh/ua/homepage/t3] }
  
  
  
  Steps to execute:
  1. export DJANGO_SETTINGS_MODULE="lufthansa_airlines.settings"
  2. Create database lufthansa in mysql and do "python manage.py syncdb" 
  3. First run the scraper.py from lufthansa_airlines/scraper.py
  4. Then run the "airlines/view.py" and give one param while running as status code(200/504/403 etc)
