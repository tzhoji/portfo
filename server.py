from flask import Flask, render_template, url_for,request,redirect
import csv
app = Flask (__name__)
print (__name__)

@app.route ('/')
def my_home():
    # print (url_for ('./static/assets', filename='favicon.ico'))
    return render_template('/index.html')


@app.route ('/about.html')
def about():
    return render_template('about.html')


@app.route ('/works.html')
def works():
    return render_template('works.html')

@app.route ('/contact.html')
def contact():
    return render_template('contact.html')

@app.route ('/components.html')
def components():
    return render_template('components.html')

@app.route ('/work.html')
def work():
    return render_template('work.html')

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open ('database.csv', newline='',mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2,delimiter=',',quotechar=',',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route ('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        try:
            data=request.form.to_dict()
            #print(data)
            write_to_csv(data)
            return redirect('./thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something goes wrong.Try again!'

    #error = None
    #if request.method == 'POST':
        #if valid_login(request.form['username'],
                      # request.form['password']):
           # return log_the_user_in(request.form['username'])
        #else:
            #error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    #return render_template('login.html', error=error)