<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Smart House Generator & Location Validator</title>
  <style>
    body {
      font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
      line-height: 1.6;
      padding: 2rem;
      max-width: 960px;
      margin: auto;
      background: #fdfdfd;
      color: #333;
    }
    h1, h2, h3 {
      color: #2c3e50;
    }
    code, pre {
      background: #f4f4f4;
      padding: 1rem;
      display: block;
      overflow-x: auto;
      border-left: 4px solid #3498db;
      margin: 1rem 0;
      border-radius: 5px;
    }
    a {
      color: #2980b9;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    ul {
      padding-left: 1.2rem;
    }
    .file-structure {
      background: #f9f9f9;
      padding: 1rem;
      border-left: 5px solid #8e44ad;
      font-family: monospace;
      white-space: pre;
      margin: 1rem 0;
    }
  </style>
</head>
<body>

  <h1>🏠 Smart House Generator & Location Validator</h1>
  <p>A Python-powered project using <strong>Blender</strong> for 3D house modeling and <strong>PyTorch</strong> for validating construction locations.</p>

  <h2>📌 Why This Project?</h2>
  <p>
    Urban planning involves both design and location analysis. This tool helps:
    <ul>
      <li>Create customizable 3D house layouts using Blender</li>
      <li>Validate geolocations for construction using AI</li>
    </ul>
  </p>

  <h2>📦 Features</h2>
  <ul>
    <li><strong>3D House Generator</strong>: Custom rooms and floors via CLI</li>
    <li><strong>Location Validator</strong>: Predicts suitability and offers alternatives</li>
  </ul>

  <h2>🏗️ Architecture Overview</h2>
  <pre>
User Input
   │
   ├──► generate_house.py ─────► Blender Engine ─────► Rendered Output (PNG)
   │
   └──► location_model.py ─────► Trained PyTorch Model ─────► Prediction + Suggestions
  </pre>

  <h2>🔧 Installation</h2>
  <h3>Python Dependencies</h3>
  <pre><code>pip install -r requirements.txt
pip install torch</code></pre>

  <h3>Blender</h3>
  <p>Install from: <a href="https://www.blender.org/download/" target="_blank">https://www.blender.org/download/</a></p>

  <h2>🚀 Usage</h2>

  <h3>🏡 House Generation (Blender)</h3>
  <pre><code>blender --background --python generate_house.py -- &lt;rooms&gt; &lt;floors&gt; &lt;output_path&gt;</code></pre>

  <p>Example:</p>
  <pre><code>blender --background --python generate_house.py -- 3 2 output.png</code></pre>

  <h3>🌐 Location Validation</h3>
  <pre><code>from location_model import validate_location

location = "12.9716,77.5946"
is_valid, suggestions = validate_location(location)

if is_valid:
    print("Location is suitable.")
else:
    print("Try these alternatives:", suggestions)</code></pre>

  <h2>🧪 Testing</h2>
  <p>Run in Python shell:</p>
  <pre><code>from location_model import validate_location
validate_location("28.6139,77.2090")</code></pre>

  <h2>📷 Screenshots</h2>
  <p>*(Add screenshots of rendered houses or terminal outputs here)*</p>

  <h2>📁 File Structure</h2>
  <div class="file-structure">
.
├── generate_house.py        # Blender-based house generator
├── location_model.py        # PyTorch model for location validation
├── location_model.pth       # Trained weights
├── requirements.txt         # Dependencies
├── README.html              # Documentation
  </div>

  <h2>🛣️ Roadmap</h2>
  <ul>
    <li>[x] CLI-based house generation</li>
    <li>[x] AI-based location validation</li>
    <li>[ ] Web UI for rendering preview</li>
    <li>[ ] Export .blend or .obj files</li>
    <li>[ ] REST API deployment</li>
  </ul>

  <h2>🤝 Contributing</h2>
  <ol>
    <li>Fork the repo</li>
    <li>Create a new feature branch</li>
    <li>Submit a pull request</li>
    <li>Use clear comments & follow PEP8</li>
  </ol>

  <h2>🙋‍♂️ Author</h2>
  <p><strong>Dharwin S</strong> – Full Stack Developer<br>
    📫 <a href="https://linkedin.com/in/dharwin-s" target="_blank">LinkedIn Profile</a>
  </p>

  <h2>📜 License</h2>
  <p>MIT License. Free to use with credit.</p>

</body>
</html>
