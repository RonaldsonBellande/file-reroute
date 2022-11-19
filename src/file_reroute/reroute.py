import sys, os

def reroute(directory_name):
    path = os.getcwd()
    previous_path = None
    while True:
        if directory_name in path:
            previous_path = path
            path = os.path.abspath(os.path.join(path, os.pardir))
            if directory_name not in path:
                path = previous_path
                break
    try:
        os.chdir(path)
        sys.path.append(os.getcwd())
    except OSError:
        print("Can't change the Current Working Directory")
