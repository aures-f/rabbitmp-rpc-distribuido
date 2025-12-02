🐰Sistema RPC Distribuído com RabbitMQ

Este projeto implementa um sistema distribuído simples utilizando RabbitMQ para chamadas RPC entre um cliente e vários serviços independentes.
O foco é demonstrar comunicação assíncrona, uso de múltiplos serviços, filas separadas e o funcionamento do padrão Request/Response.

📂 Estrutura do Projeto
rabbitmp-rpc-distribuido/
│
├── client/
│   └── rpc_client.py
│
├── common/
│   └── rpc_utils.py
│
├── services/
│   ├── service_soma.py
│   ├── service_media.py
│   ├── service_busca.py
│   └── service_dobro.py
│
└── requeriments.txt

🧠 Descrição Geral

O cliente envia solicitações para diferentes filas, e cada serviço responde apenas às chamadas do seu tipo.
Cada serviço é executado em um terminal separado, funcionando como um consumidor independente.
Se várias instâncias do mesmo serviço forem abertas, o RabbitMQ divide as requisições entre elas, mostrando a distribuição de tarefas.

Serviços disponíveis:

Soma
Média
Busca simples
Dobro

🚀 Como Executar
1. Ativar o ambiente virtual
venv\Scripts\activate

2. Instalar dependências
pip install -r requeriments.txt

3. Iniciar o RabbitMQ

No Windows (PowerShell como Administrador):

net start RabbitMQ

4. Executar os serviços

Abra um terminal diferente para cada comando:

python services/service_soma.py
python services/service_media.py
python services/service_busca.py
python services/service_dobro.py

5. Executar o cliente
python client/rpc_client.py


O cliente apresenta o menu de opções e envia as requisições para o serviço correspondente.

🧪 Exemplo de Uso

Menu exibido:

1 - Soma
2 - Média
3 - Busca
4 - Dobro
0 - Sair


Exemplo de chamada (Soma):

Informe o primeiro número: 10
Informe o segundo número: 15
Resultado: 25

📦 Dependências

O projeto utiliza a biblioteca:

pika

🔍 Observações

Os serviços devem permanecer abertos para atender as requisições.

A comunicação segue o padrão RPC do RabbitMQ.

Cada serviço possui sua própria fila.

Caso haja duas instâncias de um mesmo serviço, o RabbitMQ faz o balanceamento automaticamente.