from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sample Website</title>

        <style>
            body{
                background-color: yellow;
                font-family: Arial;
                text-align:center;
                margin-top:100px;
            }

            .box{
                width:350px;
                margin:auto;
                padding:20px;
                background:white;
                border-radius:10px;
            }

            input{
                width:90%;
                padding:8px;
                margin:10px;
            }

            button{
                padding:10px 20px;
            }
        </style>
    </head>

    <body>

    <div class="box">
        <h2>User Form</h2>

        <input type="text" placeholder="Enter Name"><br>

        <input type="email" placeholder="Enter Email"><br>

        <h3>Select Options</h3>

        <input type="checkbox"> Python<br>
        <input type="checkbox"> Java<br>
        <input type="checkbox"> Playwright<br><br>

        <button>Submit</button>

    </div>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)