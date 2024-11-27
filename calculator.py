def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def lambda_handler(event, context):

    operation = event.get("operation")
    a = event.get("a")
    b = event.get("b")


    if operation is None or a is None or b is None:
        return {
            "statusCode": 400,
            "body": "Error: Missing required parameters. Please provide 'operation', 'a', and 'b'."
        }

    try:
        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        else:
            return {
                "statusCode": 400,
                "body": f"Error: Unsupported operation '{operation}'. Supported operations are 'add', 'subtract', and 'multiply'."
            }

        return {
            "statusCode": 200,
            "body": {
                "operation": operation,
                "a": a,
                "b": b,
                "result": result
            }
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
