import argparse
import dotenv
from app import Resolver
from exception import exceptions

env_file = dotenv.find_dotenv()
dotenv.load_dotenv(env_file)

resolver = Resolver()

parser = argparse.ArgumentParser(description="K3S + Multipass virtual cluster")
parser.add_argument(
    "-c", "--cluster", help="Initiate cluster with : 'init' / Terminate cluster with : 'terminate' / Add node with : 'add'", required=True)
parser.add_argument(
    "-n", "--name", help="Required if you use option of '-c' as 'add'. New node's name"
)

argList = parser.parse_args()

if argList.cluster == "init":
    resolver.cluster_init()
elif argList.cluster == "terminate":
    resolver.terminate_cluster()
elif argList.cluster == "add":
    if not argList.name:
        raise exceptions.RequiredCommandLineOptionLost('-n')
    resolver.add_node(argList.name)
else:
    raise exceptions.WrongArgumentGiven()