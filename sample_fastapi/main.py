from fastapi import FastAPI, Request, Form, Response, Depends, HTTPException
from fastapi.responses import JSONResponse
from itsdangerous import URLSafeSerializer
import uuid

app = FastAPI()

# Secret key for signing sessions
SECRET_KEY = "mysecretkey"
serializer = URLSafeSerializer(SECRET_KEY)

# Fake database
users_db = {
    "admin1": "password123",
    "admin2": "password1234",
    "admin3": "password12345",
}

# In-memory session store
session_store = {}


# Dependency to get current user
def get_current_user(request: Request):
    session_cookie = request.cookies.get("session_id")
    print("session_store", session_store)
    print("session_cookie------->", session_cookie)
    if not session_cookie:
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        session_id = serializer.loads(session_cookie)
    except:
        raise HTTPException(status_code=401, detail="Invalid session")

    user = session_store.get(session_id)

    if not user:
        raise HTTPException(status_code=401, detail="Session expired")

    return user


# Login Route
@app.post("/login")
def login(
    response: Response,
    username: str = Form(...),
    password: str = Form(...)
):
    # Validate user
    if users_db.get(username) != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Create session
    session_id = str(uuid.uuid4())

    session_store[session_id] = username

    # Sign session ID
    signed_session = serializer.dumps(session_id)

    # Set cookie
    response.set_cookie(
        key="session_id",
        value=signed_session,
        httponly=True
    )

    return {"message": "Login successful"}


# Protected Route
@app.get("/dashboard")
def dashboard(user: str = Depends(get_current_user)):
    return {
        "message": f"Welcome {user}"
    }


# Logout Route
@app.post("/logout")
def logout(request: Request, response: Response):
    session_cookie = request.cookies.get("session_id")

    if session_cookie:
        try:
            session_id = serializer.loads(session_cookie)
            session_store.pop(session_id, None)
        except:
            pass

    response.delete_cookie("session_id")

    return {"message": "Logged out"}