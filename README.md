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
   Copy code
   cd Django-autenticacao.git
3. Crie e ative um ambiente virtual:

   ```shell
   Copy code
   python -m venv venv
   venv\Scripts\activate

4. Instale as dependências do projeto:

   ```shell
   Copy code
   pip install -r requirements.txt
   Configure as variáveis de ambiente no arquivo .env com as suas credenciais do Amazon S3.

5. Execute as migrações do banco de dados:

   ```shell
   Copy code
   python manage.py makemigrations
   python manage.py migrate
   Inicie o servidor local:

   ```shell
   Copy code
   python manage.py runserver
   Acesse o projeto no navegador: http://localhost:8000

Funcionalidades
Upload de imagens
Visualização de imagens
Edição de imagens
Exclusão de imagens
bash
Copy code

Lembre-se de substituir os dados do repositório e as informações do autor pelos seus próprios dados no README.
