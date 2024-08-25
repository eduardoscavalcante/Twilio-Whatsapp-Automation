# Twilio WhatsApp Automation

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/release/python-380/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Build Status](https://github.com/seuusuario/twilio-whatsapp-automation/workflows/CI/badge.svg)](https://github.com/seuusuario/twilio-whatsapp-automation/actions)

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
   python3 -m venv venv
   source venv/bin/activate

3. Instale as dependências:
   ```pip install -r requirements.txt

4. Configure as variáveis de ambiente:
   ```cp .env.example .env
Preencha o arquivo .env com suas credenciais do Twilio.

## Uso
Para enviar uma mensagem de teste:
```python src/main.py


