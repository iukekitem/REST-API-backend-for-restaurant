from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/customers")
async def get_all_customers():
    return {"message": "All Customers"}


@app.get("/customers/{customer_id}")
async def get_customer(customer_id: int):
    return {"message": f"Customer {customer_id}"}


@app.get("/items")
async def get_all_items():
    return {"message": "All items"}


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"message": f"Item {item_id}"}


@app.get("/orders")
async def get_all_orders():
    return {"message": "All orders"}


@app.get("/orders/{order_id}")
async def get_order(order_id: int):
    return {"message": f"Order {order_id}"}