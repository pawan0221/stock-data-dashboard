from fastapi import FastAPI
from data_processing import fetch_stock
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

companies = [
    "TCS",
    "INFY",
    "RELIANCE"
]

@app.get("/")
def home():

    return {
        "message":
        "Stock API Running"
    }


@app.get("/companies")
def get_companies():

    return companies

@app.get("/data/{symbol}")
def get_data(symbol: str):

    try:
        df = fetch_stock(symbol)

        if df.empty:
            return {"error": "No data found"}

        df = df.tail(30)

        return {
            "Date": df["Date"].astype(str).tolist(),
            "Close": df["Close"].astype(float).tolist(),
            "Volume": df["Volume"].astype(float).tolist()
        }

    except Exception as e:
        return {"error": str(e)}
        
@app.get("/summary/{symbol}")
def get_summary(symbol: str):

    try:

        df = fetch_stock(symbol)

        if df.empty:
            return {
                "error": "No data found"
            }

        high = df["High"].max()
        low = df["Low"].min()
        avg = df["Close"].mean()

        return {
            "52_week_high": float(high),
            "52_week_low": float(low),
            "average_close": float(avg)
        }

    except Exception as e:

        return {
            "error": str(e)
        }