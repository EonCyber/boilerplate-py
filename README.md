# Boilerplating is fun!

In this python project we are invited to tweak and configure our projects boilerplate, so that we can accelerate the creation of new base projects to start coding new features.

Thats possible using:
- Python (System automation)
- Jinja2 (for template rendering)
- PyYaml (for creating new template configurations)

## Node JS + Typescript

At the momment in this version we are able to create a Node + Typescript Http Express Server ready to use.

*But the code can be modified to use for any type of software project bootstrap later.*

# Using it
On your system you need to have:
- Python3 Installed
- NodeJs and Npm Installed
- Connection to the Internet (for downloading packages)

Project Creation:
on the Terminal in the Boilerplate Project directory
```ps
# Create a new Virtual Environment
python -m venv venv

# Activate Environment
.\venv\Scripts\activate  

# Install Requirements
pip install -r requirements.txt

# Run the app
python boilerplate.py <YOUR_PROJECT_NAME>

```

<YOUR_PROJECT_NAME> will be used to create the output project folder and passed to npm as project name.
OUTPUT: The /output directory is the target for the new project

# Database Mongodb

After creating a new project uncomment the db.connect in the app.ts and insert your mongodb URI and PORT. When you run the project with "npm run start:dev" it should display the Database Connection.

# Future
Ideas for the future:
- Generate new templates (with Error Handling, Mongo in-Memory Database, Etc) 
- To remove node_modules at the end of the first project test(?)
- Create options for new types of projects (Node Batch, Node Socket, React, Java Springboot, Php, etc) 

*feel free to reach me out for any suggestions or contributions*
