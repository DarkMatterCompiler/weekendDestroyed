from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


compurl = "https://20bf-34-143-135-145.ngrok-free.app/rag-pipeline"
classurl = "https://d127-34-87-94-123.ngrok-free.app/rag-pipeline"
temporalurl = "https://ae95-152-58-80-127.ngrok-free.app/rag_pipeline"
infurl = "https://a4b5-35-247-114-221.ngrok-free.app/rag_pipeline"


def comparison(query):
    # Send a POST request to the external API
    response = requests.post(compurl, json={"query": query})

    # Parse the response from the API
    result = response.json()
    comparison_answer = result

    return comparison_answer


def inference(query):

    # Send a POST request to the external API
    response = requests.post(infurl, json={"query": query})

    # Parse the response from the API
    result = response.json()
    comparison_answer = result

    return comparison_answer


def temporal(query):
    response = requests.post(temporalurl, json={"query": query})
    result = response.json()
    comparison_answer = result
    return comparison_answer


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit_query():
    query = request.form['query']
    response = requests.post(classurl, json={'query': query})
    result = response.json()
    typeof = result.get('final_answer', 'No type found')
    print(result)
    answer = None
    if (typeof == 'temporal_query'):
        answer = temporal(query)
    elif (typeof == 'comparison_query'):
        answer = comparison(query)
    elif (typeof == 'inference_query'):
        answer = inference(query)
    elif (typeof == 'null_query'):
        answer = inference(query)

    if (answer == None):
        return render_template('index.html')

    return render_template('index.html', query=query, answer=answer)


if __name__ == '__main__':
    app.run(debug=True)
