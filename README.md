# LangChain Application Template

Get a `/chat` API up and running in under 5 minutes with LangChain and FastAPI.

## Features

- Service definition with FastAPI
- Preconfigured `/chat` endpoint and basic OpenAI chain
- Testing with pytest
- Production builds with Docker
- Environment management with uv

## Getting Started

### Prerequisites

- [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html#install-cookiecutter) >= 2.6.0
- [uv](https://docs.astral.sh/uv/getting-started/installation/) >= 0.5.11
- [OpenAI API Key](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://platform.openai.com/api-keys&ved=2ahUKEwiDjITk5-iKAxWxlokEHfAwKPIQFnoECAsQAQ&usg=AOvVaw1YhcGDWJXhiKSfmL59Pnfn)

### Usage
1. From the terminal, run `cookiecutter https://github.com/jolfr/langchain-application-template`
2. Follow on-screen prompts to configure the project. Paste in the OpenAI API key when prompted.
3. Wait for the project to generate then `cd <project_slug>` into the project folder.
4. Take a look at the `README.md`. It has useful commands to help you get up and running.
5. Fire up a development server with `uv run bash scripts/dev.sh`
6. Navigate to `localhost:8000/docs` for the Swagger documentation.
7. Test the `/chat` endpoint by clicking the "Try it out" button and entering a message.