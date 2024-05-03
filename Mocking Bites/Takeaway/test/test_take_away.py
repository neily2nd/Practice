from unittest.mock import Mock, call
from lib.take_away import Menu, Order, OrderDish, Customer

class TestTakeaway:
    def test_menu_add_item(self):
        menu = Menu()
        menu.add_dish("Burger", 5.99)
        assert menu.return_list() == {"Burger": 5.99}

    def test_order_item_subtotal(self):
        order_item = OrderDish("Burger", 2, 5.99)
        assert order_item.subtotal() == 11.98

    def test_order_add_item(self):
        menu_mock = Mock()
        menu_mock.menu_items = {"Burger": 5.99}
        order = Order(menu_mock)
        order.add_dish("Burger", 2)
        assert len(order.items) == 1
        assert order.items[0].item == "Burger"

    def test_order_calculate_total(self):
        menu_mock = Mock()
        menu_mock.menu_items = {"Burger": 5.99, "Fries": 2.49}
        order = Order(menu_mock)
        order.add_dish("Burger", 2)
        order.add_dish("Fries", 1)
        assert order.calculate_total() == 14.47

    def test_customer_place_order(self):
        order_mock = Mock()
        requester_mock =Mock()
        customer = Customer(order_mock, requester_mock)
        dishes_quantities = {"Burger": 2, "Fries": 1}
        customer.order_place(dishes_quantities)
        order_mock.add_dish.assert_has_calls([
            call("Burger", 2),
            call("Fries", 1)
        ])

def test_confirm():
    order_mock = Mock()
    requester_mock = Mock(name="requester")
    response_mock = Mock(name="response")
    requester_mock.get.return_value = response_mock
    
    response_mock.json.return_value = {
        "SID":"YYYYYY"
    }
    
    customer_confirm = Customer(order_mock, requester_mock)
    result = customer_confirm.confirm()
    
    assert result == {"SID": "YYYYYY"}
        
        

