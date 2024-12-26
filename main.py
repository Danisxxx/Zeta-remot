from configs._def_main_ import *  

zeta = Client(
    "zeta", 
    api_id=os.getenv('API_ID'),
    api_hash=os.getenv('API_HASH'),
    bot_token=os.getenv('BOT_TOKEN'),
    plugins=dict(root='zaddons')
)

if __name__ == "__main__":
    try:
        zeta.run()  
    except Exception as e:
        print(f"An error occurred: {e}")