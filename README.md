# pyfix
pyfix is a simple library that can make your code more easy. it is made with other libraries that are popular.

# how to use
Download this file and import it to your code.
to use commands you have to create a instance and use it from there.
for example:
* classDate = Date() 
* result = classDate.get_year()
* print(result)

this means:
* name of your instance = name of the class
  
# Classes
  * Date: it gives you current date or just day, month or year.
     * Commands:
          * get_year(): gives you the current year. ==> integer
          * get_month(): gives you the current month. == >integer
          * get_day(): gives you the current day. ==> integer
          * date(): gives you the full date. ==> {day}/{month}/{year}
  * Roll_a_dice:
      * Commands:
             * roll_dice(): rolls a dice, gives you a integer value betweeen 1 and 6. 
  * Google:
      * Commands:
             *search(topic):searchs something on google(you have to write the topic of your search to the parameters). 
  
  * Weather: ==> !! WARNING: it uses openweather api so if you dont have a account it wont work for you!
      * Commands:
             * weather_temp(city,api_key): gives you the temperature of your city by centigrade. (you have to set your city and api_key to parameters)
             * weather_description(city,api_key): gives you the description about your weather. (you have to set your city and api_key to parameters)
  * Password_generator:
      * Commands:
             *generate(passlength): gives you a random password with the maximum chars of your choice (you have to set passlength as your parameter)
  
  
      
  
  
    






