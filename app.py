from flask import Flask, request, jsonify, render_template
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_scraper', methods=['POST'])
def run_scraper():
    data = request.form
    search_term = data.get('search_term')
    run_duration = int(data.get('run_duration'))
    
    # Simulate scraping (Replace this with actual scraping logic)
    results = []
    start_time = time.time()
    while time.time() - start_time < run_duration:
        results.append({
            "name": f"Example {len(results) + 1}",
            "description": f"Description for {search_term}",
            "price": f"${len(results) * 100}",
            "year": 2022,
            "state": "Good"
        })
        time.sleep(1)  # Simulating time between results
    
    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
