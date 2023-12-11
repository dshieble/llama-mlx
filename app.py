# python /Users/danshiebler/workspace/personal/mlx-examples/llama/app.py
# Serve a model endpoint that we can access from other programs
from flask import Flask, request
import hashlib

app = Flask(__name__)

@app.route('/get_md5', methods=['GET'])
def get_md5():
  user_agent = request.headers.get('User-Agent')
  md5_hash = hashlib.md5()
  md5_hash.update(user_agent.encode('utf-8'))
  return md5_hash.hexdigest()

if __name__ == "__main__":
  app.run()