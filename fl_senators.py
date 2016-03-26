from flask import Flask, render_template
app = Flask(__name__)

senators = [{"fname":"Joseph","lname":"Abruzzo","district":25,"party":"D","county":"Part Of Palm Beach County"},
{"fname":"Thad","lname":"Altman","district":16,"party":"R","county":"Parts Of Brevard, Indian River Counties"},
{"fname":"Aaron","lname":"Bean","district":4,"party":"R","county":"Nassau County And Part Of Duval County"},
{"fname":"Lizbeth","lname":"Benacquisto","district":30,"party":"R","county":"Parts Of Charlotte, Lee Counties"},
{"fname":"Rob","lname":"Bradley","district":7,"party":"R","county":"Alachua, Bradford, Clay Counties"},
{"fname":"Jeff","lname":"Brandes","district":22,"party":"R","county":"Parts Of Hillsborough, Pinellas Counties"},
{"fname":"Oscar","lname":"Braynon","district":36,"party":"D","county":"Parts Of Broward, Miami-Dade Counties"},
{"fname":"Dwight","lname":"Bullard","district":39,"party":"D","county":"Hendry, Monroe Counties And Parts Of Collier, Miami-Dade Counties"},
{"fname":"Jeff","lname":"Clemens","district":27,"party":"D","county":"Part Of Palm Beach County"},
{"fname":"Charles S. 'Charlie'","lname":"Dean","district":5,"party":"R","county":"Baker, Citrus, Columbia, Dixie, Gilchrist, Lafayette, Levy, Suwannee, Union Counties And Part Of Marion County"},
{"fname":"Nancy C.","lname":"Detert","district":28,"party":"R","county":"Sarasota County And Part Of Charlotte County"},
{"fname":"Miguel","lname":"Diaz de la Portilla","district":40,"party":"R","county":"Part Of Miami-Dade County"},
{"fname":"Greg","lname":"Evers","district":2,"party":"R","county":"Escambia, Santa Rosa Counties And Part Of Okaloosa County"},
{"fname":"Anitere","lname":"Flores","district":37,"party":"R","county":"Part Of Miami-Dade County"},
{"fname":"Don","lname":"Gaetz","district":1,"party":"R","county":"Bay, Holmes, Jackson, Walton, Washington Counties And Part Of Okaloosa County"},
{"fname":"Bill","lname":"Galvano","district":26,"party":"R","county":"Desoto, Glades, Hardee Counties And Parts Of Charlotte, Highlands, Hillsborough, Manatee Counties"},
{"fname":"Rene","lname":"Garcia","district":38,"party":"R","county":"Part Of Miami-Dade County"},
{"fname":"Andy","lname":"Gardiner","district":13,"party":"R","county":"Parts Of Brevard, Orange Counties"},
{"fname":"Audrey","lname":"Gibson","district":9,"party":"D","county":"Part Of Duval County"},
{"fname":"Denise","lname":"Grimsley","district":21,"party":"R","county":"Okeechobee County And Parts Of Highlands, Martin, Osceola, Polk, St. Lucie Counties"},
{"fname":"Alan","lname":"Hays","district":11,"party":"R","county":"Parts Of Lake, Marion, Orange, Sumter Counties"},
{"fname":"Dorothy L.","lname":"Hukill","district":8,"party":"R","county":"Parts Of Lake, Marion, Volusia Counties"},
{"fname":"Travis","lname":"Hutson","district":6,"party":"R","county":"Flagler, Putnam, St. Johns Counties And Part Of Volusia County"},
{"fname":"Arthenia L.","lname":"Joyner","district":19,"party":"D","county":"Parts Of Hillsborough, Manatee, Pinellas Counties"},
{"fname":"Jack","lname":"Latvala","district":20,"party":"R","county":"Part Of Pinellas County"},
{"fname":"Tom","lname":"Lee","district":24,"party":"R","county":"Part Of Hillsborough County"},
{"fname":"John","lname":"Legg","district":17,"party":"R","county":"Parts Of Hillsborough, Pasco Counties"},
{"fname":"Gwen","lname":"Margolis","district":35,"party":"D","county":"Part Of Miami-Dade County"},
{"fname":"Bill","lname":"Montford","district":3,"party":"D","county":"Calhoun, Franklin, Gadsden, Gulf, Hamilton, Jefferson, Leon, Liberty, Madison, Taylor, Wakulla Counties"},
{"fname":"Joe","lname":"Negron","district":32,"party":"R","county":"Parts Of Indian River, Martin, Palm Beach, St. Lucie Counties"},
{"fname":"Garrett","lname":"Richter","district":23,"party":"R","county":"Parts Of Collier, Lee Counties"},
{"fname":"Jeremy","lname":"Ring","district":29,"party":"D","county":"Part Of Broward County"},
{"fname":"Maria Lorts","lname":"Sachs","district":34,"party":"D","county":"Parts Of Broward, Palm Beach Counties"},
{"fname":"David","lname":"Simmons","district":10,"party":"R","county":"Seminole County And Part Of Volusia County"},
{"fname":"Wilton","lname":"Simpson","district":18,"party":"R","county":"Hernando County And Parts Of Pasco, Sumter Counties"},
{"fname":"Christopher L.","lname":"Smith","district":31,"party":"D","county":"Part Of Broward County"},
{"fname":"Eleanor","lname":"Sobel","district":33,"party":"D","county":"Part Of Broward County"},
{"fname":"Darren","lname":"Soto","district":14,"party":"D","county":"Parts Of Orange, Osceola, Polk Counties"},
{"fname":"Kelli","lname":"Stargel","district":15,"party":"R","county":"Parts Of Orange, Osceola, Polk Counties"},
{"fname":"Geraldine F. 'Geri'","lname":"Thompson","district":12,"party":"D","county":"Part Of Orange County"}];

def returnSenatorIndex(lname):
    i = 0;
    for senator in senators:
        if senator['lname'] == lname:
            return i
        else:
            i += 1    
    return -1

@app.route('/')
def index():
    return render_template('index.html', senators=senators)

@app.route('/senators/')
def senatorHome():
    return render_template('index.html', senators=senators)

@app.route('/senators/<lname>')
def senator(lname):
    senator = senators[returnSenatorIndex(lname)]
    return render_template('senator.html', senator=senator)

if __name__ == '__main__':
    app.run(debug=True)