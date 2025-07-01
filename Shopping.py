import datetime

print("...WELCOME TO OUR SHOPPING CART...")
print("Discount Rules:")
print("→ Up to ₹10,000 → 15% discount")
print("→ ₹10,001 to ₹20,000 → 25% discount")
print("→ ₹20,001 to ₹50,000 → 50% discount")
print(".............Let's start your shopping............")

# 50 Essential Products with Prices
products = {
    1: ("T-Shirt", 500), 2: ("Jeans", 1200), 3: ("Socks", 100), 4: ("Undergarments", 300),
    5: ("Jacket", 2500), 6: ("Formal Shirt", 800), 7: ("Pajamas", 600), 8: ("Saree", 2000),
    9: ("Sweater", 1500), 10: ("Raincoat", 700),
    11: ("Toothpaste", 80), 12: ("Toothbrush", 40), 13: ("Shampoo", 120), 14: ("Soap", 30),
    15: ("Hair Oil", 90), 16: ("Razor", 150), 17: ("Deodorant", 200), 18: ("Face Wash", 180),
    19: ("Hand Sanitizer", 60), 20: ("Comb", 50),
    21: ("Rice (1 kg)", 60), 22: ("Wheat Flour (1 kg)", 50), 23: ("Cooking Oil (1 L)", 150),
    24: ("Milk (1 L)", 60), 25: ("Sugar (1 kg)", 45), 26: ("Salt (1 kg)", 20),
    27: ("Tea Powder (500g)", 120), 28: ("Coffee Powder (250g)", 150), 29: ("Biscuits Pack", 25),
    30: ("Noodles Packet", 20),
    31: ("Pressure Cooker", 2000), 32: ("Frying Pan", 800), 33: ("Spoon Set", 150),
    34: ("Water Bottle", 100), 35: ("Lunch Box", 250), 36: ("Gas Lighter", 80),
    37: ("Knife Set", 300), 38: ("Chopping Board", 200), 39: ("Kettle", 700),
    40: ("Tiffin Carrier", 350),
    41: ("Smartphone", 12000), 42: ("Earphones", 500), 43: ("Power Bank", 1000),
    44: ("USB Cable", 150), 45: ("LED Bulb", 100), 46: ("Extension Board", 300),
    47: ("Bluetooth Speaker", 1500), 48: ("Fan", 2000), 49: ("Electric Iron", 1800),
    50: ("Torch Light", 300)
}

name = input("Enter your name: ")
total = 0
cart = []

# Show product list
print("\n📦 Available Products:")
for key, value in products.items():
    print(f"{key:>2}. {value[0]:<25} - ₹{value[1]}")

# Shopping Loop
while True:
    try:
        choice = int(input("\nEnter product number to add to cart: "))
        if choice in products:
            item_name, item_price = products[choice]
            qty = int(input(f"Enter quantity for {item_name}: "))
            item_total = item_price * qty
            total += item_total
            cart.append((item_name, qty, item_price, item_total))
        else:
            print("❌ Invalid product number!")
    except ValueError:
        print("⚠️ Please enter a valid number!")

    con = input("Do you want to continue shopping? (yes/no): ")
    if con.lower() != 'yes':
        break

# Apply discount
if total <= 10000:
    discount = total * 15 // 100
    discount_rate = "15%"
elif total <= 20000:
    discount = total * 25 // 100
    discount_rate = "25%"
elif total <= 50000:
    discount = total * 50 // 100
    discount_rate = "50%"
else:
    discount = 0
    discount_rate = "No discount"

subtotal = total - discount
gst = subtotal * 0.18
final_amount = subtotal + gst

# Display Summary
print("\n===== 🧾 BILL SUMMARY =====")
print(f"Customer Name: {name}")
for item, qty, price, item_total in cart:
    print(f"{item:25} x{qty:<2} - ₹{price} each - ₹{item_total}")
print(f"\nTotal Amount: ₹{total}")
print(f"Discount ({discount_rate}): -₹{discount}")
print(f"Subtotal after Discount: ₹{subtotal}")
print(f"GST (18%): ₹{gst:.2f}")
print(f"Final Amount to Pay: ₹{final_amount:.2f}")

# Save to bill.txt
now = datetime.datetime.now()
with open("bill.txt", "w", encoding="utf-8") as f:  # <-- encoding fixed
    f.write("===== SHOPPING CART RECEIPT =====\n")
    f.write(f"Customer Name: {name}\n")
    f.write(f"Date & Time: {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    for item, qty, price, item_total in cart:
        f.write(f"{item:25} x{qty:<2} - ₹{price} - ₹{item_total}\n")
    f.write(f"\nTotal: ₹{total}\n")
    f.write(f"Discount ({discount_rate}): -₹{discount}\n")
    f.write(f"Subtotal: ₹{subtotal}\n")
    f.write(f"GST (18%): ₹{gst:.2f}\n")
    f.write(f"Final Amount: ₹{final_amount:.2f}\n")
    f.write("Thank you for shopping with us!\n")


print("\n🧾 Your bill has been saved as 'bill.txt'")
print("......Thank you for visiting our shopping cart.....")
