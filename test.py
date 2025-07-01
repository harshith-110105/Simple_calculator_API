from flask import Flask , request 

app = Flask(__name__)

@app.route("/" , methods = ["GET","POST"])
def calculator ():
    result = ''
    error = ''

    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1"))
            num2 = float(request.form.get("num2"))
            operation = request.form["operation"]

            if operation == "add":
                result = num1+num2

            elif operation == "subtract":
                result = num1 - num2

            elif operation == "multiply":
                result = num1 * num2

            elif operation == "divide":
                if num2 == 0:
                    error = "cannot divide with zero"
                else:
                    result = num1/num2

            else:
                error = "invalid operation"

        except:
            error = "please enter valid numbers" 

    return f'''
        <!DOCTYPE html> 
<html lang="en"> 
<head> 
    <meta charset="UTF-8"> 
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <title>calculator</title> 
</head> 
<body> 
   <h2>SIMPLE CALCULATOR</h2>
   <form method="post">
      number1: <input type="text" name="num1" required>
      <br>
      number2: <input type="text" name="num2" required>
      <br>
      operation:
      <select name="operation">
         <option value="add">ADD</option>
         <option value="subtract">SUBTRACT</option>
         <option value="multiply">MULTIPLY</option>
         <option value="divide">DIVIDE</option>
      </select><br>
      <button style="color: blue;" type="submit">CALCULATE</button>
   </form>
   <br>
   <h3>{'Result:' + '' + str(result) if result != ' ' else ' '}</h3>
   <h3 style="color: red;">{error}</h3>
</body> 
</html> 
    '''
if __name__ == "__main__":
    app.run(debug=True)


        
    