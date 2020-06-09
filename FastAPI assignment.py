import uvicorn as uvicorn
from fastapi import FastAPI
import os, shutil

app = FastAPI()


@app.get('/departments')
def getDepartment():
    os.chdir("F:/PS2")
    departments = os.listdir()
    return departments
@app.post('/departments/{dep}')
def postDepartment(dep):
    os.chdir("F:/PS2")
    try:
        os.mkdir(dep)
        return "Department Added"
    except FileExistsError:
        return "Department already exists"


@app.put('/departments/{dep}/{newdep}')
def putDepartment(dep,newdep):
    os.chdir("F:/PS2")
    departments = os.listdir()
    check = dep in departments;
    if check:
        os.rename(dep, newdep)
        return "Department Modified"
    else:
        return "Department does not exist"
@app.delete('/departments/del/{dep}')
def deleteDepartment(dep):
    os.chdir("F:/PS2")
    departments = os.listdir()
    check = dep in departments;
    if check:
        shutil.rmtree(dep)
        return "Department Deleted"
    else:
        return "Department does not exist"

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)