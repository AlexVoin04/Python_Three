2.	Реализовать механизм записи данных пользователя в текстовый файл  с последующем  чтением этих данных. 
Пользователь должен иметь возможность вводить данные в консоль в формате id last_name first_name middle_name age.
После каждого введенного сообщения данные должны быть сохранены в текстовый файл. Если пользователь вводит команду 
show data * , все данные  из файла должны быть выведены в консоль в виде таблицы:

id 	   last_name	first_name	middle_name	age
1	      Ivanov	     Ivan	     Ivanovich	27
2	     Stepanov	    Anton	   Mikhailovich	56
…	       …	          …	           …	     …
n + 1	 Fedorov	   Nikita	    Stepanovich	35

	Если пользователь вводит команду show data {integer number}, например, 
show data 10, то необходимо вывести первые 10 записей из текстового файла в формате таблицы представленной выше.
![image](https://user-images.githubusercontent.com/99070761/208307385-5f398bfb-5630-4874-9bbd-ab838092065c.png)
