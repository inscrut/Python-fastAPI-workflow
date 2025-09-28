# Python test fastAPI workflow

Simple test coding with fastAPI.
Using local service Inventree REST API for testing.

Start backend
```bash 
uvicorn.exe src.main:app --reload
```

FastAPI UI
```bash
http://127.0.0.1:8000/docs
```

Workflow:
- init fastAPI
- use `backend/.env` file for **config.py**:
``` bash
API_KEY_INVENTREE="Token ..."
INV_IP="http://ip-address"

```
- add handlers GET, POST
- add router
- add sqlite, use `sqlalchemy`

