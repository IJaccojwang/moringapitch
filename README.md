# Moringa Pitch

## Description

Moringapitch is a flask application providing access to all capstone projects Moringa School Students undertook allowing users to also pitch project ideas to be viewed by other users

#### Authors

- Ian Jaccojwang
- Augustine Ochieng
- Badrudin Noor
- Ephraim Maina

## Setup/Installation Requirements

### Prerequisites

- python3.6
- pip
- Virtual environment(virtualenv)

### Cloning and running

- Clone the application using git clone(this copies the app onto your device). In terminal:

          `git clone https://github.com/IJaccojwang/moringapitch/`
           `cd moringapitch`

- Creating the virtual environment

          `python3.6 -m venv --without-pip virtual`
          `source virtual/bin/env`
          `curl https://bootstrap.pypa.io/get-pip.py | python`

- Installing Flask and other Modules

          `python3.6 -m pip install Flask`
          `python3.6 -m pip install Flask-Bootstrap`
          `python3.6 -m pip install Flask-Script`
          `python3.6 -m pip install -r requirements.txt`

- Run the application:

          `chmod a+x start.sh`
          `./start.sh`

### Testing the Application

- To run the tests for the class files:

          `python3.6 manage.py test`

## Technologies Used

```
* Python 3.6
* Flask
* Postgresql
* MDBootstrap
```

## Behaviour driven development/ Specifications

| Behaviour                                                         | Sample Input                                        | Sample Output                                                 |
| ----------------------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------- |
| Display landing page with pitches categorised according to cohort | Link to live site                                   | The landing page is displayed                                 |
| Display all projects for a selected cohort                        | Click on 'view projects' button                     | projects for the selected cohort displayed                    |
| View details of pitch, including comments of the pitch            | Click on 'view more' button                         | Display project description and comments                      |
| Prompt user to login                                              | Click on 'sign in'/'add comment'/'add pitch' button | Display login form                                            |
| Authenticate user to add a Pitch and comment                      | If user has no account a sign up form is displayed  | User is automatically logged in and free to add pitch/comment |
| Allow user to log out                                             | Click on 'logout' button                            | User is automatically logged out                              |

### Link to live site

[Here](https://github.com/IJaccojwang/moringapitch) is a link to the live site

## Support and contact details

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

### License

[MIT License](https://choosealicense.com/licenses/mit/)
Copyright (c) {2019}
