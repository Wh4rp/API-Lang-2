from encode import base64_encode, base64_decode
import subprocess

def dict_status(status):
  """
  This function converts the status to a dictionary
  """
  return {
    'exit status':status.returncode,
    'result':status.stdout.decode(),
    'error':status.stderr.decode()
  }

def PythonRunner(code):
  """
  This function runs the python Code
  """

  code_decoded = base64_decode(code.code).decode('utf-8')
  input_decoded = base64_decode(code.input_source).decode('utf-8') if code.input_source else None

  with open("tmp/python.py", "w+") as f:
    f.write(code_decoded)

  status = subprocess.run(["python3", 'tmp/python.py'], input=input_decoded.encode(), capture_output=True)

  return dict_status(status)

def CppRunner(code, datain=None):
  """
  This function runs the C++ Code
  """

  code_decoded = base64_decode(code.code).decode('utf-8')
  input_decoded = base64_decode(code.input_source).decode('utf-8') if code.input_source else None
  
  with open("tmp/cpp.cpp", "w+") as f:
    f.write(code_decoded)

  status = subprocess.run(["g++", 'tmp/cpp.cpp', '-o', 'tmp/cpp.out'], capture_output=True)

  if status.returncode != 0:
    return dict_status(status)

  status = subprocess.run(["tmp/cpp.out"], input=input_decoded.encode(), capture_output=True)

  return dict_status(status)