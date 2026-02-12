from requests_lab3 import getAllBooks

def average_book_price():
    books = getAllBooks()
    
books = getAllBooks()
prices = [b["price"] for b in books if b.get("price") is not None]

average = sum(prices) / len(prices) if prices else 0

print(f"Average price of {len(prices)} books is €{average:.2f}")
    
# Call the function
average_book_price()