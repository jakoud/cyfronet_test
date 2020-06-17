import pymysql

data=pymysql.connect(host='localhost', user='root', password='ENTER_PASSWORD_HERE', db='employees', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

try:
     
    with data.cursor() as kursor:
        kursor.execute("SELECT dept_manager.emp_no, AVG(salaries.salary) AS salary FROM salaries CROSS JOIN dept_manager ON salaries.emp_no=dept_manager.emp_no GROUP BY dept_manager.emp_no")
        mean=kursor.fetchall()
        print(mean)
        print('\n')
        kursor.execute("SELECT employees.first_name,employees.last_name, employees.emp_no, employees.birth_date, employees.gender, employees.hire_date, dept_manager.dept_no, dept_manager.from_date, dept_manager.to_date, AVG(salaries.salary) AS salary, GROUP_CONCAT(DISTINCT titles.title) AS titles FROM dept_manager CROSS JOIN (salaries CROSS JOIN titles CROSS JOIN employees) ON (salaries.emp_no=dept_manager.emp_no AND titles.emp_no=dept_manager.emp_no AND employees.emp_no=dept_manager.emp_no) GROUP BY dept_manager.emp_no")
        final_table=kursor.fetchall()
        
        for element in final_table:
           print(element)
           print('\n')
        


finally: data.close()