#Hashbang / shebang
#!bin/bash
echo "enter your city name:"
read city1
echo "Enter the new city name:"
read city2
echo "Enter the new city name:"
read city3
echo "enter the new city name:"
read city4
echo $city1  >> cities.txt
echo $city2 >> cities.txt
echo $city3 >> cities.txt
echo $city4 >> cities.txt
cat cities.txt | grep new > new_cities.txt
cat cities.txt | grep -i new | sed 's/New/Old/g' > old_cities.txt
cat old_cities.txt



ubuntu@ip-172-31-45-48:~$ vi cities.sh
ubuntu@ip-172-31-45-48:~$ "cities.sh" 17L, 433B written
ubuntu@ip-172-31-45-48:~$ chmod +x cities.sh
ubuntu@ip-172-31-45-48:~$ ./cities.sh
enter your city name:
New Delhi
Enter the new city name:
New York
Enter the new city name:
New Jersy
enter the new city name:
New Delhi New Jersy
Old Delhi
Old York
Old Jersy
Old Delhi Old Jersy