# Use AWS Lambda Python 3.9 runtime as the base image
FROM public.ecr.aws/lambda/python:3.9

# Copy application files
COPY . ${LAMBDA_TASK_ROOT}

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the Lambda handler
CMD ["calculator.lambda_handler"]
