# Port Scanner

##  Sobre:
Uma ferramenta desenvolvida em Python para automatizar as buscas e detectar portas abertas. Este projeto foi criado para consolidar meus estudos em Cibersegurança.

##  Tecnologias Utilizadas:
* Python 3
* Biblioteca Socket / Regex
* Linux

##  Como usar:
1. Clone o repositório.
2. Execute o comando `python scanner.py`.
3. Insira o IP alvo.

##  O que eu aprendi:
* Aprendi como funciona o handshake TCP.
* Entendi a importância de tratar exceções em scripts de rede.
* Tive dificuldade em fazer o script não travar, quando encontrava um firewall que descartava pacotes silenciosamente. Superei isso implementando o socket.setdefaulttimeout(1), garantindo que o scanner não fique esperando infinitamente por uma resposta que nunca virá.
