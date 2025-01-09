# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Development

Run FastAPI server in develpment mode with hot reloading:

`uv run bash scripts/dev.sh`

NOTE: this will auto-activate the virtual environment.

To manually activate virtual environment you can run:

`source .venv/bin/activate`

## Testing

Run all tests with pytest:

`pytest`

## Production

A Dockerfile has been included for easy builds to production.

To build run the following command:

`docker build -t {{ cookiecutter.project_slug }} .`

FastAPI will be exposed on port 80 of the image.

To run the build locally:

`docker run -p 8000:80 {{ cookiecutter.project_slug }}`

This will expose the application on port 8000 of your local machine.

As an alternative to a Docker build, a script has been included for production runs.

You can run like so:

`uv run bash scripts/prod.sh`

### Credits

This project was bootstrapped using [LangChain Application Template](https://github.com/jolfr/langchain-application-template) by [jolfr](https://github.com/jolfr)