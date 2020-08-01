# automate-create-project

Automates the process of creating a new project by creating a new repository on GitHub and cloning it to your local machine. 

## To install:

```
$ git clone https://github.com/quibbleahr/automate-create-project.git
$ cd automate-create-project/
$ pip install -r requirements.txt
$ touch .env
$ source .create_command.sh
```

## .env file:

After creating the `.env` file as shown above, put in your access token like so:

```
ACCESS_TOKEN="<your_access_token>"
```


## To use:

```
$ create <your_project_name>
```