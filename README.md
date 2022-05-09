# PasswordManager

![obraz](https://user-images.githubusercontent.com/66008982/167429199-81135ae4-d4df-4260-80b3-72d9314c685d.png)

A simple project to learn about encryption and web application security. Frontend is written in HTML, jQuery and CSS, while backend in Python. Local server was hosted by XAMPP. 

I also included a password resetting service, which works by sending an appropriate email to the user. This email contains the reset link, which is unique each time and for each user.

# Database architecture
![obraz](https://user-images.githubusercontent.com/66008982/167429106-b7aa7677-4d8f-4153-a607-909dc7666cd1.png)

Database was created in MySQL, there are 3 events responsible for refreshing user token. The file inside this repo is an export from MySQL. 
