# src/main.py
import time
import random
from fastapi import FastAPI
import uvicorn

# ---- CI/CD Simulation ----
def run_tests():
    print("🔍 Running QA tests...")
    time.sleep(1)
    if random.choice([True, False]):
        print("✅ All tests passed!")
    else:
        print("❌ Tests failed!")
        #exit(1)

def build_infrastructure():
    print("🏗️ Building infrastructure (GCP / AWS)...")
    time.sleep(1)
    print("✅ Infrastructure build successful!")

def deploy_application():
    print("🚀 Deploying application...")
    time.sleep(1)
    print("✅ Application deployed successfully!")

def run_pipeline():
    print("=== CI/CD Pipeline Started ===")
    run_tests()
    build_infrastructure()
    deploy_application()
    print("🎉 Pipeline completed successfully!")

# ---- Web Application ----
app = FastAPI()

@app.get("/")
def home():
    return {"message": "🚀 CI/CD Pipeline + App Running on Port 8000"}

# ---- Entrypoint ----
if __name__ == "__main__":
    run_pipeline()
    uvicorn.run(app, host="0.0.0.0", port=8000)
