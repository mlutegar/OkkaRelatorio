# GIT

Comando para atualizar o repositório:

```bash
$ git pull
```

Comando para adicionar todos os arquivos:

```bash
$ git add .
```

Comando para fazer commit dos arquivos:

```bash
$ git commit -m "feat: adicionando bibliotecas" --no-verify
```

Comando para fazer push dos arquivos:

```bash
$ git push --no-verify
```

# DJANGO 

Para atualizar o banco de dados, execute os comandos abaixo:

```bash
$ python manage.py makemigrations
```

```bash
$ python manage.py migrate
```

Para rodar o servidor, execute o comando abaixo:

```bash
$ python manage.py runserver
```

Para rodar o servidor em uma porta específica, execute o comando abaixo:

```bash
python manage.py runserver 0.0.0.0:8000
```

Para criar um super usuário, execute o comando abaixo:

```bash
$ python manage.py createsuperuser
```

Criar um app no Django, execute o comando abaixo:

```bash
$ python manage.py startapp backend
```

# DOCKER

Para criar um docker build, execute o comando abaixo:

```bash
docker build -t mlutegar/gtddjango:v1 .
```

Para rodar o docker, execute o comando abaixo:

```bash
docker run -p 8000:8000 mlutegar/gtddjango:v1
```

Para dá um push no docker, execute o comando abaixo:

```bash
docker push mlutegar/gtddjango:v1
```

# FLY

Para instalar o fly, execute o comando abaixo:

```bash
iwr https://fly.io/install.ps1 -useb | iex
```

Para verificar se o fly foi instalado corretamente, execute o comando abaixo:

```bash
fly version
```

Para inicializar o projeto fly, execute o comando abaixo:

```bash
fly launch
```

Para dá deploy no fly, execute o comando abaixo:

```bash
fly deploy
```

Para ver a lista de volumes, execute o comando abaixo:

```bash
fly volume list 
```

Para destruir um volume específico, execute o comando abaixo:

```bash
fly volume destroy
``` 

Para entrar no shell do fly, execute o comando abaixo:

```bash
fly ssh console
```
Para sair bastar digitar `exit` e pressionar `Enter`.