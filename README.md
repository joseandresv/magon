# magon
Repositorio de ChatBot Magon

## Instalar Requirements
`pip install -r requirements_demo.txt`

## ChatGPT token
PAra que funcione deben poner el token de su API de ChatGPT en el archivo `.env`, un ejemplo de como debe verse ese archivo esta en `.env_example`. Crea uno que se llame `.env` en tu local, este archivo esta protegido por el `.gitignore` para no subirse a github, sin embargo se cuidadose. Si necesitas uno escribeme y te comparto el mio.

## Demo
Primero se debe correr el `scrapping` para bajar las noticias del tema, despues el `ChatBot` para responder preguntas. El demo solo utiliza los articulos que descargaste.

### Scrapping
`01_scrapper_demo.ipynb` notebook demo para scrappear las noticias

### ChatBot
`02_paperqa_demo.ipynb` demo para hacer preguntas

### MongoDB database
Por ahora para guardar los documentos existe una base de datos de MongoDB en la nube. Para entender como funciona utiliza el `03_def_mongodb.ipynb`. Agrega el `client` a tu `.env`. Ve el ejemplo en `.env_example`

## TODO
- [ ] Crear pip.lock
- [ ] Mejorar scrapper para hacerlo mas robusto a missings
- [ ] Mejorar el scrapping de autores
- [ ] Parsear la respuesta del chatbot para que las citas sean mejores
- [ ] Definir formato a guardar las noticias 
- [ ] Montar base de MongoDB
- [ ] Crear Docker-dev
- [ ] Crear Docker-deployment