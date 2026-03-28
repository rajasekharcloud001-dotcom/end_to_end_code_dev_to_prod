import os
def say_hello():
    env = os.getenv("ENV_NAME","local")
    project = os.getenv("GCP_PROJECT","unknow-project")

    message = f"hello from {env.upper()} enviroment"
    print(message)
    print(f"gcp project :{project}")
    print("Pipeline is working perfectly! ✅")
if __name__=="__main__":
    say_hello()

