from flask import Flask, render_template, redirect
import urllib.parse

app = Flask(__name__)

# --- CONFIGURACIÓN DE DATOS ---
PAYPAL_EMAIL = "edgarj300901@gmail.com"
WHATSAPP_PHONE = "18296396788"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pagar-paypal')
def pagar_paypal():
    paypal_url = f"https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business={urllib.parse.quote(PAYPAL_EMAIL)}&currency_code=USD&item_name=Aporte+Xbox+Series+X+-+Cumpleanos+Edgar"
    return redirect(paypal_url)

@app.route('/whatsapp')
def enviar_whatsapp():
    mensaje = "¡Hola Edgar! Te escribo para enviarte el comprobante de mi aporte para tu Xbox Series X y que estés listo para el GTA VI. 🎮🔥"
    mensaje_codificado = urllib.parse.quote(mensaje)
    whatsapp_url = f"https://api.whatsapp.com/send?phone={WHATSAPP_PHONE}&text={mensaje_codificado}"
    return redirect(whatsapp_url)

if __name__ == '__main__':
    app.run(debug=True, port=5000)