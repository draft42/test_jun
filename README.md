# test_jun

###1 задание:

SELECT DISTINCT ON (department) * FROM employee  ORDER BY department, salary DESC;

из предложенного дампа получим:
```
 id  |         name         |        department        | salary 
-----+----------------------+--------------------------+--------
 999 | Ivan Chernoff        | Accounting               | 992811
 611 | Lanette Duggan       | Business Development     | 999519
 906 | Helenelizabeth Rathe | Engineering              | 979031
 813 | Audie Beade          | Human Resources          | 988426
 689 | Siusan Capron        | Legal                    | 991445
 882 | Hayyim Mollitt       | Marketing                | 992312
 615 | Elva Towne           | Product Management       | 987297
 669 | Magdaia Pilmoor      | Research and Development | 998099
 765 | Saloma Dirkin        | Sales                    | 999051
 731 | Giffer Stothard      | Services                 | 966848
 221 | Oralie Bourne        | Support                  | 987936
 200 | Cassandre Halsho     | Training                 | 998243
``` 
 Стоит отметить,что на поставленную задачу запрос отвечает (выводит одного человека из каждого отдела),  но в отделах может быть несколько человек с самой большой одинаковой зарплатой. 
 
 
 ###2 задание: 
 
 Для загрузки изображений запустить app.py.
 
 Нашел все страницы календарей с предложенной ссылки https://www.smashingmagazine.com/tag/wallpapers/ при помощи pars.py,   из них отобрал ссылки, в которых присутствует дата.  
