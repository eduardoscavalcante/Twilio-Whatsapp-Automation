from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(to, message):
    to_whatsapp_number = f'whatsapp:{to}'

    client.messages.create(
        body=message,
        from_=TWILIO_WHATSAPP_NUMBER,
        to=to_whatsapp_number
    )

if __name__ == "__main__":
    send_whatsapp_message('+5511999999999', 'Olá, isso é um teste!')
