<!DOCTYPE html>
<html>
<head>
</head>
<body>
	<h1>Django Social Media Web App -- Djinsta🔥</h1>
<p>This is a Django-based social media web app that uses Docker for containerization. The app allows users to create posts, like and comment on posts,chat and follow other users.</p>

<h2>Requirements</h2>

<ul>
	<li>Docker</li>
	<li>Docker Compose</li>
</ul>

<h2>Installation and Setup</h2>

<ol>
	<li>Clone the repository:
	<pre>
		git clone https://github.com/sankalp-7/Djinsta.git
		cd social_media_app
	</pre>
	</li>
	<li>Install Requirements
	<pre>
		pip install -r requirements.txt
	</pre>
	</li>
	<li>Create a .env file in the root directory with the following environment variables:
	<pre>
		SECRET_KEY=your_secret_key_here
		DEBUG=True
		DB_NAME=YOUR_DB_NAME
		DB_USER=YOUR_DB_USERNAME
		DB_PASSWORD=YOUR_DB_PASSWORD
		DB_HOST=YOUR_DB_HOST
		DB_PORT=YOUR_DB_PORT(3306 FOR MYSQL)
	</pre>
	</li>
	<li>Build and start the Docker containers:
	<pre>docker-compose up --build</pre>
	</li>
	<li>Create the initial database tables and load the initial data:
	<pre>
		docker-compose exec web python manage.py migrate
		docker-compose exec web python manage.py loaddata initial_data.json
	</pre>
	</li>
	<li>Create a superuser account:
	<pre>docker-compose exec web python manage.py createsuperuser</pre>
	</li>
	<li>
		<pre>Access the web app at <a href="http://localhost:8000/">http://localhost:8000/</a> and log in with your superuser account.</pre></li>
</ol>

<h2>Usage</h2>

<p>The web app allows users to create posts, like and comment on posts, and follow other users. Users can also edit their profiles and view other users' profiles.</p>

<h2>Development</h2>

<p>The web app can be developed and tested locally by running the Django development server:</p>
<pre>docker-compose up --build</pre>
<p>You can then access the development server at <a href="http://localhost:8000/">http://localhost:8000/</a>.</p>

<h2>Deployment</h2>

<p>The web app can be deployed to a production server using a platform like Docker Swarm or Kubernetes. You will need to update the <code>docker-compose.yml</code> file with your production environment settings and configure your production server accordingly.</p>
</body>
</html>

