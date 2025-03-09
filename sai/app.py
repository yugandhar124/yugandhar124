from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# Store polls in a dictionary
polls = {}

@app.route('/')
def index():
    return render_template('index.html', polls=polls)

@app.route('/create_poll', methods=['GET', 'POST'])
def create_poll():
    if request.method == 'POST':
        poll_question = request.form['question']
        options = request.form.getlist('options')
        poll_id = len(polls) + 1
        polls[poll_id] = {'question': poll_question, 'options': options, 'votes': [0] * len(options)}
        return redirect(url_for('index'))
    return render_template('create_poll.html')

@app.route('/poll/<int:poll_id>', methods=['GET', 'POST'])
def poll(poll_id):
    poll = polls[poll_id]
    options_with_indices = list(enumerate(poll['options']))
    if request.method == 'POST':
        selected_option = int(request.form['option'])
        poll['votes'][selected_option] += 1
        return redirect(url_for('poll', poll_id=poll_id))
    return render_template('poll.html', poll=poll, poll_id=poll_id, options_with_indices=options_with_indices)


if __name__ == '__main__':
    app.run(debug=True)
