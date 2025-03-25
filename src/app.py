# Intentionally vulnerable Python code
def vulnerable_function(user_input):
    # Using eval directly without sanitizing the input
    return eval(user_input)  # This introduces a potential code injection vulnerability

# Sample usage that could lead to exploitation
input_data = "2 + 2"  # Replace with malicious input to see the impact
print("Result:", vulnerable_function(input_data))
