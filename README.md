<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Olympics Analysis Streamlit App</title>
</head>
<body>

  <h1>🏅 Olympics Analysis Streamlit App</h1>

  <p>
    This is an interactive <b>Streamlit web application</b> that provides insights and visualizations on the <b>Olympics dataset</b>.  
    The app allows users to explore medal tallies, overall trends, country-wise performance, and athlete statistics using interactive dashboards.  
  </p>

  <hr>

  <h2>🚀 Features</h2>
  <ul>
    <li><b>Medal Tally</b>: View medals by year and country.</li>
    <li><b>Overall Analysis</b>: Explore editions, hosts, sports, events, nations, and athletes with visualizations over time.</li>
    <li><b>Country-wise Analysis</b>: Track medal tallies and top athletes for a selected country.</li>
    <li><b>Athlete-wise Analysis</b>: Explore age distributions, participation trends, and gender analysis.</li>
  </ul>

  <hr>

  <h2>📂 Project Structure</h2>
  <pre>
.
├── app.py                # Main Streamlit app
├── helper.py             # Utility functions for medal tally, top athletes, etc.
├── preprocess.py         # Data preprocessing functions
├── athlete_events.csv    # Olympics dataset (not included in repo if gitignored)
├── noc_regions.csv       # Region mapping dataset
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
  </pre>

  <hr>

  <h2>📊 Datasets</h2>
  <ul>
    <li><a href="https://www.kaggle.com/datasets/mysarahmadbhat/120-years-of-olympic-history-athletes-and-results" target="_blank">athlete_events.csv</a> – Olympics dataset with athlete information and event results.</li>
    <li>noc_regions.csv – Country/NOC region mapping dataset.</li>
  </ul>
  <p>If these files are in <code>.gitignore</code>, you’ll need to download them manually and place them in the project root.</p>

  <hr>

  <h2>🔧 Setup Instructions</h2>

  <h3>1. Clone the repository</h3>
  <pre>
git clone https://github.com/your-username/olympics-analysis.git
cd olympics-analysis
  </pre>

  <h3>2. Install dependencies</h3>
  <pre>
pip install -r requirements.txt
  </pre>

  <h3>3. Run the app locally</h3>
  <pre>
streamlit run app.py
  </pre>

  <hr>

  <h2>🌐 Deployment on Render</h2>
  <p>This app can be deployed on <a href="https://render.com" target="_blank">Render</a>.</p>

  <h3>render.yaml</h3>
  <pre>
services:
  - type: web
    name: olympics-analysis
    env: python
    plan: free
    buildCommand: "pip install -r requirements.txt"
    startCommand: "streamlit run app.py --server.port $PORT --server.address 0.0.0.0"
  </pre>

  <hr>

  <h2>📷 Preview</h2>
  <ul>
    <li><b>Sidebar</b>: App logo, title, and navigation options.</li>
    <li><b>Example Analysis</b>: Medal tallies, participating nations over years, top athletes, and gender participation trends.</li>
  </ul>

  <hr>

  <h2>🤝 Contributing</h2>
  <p>Contributions, issues, and feature requests are welcome!</p>

  <hr>

  <h2>📜 License</h2>
  <p>This project is licensed under the MIT License.</p>

</body>
</html>
