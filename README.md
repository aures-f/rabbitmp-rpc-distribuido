## 🐇 Sistema RPC Distribuído com RabbitMQ

Este projeto implementa um sistema simples utilizando RabbitMQ para comunicação RPC entre um cliente e vários serviços independentes.  
Cada serviço roda em um processo separado, consumindo sua própria fila.  
O objetivo é demonstrar comunicação assíncrona, distribuição de tarefas e o uso do padrão Request/Response.

---

## 📂 Estrutura do projeto

```text
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
```

---

## 🚀 Como executar

### 1. Ativar o ambiente virtual
```
venv\Scripts\activate
```

### 2. Instalar as dependências
```
pip install pika
```
```
pip install -r requeriments.txt
```


### 3. Iniciar o RabbitMQ  
No Windows (PowerShell como administrador):
```
net start RabbitMQ
```

### 4. Iniciar os serviços (um terminal para cada um)
```
python services/service_soma.py
python services/service_media.py
python services/service_busca.py
python services/service_dobro.py
```

### 5. Executar o cliente
```
python client/rpc_client.py
```

---

## 🧠 Funcionamento

O cliente envia requisições para filas específicas e aguarda a resposta.  
Cada serviço só responde aos pedidos da sua própria fila.  
Se duas instâncias do mesmo serviço estiverem rodando, o RabbitMQ divide as requisições automaticamente.

Serviços disponíveis:

- Soma  
- Média  
- Busca  
- Dobro  

---

## 🧪 Exemplo de uso

Menu exibido:

```
1 - Soma
2 - Média
3 - Busca
4 - Dobro
0 - Sair
```

Exemplo de operação (Soma):

```
Primeiro número: 10
Segundo número: 15
Resultado: 25
```

---

## 📦 Dependências

```
pika
```

---

## 📌 Observações

- Os serviços precisam estar rodando para atender o cliente.  
- Cada serviço funciona como um consumidor independente no RabbitMQ.  
- A comunicação segue o padrão RPC demonstrado no Tutorial 6 do RabbitMQ.  
