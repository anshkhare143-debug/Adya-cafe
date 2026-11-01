<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ADYA FOODS - Order Now</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:system-ui}
body{background:#f5f5f5}
.header{background:#ff3b30;color:#fff;padding:12px;text-align:center;font-weight:800;position:sticky;top:0;z-index:10}
.container{max-width:480px;margin:0 auto;background:#fff;min-height:100vh}
.item{display:flex;justify-content:space-between;padding:12px;border-bottom:1px solid #eee;align-items:center}
.item button{background:#ff3b30;color:#fff;border:0;padding:6px 14px;border-radius:20px;font-weight:700}
.cart{position:sticky;bottom:0;background:#fff;border-top:2px solid #000;padding:12px}
input,select,textarea{width:100%;padding:12px;margin:6px 0;border:1px solid #ccc;border-radius:8px;font-size:15px}
.btn-main{background:#000;color:#fff;width:100%;padding:14px;border:0;border-radius:10px;font-size:16px;font-weight:800;margin-top:10px}
.tag{padding:4px 10px;border-radius:20px;font-size:12px;font-weight:700}
.delivery-active{background:#000;color:#fff}
.takeaway-active{background:#eee}
.hidden{display:none}
#loader{position:fixed;inset:0;background:rgba(0,0,0,0.8);color:#fff;display:none;align-items:center;justify-content:center;flex-direction:column;z-index:100}
.admin-card{border:2px solid #000;margin:10px;padding:12px;border-radius:10px;background:#fff9f9}
</style>
</head>
<body>
<div id="loader"><h2>Payment check ho raha hai...</h2><p>UTR verify...</p><div style="margin-top:20px">⏳</div></div>

<div class="header" id="shopHeader">ADYA FOODS - <span id="shopStatus">OPEN</span> 🟢</div>

<div class="container" id="customerView">
<div style="padding:10px;display:flex;gap:10px">
<button id="btnDelivery" class="tag delivery-active" onclick="setType('delivery')">🛵 Delivery (1KM) + ₹30</button>
<button id="btnTakeaway" class="tag" onclick="setType('takeaway')">🏪 Takeaway FREE - 45 Min</button>
</div>
<div id="distanceMsg" style="padding:0 10px;color:red;font-size:13px;font-weight:700"></div>

<div style="padding:10px">
<input id="custName" placeholder="Name *">
<input id="custMobile" placeholder="Mobile No. * (10 digit)" type="tel">
<div id="addressBox">
<textarea id="custAddress" placeholder="Apna pura Address likho * (Delivery ke liye)"></textarea>
<button onclick="getLiveLocation()" style="background:#007aff;color:#fff;border:0;padding:10px;border-radius:8px;width:100%;font-weight:700">📍 Current Location Use Karo</button>
<div id="liveLocText" style="font-size:12px;color:green;margin-top:5px"></div>
</div>
<input id="couponInput" placeholder="Coupon Code (ADYA50)">
<button onclick="applyCoupon()" style="padding:8px 12px;margin:5px 0;background:#eee;border:1px dashed #000;border-radius:5px">Apply Coupon</button>
<div id="couponMsg" style="font-size:13px;font-weight:700;color:green"></div>

<input id="utrInput" placeholder="UTR No. * (Payment ke baad)">
<div style="text-align:center;padding:10px;border:1px solid #000;margin:10px 0;border-radius:10px">
<p style="font-weight:800">Pehle Payment Karo - QR Scan karo</p>
<img id="qrImg" src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=upi://pay?pa=adya@upi" style="width:180px;margin:10px">
<p style="font-size:12px">UPI ID: adya@upi</p>
<p style="font-size:11px;color:#666">QR auto change 3 tarik ko</p>
</div>
</div>

<div id="itemsList"></div>

<div class="cart">
<div style="display:flex;justify-content:space-between"><span>Subtotal</span><span id="subtotal">₹0</span></div>
<div style="display:flex;justify-content:space-between"><span>Delivery</span><span id="deliveryCharge">₹30</span></div>
<div style="display:flex;justify-content:space-between"><span>Discount (ADYA50)</span><span id="discount">-₹0</span></div>
<div style="display:flex;justify-content:space-between;font-weight:800;font-size:18px;border-top:1px solid #000;margin-top:5px;padding-top:5px"><span>Total</span><span id="total">₹0</span></div>
<button class="btn-main" onclick="placeOrder()">Pay & Order</button>
<p style="font-size:11px;text-align:center;margin-top:5px">Payment pehle, fir order jayega</p>
</div>
</div>

<div class="container hidden" id="adminView" style="padding:10px">
<h2>Admin Panel - ADYA FOODS</h2>
<button onclick="toggleShop()" id="toggleBtn" style="padding:10px;background:red;color:#fff;border:0;border-radius:5px;margin:10px 0">Shop OFF Karo</button>
<button onclick="changeQR()" style="padding:10px;background:#000;color:#fff;border:0;border-radius:5px">QR Change Karo</button>
<p style="font-size:12px;margin:5px 0">QR Last Change: <span id="qrDate">-</span></p>
<h3 style="margin-top:15px">Live Orders</h3>
<div id="adminOrders"></div>
<audio id="ringTone" src="https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg" preload="auto"></audio>
</div>

<script>
// CONFIG
const SHOP_LAT = 26.8756; // Krishna Nagar Lucknow
const SHOP_LNG = 80.9115;
let orderType = 'delivery';
let cart = {};
let couponDiscount = 0;
let shopOpen = localStorage.getItem('shopOpen') !== 'false';
let qrLastChange = localStorage.getItem('qrLastChange') || 'Never';
let userLatLng = '';

// 58 ITEMS
const ITEMS = [
{name:"Margherita Pizza",price:99},{name:"Cheese Pizza",price:129},{name:"Paneer Pizza",price:149},{name:"Veg Burger",price:49},{name:"Cheese Burger",price:69},{name:"Paneer Burger",price:79},{name:"Veg Sandwich",price:39},{name:"Grilled Sandwich",price:59},{name:"Paneer Sandwich",price:69},{name:"French Fries",price:49},{name:"Cheese Fries",price:69},{name:"Veg Momos 6pc",price:59},{name:"Paneer Momos 6pc",price:79},{name:"Fried Momos",price:89},{name:"Veg Roll",price:49},{name:"Paneer Roll",price:69},{name:"Chicken Roll",price:89},{name:"Pasta White",price:79},{name:"Pasta Red",price:79},{name:"Noodles Veg",price:59},{name:"Noodles Paneer",price:79},{name:"Fried Rice",price:69},{name:"Manchurian",price:79},{name:"Chilli Paneer",price:99},{name:"Veg Thali",price:99},{name:"Paneer Thali",price:129},{name:"Dal Chawal",price:69},{name:"Rajma Chawal",price:79},{name:"Chole Bhature 2pc",price:79},{name:"Samosa 2pc",price:30},{name:"Kachori 2pc",price:30},{name:"Pav Bhaji",price:69},{name:"Idli Sambhar 4pc",price:49},{name:"Dosa Masala",price:69},{name:"Uttapam",price:59},{name:"Poha",price:29},{name:"Upma",price:39},{name:"Aloo Paratha",price:39},{name:"Paneer Paratha",price:59},{name:"Cold Coffee",price:49},{name:"Hot Coffee",price:39},{name:"Tea",price:15},{name:"Masala Tea",price:20},{name:"Green Tea",price:25},{name:"Lassi Sweet",price:39},{name:"Lassi Salted",price:39},{name:"Cold Drink 250ml",price:20},{name:"Water Bottle",price:15},{name:"Ice Cream Cup",price:29},{name:"Choco Ice Cream",price:49},{name:"Gulab Jamun 2pc",price:39},{name:"Rasgulla 2pc",price:39},{name:"Brownie",price:49},{name:"Donut",price:39},{name:"Pastry",price:49},{name:"Garlic Bread",price:59},{name:"Cheese Garlic Bread",price:79},{name:"Veg Nuggets 6pc",price:59},{name:"Chicken Nuggets 6pc",price:89}
];

function renderItems(){
  let html='';
  ITEMS.forEach((it,i)=>{
    html+=`<div class="item"><div><b>${it.name}</b><br>₹${it.price}</div><div><button onclick="addToCart(${i})">Add</button> <span id="qty${i}">${cart[i]||0}</span></div></div>`;
  });
  document.getElementById('itemsList').innerHTML=html;
  updateCart();
}
function addToCart(i){cart[i]=(cart[i]||0)+1; document.getElementById('qty'+i).innerText=cart[i]; updateCart();}
function updateCart(){
  let sub=0; Object.keys(cart).forEach(k=>{sub+=ITEMS[k].price*cart[k]});
  let delivery = orderType==='delivery'?30:0;
  if(sub===0) delivery=0;
  let total = sub+delivery-couponDiscount;
  if(total<0) total=0;
  document.getElementById('subtotal').innerText='₹'+sub;
  document.getElementById('deliveryCharge').innerText='₹'+delivery;
  document.getElementById('discount').innerText='-₹'+couponDiscount;
  document.getElementById('total').innerText='₹'+total;
}
function setType(t){
  orderType=t;
  document.getElementById('btnDelivery').className=t==='delivery'?'tag delivery-active':'tag';
  document.getElementById('btnTakeaway').className=t==='takeaway'?'tag delivery-active':'tag';
  document.getElementById('addressBox').style.display=t==='delivery'?'block':'none';
  updateCart();
  if(t==='delivery') checkDistance();
}
function applyCoupon(){
  let code=document.getElementById('couponInput').value.trim().toUpperCase();
  let sub=0; Object.keys(cart).forEach(k=>{sub+=ITEMS[k].price*cart[k]});
  if(code==='ADYA50' && sub>=500){couponDiscount=50; document.getElementById('couponMsg').innerText='ADYA50 Applied! 50 OFF';}
  else if(code==='ADYA50'){document.getElementById('couponMsg').innerText='500 se zyada ka order chahiye'; couponDiscount=0;}
  else {document.getElementById('couponMsg').innerText='Invalid Coupon'; couponDiscount=0;}
  updateCart();
}
function getLiveLocation(){
  if(!navigator.geolocation){alert('Location not supported');return;}
  navigator.geolocation.getCurrentPosition(pos=>{
    let lat=pos.coords.latitude; let lng=pos.coords.longitude;
    userLatLng=lat+','+lng;
    document.getElementById('liveLocText').innerHTML=`Live: ${lat.toFixed(5)}, ${lng.toFixed(5)} <a href="https://www.google.com/maps?q=${lat},${lng}" target="_blank">Map pe dekho</a>`;
    document.getElementById('custAddress').value=`Live Location: ${lat}, ${lng} - https://www.google.com/maps?q=${lat},${lng}`;
    checkDistanceWithPos(lat,lng);
  });
}
function checkDistance(){
  if(!navigator.geolocation) return;
  navigator.geolocation.getCurrentPosition(pos=>{checkDistanceWithPos(pos.coords.latitude,pos.coords.longitude)});
}
function checkDistanceWithPos(lat,lng){
  let d=getDistance(SHOP_LAT,SHOP_LNG,lat,lng);
  if(d>1){document.getElementById('distanceMsg').innerText=`Tu ${d.toFixed(2)} KM door hai - Delivery sirf 1KM tak! Takeaway lo`; if(orderType==='delivery'){setType('takeaway')}}
  else {document.getElementById('distanceMsg').innerText=`Tu ${d.toFixed(2)} KM pe hai - Delivery ho jayega!`; }
}
function getDistance(lat1,lon1,lat2,lon2){
  let R=6371; let dLat=(lat2-lat1)*Math.PI/180; let dLon=(lon2-lon1)*Math.PI/180;
  let a=Math.sin(dLat/2)*Math.sin(dLat/2)+Math.cos(lat1*Math.PI/180)*Math.cos(lat2*Math.PI/180)*Math.sin(dLon/2)*Math.sin(dLon/2);
  return R*2*Math.atan2(Math.sqrt(a),Math.sqrt(1-a));
}
function placeOrder(){
  let name=document.getElementById('custName').value.trim();
  let mobile=document.getElementById('custMobile').value.trim();
  let address=document.getElementById('custAddress').value.trim();
  let utr=document.getElementById('utrInput').value.trim();
  if(!name||!mobile||!utr){alert('Name, Mobile, UTR bharo!');return;}
  if(orderType==='delivery'&&!address){alert('Delivery ke liye Address dalo ya Live Location use karo!');return;}
  if(Object.keys(cart).length===0){alert('Item add karo!');return;}
  if(!shopOpen){alert('Shop abhi OFF hai!');return;}
  document.getElementById('loader').style.display='flex';
  setTimeout(()=>{
    document.getElementById('loader').style.display='none';
    let orders=JSON.parse(localStorage.getItem('orders')||'[]');
    let sub=0; let itemsText='';
    Object.keys(cart).forEach(k=>{sub+=ITEMS[k].price*cart[k]; itemsText+=ITEMS[k].name+' x'+cart[k]+', ';});
    let delivery = orderType==='delivery'?30:0;
    let total = sub+delivery-couponDiscount;
    let order={id:Date.now(),name,mobile,address:orderType==='delivery'?address:'Takeaway - No Address',liveLoc:userLatLng,type:orderType,items:itemsText,subtotal:sub,delivery,coupon:couponDiscount>0?'ADYA50':'-',total,utr,status:'new',time:new Date().toLocaleString()};
    orders.push(order); localStorage.setItem('orders',JSON.stringify(orders));
    alert('Order bhej diya! Admin check karega. Status ka notification ayega.');
    cart={}; couponDiscount=0; renderItems(); document.getElementById('couponMsg').innerText='';
    if(navigator.vibrate) navigator.vibrate([500,200,500]);
  },2500);
}
function loadAdmin(){
  let orders=JSON.parse(localStorage.getItem('orders')||'[]').reverse();
  let html='';
  orders.forEach(o=>{
    html+=`<div class="admin-card">
    <b>#${o.id} - ${o.name} - ${o.mobile}</b><br>
    UTR: ${o.utr} <button onclick="navigator.clipboard.writeText('${o.utr}')">Copy</button><br>
    Type: ${o.type==='delivery'?'🛵 Delivery (+30)':'🏪 Takeaway FREE'} - ${o.type==='delivery'?'45 Min':''}<br>
    <b>ADDRESS:</b> ${o.address}<br>
    ${o.liveLoc?`<a href="https://www.google.com/maps?q=${o.liveLoc}" target="_blank">📍 Live Location Map Pe Dekho</a><br>`:''}
    Items: ${o.items}<br>
    Subtotal: ${o.subtotal} | Delivery: ${o.delivery} | Coupon: ${o.coupon} | <b>Total: ${o.total}</b><br>
    Time: ${o.time}<br>Status: <b>${o.status}</b><br>
    <button onclick="updateOrder(${o.id},'accepted')" style="background:green;color:#fff;padding:8px;border:0;border-radius:5px;margin:5px">✅ ACCEPT</button>
    <button onclick="updateOrder(${o.id},'rejected')" style="background:red;color:#fff;padding:8px;border:0;border-radius:5px">❌ REJECT</button>
    </div>`;
  });
  document.getElementById('adminOrders').innerHTML=html||'No orders';
  document.getElementById('qrDate').innerText=qrLastChange;
}
function updateOrder(id,status){
  let orders=JSON.parse(localStorage.getItem('orders')||'[]');
  let idx=orders.findIndex(o=>o.id===id); if(idx>-1){orders[idx].status=status; localStorage.setItem('orders',JSON.stringify(orders)); loadAdmin(); localStorage.setItem('lastStatus_'+id,status); alert('Customer ko '+status+' ka notification jayega (live check)');}
}
function toggleShop(){shopOpen=!shopOpen; localStorage.setItem('shopOpen',shopOpen); document.getElementById('shopStatus').innerText=shopOpen?'OPEN':'CLOSED'; document.getElementById('toggleBtn').innerText=shopOpen?'Shop OFF Karo':'Shop ON Karo'; document.getElementById('toggleBtn').style.background=shopOpen?'red':'green';}
function changeQR(){
  let today=new Date().getDate();
  if(today!==3){if(!confirm('Aaj 3 tarik nahi hai! Fir bhi QR change karna hai?')) return;}
  let newUpi=prompt('Naya UPI ID dalo:','adya@upi');
  if(newUpi){document.getElementById('qrImg').src=`https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=upi://pay?pa=${newUpi}`; localStorage.setItem('qrData',newUpi); qrLastChange=new Date().toLocaleString(); localStorage.setItem('qrLastChange',qrLastChange); document.getElementById('qrDate').innerText=qrLastChange;}
}
// INIT
renderItems(); setType('delivery');
if(window.location.search.includes('admin')){document.getElementById('customerView').classList.add('hidden'); document.getElementById('adminView').classList.remove('hidden'); loadAdmin(); setInterval(()=>{let orders=JSON.parse(localStorage.getItem('orders')||'[]'); if(orders.length>0 && orders[orders.length-1].status==='new'){document.getElementById('ringTone').play(); if(navigator.vibrate) navigator.vibrate([1000,500,1000]); loadAdmin();}},3000);}
document.getElementById('shopStatus').innerText=shopOpen?'OPEN':'CLOSED';
let savedQR=localStorage.getItem('qrData'); if(savedQR){document.getElementById('qrImg').src=`https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=upi://pay?pa=${savedQR}`;}

// Live order status check for customer
setInterval(()=>{
  let orders=JSON.parse(localStorage.getItem('orders')||'[]');
  orders.forEach(o=>{
    let last=localStorage.getItem('lastStatus_'+o.id);
    if(last && last!==o.status && last!=='new'){/* notification logic */ }
  });
},2000);
</script>
</body>
</html>
