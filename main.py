from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

# defining ds 

class User(BaseModel):
    id:int
    name:str
    isAdmin: bool

users : List[User] = []

# fastapi majorly work on python decarator 

@app.get("/")
def home():
    return {
        "message":"welcome to user home page"
    }
    
@app.get("/user")
def getAllUser():
    return users

@app.post("/user")
def addNewUser(user :User):
    users.append(user)
    return user

@app.put("/user/{userId}")
def updatUser(userId:int, updated_usr:User):
    for index, user in enumerate(users):
        if user.id == userId:
            users[index] = updated_usr
            return updated_usr
    return {"error":"unaable to find user"}

@app.delete("/user/{userId}")
def delUser(userId:int):
     for index, user in enumerate(users):
        if user.id == userId:
            usr = users.pop(index)
            return {"sucess":"user data delated", "user":usr}
     return {"error":"unaable to find user"}
 