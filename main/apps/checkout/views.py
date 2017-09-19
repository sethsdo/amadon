from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
  if 'quantity' and 'price' and 'total_price' not in request.session:
      request.session['quatity'] = 0
      request.session['price'] = 0
      request.session['total_price'] = 0
  return render(request, 'temp/index.html')

def process(request):
      print "hello"
      price = {
          '1': 10,
          '2': 15,
          '3': 20,
          '4': 11,
      }
      total = int(request.POST['quantity'])
      print total
      id = request.POST['product_id']
      print price[id]

      request.session['quantity'] = request.POST['quantity']
      print request.session['quantity']

      request.session['price'] = price[id] * total
      print request.session['price']

      request.session['total_price'] += request.session['price']

      print request.session['total_price']
      return redirect("/item_checkout")

def buy(request):
  return render(request, 'temp/checkout.html')

def back(request):
  return redirect("/")
 
