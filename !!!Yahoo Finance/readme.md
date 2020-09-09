yahoo_finance.py
---
爬取yahoo finance上不同公司的financials

us_public_company_list.py
---
爬取美国上市公司名单

selenium_login_yahoo_finance.py
---
模拟登陆yahoo finance获取premium financials数据

sourcing.py(**Final Version**)
---

Please run the code in **Terminal** to have full functionality of the code. 

The financial report files that would be downloaded is under the code file path. if you wanna change the path, you can revise it under **write_to_csv()** function.

The default list of public company symbol was only 50 records for test. If you wanna retrieve all the list, you can revise it under **main()** function.

When you start to run the program, you need to type 0,1 or 2. '0' is for "income_statement", '1' is for "balance_sheet" and '2' is for "cash_flow". 

There might be some error messages on the command line when the code is running, that is because the original data is missing, just ignore them. 

Since I copied and pasted my cookies to my code, you don't need to use selenium to open the browser again to retrieve data. **log_in()**, **wait_until_verified()** and **get_cookie()** are functions for your reference.

Hope my code works well on your computer, if any problems, please let me know.