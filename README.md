# Sistema de Gerenciamento de Tarefas

## Objetivo

Este projeto tem como objetivo desenvolver uma aplicação web de gerenciamento de tarefas, inspirada no Trello. A aplicação permitirá que os usuários organizem suas tarefas, oferecendo funcionalidades como criar, editar, excluir e atribuir tarefas a outros usuários. Além disso, será possível acompanhar o status de cada tarefa, seja ela pendente, em andamento ou concluída.

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

- **Backend**: O sistema será desenvolvido utilizando os frameworks Flask ou Django.
- **Banco de Dados**: Um banco de dados será implementado para armazenar as informações de usuários e tarefas.
- **Autenticação**: A autenticação será aplicada para garantir que apenas usuários registrados possam acessar e gerenciar tarefas.
- **Frontend**: 
  - HTML e CSS serão utilizados para construir a interface.
  - O Bootstrap poderá ser incorporado para criar uma interface mais atraente e minimamente responsiva.