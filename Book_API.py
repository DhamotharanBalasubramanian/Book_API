from flask import Flask, render_template


# Create a Flask Inastance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

#def index():
#	return "<h1>Book API</h1>"



def insdex():
	first_name = "Dhamu"
	stuff = "For <strong> Ignitesol </strong>"
	Filter = ["Book ID", "Language", "Mime-type", "Author", "Title"]
	return render_template("index.html", 
		first_name=first_name,
		stuff=stuff,
		Filter=Filter)

# localhost:5000/user/Dhamotharan
@app.route('/user/<name>')

def user(name):
	return render_template("users.html", user_name=name)

	# Create Custom Error Pages

	# Invalid URL
def page_not_found(e):
	return render_template("404.html"), 404

	# Internal Server Error
	@app.errorhandler(500)
	def page_not_found(e):
		return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(debug=True) 