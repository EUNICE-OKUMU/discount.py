class SaleItem:
  def __init__(self, item_id, name, unit_price):
    self.item_id = item_id
    self.name = name
    self.unit_price = unit_price

  def calculate_total(self, quantity):

    raise NotImplementedError("Subclass must implement calculate_total()")

class StandardItem(SaleItem):

  def __init__(self, item_id, name, unit_price):
    super().__init__(item_id, name, unit_price)

  def calculate_total(self, quantity):

    return self.unit_price * quantity

class DiscountedItem(SaleItem):
  

  def __init__(self, item_id, name, unit_price, discount_percentage):
    super().__init__(item_id, name, unit_price)
    self.discount_percentage = discount_percentage

  def calculate_total(self, quantity):

    discounted_price = self.unit_price * (1 - self.discount_percentage / 100)
    return discounted_price * quantity

class ServiceItem(SaleItem):

  def __init__(self, item_id, name, hourly_rate):
    super().__init__(item_id, name, hourly_rate)  # Hourly rate acts as unit price here

  def calculate_total(self, quantity):

    return self.unit_price * quantity  # Hourly rate is already stored in unit_price

# Example usage
standard_item = StandardItem(100, "Trouser", 10.50)
total_cost_standard = standard_item.calculate_total(2)
print(f"Standard Item (Trouser, 2 units): ${total_cost_standard:.2f}")

discounted_item = DiscountedItem(200, "skirt", 20.00, 15)
total_cost_discounted = discounted_item.calculate_total(1)
print(f"Discounted Item (skirt, 1 unit with 15% discount): ${total_cost_discounted:.2f}")

service_item = ServiceItem(300, "Consulting Service", 75.00)
total_cost_service = service_item.calculate_total(3)  # Assuming quantity represents hours here
print(f"Service Item (Consulting, 3 hours): ${total_cost_service:.2f}")
