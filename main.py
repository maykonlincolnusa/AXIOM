import subprocess
import sys

print("🚀 Starting Axiom AI System...")

# Start backend
subprocess.Popen([
    sys.executable, "-m", "uvicorn", "backend.app.main:app", "--reload"
])

# Start frontend
subprocess.Popen([
    sys.executable, "-m", "streamlit", "run", "frontend.py"
])

input("Press ENTER to stop everything...")

