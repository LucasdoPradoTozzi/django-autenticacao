# Django-Autenticacao


## Descrição

O Alura Space é um projeto desenvolvido durante os cursos de Django: Django: templates e boas práticas, Django: persistência de dados e Admin, Django: autenticação de formulários e alertas e Django: CRUD e persistência no S3 da Alura. Ele é um website que permite o upload, visualização, edição e exclusão de imagens. Além disso, o projeto pode ser personalizado e compartilhado nas redes sociais.

## Tecnologias Utilizadas

- Python
- Django
- Amazon S3

## Instruções de Instalação

1. Clone o repositório do projeto:

   ```shell
   git clone git@github.com:LucasdoPradoTozzi/django-autenticacao.git

2. Acesse a pasta do projeto:

   ```shell
   cd Django-autenticacao.git

3. Crie e ative um ambiente virtual:

   ```shell
   python -m venv venv
   venv\Scripts\activate

4. Instale as dependências do projeto:

   ```shell
   pip install -r requirements.txt

5. Execute as migrações do banco de dados:

   ```shell
   python manage.py makemigrations
   python manage.py migrate

8. Configure suas próprias chaves do django e do Amazon S3:

   Crie um arquivo .env na base do projeto e complete com as informações:
   ```shell
   SECRET_KEY = 'suasecretkey'

   AWS_ACCESS_KEY_ID = 'suaawskey'

   AWS_SECRET_ACCESS_KEY = 'suaawssecretkey'

   AWS_STORAGE_BUCKET_NAME = 'nomedoseubucket'

7. Inicie o servidor local:

   ```shell
   python manage.py runserver
   Acesse o projeto no navegador: http://localhost:8000

## Funcionalidades:

1. Criação de Usuário
2. Login
3. Logout
4. Upload de imagens
5. Visualização de imagens
6. Edição de imagens
7. Exclusão de imagens

