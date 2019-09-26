# CodePage
CodePage is a code-sharing website curated by the community and built with open source
technologies.

## Architecture
CodePage is built with Flask and uses PostgreSQL as its database backend. In this repository,
there is a `docker-compose.yml` file specifying two containers, `database` and `webserver`.

If you want to install Postgres and Python on your local machine that is fine too. Just
change the relevant configuration in the `webserver` directory to point to your Postgres
instance and install the same packages that are installed by the `webserver` Dockerfile.

## Setup
Build the Docker containers with `docker-compose build`
Create the database schema `docker-compose exec webserver python src/makedb.py`

