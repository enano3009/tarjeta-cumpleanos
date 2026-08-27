import os
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

# Configuración de PayPal y WhatsApp
PAYPAL_ME_URL = "https://paypal.me/edgarjose3"  # Cambia esto si tienes otra URL de PayPal
WHATSAPP_NUMBER = "18296335160"  # Número de WhatsApp configurado para notificaciones

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagar-paypal')
def pagar_paypal():
    # Redirige directamente al perfil o checkout de PayPal
    return redirect(PAYPAL_ME_URL)

@app.route('/whatsapp')
def whatsapp():
    # Mensaje predeterminado para el chat de WhatsApp
    mensaje = "¡Hola Edgar! Estuve viendo tu página de cumpleaños y quiero apoyarte con tu meta del Xbox Series X 🎮🎂."
    whatsapp_url = f"https://api.whatsapp.com/send?phone={WHATSAPP_NUMBER}&text={mensaje.replace(' ', '%20')}"
    return redirect(whatsapp_url)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
