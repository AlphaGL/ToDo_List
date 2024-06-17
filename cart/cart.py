class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get a session key if it exists

        cart = self.session.get('session_key')

        # if the user is new no session key

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # lets make sure the cart is available to all pages

        # self.cart = cart

        # def add(self, product):
        # product_id = str(product.id)

        # #logic
        # if product_id in self.cart:
        #     pass
        # else:
        #     self.cart[product_id] = {'price': product.price}
        
        # self.session.modified = True


        