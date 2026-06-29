# Backend de Auto Factory

Aqui temos nossa API que salva conteúdo no banco de dados e faz comunicações MQTT com os Iot da fábrica.

## Organização do projeto

### /src/config/
Configurações básicas do projeto, a principio sendo usado apenas para se conctar ao BROKER do MQTT e gerenciar as as mensagens recebidas.

### /src/controllers/
É o controller e router da nossa API, aqui tem endpoints e chamada de funções que cuidam das regras de negócio.

### /src/handlers/
É aqui que são processadas as novas mensagens do MQTT.

### /src/services/
Onde se encontra a lógica de negócio, normalmente chamada por um controller.

### /src/main.py
Inicia todos os serviços.