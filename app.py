from flask import Flask, render_template
from flask import send_file
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64



app = Flask(__name__,static_url_path='/static')

locations =  [
    ("Hotel Aashirwad", 18.408741725077917, 73.50822872726852,3.59),
    ("Yuvraj", 18.40844523761252, 73.50826426653822,1.59),
    ("Vignesh", 18.4083230795381, 73.50776403454569,1.5),
    ("Anna Kerala", 18.408251184382486, 73.50775867012744,3),
    ("Burgerous", 18.408397519623335, 73.50792966095928,1.6),
    ("Shree Pure Veg", 18.40870227827591, 73.50806310085574,1.71),
    ("Mangalmurti", 18.408188832805724, 73.50787333457124,3.23),
    ("Rohan Soda Shop", 18.4080762181688, 73.50771709588959,2.5),
    ("Anna Dosa", 18.40797676380424, 73.50672446558784,3),
    ("Honey's Gourmet", 18.40782858445402, 73.50682801595848,2.5),
    ("American Diner", 18.407159256544432, 73.50602871766135,3),
    ("Kofta Kebab (Box 50)", 18.40624409465115, 73.5056604288122,2),
    ("Tantos", 18.404575208380617, 73.50533521096605,3.5),
    ("NJ Food Express", 18.404510946711373, 73.50540092508967,2.5),
    ("Happy Sandwich", 18.404604476063618, 73.50565238219534,2.5),
    ("Nana Ice Cream Parlour", 18.408526925226216, 73.5080476182074,3),
    ("Cafe By The Valley", 18.411602739147025, 73.50722954604615,3.5)
]


@app.route('/')
def home():
    return render_template('home.html',locations=locations)

@app.route('/developers')
def developers():
    return render_template('developers.html')

@app.route('/analysis')
def analysis():
    # Read Excel data into pandas DataFrame
    
    df = pd.read_excel('/Users/jasonseraphim/Desktop/SEM 3/Data Analytics Lab/Lavasa - project 1/data_analytics.xlsx')

    # Convert DataFrame to HTML table
    html_table = df.to_html(index=False)

    return render_template('analysis.html', html_table=html_table)



if __name__ == '__main__':
   app.run(debug=True)
