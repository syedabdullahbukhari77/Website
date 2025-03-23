from flask import Flask  , jsonify, render_template 
from flask_cors import CORS


app =  Flask (__name__)
cors = CORS(app, origins='*')

@app.route('/Home')
def Home () :
    return render_template('index.html')

@app.route ('/api/users' , methods=['GET'])
def users():
    return jsonify(
        {
            'users' : [
                'Syed Abdullah Bukari',
                'Syed Hussain',
                'Umar',
                'Abu bakr' 
            ]
        }
    )

if  __name__ == "__main__":
    app.run (debug=True , port=3000)
