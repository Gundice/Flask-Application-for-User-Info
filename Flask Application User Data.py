from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['user_data']
collection = db['users']

class User:
    def __init__(self, name, age, gender, total_income, utilities, entertainment, school_fees, shopping, healthcare):
        self.name = name
        self.age = self.convert_to_int(age)
        self.gender = gender
        self.total_income = self.convert_to_int(total_income)
        self.utilities = self.convert_to_int(utilities)
        self.entertainment = self.convert_to_int(entertainment)
        self.school_fees = self.convert_to_int(school_fees)
        self.shopping = self.convert_to_int(shopping)
        self.healthcare = self.convert_to_int(healthcare)

    def convert_to_int(self, value):
        try:
            return int(value)
        except ValueError:
            return 0  # Return 0 if conversion fails

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        total_income = request.form['total_income']
        utilities = request.form['utilities']
        entertainment = request.form['entertainment']
        school_fees = request.form['school_fees']
        shopping = request.form['shopping']
        healthcare = request.form['healthcare']
        # Create User instance
        user = User(name, age, gender, total_income, utilities, entertainment, school_fees, shopping, healthcare)
        # Insert user data into MongoDB
        collection.insert_one(user.__dict__)
        
        # Redirect to the home page after submitting data
        return render_template('index.html')
        
    # Render the home page template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)