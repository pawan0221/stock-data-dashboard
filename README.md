# stock-data-dashboard

# Stock Data Intelligence Dashboard

## 📌 Project Overview

The **Stock Data Intelligence Dashboard** is a full-stack application that collects stock market data, processes it, and displays insights through REST APIs and an interactive dashboard.

This project demonstrates backend development, data processing, API integration, and frontend visualization — key skills required for software engineering and data engineering roles.

The system fetches real-time stock data, calculates useful metrics, and visualizes the information in a user-friendly dashboard.

---

## 🚀 Features

* Fetch real-time stock data using **yfinance**
* Clean and process data using **pandas**
* RESTful APIs built with **FastAPI**
* Interactive dashboard with charts
* CORS-enabled frontend-backend integration
* Moving average and volatility calculations
* Company selection dropdown
* Real-time data visualization

---

## 🛠️ Technologies Used

### Backend

* Python
* FastAPI
* Pandas
* NumPy
* yfinance

### Frontend

* HTML
* CSS
* JavaScript
* Chart.js

### Tools

* Git
* GitHub
* VS Code

---

## 📂 Project Structure

```
StockDashboard/
│
├── main.py                 # FastAPI backend server
├── data_processing.py      # Data fetching and processing logic
├── dashboard.html          # Frontend dashboard UI
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── venv/                   # Virtual environment
```

---

## ⚙️ Installation and Setup

### Step 1 — Clone the Repository

```
git clone https://github.com/pawan0221/stock-data-dashboard.git
cd stock-data-dashboard
```

### Step 2 — Create Virtual Environment

```
python -m venv venv
```

Activate environment:

Windows:

```
venv\Scripts\activate
```

---

### Step 3 — Install Dependencies

```
pip install -r requirements.txt
```

---

### Step 4 — Run the Server

```
python -m uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

### Step 5 — Open Dashboard

Open:

```
dashboard.html
```

Or run using Live Server.

---

## 🔌 API Endpoints

### Get List of Companies

```
GET /companies
```

Example Response:

```
["TCS", "INFY", "RELIANCE"]
```

---

### Get Stock Data

```
GET /data/{symbol}
```

Example:

```
GET /data/TCS
```

Response:

```
{
  "Date": [...],
  "Close": [...],
  "Volume": [...]
}
```

---

### Get Stock Summary

```
GET /summary/{symbol}
```

Returns:

* 52-week high
* 52-week low
* Average closing price

---

## 📊 Data Processing

The system performs:

* Missing value handling
* Moving average calculation
* Volatility calculation
* Data cleaning
* Data formatting for visualization

---

## 📈 Dashboard Features

* Stock price line chart
* Volume bar chart
* Company selection dropdown
* Real-time data updates
* Responsive layout
* Error handling

---

## 🔮 Future Improvements

* Deploy backend to cloud
* Add stock comparison feature
* Add authentication
* Add prediction using machine learning
* Add export to CSV
* Add Docker support

---

## 📷 Screenshots

Add screenshot here after running the dashboard.

Example:

```
Dashboard showing stock price and volume charts
```

---

## 👨‍💻 Author

**Pawan Soni**
B.Tech — Computer Science and Engineering

Skills:

* Java
* Python
* FastAPI
* Web Development
* Data Analysis
* APIs
* Git and GitHub

---

## 📄 License

This project is developed for educational and internship demonstration purposes.
