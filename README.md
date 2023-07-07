# Prem Doctor

Prem Doctor is a web app built with Python, Streamlit, LangChain and [PremAI](https://www.premai.io/) to allow simple medical consultations before attending a doctor. Prom Doctor does not store the data, which gives greater confidence and security for users.
The idea of this project is to save people time and money and to know which doctor to see in case of the medical problem they have.

## Licence
[MIT](./LICENCE)

## Demo
Video (with an explanation): 

## How works

1. Install [PremAI](https://www.premai.io/) in your computer or a server.
2. Configure one model of those available in the service, and copy its URL.
3. Install [Streamlit](https://streamlit.io/) or use Streamlit Cloud.
4. Install all libraries in [requirements.txt](./requirements.txt).
5. Add these secrets in Streamlit:
   a. _openai_key_: Any random secret, because with PremAI you don't need key, but because the platform use OpenAI Python library, you need to specify anything.
   b. _openai_url: The URL for your model on PremAI (step 2). For example: http://localhost:8111/v1
   c. _max_tokens_: The maximum number of tokens for the generated response. 
6. Run the web app (in Streamlit Cloud just wait to compile automatically).

Created by [Néstor Nicolás Campos Rojas](https://www.linkedin.com/in/nescampos/)
