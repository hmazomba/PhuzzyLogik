import wikipediaapi
from flask import Flask, request, jsonify

app = Flask(__name__)
wiki = wikipediaapi.Wikipedia('en')

@app.route('/answer')
def answer_question():
    question = request.args.get('q')
    if question is None:
        return jsonify(error='Missing question'), 400
    
    page = wiki.page(question)
    if not page.exists():
        return jsonify(error='Page not found'), 404
    
    summary = page.summary[:200] + '...'
    return jsonify(answer=summary)

if __name__ == '__main__':
    app.run()
