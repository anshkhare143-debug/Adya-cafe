from flask import Flask...
app = Flask(__name__)
@app.route('/static/qr.jpg')
def qr_file():
    import os
    from flask import send_file
    if os.path.exists('static/qr.jpg'):
        return send_file('static/qr.jpg')
    return send_file('IMG-20261022-WA0015.jpg')

app.secret_key = ...
MENU = [
    {"id":1,"name":"Tomato pizza","price":79,"cat":"PIZZA"},
    {"id":2,"name":"Onion pizza","price":89,"cat":"PIZZA"},
    {"id":3,"name":"Sweet corn pizza","price":89,"cat":"PIZZA"},
    {"id":4,"name":"Margherita pizza","price":99,"cat":"PIZZA"},
    {"id":5,"name":"Paneer pizza","price":149,"cat":"PIZZA"},
    {"id":6,"name":"Veg hotel pizza","price":149,"cat":"PIZZA"},
    {"id":7,"name":"Cheese pizza","price":179,"cat":"PIZZA"},
    {"id":8,"name":"Burger","price":40,"cat":"BURGER"},
    {"id":9,"name":"Cheese burger","price":60,"cat":"BURGER"},
    {"id":10,"name":"Paneer burger","price":70,"cat":"BURGER"},
    {"id":11,"name":"Red sauce pasta","price":100,"cat":"PASTA"},
    {"id":12,"name":"White sauce pasta","price":120,"cat":"PASTA"},
    {"id":13,"name":"Pink sauce pasta","price":130,"cat":"PASTA"},
    {"id":14,"name":"Veg sandwich","price":50,"cat":"SANDWICH"},
    {"id":15,"name":"Veg loted sandwich","price":70,"cat":"SANDWICH"},
    {"id":16,"name":"Paneer sandwich","price":80,"cat":"SANDWICH"},
    {"id":17,"name":"Veg hakka noodles","price":50,"cat":"NOODLES"},
    {"id":18,"name":"Paneer noodles","price":70,"cat":"NOODLES"},
    {"id":19,"name":"Masala maggi","price":40,"cat":"MAGGI"},
    {"id":20,"name":"Sazwean maggi","price":50,"cat":"MAGGI"},
    {"id":21,"name":"Veg loted maggi","price":60,"cat":"MAGGI"},
    {"id":22,"name":"Paneer maggi","price":70,"cat":"MAGGI"},
    {"id":23,"name":"Cheese maggi","price":80,"cat":"MAGGI"},
    {"id":24,"name":"French fries","price":50,"cat":"FRIES"},
    {"id":25,"name":"Peri peri french fries","price":60,"cat":"FRIES"},
    {"id":26,"name":"Cheese french fries","price":100,"cat":"FRIES"},
    {"id":27,"name":"Bread pagoda","price":15,"cat":"FRIES"},
    {"id":28,"name":"Fried rice","price":60,"cat":"FRIES"},
    {"id":29,"name":"Veg biryani","price":60,"cat":"FRIES"},
    {"id":30,"name":"Chocolate shake","price":80,"cat":"SHAKES"},
    {"id":31,"name":"Kitkat shake","price":90,"cat":"SHAKES"},
    {"id":32,"name":"Oreo shake","price":100,"cat":"SHAKES"},
    {"id":33,"name":"Hot coffee","price":60,"cat":"COFFEE"},
    {"id":34,"name":"Cold coffee","price":90,"cat":"COFFEE"},
    {"id":35,"name":"Cold coffee with ice-cream","price":110,"cat":"COFFEE"},
    {"id":36,"name":"Virgin mojito","price":50,"cat":"MOCKTAIL"},
    {"id":37,"name":"Watermelon mojito","price":60,"cat":"MOCKTAIL"},
    {"id":38,"name":"Blue lagoon mojito","price":70,"cat":"MOCKTAIL"},
    {"id":39,"name":"Honey donut","price":49,"cat":"DONUT"},
    {"id":40,"name":"Chocolate donut","price":69,"cat":"DONUT"},
    {"id":41,"name":"Vanilla cupcake","price":69,"cat":"CUPCAKE"},
    {"id":42,"name":"Blueberry cupcake","price":69,"cat":"CUPCAKE"},
    {"id":43,"name":"Pineapple cupcake","price":69,"cat":"CUPCAKE"},
    {"id":44,"name":"Chocolate cupcake","price":79,"cat":"CUPCAKE"},
    {"id":45,"name":"Choco chip cupcake","price":79,"cat":"CUPCAKE"},
    {"id":46,"name":"Honey butter waffle","price":59,"cat":"WAFFLE"},
    {"id":47,"name":"Dark chocolate waffle","price":99,"cat":"WAFFLE"},
    {"id":48,"name":"White chocolate waffle","price":99,"cat":"WAFFLE"},
    {"id":49,"name":"Dark chocolate fantasy","price":119,"cat":"WAFFLE"},
    {"id":50,"name":"Dark chocolate","price":119,"cat":"WAFFLE"},
    {"id":51,"name":"Ice-cream waffle","price":129,"cat":"WAFFLE"},
    {"id":52,"name":"Mixnut waffle","price":149,"cat":"WAFFLE"},
    {"id":53,"name":"Veg momos","price":50,"cat":"MOMOS"},
    {"id":54,"name":"Paneer momos","price":70,"cat":"MOMOS"},
    {"id":55,"name":"Vegetable soup","price":30,"cat":"SOUP"},
    {"id":56,"name":"Kulhad tea","price":15,"cat":"TEA"},
    {"id":57,"name":"Lemon tea","price":25,"cat":"TEA"},
    {"id":58,"name":"Green tea","price":35,"cat":"TEA"},
]

UPI_ID = "BHARATPE2M0M0J3M9G67879@unitype"
OWNER = "ACHINTYA KUMAR KHARE"

@app.route('/')
def home():
    cart=session.get('cart',{}); tot=sum(next((x['price'] for x in MENU if x['id']==int(k)),0)*v for k,v in cart.items()); cnt=sum(cart.values())
    return render_template_string("""
<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Adya Cafe - Takeaway</title>
<style>
body{font-family:system-ui;margin:0;background:#fff8f0}
.h{background:#ff6b35;color:white;padding:16px;text-align:center;font-size:22px;font-weight:bold}
.s{background:#111;color:#ffcc00;padding:8px;text-align:center;font-size:12px}
.cat{background:#222;color:#ffcc00;padding:6px 12px;margin:15px 10px 5px 10px;border-radius:20px;font-weight:bold;font-size:13px;display:inline-block}
.c{background:white;margin:8px 10px;border-radius:12px;padding:12px;display:flex;justify-content:space-between;align-items:center;box-shadow:0 2px 6px rgba(0,0,0,.08)}
.btn{background:#ff6b35;color:white;border:none;padding:8px 16px;border-radius:20px;font-weight:bold}
.cart{position:fixed;bottom:0;left:0;right:0;background:#111;color:white;padding:12px 16px;display:flex;justify-content:space-between;align-items:center;z-index:99}
</style></head><body>
<div class="h">ADYA CAFE - Lucknow</div>
<div class="s">🥡 TAKEAWAY ONLY • 45 Min Me Ready • Payment First</div>
{% for i in menu %}
<div class="c"><div><b>{{i.name}}</b> ({{i.cat}})<br>₹{{i.price}}</div><div><a href="/add/{{i.id}}"><button class="btn">Add +</button></a></div></div>
{% endfor %}
<div style="height:80px"></div>
<div class="cart"><div>🛒 {{cnt}} items | ₹{{tot}}</div>{% if tot>0 %}<a href="/checkout"><button class="btn" style="background:#25D366">Pay ₹{{tot}} & Takeaway</button></a>{% endif %}</div>
</body></html>
""", menu=MENU, tot=tot, cnt=cnt)

@app.route('/add/<int:id>')
def add(id):
    cart=session.get('cart',{}); cart[str(id)]=cart.get(str(id),0)+1; session['cart']=cart; return redirect('/')

@app.route('/checkout')
def checkout():
    cart=session.get('cart',{}); tot=sum(next((x['price'] for x in MENU if x['id']==int(k)),0)*v for k,v in cart.items()); cnt=sum(cart.values())
    if tot==0: return redirect('/')
    return render_template_string(f"""
<html><head><meta name='viewport' content='width=device-width,initial-scale=1'><style>body{{font-family:system-ui;background:#fff8f0;padding:16px}}.b{{background:white;border-radius:16px;padding:20px;text-align:center}}.btn{{width:100%;padding:14px;border:none;border-radius:12px;font-weight:bold;margin-top:10px}}.qr{{width:280px}}.btn-pay{{background:#111;color:white}}.btn-upi{{background:#25D366;color:white}}input{{width:100%;padding:12px;margin:6px 0;border-radius:8px;border:1px solid #ccc;box-sizing:border-box}}</style></head><body>
<div class='b'><h2>🥡 Takeaway - 45 Min</h2><p>Order: <b>₹{tot}</b> ({cnt} items)<br><b style='color:green'>⏱️ 45 Min Me Ready</b></p>
<img src='/static/qr.jpg' class='qr'><p><b>{OWNER}</b><br><code>{UPI_ID}</code></p>
<a href='upi://pay?pa={UPI_ID}&pn={OWNER}&am={tot}&cu=INR'><button class='btn btn-upi'>📲 UPI Se ₹{tot} Pay Karo</button></a>
<form method='POST' action='/confirm' style='text-align:left;margin-top:15px'>
<input name='name' placeholder='Naam *' required><input name='phone' placeholder='Mobile * (Call isi pe jayegi)' required>
<input name='utr' placeholder='UTR / Transaction ID * Compulsory' required style='border:2px solid #ff6b35'>
<div style='background:#fff3cd;padding:10px;border-radius:8px;margin:10px 0;font-size:13px'>⏱️ 45 Min Fixed<br>Ready hote hi call aayegi<br>📍 Adya Cafe - Takeaway Only</div>
<label style='font-size:13px'><input type='checkbox' required> Maine payment kiya hai, 45 min me khud lene aaunga</label>
<button class='btn btn-pay'>✅ Payment Done - Order Confirm</button></form></div></body></html>
""")

@app.route('/confirm', methods=['POST'])
def confirm():
    cart=session.get('cart',{}); tot=sum(next((x['price'] for x in MENU if x['id']==int(k)),0)*v for k,v in cart.items())
    name=request.form.get('name'); phone=request.form.get('phone'); utr=request.form.get('utr')
    print(f"NEW TAKEAWAY 45MIN ORDER: {name} {phone} Rs{tot} UTR:{utr}")
    session['cart']={}
    return f"<html><body style='font-family:system-ui;background:#e8f5e9;text-align:center;padding:30px'><div style='background:white;padding:30px;border-radius:16px'><h1>✅</h1><h2>Order Confirmed!</h2><p><b>Token: ADYA{phone[-4:]}</b></p><p>{name}<br>Rs {tot} Paid<br>UTR: {utr}<br>Phone: {phone}</p><div style='background:#d4edda;padding:15px;border-radius:10px;margin:15px 0'>⏱️ 45 Min me ready!<br>Call aayegi {phone} pe<br>📍 Adya Cafe</div><a href='/'><button style='padding:12px 20px;background:#ff6b35;color:white;border:none;border-radius:8px'>New Order</button></a></div></body></html>"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=10000)
