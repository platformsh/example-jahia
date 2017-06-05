# Jahia template for Platform.sh

This project provides a starter kit for Jahia single-node projects hosted on Platform.sh. Jahia single-node projects are strongly recommended to use this template.

## Starting a new project

To start a new project based on this template, follow these 3 simple steps:

1. Clone this repository locally.  You may optionally remove the `origin` remote or remove the `.git` directory and re-init the project if you want a clean history.

2. Create a new project through the Platform.sh user interface and select "Import an existing project" when prompted.

3. Run the provided Git commands to add a Platform.sh remote and push the code to the Platform.sh repository.

That's it!  You now have a working "hello world" level project you can build on.

## Jahia-as-a-Service

Jahia itself runs as a pre-build Service within the cluster rather than being the primary "application".  In that sense it is managed more akin to MySQL or Redis.  (See [`services.yaml`](.platform/services.yaml).)  Incoming requests are then routed to that service directly rather than the application container.

The Jahia configuration files may be specified by the `services.yaml` file.  Although defaults are present providing custom configuration files is strongly recommended.

What is stored in Git is any custom code for additional plugins that need to be compiled and installed.
  The included `.platform.app.yaml` file handles that process.  Each plugin should be placed in its own directory and then compiled by the build hook.  Modify the build hook as needed.

On deploy, the provided `deploy.py` script is executed.  The only value in that script that should be edited is the JAHIA_RELATIONSHIP variable at the top, if the jahia service is named differently from the template.  In most cases that is not necessary.
  
The `deploy.json` file specifies what jar files to install.  Any file listed there will be POSTed over HTTP to the Jahia service after it is compiled, and marked to both install and enable.

In most circumstances the Jahia service will not restart on deployment of a new commit, although on deployment of a new branch it may take 1-2 minutes to become available.  If the contents of the `.platform` directory are modified, however, the Jahia service may restart, and be unavailable for 1-2 minutes.
