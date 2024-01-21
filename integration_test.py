from unittest.mock import MagicMock

import order_service
import invoice_service
import shipping_service

# Module stubs
order_service.get_order = MagicMock(return_value={'id': 1}) 
invoice_service.generate_invoice = MagicMock(return_value=999)
shipping_service.get_shipping_cost = MagicMock(return_value=10.99)

# Integration test
def test_order_flow():
    order = order_service.get_order()
    
    invoice_num = invoice_service.generate_invoice(order)
    
    shipping_cost = shipping_service.get_shipping_cost(order)
    
    assert invoice_num == 999
    assert shipping_cost == 10.99