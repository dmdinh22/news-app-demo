from flask import Flask
from flask import render_template
from flask import abort
import csv

app = Flask(__name__)

def get_csv():
    csv_path = './static/la-riots-deaths.csv'
    csv_file = open(csv_path, 'rb') # open csv file from path
    csv_obj = csv.DictReader(csv_file) #parse as dictionary obj
    csv_list = list(csv_obj) #convert to list to not lose objects once used
    return csv_list

#method to return index
@app.route("/")
def index():
    template = 'index.html'
    object_list = get_csv() # pull csv data into index
    return render_template(template, object_list=object_list) #pass into template

# route to each individual id from csv to open detailed page
@app.route('/<row_id>/')
def detail(row_id):
    template = 'detail.html'
    object_list = get_csv() # pull csv data into detail function
    for row in object_list: #iterate over every row
        if row['id'] == row_id: # if row matches the id from uri
            return render_template(template, object=row) #return matching obj
    abort(404)

if __name__ == '__main__':
    # fire up flask server
    app.run(debug=True, use_reloader=True)