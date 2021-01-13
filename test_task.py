def test_btn_add_to_cart_exist(self, browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    Cart_btn = browser.find_element_by_css_selector(".btn-add-to-basket")
    cart_btn_language = cart_btn.text
    assert cart_btn_language == "Añadir al carrito"
