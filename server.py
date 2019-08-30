# Help the squidlet become a full-fledge squid by
# guiding the squid to all the lost gear and ultimately 
# his dream motorcylcle. :)
# List of things [helmet, gloves, boots, jacket, jeans, money, motorcycle]

from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'SECRET'

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/proccess_item', methods=['POST'])
def addGear():
    
    if request.form['building'] == 'helmet':
        act1 = 'You found a helmet!'
        print(act1)
        session['helmet'] = 'Helmet'
        session['activity1'] = act1
        return redirect('/')

    elif request.form['building'] == 'gloves':
        act2 = 'You found some gloves!'
        print(act2)
        session['gloves'] = 'Gloves'
        session['activity2'] = act2
        return redirect('/')

    elif request.form['building'] == 'boots':
        act3 = 'You found some boots!'
        print(act3)
        session['boots'] = 'Boots'
        session['activity3'] = act3
        return redirect('/')

    elif request.form['building'] == 'jacket':
        act4 = 'You found a sweet jacket!'
        print(act4)
        session['jacket'] = 'Jacket'
        session['activity1'] = act4
        return redirect('/')

    elif request.form['building'] == 'jeans':
        act5 = 'You found a pair of armored jeans!'
        print(act5)
        session['jeans'] = 'Jeans'
        session['activity2'] = act5
        return redirect('/')

    elif request.form['building'] == 'money':
        print('You are about to withdraw 10 dollars!')
        act6 = 'You withdrew $10'
        if 'money' in session:
            session['money'] += 10
            print(act6)
            session['activity3'] = act6
        else:
            session['money'] = 10
            print(act6)
            session['activity3'] = act6
        return redirect('/')
    elif request.form['building'] == 'bet':
        print('Good Luck')
        if 'money' in session:
            act7 = 'Oops you lost'
            randNum = random.randint(-1000,1000)
            if randNum < 0:
                print(act7, randNum)
                session['activity1'] = act7, randNum
            else:
                print('YAY you won $', randNum)
                session['activity2'] = act7, randNum

            session['money'] += randNum
        else:
            print('You must have money to bet first.')
        return redirect('/')
    elif request.form['building'] == 'mowty':
        print('this is where you buy a motorcycle!')
        if 'jeans' in session and 'jacket' in session and 'boots' in session and 'gloves' in session and 'helmet' in session:
            print('all the junk is in')
            if session['jeans'] == 'Jeans' and session['jacket'] == 'Jacket' and session['boots'] == 'Boots' and session['gloves'] == 'Gloves' and session['helmet'] == 'Helmet':
                print('IT WORKED!')
                if 'money' in session:
                    if session['money'] > 5000:
                        print('You earned a mowty!')
                        session['mowty'] = 'Suzuki SV650'
                        session['money'] -= 5000
                        return redirect('/')
                    else:
                        print('You cannot affort this yet')
                        return redirect('/')
                else:
                    print('you dont have any Money!')
                    return redirect('/')
            else:
                print('You do not have all your gear')
                return redirect('/')
        else:
            print('not all the things are in')
            return redirect('/')
app.run(debug=True)