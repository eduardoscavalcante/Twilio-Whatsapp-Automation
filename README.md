# Twilio WhatsApp Automation

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/release/python-380/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Tabela de Conteúdos
1. [Sobre o Projeto](#sobre-o-projeto)
2. [Funcionalidades](#funcionalidades)
3. [Configuração](#configuração)
4. [Uso](#uso)

## Sobre o Projeto
Este projeto demonstra como automatizar o envio de mensagens no WhatsApp usando a API do Twilio. Ideal para notificações automáticas, mensagens em massa, e muito mais.

## Funcionalidades
- Envio de mensagens automáticas pelo WhatsApp.
- Suporte a múltiplos destinatários.
- Integração fácil com sistemas existentes.

## Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/twilio-whatsapp-automation.git
   cd twilio-whatsapp-automation

2. Crie e ative o ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt

4. Configure as variáveis de ambiente:
   ```bash
   cp .env.example .env
Preencha o arquivo .env com suas credenciais do Twilio.

## Uso
Para enviar uma mensagem de teste:
   ```bash
   python src/main.py

## Explicação do main.py:
Carregamento de Variáveis de Ambiente:

As credenciais do Twilio (TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, e TWILIO_PHONE_NUMBER) são carregadas a partir de um arquivo .env usando a biblioteca dotenv.
Inicialização do Cliente Twilio:

Um cliente Twilio é criado para facilitar o envio de mensagens.
Função send_whatsapp_message:

Esta função recebe dois parâmetros (to e message) e envia uma mensagem via WhatsApp utilizando a API do Twilio.
A função retorna um dicionário com o status da operação (success ou failed) e o sid da mensagem ou uma mensagem de erro.
Função main:

A função principal prepara uma lista de destinatários e mensagens.
Para cada destinatário, a função send_whatsapp_message é chamada, e o resultado é exibido no console.
Execução:

O código dentro de if __name__ == "__main__": garante que a função main() seja chamada apenas quando o arquivo é executado diretamente, e não quando importado como módulo.
