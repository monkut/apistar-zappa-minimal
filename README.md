# Minimal apistar Project

This is a minimal [apistar](https://github.com/encode/apistar) project intended to be used with [zappa](https://github.com/Miserlou/Zappa).

## Deploy

1. Create `.venv`: 

    ```
    python -m venv .venv
    ```
    
2. Enter venv and update `pip` and `setuptools`:

    ```
    $ source .venv/bin/activate
    (.venv)$ pip install pip setuptools --upgrade
    ```

3. Install requirements:

    ```
    (.venv)$ pip install -r requirements.txt 
    ```
    
4. Update the default `zappa_settings.json` (or delete and startover using `zappa init` )configuration included here:

    ```
    {
        "dev": {
            "app_function": "app.app",
            "aws_region": "us-west-2",  # <-- Add region you want to use here!
            "profile_name": "default",  # <-- Add AWS CLI profile you want to use here!
            "s3_bucket": "zappa-[my bucket]",  # <-- Add random bucket name here!
            "keep_warm": false,
            "slim_handler": true  # <-- for testing..feel free to remove
        }
    }
    ```    

    
5. Deploy to AWS lambda via zappa

    ```
    (.venv)$ zappa deploy
    ...
    Deploying API Gateway..
    Your updated Zappa deployment is live!: https://[URL]/dev
    ```
        
6. Check the URL displayed in deployment for the following message:

    ```
    {"message": "200 Installed!"}
    ```    
    
7. Enjoy the magic that is [apistar](https://github.com/encode/apistar) & [zappa](https://github.com/Miserlou/Zappa)!    
