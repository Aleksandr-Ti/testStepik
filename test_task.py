def test_btn_add_to_cart_exist_on_es(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    browser.get(link)
    Cart_btn = browser.find_element_by_css_selector(".btn-add-to-basket").text
    assert Cart_btn == "Añadir al carrito", f"get '{Cart_btn}' instead of 'Añadir al carrito'"
