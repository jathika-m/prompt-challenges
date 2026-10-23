"""
CelebrAI - Application Runner
Starts the CelebrAI server using environment variables for cloud deployment,
with fallback defaults for local development.
"""
import os
import uvicorn

if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8000))
    reload = os.environ.get("RELOAD", "false").lower() in ("true", "1", "yes") or os.environ.get("ENV") == "development"

    print("=" * 60)
    print("  CelebrAI — Your Personal AI Event Planner")
    print(f"  Server launching on: http://{host}:{port}")
    print("  Demo Account: alexa.celebrate@example.com / CelebrAI2026!")
    print("=" * 60)
    uvicorn.run("app.main:app", host=host, port=port, reload=reload)
