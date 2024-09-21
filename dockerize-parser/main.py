from seleniumbase import SB

def test_swag_labs(sb):
    sb.open("https://www.saucedemo.com")
    sb.type("#user-name", "standard_user")
    sb.type("#password", "secret_sauce\n")
    sb.assert_element("div.inventory_list")
    sb.assert_exact_text("Products", "span.title")
    sb.click('button[name*="backpack"]')
    sb.click("#shopping_cart_container a")
    sb.assert_exact_text("Your Cart", "span.title")
    sb.assert_text("Backpack", "div.cart_item")
    sb.click("button#checkout")
    sb.type("#first-name", "SeleniumBase")
    sb.type("#last-name", "Automation")
    sb.type("#postal-code", "77123")
    sb.click("input#continue")
    sb.assert_text("Checkout: Overview")
    sb.assert_text("Backpack", "div.cart_item")
    sb.assert_text("29.99", "div.inventory_item_price")
    sb.click("button#finish")
    sb.assert_exact_text("Thank you for your order!", "h2")
    sb.assert_element('img[alt="Pony Express"]')
    sb.js_click("a#logout_sidebar_link")
    sb.assert_element("div#login_button_container")
    print("FINISHED---")


with SB() as sb:
    sb.get_new_driver()
    test_swag_labs(sb)
