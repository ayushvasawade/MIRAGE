from flask import Flask, render_template, request, send_file, url_for
import json
import pandas as pd
import os
from extract_engine import extract_measurements, generate_blender_instructions

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    measurements = []
    organs_detected = set()

    if request.method == 'POST':
        report = request.form['report']
        data = extract_measurements(report)

        # Save organ_dimensions.json
        with open("organ_dimensions.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        # Save blender_modeling_guide.txt
        guide = generate_blender_instructions(data)
        clean_guide = guide.encode('ascii', 'ignore').decode()
        with open("blender_modeling_guide.txt", "w", encoding="utf-8") as f:
            f.write(clean_guide)

        # Extract unique organs for QR code display
        organs_detected = {entry['Organ'].lower().replace(" ", "_") for entry in data}
        measurements = pd.DataFrame(data).to_html(classes='styled-table', index=False, border=0)

    return render_template("index.html", measurements=measurements, organs_detected=organs_detected)

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
