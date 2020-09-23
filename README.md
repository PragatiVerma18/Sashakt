
<div align="center"> <img align="center" alt="sashakt" src="https://sashakt.netlify.app/static/media/awsar.e12625ad.png" height='150' width='350'></div>

# Sashakt

Sashakt is an online job portal for rural women that connects them easily with the employers looking for talented and skilled women, accompanied by a number of features to ease the process for rural women and the employers.

The platform is available with multiple language support which eleminates all the entry barriers for rural women seeking for jobs.

> See the hosted website [Here](https://sashakt.netlify.app/)

## Demo Video:
<a href="https://www.youtube.com/watch?v=2DG5oM-qdXk" target="_blank" rel="noopener">
  <img src="https://user-images.githubusercontent.com/42115530/93972332-b2321a00-fd8f-11ea-96eb-fd871e4dfbb5.png" alt="Sashakt: Job Portal for women"
	title="Sashakt" width="500px" />
</a>

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

## Links:
- **Frontend**: [https://sashakt.netlify.app/](https://sashakt.netlify.app/)
- **Backend**: [https://sashakt.herokuapp.com/](https://sashakt.herokuapp.com/)
- **PPT**: [http://bit.ly/sashakt2020](http://bit.ly/sashakt2020)
- **YouTube Video**: [https://youtu.be/2DG5oM-qdXk](https://youtu.be/2DG5oM-qdXk)

## Setup


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

## GirlScript India Summit 2020
> Team Alpha was selected as the 2nd runner-up in GirlScript India Summit 2020 Hackathon

[![GirlScript India Summit](https://girlscriptsummit.com/images/summitlogolg.png)](https://girlscriptsummit.com/hackathon/)

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody><tr>
    <td align="center"><a href="https://rajat2502.github.io/portfolio/"><img alt="" src="https://avatars2.githubusercontent.com/u/42200276?v=4" width="100px;"><br><sub><b>Rajat Verma</b></sub></a><br><a href="https://github.com/PragatiVerma18/Sashakt/commits?author=rajat2502" title="Code">💻</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/PragatiVerma18/"><img alt="" src="https://avatars2.githubusercontent.com/u/42115530?v=4" width="100px;"><br><sub><b>Pragati Verma</b></sub></a><br><a href="https://github.com/PragatiVerma18/Sashakt/commits?author=PragatiVerma18" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/shristisingh29"><img alt="" src="https://avatars1.githubusercontent.com/u/44435610?v=4" width="100px;"><br><sub><b>Shristi Singh</b></sub></a><br><a href="#design-shristisingh29" title="Design">🎨</a></td>
        <td align="center"><a href="https://github.com/stark019"><img alt="" src="https://avatars2.githubusercontent.com/u/46189913?s=460&u=8dc90bd6845b9c91f75f51674ce9804c12cabe9b&v=4" width="100px;"><br><sub><b>Nihal Pandey</b></sub></a><br><a href="https://github.com/PragatiVerma18/Sashakt/commits?author=stark019" title="Code">💻</a></td>
  </tr>
</tbody></table>

