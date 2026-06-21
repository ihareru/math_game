import random
from flask import render_template, request, session, redirect, url_for
from app import app

@app.route('/')
def index():
    return redirect(url_for('math'))
    

@app.route('/math', methods=['GET', 'POST'])
def math():
    action_sym = ['+', '-']
    if 'correct' not in session:
        session['correct'] = 0
        session['wrong'] = 0

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'stop':
            result_data = {
                'correct': session['correct'],
                'wrong': session['wrong']
            }
            session.clear()
            return render_template('math_results.html', **result_data)

        num1 = int(request.form.get('num1'))
        num2 = int(request.form.get('num2'))
        action_math = request.form.get('action_math')
        user_answer = int(request.form.get('answer'))
        if action_math == '+':
            correct_answer = num1 + num2
        elif action_math == '-':
            correct_answer = num1 - num2

        if user_answer == correct_answer:
            session['correct'] += 1
            feedback = 'Правильно! 🎉'
            feedback_class = 'feedback correct'
        else:
            session['wrong'] += 1
            feedback = f'Неправильно. Правильный ответ: {correct_answer}'
            feedback_class = 'feedback incorrect'

            # Новый пример
        new_num1 = random.randint(1, 10)
        new_num2 = random.randint(1, 10)
        new_action_math = random.choice(action_sym)
        while True:
            if new_action_math == '-' and new_num1 < new_num2:
                new_num1 = random.randint(1, 10)
                new_num2 = random.randint(1, 10)
                new_action_math = random.choice(action_sym)
            else:
                break

        return render_template('math.html',
                            num1=new_num1,
                            num2=new_num2,
                            action_math=new_action_math,
                            feedback=feedback,
                            feedback_class=feedback_class,
                            correct=session['correct'],
                            wrong=session['wrong']
                            )
    # Первый заход
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    action_math = random.choice(action_sym)
    while True:
        if action_math == '-' and num1 < num2:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            action_math = random.choice(action_sym)
        else:
            break

    return render_template('math.html', num1=num1, num2=num2, 
                           action_math=action_math)
