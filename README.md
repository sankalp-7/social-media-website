<!DOCTYPE html>
<html>
<head>
</head>
<body>
	<h1>Django Social Media Web App -- Djinsta</h1>
<p>This is a Django-based social media web app that has key functionalities like posting, following,
commenting, like, chat, and notifications..</p>

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
	<li>
	<pre>
		python manage.py makemigrations
	</pre>
	</li>
	<li>
	<pre>
		python manage.py migrate
	</pre>
	</li>
	<li>
	<pre>
		python manage.py runserver
	</pre>
	</li>
</ol>

<h3>OR IF YOU HAVE DOCKER</h3>

<ol>
	<li>
		<pre>
			docker-compose up
		</pre>
	</li>
</ol>

<h2>Usage</h2>

<p>The web app allows users to create posts, like and comment on posts,Chat with fellow friends and follow other users. Users can also edit their profiles and view other users' profiles.</p>

<h2>Development</h2>

<p>The web app can be developed and tested locally by running the Django development server:</p>
<pre>docker-compose up --build</pre>
<p>You can then access the development server at <a href="http://localhost:8000/">http://localhost:8000/</a>.</p>

<h2>Deployment</h2>

<p>The web app can be deployed to a production server using a platform like Docker Swarm or Kubernetes. You will need to update the <code>docker-compose.yml</code> file with your production environment settings and configure your production server accordingly.</p>
</body>
</html>
<h2>Signin Page</h2>
![image](https://github.com/sankalp-7/Djinsta/assets/104098061/c2baecf4-aa29-4d25-952c-347d2637bc50)
<h2>Home Page</h2>
![image](https://github.com/sankalp-7/Djinsta/assets/104098061/d979d038-6593-4c0a-a3f9-0e155bd45563)
<h2>Profile Page Of Users</h2>
![image](https://github.com/sankalp-7/Djinsta/assets/104098061/9bce93fe-bba7-4995-84a4-5a7f5c804192)
<h2>Group Chat Page</h2>
![image](https://github.com/sankalp-7/Djinsta/assets/104098061/f6414d13-8ffc-4265-8983-d515ffefe45d)
<h2>Real Time Notification System</h2>
![image](https://github.com/sankalp-7/Djinsta/assets/104098061/a9868c0c-4bdc-4ef3-8395-cd3f2ec8170d)
<h2>Account Search System</h2>
![image](https://github.com/sankalp-7/Djinsta/assets/104098061/453e6606-1535-41e7-922b-f1385ce3fa85)
<h2>Mobile Home Page View</h2>
![image](https://github.com/sankalp-7/Djinsta/assets/104098061/82611592-e913-4434-b2c8-0cf8614e6432)



