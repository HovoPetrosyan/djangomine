class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')  # skey = sessionkey
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart

    def add(self, product, qty):
        """
        adding and aupdating the user sessin data
        :param product:
        :return:
        """
        product_id = product.id
        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price), "qty": int(qty)}

        self.session.modified = True

    def __len__(self):
        """
        get and caount cart data qty
        :return:
        """
        return sum(item['qty'] for item in self.cart.values())
