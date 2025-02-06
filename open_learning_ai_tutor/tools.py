from langchain_core.tools import tool
from e2b_code_interpreter import Sandbox
from langchain_experimental.utilities import PythonREPL

@tool
def text_student(nessage_to_student: str):
    """A tool to send a message to your student. This tool is the only way for you to communicate with your student. The input should be your message. After the message is sent, you will wait for the student's next message."""
    return nessage_to_student

@tool
def whiteboard(query):
    """A whiteboard to show graphs to your student. The input should be valid matplotlib plot commands. refer to this tool as the 'whiteboard' and don't mention you use python"""
    whiteboard_used = True
    try:
        exec(query)
        print('\n\nWHITEBOARD UPDATED\n\n') 
        return "Whiteboard updated"
    except Exception as e:
        return str(e)
                
python_repl = PythonREPL()
@tool
def execute_python(query: str):
    """A Python shell. Use SymPy to solve complex equations. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`."""
    try:
        return python_repl.run(query)
    except Exception as e:
        return str(e)
    

sbx = Sandbox()
# if we need to import a custom dataset.
# with open("/local/file", "rb") as file:
#    # Upload file to the sandbox to path '/home/user/my-file'
# 	sbx.files.write("/home/user/my-file", file)

@tool
def R_code_interpreter(code:str):
    """A R code interpreter. Use this tool to execute R code. Input should be a valid R command. If you want to see the output of a value, you should print it out with `print(...)`"""
    return sbx.run_code(code, language = 'r' )

