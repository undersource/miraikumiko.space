import uvicorn
from backend.main import app
from backend.misc.arguments import args
from backend.misc.config import config
from backend.misc.security import get_password_hash
from backend.misc.database import session, User

MODE = config["app"]["MODE"]
SOCKET = config["app"]["SOCKET"] or "miraikumiko.sock"
HOST = config["app"]["HOST"] or "127.0.0.1"
PORT = config["app"]["PORT"] or 8000

if __name__ == "__main__":
    if not (args.login is None or args.password is None):
        user = User()
        hpw = get_password_hash(args.password)
    
        if args.name is not None:
            user.name = args.name
        else:
            user.name = args.login
        
        if args.phone is not None:
            user.phone = args.phone

        if args.email is not None:
            user.email = args.email

        user.login = args.login
        user.password = hpw

        session.add(user)
        session.commit()
        
        print(f'User "{user.name}" has been created')
    else:
        if MODE == "prod":
            uvicorn.run("run:app", uds=SOCKET, reload=True)
        else:
            uvicorn.run("run:app", host=HOST, port=PORT, reload=True)
