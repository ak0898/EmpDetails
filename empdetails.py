from flask import Flask,request,jsonify,json
from json import dumps
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/emp_info",methods=["POST","GET"])
def emp():
    df = pd.read_csv(r"C:\Users\HP\Desktop\SQL\EmpDetails.csv")
    
    if request.method == "GET":
        final_df = df.to_dict(orient="records")
        return jsonify(final_df)
    if request.method == "POST":
        ID = request.json["id"]
     
    final_df = df[df["empid"] == ID]
    final_df = final_df.to_dict(orient="records")
    return jsonify(final_df)

if __name__ == "__main__":
    app.run(debug=True)