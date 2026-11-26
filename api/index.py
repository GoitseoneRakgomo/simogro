import os
import sys

# Make the project root importable when running as a Vercel function.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app  # noqa: E402,F401
