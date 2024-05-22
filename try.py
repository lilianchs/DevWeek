import boto3
import json
import re

bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-west-2')

prompt = "What are some packages for knowledge graph embedding?"

kwargs = {
    "modelId": "anthropic.claude-3-haiku-20240307-v1:0",
    "contentType": "application/json",
    "accept": "application/json",
    "body": json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": [

                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    })
}

response = bedrock_runtime.invoke_model(**kwargs)

body = json.loads(response['body'].read())

edit_body = body['content'][0]['text']

matches = re.findall(r'\*\*(.*?)\*\*', edit_body)
new_match = ""
for match in matches:
    new_match = new_match + ", " + match
new_prompt = "Give me the github repo link to all those packages: " + new_match


new_kwargs = {
    "modelId": "anthropic.claude-3-haiku-20240307-v1:0",
    "contentType": "application/json",
    "accept": "application/json",
    "body": json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": [

                    {
                        "type": "text",
                        "text": new_prompt
                    }
                ]
            }
        ]
    })
}

new_response = bedrock_runtime.invoke_model(**new_kwargs)

new_body = json.loads(new_response['body'].read())

new_edit_body = new_body['content'][0]['text']
print(new_edit_body)


new_prompt = "Give me github links to projects that are using the packages: " + new_edit_body


new_kwargs = {
    "modelId": "anthropic.claude-3-haiku-20240307-v1:0",
    "contentType": "application/json",
    "accept": "application/json",
    "body": json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": [

                    {
                        "type": "text",
                        "text": new_prompt
                    }
                ]
            }
        ]
    })
}

new_response = bedrock_runtime.invoke_model(**new_kwargs)

new_body = json.loads(new_response['body'].read())

new_edit_body = new_body['content'][0]['text']
print(new_edit_body)
