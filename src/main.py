import time
import random,os
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

# ---- CI/CD Simulation ----
def run_tests():
    print("🔍 Running QA tests...")
    time.sleep(1)
    if random.choice([True, False]):
        print("✅ All tests passed!")
        return {"status": "success", "message": "All tests passed!"}
    else:
        print("❌ Tests failed!")
        return {"status": "failed", "message": "Some tests failed."}

def build_infrastructure():
    print("🏗️ Building infrastructure (GCP / AWS)...")
    time.sleep(1)
    print("✅ Infrastructure build successful!")
    return {"status": "success", "message": "Infrastructure build successful"}

def deploy_application():
    print("🚀 Deploying application...")
    time.sleep(1)
    print("✅ Application deployed successfully!")
    return {"status": "success", "message": "Application deployed successfully"}

def run_pipeline():
    print("=== CI/CD Pipeline Started ===")
    result_tests = run_tests()
    if result_tests["status"] == "failed":
        return {"status": "failed", "step": "tests", "message": "Pipeline stopped: Tests failed"}

    result_build = build_infrastructure()
    result_deploy = deploy_application()

    print("🎉 Pipeline completed successfully!")
    return {
        "status": "success",
        "steps": {
            "tests": result_tests,
            "build": result_build,
            "deploy": result_deploy
        }
    }

# ---- Web Application ----
app = FastAPI()
app.mount("/static", StaticFiles(directory="/app"), name="app")
templates = Jinja2Templates(directory=os.path.abspath(os.path.expanduser('templates')))

@app.get("/")
def home():
    return {"message": "🚀 CI/CD Pipeline + App Running on Port 8000"}

# API Endpoints
@app.get("/tests")
def trigger_tests():
    return run_tests()

@app.get("/build")
def trigger_build():
    return build_infrastructure()

@app.get("/deploy")
def trigger_deploy():
    return deploy_application()

@app.get("/pipeline")
def trigger_pipeline():
    return run_pipeline()

# UI Dashboard
@app.get("/ui", response_class=HTMLResponse)
def ui_dashboard(request: Request):
    # ---- Entrypoint ----
    return templates.TemplateResponse("dashboard.html", {"request": request})

if __name__ == "__main__":
    # Run pipeline first, then start the web server
    run_pipeline()
    uvicorn.run(app, host="0.0.0.0", port=8000)
