import uvicorn
from backend.main import app
from backend.misc.arguments import args
from backend.misc.security import get_password_hash
from backend.misc.database import session, User

if __name__ == "__main__":
    if args.name is not None and args.password is not None:
        user = User()
        hpw = get_password_hash(args.password)
    
        user.name = args.name
        user.password = hpw

        session.add(user)
        session.commit()
        
        print(f'User "{args.name}" has been created')

    else:
        uvicorn.run("run:app", uds="miraikumiko.sock", reload=True)
