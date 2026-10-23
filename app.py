from flask import Flask, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__)

MENU = [
  {"id":1,"name":"Tomato pizza","price":79,"cat":"PIZZA","available":True,"img":"🍕"},
  {"id":2,"name":"Onion pizza","price":89,"cat":"PIZZA","available":True,"img":"🍕"},
  {"id":3,"name":"Sweet corn pizza","price":89,"cat":"PIZZA","available":True,"img":"🍕"},
  {"id":4,"name":"Margherita pizza","price":99,"cat":"PIZZA","available":True,"img":"🍕"},
  {"id":5,"name":"Paneer pizza","price":149,"cat":"PIZZA","available":True,"img":"🍕"},
  {"id":6,"name":"Veg hotel pizza","price":149,"cat":"PIZZA","available":True,"img":"🍕"},
  {"id":7,"name":"Cheese pizza","price":179,"cat":"PIZZA","available":True,"img":"🍕"},
  {"id":8,"name":"Burger","price":40,"cat":"BURGER","available":True,"img":"🍔"},
  {"id":9,"name":"Cheese burger","price":60,"cat":"BURGER","available":True,"img":"🍔"},
  {"id":10,"name":"Paneer burger","price":70,"cat":"BURGER","available":True,"img":"🍔"},
  {"id":11,"name":"Red sauce pasta","price":100,"cat":"PASTA","available":True,"img":"🍝"},
  {"id":12,"name":"White sauce pasta","price":120,"cat":"PASTA","available":True,"img":"🍝"},
  {"id":13,"name":"Pink sauce pasta","price":130,"cat":"PASTA","available":True,"img":"🍝"},
  {"id":14,"name":"Veg sandwich","price":50,"cat":"SANDWICH","available":True,"img":"🥪"},
  {"id":15,"name":"Veg loaded sandwich","price":70,"cat":"SANDWICH","available":True,"img":"🥪"},
  {"id":16,"name":"Paneer sandwich","price":80,"cat":"SANDWICH","available":True,"img":"🥪"},
  {"id":17,"name":"Veg hakka noodles","price":50,"cat":"NOODLES","available":True,"img":"🍜"},
  {"id":18,"name":"Paneer noodles","price":70,"cat":"NOODLES","available":True,"img":"🍜"},
  {"id":19,"name":"Masala maggi","price":40,"cat":"MAGGI","available":True,"img":"🍜"},
  {"id":20,"name":"Sazwean maggi","price":50,"cat":"MAGGI","available":True,"img":"🍜"},
  {"id":21,"name":"Veg loaded maggi","price":60,"cat":"MAGGI","available":True,"img":"🍜"},
  {"id":22,"name":"Paneer maggi","price":70,"cat":"MAGGI","available":True,"img":"🍜"},
  {"id":23,"name":"Cheese maggi","price":80,"cat":"MAGGI","available":True,"img":"🍜"},
  {"id":24,"name":"French fries","price":50,"cat":"FRIES","available":True,"img":"🍟"},
  {"id":25,"name":"Peri peri fries","price":60,"cat":"FRIES","available":True,"img":"🍟"},
  {"id":26,"name":"Cheese fries","price":100,"cat":"FRIES","available":True,"img":"🍟"},
  {"id":27,"name":"Bread pakoda","price":15,"cat":"MORE","available":True,"img":"🍞"},
  {"id":28,"name":"Fried rice","price":60,"cat":"MORE","available":True,"img":"🍚"},
  {"id":29,"name":"Veg biryani","price":60,"cat":"MORE","available":True,"img":"🍚"},
  {"id":30,"name":"Chocolate shake","price":80,"cat":"SHAKES","available":True,"img":"🥤"},
  {"id":31,"name":"Kitkat shake","price":90,"cat":"SHAKES","available":True,"img":"🥤"},
  {"id":32,"name":"Oreo shake","price":100,"cat":"SHAKES","available":True,"img":"🥤"},
  {"id":33,"name":"Hot coffee","price":60,"cat":"COFFEE","available":True,"img":"☕"},
  {"id":34,"name":"Cold coffee","price":90,"cat":"COFFEE","available":True,"img":"☕"},
  {"id":35,"name":"Cold coffee ice-cream","price":110,"cat":"COFFEE","available":True,"img":"☕"},
  {"id":36,"name":"Virgin mojito","price":50,"cat":"MOCKTAIL","available":True,"img":"🍹"},
  {"id":37,"name":"Watermelon mojito","price":60,"cat":"MOCKTAIL","available":True,"img":"🍹"},
  {"id":38,"name":"Blue lagoon","price":70,"cat":"MOCKTAIL","available":True,"img":"🍹"},
  {"id":39,"name":"Honey donut","price":49,"cat":"DONUT","available":True,"img":"🍩"},
  {"id":40,"name":"Chocolate donut","price":69,"cat":"DONUT","available":True,"img":"🍩"},
  {"id":41,"name":"Vanilla cupcake","price":69,"cat":"CUPCAKE","available":True,"img":"🧁"},
  {"id":42,"name":"Blueberry cupcake","price":69,"cat":"CUPCAKE","available":True,"img":"🧁"},
  {"id":43,"name":"Pineapple cupcake","price":69,"cat":"CUPCAKE","available":True,"img":"🧁"},
  {"id":44,"name":"Chocolate cupcake","price":79,"cat":"CUPCAKE","available":True,"img":"🧁"},
  {"id":45,"name":"Choco chip cupcake","price":79,"cat":"CUPCAKE","available":True,"img":"🧁"},
  {"id":46,"name":"Honey butter waffle","price":59,"cat":"WAFFLE","available":True,"img":"🧇"},
  {"id":47,"name":"Dark chocolate waffle","price":99,"cat":"WAFFLE","available":True,"img":"🧇"},
  {"id":48,"name":"White chocolate waffle","price":99,"cat":"WAFFLE","available":True,"img":"🧇"},
  {"id":49,"name":"Dark chocolate fantasy","price":119,"cat":"WAFFLE","available":True,"img":"🧇"},
  {"id":50,"name":"Dark chocolate special","price":119,"cat":"WAFFLE","available":True,"img":"🧇"},
  {"id":51,"name":"Ice-cream waffle","price":129,"cat":"WAFFLE","available":True,"img":"🧇"},
  {"id":52,"name":"Mixnut waffle","price":149,"cat":"WAFFLE","available":True,"img":"🧇"},
  {"id":53,"name":"Veg momos","price":50,"cat":"MOMOS","available":True,"img":"🥟"},
  {"id":54,"name":"Paneer momos","price":70,"cat":"MOMOS","available":True,"img":"🥟"},
  {"id":55,"name":"Veg soup","price":30,"cat":"SOUP","available":True,"img":"🍲"},
  {"id":56,"name":"Kulhad tea","price":15,"cat":"TEA","available":True,"img":"🫖"},
  {"id":57,"name":"Lemon tea","price":25,"cat":"TEA","available":True,"img":"🫖"},
  {"id":58,"name":"Green tea","price":35,"cat":"TEA","available":True,"img":"🫖"}
]

ORDERS = []
ORDER_ID = 100

@app.route('/')
def home(): return render_template('index.html')

@app.route('/admin')
def admin(): return render_template('admin.html')

@app.route('/api/menu')
def api_menu(): return jsonify(MENU)

@app.route('/api/order', methods=['POST'])
def api_order():
    global ORDER_ID
    data = request.json
    total = data.get('total',0)
    coupon = data.get('coupon','').upper()
    discount = 0
    if coupon == 'ADYASUNDAY':
        if datetime.now().weekday() != 6:
            return jsonify({'error':'Sunday only'}),400
        discount = int(total*0.2)
    final = total - discount
    ORDER_ID+=1
    order = {'id':ORDER_ID,'items':data.get('items',[]),'total':total,'discount':discount,'final_total':final,'coupon':coupon,'name':data.get('name',''),'phone':data.get('phone',''),'time':datetime.now().strftime('%d/%m %I:%M %p'),'status':'New'}
    ORDERS.append(order)
    return jsonify({'order_id':ORDER_ID,'final_total':final})

@app.route('/api/orders')
def api_orders(): return jsonify(list(reversed(ORDERS)))

@app.route('/api/toggle/<int:item_id>', methods=['POST'])
def toggle(item_id):
    for i in MENU:
        if i['id']==item_id: i['available']=not i['available']
    return jsonify({'ok':True})

@app.route('/health')
def health(): return 'ok'

if __name__=='__main__': app.run(debug=True)
