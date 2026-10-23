"""
CelebrAI - Application Runner
Starts the CelebrAI Uvicorn server on http://127.0.0.1:8000
"""
import uvicorn

if __name__ == "__main__":
    print("=" * 60)
    print("  CelebrAI — Your Personal AI Event Planner")
    print("  Server launching on: http://127.0.0.1:8000")
    print("  Demo Account: alexa.celebrate@example.com / CelebrAI2026!")
    print("=" * 60)
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
