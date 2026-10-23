from flask import Flask, request, jsonify, redirect
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'adya-cafe-58-final'

MENU = [
    {"id":1,"name":"Tomato pizza","cat":"PIZZA","price":79,"img":"🍕","available":True},
    {"id":2,"name":"Onion pizza","cat":"PIZZA","price":89,"img":"🧅","available":True},
    {"id":3,"name":"Sweet corn pizza","cat":"PIZZA","price":89,"img":"🌽","available":True},
    {"id":4,"name":"Margherita pizza","cat":"PIZZA","price":99,"img":"🍕","available":True},
    {"id":5,"name":"Paneer pizza","cat":"PIZZA","price":149,"img":"🧀","available":True},
    {"id":6,"name":"Veg hotel pizza","cat":"PIZZA","price":149,"img":"🍕","available":True},
    {"id":7,"name":"Cheese pizza","cat":"PIZZA","price":179,"img":"🧀","available":True},
    {"id":8,"name":"Burger","cat":"BURGER","price":40,"img":"🍔","available":True},
    {"id":9,"name":"Cheese burger","cat":"BURGER","price":60,"img":"🍔","available":True},
    {"id":10,"name":"Paneer burger","cat":"BURGER","price":70,"img":"🍔","available":True},
    {"id":11,"name":"Red sauce pasta","cat":"PASTA","price":100,"img":"🍝","available":True},
    {"id":12,"name":"White sauce pasta","cat":"PASTA","price":120,"img":"🍝","available":True},
    {"id":13,"name":"Pink sauce pasta","cat":"PASTA","price":130,"img":"🍝","available":True},
    {"id":14,"name":"Veg sandwich","cat":"SANDWICH","price":50,"img":"🥪","available":True},
    {"id":15,"name":"Veg loted sandwich","cat":"SANDWICH","price":70,"img":"🥪","available":True},
    {"id":16,"name":"Paneer sandwich","cat":"SANDWICH","price":80,"img":"🥪","available":True},
    {"id":17,"name":"Veg hakka noodles","cat":"NOODLES","price":50,"img":"🍜","available":True},
    {"id":18,"name":"Paneer noodles","cat":"NOODLES","price":70,"img":"🍜","available":True},
    {"id":19,"name":"Masala maggi","cat":"MAGGI","price":40,"img":"🍜","available":True},
    {"id":20,"name":"Sazwean maggi","cat":"MAGGI","price":50,"img":"🍜","available":True},
    {"id":21,"name":"Veg loted maggi","cat":"MAGGI","price":60,"img":"🍜","available":True},
    {"id":22,"name":"Paneer maggi","cat":"MAGGI","price":70,"img":"🍜","available":True},
    {"id":23,"name":"Cheese maggi","cat":"MAGGI","price":80,"img":"🧀","available":True},
    {"id":24,"name":"French fries","cat":"FRIES & MORE","price":50,"img":"🍟","available":True},
    {"id":25,"name":"Peri peri french fries","cat":"FRIES & MORE","price":60,"img":"🍟","available":True},
    {"id":26,"name":"Cheese french fries","cat":"FRIES & MORE","price":100,"img":"🍟","available":True},
    {"id":27,"name":"Bread pagoda","cat":"FRIES & MORE","price":15,"img":"🍞","available":True},
    {"id":28,"name":"Fried rice","cat":"FRIES & MORE","price":60,"img":"🍚","available":True},
    {"id":29,"name":"Veg biryani","cat":"FRIES & MORE","price":60,"img":"🍛","available":True},
    {"id":30,"name":"Chocolate shake","cat":"SHAKES","price":80,"img":"🥤","available":True},
    {"id":31,"name":"Kitkat shake","cat":"SHAKES","price":90,"img":"🍫","available":True},
    {"id":32,"name":"Oreo shake","cat":"SHAKES","price":100,"img":"🥤","available":True},
    {"id":33,"name":"Hot coffee","cat":"COFFEE","price":60,"img":"☕","available":True},
    {"id":34,"name":"Cold coffee","cat":"COFFEE","price":90,"img":"🧋","available":True},
    {"id":35,"name":"Cold coffee with ice-cream","cat":"COFFEE","price":110,"img":"🍦","available":True},
    {"id":36,"name":"Virgin mojito","cat":"MOCKTAIL","price":50,"img":"🍹","available":True},
    {"id":37,"name":"Watermelon mojito","cat":"MOCKTAIL","price":60,"img":"🍉","available":True},
    {"id":38,"name":"Blue lagoon mojito","cat":"MOCKTAIL","price":70,"img":"💙","available":True},
    {"id":39,"name":"Honey donut","cat":"DONUT","price":49,"img":"🍩","available":True},
    {"id":40,"name":"Chocolate donut","cat":"DONUT","price":69,"img":"🍩","available":True},
    {"id":41,"name":"Vanilla cupcake","cat":"CUPCAKE","price":69,"img":"🧁","available":True},
    {"id":42,"name":"Blueberry cupcake","cat":"CUPCAKE","price":69,"img":"🧁","available":True},
    {"id":43,"name":"Pineapple cupcake","cat":"CUPCAKE","price":69,"img":"🍍","available":True},
    {"id":44,"name":"Chocolate cupcake","cat":"CUPCAKE","price":79,"img":"🧁","available":True},
    {"id":45,"name":"Choco chip cupcake","cat":"CUPCAKE","price":79,"img":"🧁","available":True},
    {"id":46,"name":"Honey butter waffle","cat":"WAFFLE","price":59,"img":"🧇","available":True},
    {"id":47,"name":"Dark chocolate waffle","cat":"WAFFLE","price":99,"img":"🧇","available":True},
    {"id":48,"name":"White chocolate waffle","cat":"WAFFLE","price":99,"img":"🧇","available":True},
    {"id":49,"name":"Dark chocolate fantasy","cat":"WAFFLE","price":119,"img":"🍫","available":True},
    {"id":50,"name":"Dark chocolate","cat":"WAFFLE","price":119,"img":"🍫","available":True},
    {"id":51,"name":"Ice-cream waffle","cat":"WAFFLE","price":129,"img":"🍦","available":True},
    {"id":52,"name":"Mixnut waffle","cat":"WAFFLE","price":149,"img":"🥜","available":True},
    {"id":53,"name":"Veg momos","cat":"MOMOS","price":50,"img":"🥟","available":True},
    {"id":54,"name":"Paneer momos","cat":"MOMOS","price":70,"img":"🥟","available":True},
    {"id":55,"name":"Vegetable soup","cat":"SOUP","price":30,"img":"🍲","available":True},
    {"id":56,"name":"Kulhad tea","cat":"TEA","price":15,"img":"☕","available":True},
    {"id":57,"name":"Lemon tea","cat":"TEA","price":25,"img":"🍋","available":True},
    {"id":58,"name":"Green tea","cat":"TEA","price":35,"img":"🍵","available":True},
]

ORDERS = []

@app.route('/static/qr.jpg')
def qr_file():
    # Tere UPI ID se QR generate - file ki zaroorat nahi
    upi = "BHARATPE2M0M0J3M9G67879@unitype"
    name = "ACHINTYA KUMAR KHARE"
    return redirect(f"https://api.qrserver.com/v1/create-qr-code/?size=500x500&data=upi://pay?pa={upi}&pn={name}&cu=INR")

@app.route('/')
def index():
    return INDEX_HTML

@app.route('/api/menu')
def api_menu():
    return jsonify(MENU)

@app.route('/api/order', methods=['POST'])
def api_order():
    data = request.get_json()
    order_id = len(ORDERS) + 1
    final_total = data.get('total', 0)
    coupon = data.get('coupon','')
    if coupon == 'ADYASUNDAY' and datetime.now().weekday() == 6:
        final_total = int(final_total * 0.8)
    ORDERS.append({"id": order_id, "data": data, "time": str(datetime.now()), "final": final_total})
    return jsonify({"order_id": order_id, "final_total": final_total})

INDEX_HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ADYA CAFE - Lucknow</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
<style>body{font-family:'Poppins',sans-serif}</style>
</head>
<body class="bg-[#FFF8F0] min-h-screen">
<div class="bg-[#FF6B35] text-white p-4 sticky top-0 z-40 shadow">
<div class="max-w-6xl mx-auto flex justify-between items-center">
<div><h1 class="text-xl font-bold">ADYA CAFE - Lucknow</h1><p class="text-xs opacity-90">TAKEAWAY ONLY • 45 Min Me Ready • Payment First</p></div>
<button onclick="toggleCart()" class="bg-white text-[#FF6B35] px-4 py-2 rounded-full font-bold text-sm">🛒 <span id="cart-count">0</span> | ₹<span id="cart-total-mini">0</span></button>
</div></div>
<div class="max-w-6xl mx-auto px-3 mt-3">
<div class="bg-gradient-to-r from-orange-500 to-red-500 rounded-xl p-3 text-white flex justify-between items-center"><div><p class="font-bold">Sunday Special 🎉 ADYASUNDAY - 20% OFF</p><p class="text-xs">Sirf Sunday ko valid</p></div><div class="text-3xl">🍕</div></div>
<input id="search" oninput="renderMenu()" placeholder="Search pizza, burger, maggi, waffle, tea..." class="w-full p-3 rounded-xl border mt-3">
<div id="categories" class="flex gap-2 overflow-x-auto mt-3 pb-2"></div>
</div>
<div class="max-w-6xl mx-auto px-3 mt-3 pb-24"><div id="menu-grid" class="grid grid-cols-1 gap-3"></div></div>
<div id="cart-drawer" class="fixed inset-0 bg-black/50 hidden z-50">
<div class="absolute bottom-0 w-full max-w-md right-0 left-0 mx-auto bg-white rounded-t-3xl max-h-[90vh] flex flex-col">
<div class="p-4 border-b flex justify-between items-center"><h2 class="font-bold text-lg">🥡 Takeaway - 45 Min</h2><button onclick="toggleCart()" class="text-2xl">×</button></div>
<div class="p-4 flex-1 overflow-y-auto">
<p class="text-center">Order: ₹<span id="cart-order-total">0</span> (<span id="cart-items-count">0</span> items)</p>
<p class="text-center text-green-600 font-bold">⏱ 45 Min Me Ready</p>
<div class="bg-white border-2 rounded-2xl p-3 mt-4 flex flex-col items-center">
<img id="qr-img" src="/static/qr.jpg" class="w-64 h-64 object-contain border rounded-xl">
<p class="font-bold mt-3">ACHINTYA KUMAR KHARE</p>
<p class="text-xs font-mono break-all text-center">BHARATPE2M0M0J3M9G67879@unitype</p>
</div>
<div id="cart-items" class="space-y-2 mt-4"></div>
<div class="flex gap-2 mt-4"><input id="coupon" placeholder="Coupon ADYASUNDAY" class="flex-1 p-3 rounded-xl border text-sm"><button onclick="applyCoupon()" class="bg-black text-white px-5 rounded-xl text-sm">Apply</button></div>
<p id="coupon-msg" class="text-xs mt-1"></p>
<div class="space-y-1 text-sm mt-3 bg-gray-50 p-3 rounded-xl"><div class="flex justify-between"><span>Subtotal</span><span id="subtotal">₹0</span></div><div class="flex justify-between text-green-600 hidden" id="discount-row"><span>Discount</span><span id="discount">-₹0</span></div><div class="flex justify-between font-bold text-lg"><span>Total</span><span id="final-total">₹0</span></div></div>
<input id="cust-name" placeholder="Naam *" class="w-full p-3 rounded-xl border mt-3">
<input id="cust-phone" placeholder="Mobile * (Call isi pe jayegi)" class="w-full p-3 rounded-xl border mt-2">
<input id="cust-utr" placeholder="UTR / Transaction ID * Compulsory" class="w-full p-3 rounded-xl border-2 border-orange-500 mt-2">
<button onclick="placeOrder()" class="w-full bg-[#22c55e] text-white py-3 rounded-xl font-bold text-lg mt-3">📱 UPI Se ₹<span id="btn-total">0</span> Pay Karo</button>
</div></div></div>
<div class="fixed bottom-0 left-0 right-0 bg-black text-white p-3 flex justify-between items-center z-30"><span>🛒 <span id="bottom-count">0</span> items | ₹<span id="bottom-total">0</span></span><button onclick="toggleCart()" class="bg-[#22c55e] px-5 py-2 rounded-full font-bold text-sm">Pay ₹<span id="bottom-pay">0</span> & Takeaway</button></div>
<script>
let MENU=[],CART={},CATEGORY='ALL',COUPON='',DISCOUNT=0,_subtotal=0;
async function loadMenu(){const r=await fetch('/api/menu');MENU=await r.json();buildCategories();renderMenu();}
function buildCategories(){const cats=['ALL',...new Set(MENU.map(m=>m.cat))];document.getElementById('categories').innerHTML=cats.map(c=>`<button onclick="setCat('${c}')" class="px-4 py-2 rounded-full text-sm font-semibold whitespace-nowrap ${CATEGORY===c?'bg-[#FF6B35] text-white':'bg-white border'}">${c}</button>`).join('');}
function setCat(c){CATEGORY=c;buildCategories();renderMenu();}
function renderMenu(){const q=document.getElementById('search').value.toLowerCase();let f=MENU.filter(m=>{const mc=CATEGORY==='ALL'||m.cat===CATEGORY;const mq=m.name.toLowerCase().includes(q);return mc&&mq;});document.getElementById('menu-grid').innerHTML=f.map(item=>`<div class="bg-white rounded-2xl p-4 shadow-sm flex justify-between items-center"><div><h3 class="font-bold text-base">${item.img} ${item.name} <span class="text-xs font-normal text-gray-500">(${item.cat})</span></h3><p class="font-bold mt-1">₹${item.price}</p></div><div>${CART[item.id]?`<div class="flex items-center gap-2 bg-[#FFF0E8] rounded-full p-1"><button onclick="updateQty(${item.id},-1)" class="w-8 h-8 rounded-full bg-white shadow font-bold">-</button><span class="w-6 text-center font-bold text-sm">${CART[item.id]}</span><button onclick="updateQty(${item.id},1)" class="w-8 h-8 rounded-full bg-[#FF6B35] text-white font-bold">+</button></div>`:`<button onclick="updateQty(${item.id},1)" class="bg-[#FF6B35] text-white px-6 py-2 rounded-full font-bold text-sm">Add +</button>`}</div></div>`).join('');}
function updateQty(id,d){CART[id]=(CART[id]||0)+d;if(CART[id]<=0)delete CART[id];renderMenu();renderCart();}
function renderCart(){const ids=Object.keys(CART);let sub=0,html='',cnt=0;ids.forEach(id=>{const item=MENU.find(m=>m.id==id);const qty=CART[id];sub+=item.price*qty;cnt+=qty;html+=`<div class="flex justify-between items-center bg-gray-50 p-3 rounded-xl"><div><p class="font-semibold text-sm">${item.name}</p><p class="text-xs">₹${item.price} x ${qty}</p></div><div class="flex items-center gap-2"><button onclick="updateQty(${id},-1)" class="w-7 h-7 bg-white rounded-full shadow">-</button><span class="text-sm font-bold">${qty}</span><button onclick="updateQty(${id},1)" class="w-7 h-7 bg-[#FF6B35] text-white rounded-full">+</button></div></div>`;});if(!ids.length)html='<p class="text-center text-gray-400 mt-6">Cart empty hai 🍕</p>';document.getElementById('cart-items').innerHTML=html;_subtotal=sub;const total=sub-DISCOUNT;document.getElementById('subtotal').innerText='₹'+sub;document.getElementById('final-total').innerText='₹'+total;document.getElementById('btn-total').innerText=total;document.getElementById('cart-order-total').innerText=total;document.getElementById('cart-items-count').innerText=cnt;document.getElementById('cart-count').innerText=cnt;document.getElementById('cart-total-mini').innerText=total;document.getElementById('bottom-count').innerText=cnt;document.getElementById('bottom-total').innerText=total;document.getElementById('bottom-pay').innerText=total;document.getElementById('discount').innerText='-₹'+DISCOUNT;document.getElementById('discount-row').classList.toggle('hidden',DISCOUNT===0);document.getElementById('qr-img').src=`/static/qr.jpg?amount=${total}&t=${Date.now()}`;}
function toggleCart(){document.getElementById('cart-drawer').classList.toggle('hidden');}
function applyCoupon(){const code=document.getElementById('coupon').value.trim().toUpperCase();if(code==='ADYASUNDAY'){if(new Date().getDay()!==0){document.getElementById('coupon-msg').innerHTML='<span class="text-red-500">Sirf Sunday ko valid hai!</span>';return;}DISCOUNT=Math.floor(_subtotal*0.2);COUPON=code;document.getElementById('coupon-msg').innerHTML='<span class="text-green-600">20% OFF lag gaya!</span>';}else if(code===''){DISCOUNT=0;COUPON='';document.getElementById('coupon-msg').innerHTML='';}else{document.getElementById('coupon-msg').innerHTML='<span class="text-red-500">Invalid coupon</span>';DISCOUNT=0;}renderCart();}
async function placeOrder(){const name=document.getElementById('cust-name').value.trim();const phone=document.getElementById('cust-phone').value.trim();const utr=document.getElementById('cust-utr').value.trim();if(!Object.keys(CART).length)return alert('Cart khali hai!');if(!name||!phone)return alert('Naam aur Mobile bharo!');if(!utr)return alert('UTR / Transaction ID dalna compulsory hai!');const items=Object.keys(CART).map(id=>{const m=MENU.find(x=>x.id==id);return{id:m.id,name:m.name,price:m.price,qty:CART[id]};});const body={items,total:_subtotal,coupon:COUPON,name,phone,utr};const res=await fetch('/api/order',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});const data=await res.json();alert('Order Placed! ID: #'+data.order_id+' Final: ₹'+data.final_total);CART={};COUPON='';DISCOUNT=0;document.getElementById('coupon').value='';renderMenu();renderCart();toggleCart();}
loadMenu();
</script></body></html>
"""

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
