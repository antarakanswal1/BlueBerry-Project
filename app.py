from flask import Flask, render_template
app = Flask(__name__)   # Flask constructor 
  
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/')       
def home():
    return render_template('index.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/offers')
def offers():
    return render_template('offers.html')
    
@app.route('/products')
def products():
    return render_template('products.html')

if __name__=='__main__': 
   app.run(debug=True) 