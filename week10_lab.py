"""
Order Processor:
This script processes raw order data, validates integrity, and calculates totals.
please keep in mind that this demo will be used on your first lab exercise
"""

# --- 1. Constants (Week 10: No "Magic Numbers") ---
# We define these at the top so they are easy to change later.
TAX_RATE = 0.15          # 15% Sales Tax
#Constant, does not change, can be defined globally.
SHIPPING_COST = 5.99     # Flat rate shipping
FREE_SHIPPING_THRESHOLD = 50.00

# --- 2. Input Data (Simulating a JSON API response) ---
raw_orders = [
    {"id": "ORD-001", "item": "Wireless Mouse", "price": 25.00, "quantity": 2, "vip":False},
    {"id": "ORD-002", "item": "Gaming Monitor", "price": 300.00, "quantity": 1, "vip":True},
    {"id": "ORD-003", "item": "Corrupted Item", "price": -10.00, "quantity": 1, "vip":False}, # Error: Negative price
    {"id": "ORD-004", "item": "Ghost Item", "quantity": 5,"vip":True},                       # Error: Missing price
    {"id": "ORD-005", "item": "USB Cable", "price": 5.00, "quantity": 0,"vip":False}          # Error: Zero quantity
]

# --- 3. Helper Functions (Week 4 & 10: Single Responsibility Principle) ---

def is_valid_order(order):
    """
    Checks if an order dictionary contains all necessary fields and valid values.
    Returns True if valid, False otherwise.
    """
    # Check for missing keys
    if "price" not in order or "quantity" not in order or "item" not in order:
        print(f"FAILED: Order {order.get('id', 'Unknown')} is missing data.") #If there is missing data, it is handled here. Otherwise problems occur later and the program crashes.
        return False

    # Check for logical errors (business rules)
    if order["price"] <= 0:
        print(f"FAILED: Order {order['id']} has an invalid price: ${order['price']}")
        return False
    
    if order["quantity"] <= 0:
        print(f"FAILED: Order {order['id']} has an invalid quantity: {order['quantity']}")
        return False

    return True

def calculate_final_price(price, quantity, vip):
    """
    Calculates total cost including tax and shipping logic.
    """
    subtotal = price * quantity
    tax_amount = subtotal * TAX_RATE
    
    if quantity>5:
        subtotal=subtotal-(subtotal*0.9)
    # Industry Logic: Conditional shipping costs
    if subtotal >= FREE_SHIPPING_THRESHOLD or vip==True:
        shipping = 0.00
    else:
        shipping = SHIPPING_COST
        
    total = subtotal + tax_amount + shipping
    return round(total, 2)

# --- 4. Main Logic (Week 3: Loops) ---

def process_order_batch(orders):
    """
    Main driver function to process a list of orders.
    """
    print("--- STARTING BATCH PROCESSING ---\n")
    
    valid_orders = []
    total_revenue = 0.00

    # Loop through every order in the list
    for current_order in orders:
        
        # Step A: Validate (Defensive Coding)
        if is_valid_order(current_order):
            
            # Step B: Calculate logic (only if valid)
            final_price = calculate_final_price(
                current_order["price"], 
                current_order["quantity"],
                current_order["vip"]
            )
            
            # Step C: Store clean data
            # We create a new 'clean' dictionary rather than mutating the old one
            processed_record = {
                "id": current_order["id"],
                "product": current_order["item"],
                "final_bill": final_price
            }
            
            valid_orders.append(processed_record)
            total_revenue += final_price
            print(f"SUCCESS: Processed {current_order['id']} - Total: ${final_price}")
    #Tax is added at the end as there are many factors that affect the intermediate cost before tax.
    print(f"\n--- BATCH COMPLETE ---")
    print(f"Total Valid Orders: {len(valid_orders)}")
    print(f"Total Revenue Generated: ${round(total_revenue, 2)}")
    
    return valid_orders

# --- 5. Execution ---
if __name__ == "__main__":
    clean_report = process_order_batch(raw_orders)
    # real world: we would now save 'clean_report' to a CSV or Database