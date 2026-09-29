
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title="Shopping Cart API")


# Pydantic model for adding products
class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=1, le=100)


# Pydantic model for updating products
# All fields are optional so we can update only one field.
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = Field(default=None, gt=0)
    quantity: Optional[int] = Field(default=None, ge=1, le=100)


# Temporary storage
cart = []


# 1. POST /addproduct
@app.post("/addproduct")
def add_product(product: Product):
    cart.append(product)

    return {
        "message": "Product added successfully",
        "product": product
    }


# 2. GET /getproducts
@app.get("/getproducts")
def get_products():
    return {
        "products": cart
    }


# Bonus: GET /getproduct/{index}
@app.get("/getproduct/{index}")
def get_product(index: int):
    if index < 0 or index >= len(cart):
        raise HTTPException(
            status_code=404,
            detail="Product index not found"
        )

    return {
        "product": cart[index]
    }


# 3. PUT /updateproduct/{index}
@app.put("/updateproduct/{index}")
def update_product(index: int, product: ProductUpdate):
    if index < 0 or index >= len(cart):
        raise HTTPException(
            status_code=404,
            detail="Product index not found"
        )

    # Get only the fields that were provided in the request
    update_data = product.model_dump(exclude_unset=True)

    # Update the existing product
    current_product = cart[index]

    updated_product = current_product.model_copy(
        update=update_data
    )

    cart[index] = updated_product

    return {
        "message": "Product updated successfully",
        "product": updated_product
    }


# 4. DELETE /deleteproduct/{index}
@app.delete("/deleteproduct/{index}")
def delete_product(index: int):
    if index < 0 or index >= len(cart):
        raise HTTPException(
            status_code=404,
            detail="Product index not found"
        )

    deleted_product = cart.pop(index)

    return {
        "message": "Product deleted successfully",
        "product": deleted_product
    }


# Bonus: GET /total
@app.get("/total")
def get_total():
    total = sum(
        product.price * product.quantity
        for product in cart
    )

    return {
        "total": total
    }

