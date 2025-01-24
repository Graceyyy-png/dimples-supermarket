# from flask import*
# import pymysql
# from at_sms import*
# from mpesa import *

# app=Flask(__name__)

# connection =pymysql.connect(host='localhost',user='root',password='',database='Diamples_phylls_chatu')
# cursor = connection.cursor()

# @app.route('/')
# def home():
#     '''
#     Home route
#     '''

# @app.route('/upload',methods=['GET','POST'])
# def upload():
      
#       '''
#       Form display and upload route
#       '''
#       if request.method=='POST':
#             product_name = request.form['product_name']
#             product_desc = request.form['product_desc']
#             product_cost = request.form['product_cost']
#             product_image = request.files['product_image']
#             product_category = request.form['product_category']

#             product_image.save('static/images/'+ product_image.filename)

#             connection =  pymysql.connect (host='localhost', 
#             user='root', password='',
#             database='Diamples_phylls_chatu')

#             cursor = connection.cursor()

#             data=(product_name,product_desc,product_cost
#             ,product_image.filename,product_category)

#             sql='INSERT INTO products (product_name, product_desc,product_cost,product_image_name,product_category) values(%s,%s,%s,%s,%s)'

#             cursor.execute(sql,data)
#             connection.commit()
#             return render_template('upload.html',msg='upload successful')
#       else:
#             return render_template('upload.html')
      
      
# @app.route('/single_item/<product_id>')
# def single_item(product_id):

#       connection=pymysql.connect(host='localhost',user='root',password='',database='Diamples_phylls_chatu')  
#       cursor=connection.cursor()

#       sql = 'SELECT * FROM products WHERE product_id = %s'

#       cursor.execute(sql,product_id)
#       product=cursor.fetchone()

#       return render_template('single_item.html',product=product) 

# '''
# register route
# '''
# @app.route('/register',methods = ['GET','POST'])
# def register():
      
#    if request.method == 'GET':

#             return render_template('register.html') 
#    else:
#           username = request.form['username']
#           email = request.form['email']
#           phone = request.form['phone']
#           password = request.form['password']
#           confirm_password = request.form['confirm_password']

#           if len(password)<8:
#                 return render_template('register,html', error = 'Password must be long than 8 characters long')
#           elif password != confirm_password:
#                 return render_template('register.html', error = 'Passwords do not match')
#           else:
#             connection=pymysql.connect(host='localhost',user='root',password='',database = 'Diamples_phylls_chatu')

#             cursor=connection.cursor()
            
#             sql = 'INSERT INTO Users (username, email, phone, password) VALUES (%s, %s, %s, %s)'
#             cursor.execute(sql,(username,email,phone,password))

#             connection.commit()

#             send_sms(phone,  'Thankyou for registering')

#             return render_template('register.html', success = 'Registration successful')
          

#           '''
#           login route
#           '''

# @app.route('/login',methods=['GET', 'POST']) 
# def login ():

#       if request.method =='GET':

#        return render_template('login.html')
#       else:
#            username = request.form['username']
#            password = request.form['password']

      
#            connection=pymysql.connect(host='localhost',user='root',password= '',database= 'Diamples_phylls_chatu')

#            cursor=connection.cursor()
#            sql = 'SELECT * FROM Users WHERE username =%s AND password =%s'

#            cursor.execute(sql,(username,password))

#            if cursor.rowcount==0:
#                 return render_template('login.html',error='Invalid credentials'), 401
#            else:
#                 session['username']=username  
#                 return redirect('/') 
           
#            '''
#            logout
#            '''
# @app.route('/logout')    
# def logout ():   
#   session.clear()    
#   return redirect('/')

# '''
# mpesa route
# '''
# @app.route('/mpesa',methods=['POST'])
# def mpesa():
#      phone = request.form['phone']
#      amount = request.form['amount']

#      stk_push(phone,amount)

#      return '<h4>Complete yoou order payment and we will brgin processing your transactions ASAP! You\'ll receive your order in minutes</h4> <a href="/">Go back to Home page</a>'

     

# app.secret_key ='aab3047eb9ccfb3973f928d4ebdead9e60beb936b4d2838f7725c9cc165f0c8a'

    
# '''
# register route
# '''
# @app.route('/vendor',methods = ['GET','POST'])
# def vendor():
      
#    if request.method == 'GET':

#             return render_template('vendor.html') 
#    else:
#           firstname = request.form['firstname']
#           lastname = request.form['lastname']
#           county = request.form['county']
#           password = request.form['password']
#           confirm_password = request.form['confirm_password']
#           email=request.form['email']

#           if len(password)<8:
#                 return render_template('vendor.html', error = 'Password must be long than 8 characters long')
#           elif password != confirm_password:
#                 return render_template('vendor.html', error = 'Passwords does not mirror the latter')
#           else:
#             connection=pymysql.connect(host='localhost',user='root',password='',database = 'Diamples_phylls_chatu')

#             cursor=connection.cursor()
            
#             sql = 'INSERT INTO Vendors (firstname,lastname, county,email, password) VALUES (%s, %s, %s, %s,%s)'
#             cursor.execute(sql,(firstname,lastname,county,email,password))

#             connection.commit()


#             return render_template('vendor.html', success = 'Registration successful')
          

          
          
# app.run(debug=True)
