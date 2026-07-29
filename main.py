from fastapi import FastAPI
app=FastAPI()
students=[]
@app.get("/test")
def test():
    return {"message":" Student Api is working"}

@app.get("/students")
def get_students():
    return students

@app.post("/students")
def add_student(name: str):
    students.append(name)
    return {"message":"student added successfully"}

@app.put("/students/{id}")
def update_student(id:int,name:str):
    students[id]=name
    return {"message":"student updated successfully"}

@app.patch("/students/{id}")
def patch_student(id:int,name:str):
    students[id]=name
    return {"message":"student updated  partially"}    

@app.delete(("/students/{id}"))
def delete_students(id:int):
    students.pop(id)
    return {"message":"student deleted successfully"}