# Prem Doctor

Prem Doctor is a web app built with Python, [Streamlit](https://streamlit.io/), [LangChain](https://python.langchain.com/docs/get_started/introduction.html), and [PremAI](https://www.premai.io/) to allow simple medical consultations before attending a doctor. Prom Doctor does not store the data, giving users greater confidence and security.
The idea of this project is to save people time and money and to know which doctor to see in case of a medical problem they have.

## Licence
[MIT](./LICENCE)

## How works

1. Install [PremAI](https://www.premai.io/) in your computer or a server.
2. Configure one model of those available in the service, and copy its URL.
3. Install [Streamlit](https://streamlit.io/) or use Streamlit Cloud.
4. Install all libraries in [requirements.txt](./requirements.txt).
5. Add these secrets in Streamlit:
   - _openai_key_: Any random secret, because with PremAI you don't need a key, but because the platform use OpenAI Python library, you need to specify anything.
   - _openai_url: The URL for your model on PremAI (step 2). For example: http://localhost:8111/v1
   - _max_tokens_: The maximum number of tokens for the generated response. 
6. Run the web app (in Streamlit Cloud just wait to compile automatically).

Created by [Néstor Nicolás Campos Rojas](https://www.linkedin.com/in/nescampos/)
