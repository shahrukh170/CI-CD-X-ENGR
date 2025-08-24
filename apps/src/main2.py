# src/main.py
import time
import random

def run_tests():
    print("🔍 Running QA tests...")
    time.sleep(1)
    # simulate test result
    if random.choice([True, False]):
        print("✅ All tests passed!")
    else:
        print("❌ Tests failed!")
        exit(1)

def build_infrastructure():
    print("🏗️ Building infrastructure (GCP / AWS)...")
    time.sleep(1)
    print("✅ Infrastructure build successful!")

def deploy_application():
    print("🚀 Deploying application...")
    time.sleep(1)
    print("✅ Application deployed successfully!")

def main():
    print("=== CI/CD Pipeline Started ===")
    print("🚀 Starting CI/CD pipeline automation...")

    # Example placeholder steps
    print("1. Running tests...")
    run_tests()
    print("2. Building Docker image...")
    build_infrastructure()
    print("3. Deploying to GCP/AWS...")
    deploy_application()

    print("🎉 Pipeline completed successfully!")

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
