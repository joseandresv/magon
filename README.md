# magon
Repositorio de ChatBot Magon

## ChatGPT token
PAra que funcione deben poner el token de su API de ChatGPT en el archivo `.env`, un ejemplo de como debe verse ese archivo esta en `.env_example`. Crea uno que se llame `.env` en tu local, este archivo esta protegido por el `.gitignore` para no subirse a github, sin embargo se cuidadose.

## Demo
Primero se debe correr el `scrapping` para bajar las noticias del tema, despues el `ChatBot` para responder preguntas. El demo solo utiliza los articulos que descargaste.

### Scrapping
`01_scrapper_demo.ipynb` notebook demo para scrappear las noticias

### ChatBot
`02_paperqa_demo.ipynb` demo para hacer preguntas


## TODO
- [ ] Crear pip.lock
- [ ] Mejorar scrapper para hacerlo mas robusto a missings
- [ ] Mejorar el scrapping de autores
- [ ] Parsear la respuesta del chatbot para que las citas sean mejores
- [ ] Definir formato a guardar las noticias 
- [ ] Montar base de MongoDB