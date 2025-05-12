from fastapi import FastAPI, Depends, Query, HTTPException, status
from typing import Annotated

app = FastAPI()

# 1. Simple Dependency
def simple_dep():
    return {"goal": "Learn Dependency Injection"}

@app.get("/goal")
def get_goal(info: Annotated[dict, Depends(simple_dep)]):
    return info

# 2. Dependency with Query Params
def login_check(username: str = Query(...), password: str = Query(...)):
    if username == "admin" and password == "admin":
        return {"msg": "Welcome admin"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/login")
def login(result: Annotated[dict, Depends(login_check)]):
    return result

# 3. Multiple Dependencies
def plus_one(num: int):
    return num + 1

def plus_two(num: int):
    return num + 2

@app.get("/add/{num}")
def add_total(num: int, one: Annotated[int, Depends(plus_one)], two: Annotated[int, Depends(plus_two)]):
    return {"total": num + one + two}

# 4. Class-based Dependency
blogs = {"1": "AI", "2": "ML", "3": "DL"}

class GetObjectOr404:
    def __init__(self, model):
        self.model = model

    def __call__(self, id: str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=404, detail="Not Found")
        return obj

blog_dep = GetObjectOr404(blogs)

@app.get("/blog/{id}")
def get_blog(name: Annotated[str, Depends(blog_dep)]):
    return {"blog": name}
