import boto3
import json
import os
from dotenv import load_dotenv
load_dotenv()

model_arn = os.getenv("MODEL_ARN")
region = os.getenv("REGION")
knowledge_base_id = os.getenv("KNOWLEDGE_BASE_ID")


# Initialize the Bedrock Agent Runtime client
client = boto3.client("bedrock-agent-runtime", region_name=region)

response = client.retrieve_and_generate(
    input={
        "text": "What is attention mechanism in deep learning?"
    },
    retrieveAndGenerateConfiguration={
        "type": "KNOWLEDGE_BASE",
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": knowledge_base_id,
            "modelArn": model_arn
        }
    },
    # Optional:
    # sessionId="your-session-id",
    # sessionConfiguration={"kmsKeyArn": "..."},
)

#print("==== Response from Bedrock ====")
#print(json.dumps(response, indent=2))

# Typically you’ll want just the generated text:
try:
    print("\n==== Generated Answer ====")
    print(response["output"]["text"])
except Exception as e:
    print("Could not extract output text:", e)
