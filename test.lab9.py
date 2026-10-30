from inventory_manager import (Product, PhysicalProduct, DigitalProduct,
                              CanBeShipped, Inventory,
                              save_inventory, load_inventory)

guitar = PhysicalProduct("P001", "Guitar", 299.99, 10, 2.5)
os_lic = DigitalProduct("D001", "Operating System", 149.00, 100, 4500)

print("--- Weights and download sizes are displayed ---")
guitar.display_information()
os_lic.display_information()

print("--- get_fulfilment_info() ---")
print(guitar.get_fulfilment_info())
print(os_lic.get_fulfilment_info())

print("--- Product cannot be instantiated ---")
try:
    Product("X001", "Generic", 1.0, 1)
    print("FAIL: Product was created")
except TypeError as e:
    print("PASS:", e)

print("--- Shipping cost (expect 6.0 and 55.0) ---")
print(PhysicalProduct("P002", "Book", 15.0, 50, 0.5).calculate_shipping_cost())
print(PhysicalProduct("P003", "Anvil", 120.0, 3, 25).calculate_shipping_cost())

print("--- Digital is not shippable (expect True, False, False) ---")
print(isinstance(guitar, CanBeShipped))
print(isinstance(os_lic, CanBeShipped))
print(hasattr(os_lic, "calculate_shipping_cost"))

print("--- Inventory operations ---")
inv = Inventory()
print(inv.add_product(guitar))                     # True
print(inv.add_product(os_lic))                     # True
print(inv.add_product(guitar))                     # False (duplicate)
print(inv.search_product("D001") is os_lic)        # True
print(inv.search_product("Z999"))                  # None
print(os_lic.update_stock(50))                     # True
print(os_lic.update_stock(-1))                     # False

print("--- JSON round trip ---")
save_inventory(inv)
loaded = load_inventory()
loaded.display_all()
print(type(loaded.search_product("P001")).__name__)   # PhysicalProduct
print(type(loaded.search_product("D001")).__name__)   # DigitalProduct