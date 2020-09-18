
<div align="center"> <img align="center" alt="codeinn" src="https://sashakt.netlify.app/static/media/awsar.e12625ad.png" height='150' width='350'></div>

# Sashakt

Sashakt is an online job portal for rural women that connects them easily with the employers looking for talented and skilled women, accompanied by a number of features to ease the process for rural women and the employers.

The platform is avalible with multiple language support which eleminates all the entry barriers for rural women seeking for jobs.

## Key Features:
- Professional profiles for the users as well as organisations.
- Schedule Interviews using google meet integrations.
- Multi lingual interface makes it more assesable in rural areas
- Progressive Web App (mobile friendly interface as most of the user don't have access to desktops)
- Getting a job by competing 1000s of applicants is not an easy task so to celebrate your achievement the platform also awards you with "Certificate of Selection".
- Jobs at its core are the game of demand and supply of skills so to full fill this the platform offers courses to upskill yourself and detailed analytics of in-demand skills in market.

## Technology Stack:
- **Frontend**: React
- **Backend**: Django, Django Rest Framework
- **IDE**: VS Code
- **Design**: Adobe Photoshop, Canva
- **API Testing & Documentation**: Postman
- **Version Control**: Git and GitHub
- **Machine Learning**: Python, Jupyter Notebook
- **Database**: Sqllite3
- **Hosting**: Heroku, Netlify

#### Setup


<details>
  <summary><strong>Frontend Setup Instructions</strong></summary>
  
  
- Fork and Clone the repo using
```
$ git clone https://github.com/PragatiVerma18/Sashakt.git
$ cd Sashakt
```

- Get the API key from [https://api.imgbb.com/](https://api.imgbb.com/) and replace it with `REACT_APP_IMGBB_API_KEY` in `.env.example`

- Get a new API key from [https://smtpjs.com/](https://smtpjs.com/) and replace it with `REACT_APP_API_KEY` in `.env.example`

- Rename the file `.env.example` to `.env`

- Install node dependencies
```
$ npm install
```
- Run Server at localhost using
```
$ npm start
```

  
</details>


<details>
  <summary><strong>Backend Setup Instructions</strong></summary>

- Fork and Clone the repo using
```
$ git clone https://github.com/PragatiVerma18/Sashakt.git
$ cd Sashakt
```
- Change Branch to `backend` using 
```
$ git checkout backend
```
- Setup Virtual environment
```
$ python3 -m venv env
```
- Activate the virtual environment
```
$ source env/bin/activate
```
- Install dependencies using
```
$ pip install -r requirements.txt
```
- Make migrations using
```
$ python manage.py makemigrations
```
- Migrate Database
```
$ python manage.py migrate
```
- Create a superuser
```
$ python manage.py createsuperuser
```
- Run server using
```
$ python manage.py runserver
``` 
</details>

## Team:

> Team Members

| S.No. | Team Member Name | Role | GitHub Username |
| --------------- | --------------- | --------------- | --------------- |
| 1. | Pragati Verma(Team Leader) | Backend Development | [@PragatiVerma18](https://github.com/PragatiVerma18) |
| 2. | Rajat Verma | Frontend Developer| [@rajat2502](https://github.com/rajat2502)  |
| 3. | Shristi Singh | UI Designer/Frontend Developer | [@shristisingh29](https://github.com/shristisingh29)  |
| 4. | Nihal Pandey | Project documentation and Backend | [@stark019](https://github.com/stark019) |

