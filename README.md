# TELEGRAM LINK BOT
## About
This bot can shorten your links.

Bot name: ShortenLink   
Link for bot:  t.me/ShortenLinksManagerBot

It has options:  

- `/help` - see commands.
- `/last` - 10 last links.
- `{url}` - url to shorten. 
- `/start` - first command to start using bot.

If your url is valid bot return error. Otherwise it return warning.  

All links\` and users\` data save in database.Structure your can see in `models.py`
 
## Build and launch the bot
#### Токен для бота присылался отдельно в сообщение с ссылкой на проект!

### Using Docker

##### The first build

1. You need mysql docker image, for downloading it execute:  
`docker pull mysql`
2. Clone the project.
3. __Change config.py: PUT BOT`s TOKEN__

	```python
	
	DB = "db"            		# Name mysql docker service, bot connect with it. 
	DB_USER = 'root'     		# User.
	DB_PASSWORD = 'root' 		# Password for user.
	DB_NAME = 'bot' 			# Name of database with bot data.
	# PUT TOKEN FOR BOT 
	TOKEN = {TOKEM}				# Bot token, example: TOKEN = '78362876ablabla3829'
	```

3. Build the project with:  
`docker-compose build`
4. First launch with:  
`docker-compose up`

##### To start and stop the app later
- `docker-compose start`
- `docker-compose stop`

### From sources
1. Clone the Project.
2. Setup Environment.  
`pip install pipenv`
3. Install dependencies.  
`pip install -r requirements.txt`
4. You need mysql server on your desktop. Download from https://dev.mysql.com/downloads/mysql/  and install  it.
5. Create database   
`mysql -u{DB_USER} -p{DB_PASSWORD}`.  
`CREATE DATABASE DB_NAME;`.  
6. __Change config.py for your settings.__

	```python
	DB = "127.0.0.1"            # '127.0.0.1' for local database
	DB_USER = 'root'     		# Check for your user
	DB_PASSWORD = 'root' 		# Check for your password
	DB_NAME = 'bot'  			# Check for your database
    #PUT TOKEN FOR BOT 
	TOKEN = {TOKEM}				# Bot token, example: TOKEN = '78362876ablabla3829'
	```   

5. Run server  
`python bot.py `
 
