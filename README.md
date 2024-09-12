# Sistema de Gerenciamento de Tarefas

## Objetivo

Este projeto tem como objetivo desenvolver uma aplicação web para gerenciamento de tarefas, inspirada no Trello. A aplicação permitirá que os usuários organizem suas tarefas com funcionalidades como criar, editar, excluir e atribuir tarefas. Além disso, será possível acompanhar o status de cada tarefa, seja ela pendente, em andamento ou concluída.

## Funcionalidades

1. **Cadastro e Autenticação de Usuários**:  
   - Registro de novos usuários, login e logout para controle de sessão.
   - Cada usuário terá acesso apenas às suas próprias tarefas, que poderão ser gerenciadas individualmente.

2. **Gerenciamento de Tarefas**:  
   - Criação, visualização, edição e exclusão de tarefas.
   - Cada tarefa incluirá um título, descrição e status.
   - As tarefas podem ser atribuídas a outros usuários do sistema para promover a colaboração.

3. **Status das Tarefas**:  
   - As tarefas poderão ter os seguintes status: "pendente", "em andamento" ou "concluída".
   - O sistema permitirá filtrar tarefas por status, facilitando a organização.

4. **Dashboard de Tarefas**:  
   - Um painel para que os usuários acompanhem todas as tarefas do grupo, facilitando a visualização do progresso coletivo.

## Tecnologias Utilizadas

- **Backend**: Flask
- **Banco de Dados**: SQLAlchemy
- **Autenticação**: Flask-Login
- **Frontend**: 
  - HTML e CSS
  - Tailwind (para uma interface mais atraente e responsiva)

## Instalação

1. **Clone o Repositório**
    https://github.com/kieskii/Trabalho-WebPython.git   
    cd Trabalho-WebPython

2. **Crie e Ative um Ambiente Virtual**
   python -m venv venv
   source venv/bin/activate

3. **Instale as Dependências**
   pip install -r requirements.txt

4. **Configure o Banco de Dados**
   flask db upgrade

5. **Execute a Aplicação**
   flask run

   A aplicação estará disponível em `http://127.0.0.1:5000`.

## Uso

- **Cadastro e Login**: Acesse `/register` para criar uma nova conta e `/login` para autenticar-se.
- **Gerenciamento de Tarefas**: Após o login, você pode acessar o dashboard para gerenciar suas tarefas e criar novas tarefas através da interface.