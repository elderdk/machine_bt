import os
from tempfile import NamedTemporaryFile
from dotenv import load_dotenv


def inject_google_cred_json() -> None:
    """Set the Credential filepath.

    This reads the json string from the environment variable and puts it in a
    TemporaryFile, the path of which is then set as the os.environ credential
    file path.
    """
    tf = NamedTemporaryFile(delete=False)

    with open(tf.name, mode="w") as f:
        f.write(os.getenv("GOOGLE_API_JSON"))
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = tf.name


def set_creds() -> str:
    """Handle environment variables.

    This returns the project_id and calls the inject_google_cred_json func.
    """
    load_dotenv()
    inject_google_cred_json()

    if os.path.exists(".env"):  # if local dev environ
        project_id = os.getenv("PROJECT_ID")

    else:  # if AWS lambda envion
        project_id = os.environ["PROEJCT_ID"]

    return project_id


if __name__ == "__main__":
    pass
