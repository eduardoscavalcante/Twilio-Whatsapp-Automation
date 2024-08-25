import os
from twilio.rest import Client
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração das credenciais do Twilio
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Inicializa o cliente do Twilio
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(to, message):
    """
    Envia uma mensagem via WhatsApp usando a API do Twilio.

    Args:
        to (str): Número de telefone do destinatário no formato internacional (ex: +5511999999999).
        message (str): Texto da mensagem a ser enviada.

    Returns:
        dict: Informações sobre a mensagem enviada.
    """
    try:
        message = client.messages.create(
            body=message,
            from_=f'whatsapp:{TWILIO_PHONE_NUMBER}',
            to=f'whatsapp:{to}'
        )
        print(f"Mensagem enviada com sucesso para {to}")
        return {'status': 'success', 'sid': message.sid}
    except Exception as e:
        print(f"Falha ao enviar mensagem para {to}: {e}")
        return {'status': 'failed', 'error': str(e)}

def main():
    """
    Função principal que orquestra o envio das mensagens.

    Args:
        None

    Returns:
        None
    """
    # Exemplo de lista de destinatários e mensagens
    recipients = [
        {"phone": "+5511999999999", "message": "Olá! Esta é uma mensagem automatizada."},
        {"phone": "+5511888888888", "message": "Este é outro exemplo de mensagem via WhatsApp."}
    ]

    # Loop para enviar as mensagens
    for recipient in recipients:
        response = send_whatsapp_message(recipient['phone'], recipient['message'])
        if response['status'] == 'success':
            print(f"Mensagem para {recipient['phone']} enviada com SID: {response['sid']}")
        else:
            print(f"Erro ao enviar mensagem para {recipient['phone']}: {response['error']}")

if __name__ == "__main__":
    main()
