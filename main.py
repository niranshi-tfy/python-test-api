# from fastapi import FastAPI
# import asyncio
# import os
# import dotenv
# import clickhouse_connect
# import openai
# from random import randint
# import datetime

# app = FastAPI()


# client = clickhouse_connect.get_client(host='q8e06zc0cb.ap-south-1.aws.clickhouse.cloud', secure=True, port=8443, user='default', password='YlmjThZARWZ.0', database="models")
# # client.command('''
# #                CREATE TABLE logs (id UInt16, model_name String, time DateTime, input_tokens UInt16) ENGINE MergeTree() 
# #                ORDER BY (id)
# #                PRIMARY KEY (id)
# #                ''')
# resp = client.command('SHOW TABLE logs')
# print(resp)

# dotenv.load_dotenv(".env")
# @app.post("/")
# async def infer(model):
#     # openai.api_key = "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"
#     # completion = openai.ChatCompletion.create(
#     # model=model,
#     # messages=[
#     #     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     #     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#     # ]
#     # )
#     num = randint(1000, 9999)
#     num1 = randint(100,999)
#     date = datetime.datetime.now()
#     data = [num, model, date, num1]
#     print(data)
#     client.insert(table='logs', data=[data], column_names="*")
#     # return completion.choices[0].message



# import requests

# response = requests.post(
#     "http://localhost:5002/api/inference/chat",
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImd0eSI6WyJhdXRob3JpemF0aW9uX2NvZGUiXSwia2lkIjoibHNXSUM1a2RTVXVteDVySDk2RHpsV1hQbElNIn0.eyJhdWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJleHAiOjE3MDE3NTY5NTYsImlhdCI6MTcwMTE1MjE1NiwiaXNzIjoidHJ1ZWZvdW5kcnkuY29tIiwic3ViIjoiMWVmNGFlMWUtZDE2OC00Y2Q3LWJkNzMtODlmZWU1NmVjYzM3IiwianRpIjoiZWI2Y2Y0OTUtNGU0Yi00ZTJlLWFhNjMtYWZlNjlhNDc2N2U1IiwiYXV0aGVudGljYXRpb25UeXBlIjoiR09PR0xFIiwiZW1haWwiOiJuaXJhbnNoaUB0cnVlZm91bmRyeS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoibmlyYW5zaGkiLCJhcHBsaWNhdGlvbklkIjoiODk1MjUzYWYtZWM5ZC00YmU2LTgzZDEtNmYyNDhlNjQ0ZTc5Iiwic2NvcGUiOiJvcGVuaWQgb2ZmbGluZV9hY2Nlc3MiLCJyb2xlcyI6WyJ0ZW5hbnQtYWRtaW4iXSwic2lkIjoiNmQ3NzhmMjQtY2JmNC00YWY3LTgyMWQtZDIxM2MxZDNkNzEwIiwiYXV0aF90aW1lIjoxNzAxMTUyMTU2LCJ0aWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJtZW1iZXJzaGlwcyI6W10sInRlbmFudE5hbWUiOiJ0cnVlZm91bmRyeSIsInVzZXJUeXBlIjoidXNlciIsInVzZXJuYW1lIjoibmlyYW5zaGkifQ.GZg7z1gm30c3Lx-VRn-aMbe2tTpGv-ozOR1Z8kOSF7mrwZboqvdJ7ggkZoRj-kb77LZ2mRRLP0__Hh0UqsH2-_sSpz5n7wUmjCgtowJpHe4UH8QgT--VwTjUBGxisnbhxTTdokkjQnF3FrWzy22k2MQyYuQqNzueJho6E2bd10R7QIpk0t_BYywcSInuJSWdb2SPUEr70q8ah0n4t3arWCsr-jMsmF6LcSc7115HkHxwfJFzsbr21w8FUGWiOgcQEWI9oSIh8YypIbmhHLAriBHDxssJePyF3V2gaD3Wv7sc1GOCTcWmyK5AJ7TsXwzhUK3Sux-SWH2Zcf6XdF1i0w",
#     },
#     json = {
#         "messages": [
#             {"role": "system", "content": "You are an AI bot."},
#             {"role": "user", "content":"Enter your prompt here"}
#         ],
#         "model":
#             {
#                 "name": "truefoundry-public/CodeLlama-Instruct(34B)",
#                 "parameters":
#                 {
#                     "temperature": 0.7,
#                     "maximum_length": 500,
#                     "top_p": 0.95,
#                     "top_k": 50,
#                     "repetition_penalty": 1.2,
#                     "stop_sequences": [
#                         "</s>"
#                     ]
#                 }
#             }
#     }
# )
# print(response)
# data = response.json()
# print(data)
# text = data.get('text')
# print(text)



# import requests

# response = requests.post(
#     "https://llm-gateway.truefoundry.com/api/inference/chat",
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImd0eSI6WyJhdXRob3JpemF0aW9uX2NvZGUiXSwia2lkIjoiaE9PejV4NkhPVUdYa2FudnlKMVNudGIyS0tvIn0.eyJhdWQiOiJmODBiOTFlMC0yYWM4LTRiMDMtOGUwYi1lODhlNzg0NGZkMTEiLCJleHAiOjE3MDE3MTAyMzgsImlhdCI6MTcwMTEwNTQzOCwiaXNzIjoidHJ1ZWZvdW5kcnkuY29tIiwic3ViIjoiYzQ3OWVhZjgtMzNlNi00OWViLWI4M2ItYWMyMmNjMDU4MjkzIiwianRpIjoiMDcxNDMwNmUtMGE5Zi00YTY2LTk3OTAtNDViNzhhYWEyNTRhIiwiYXV0aGVudGljYXRpb25UeXBlIjoiUElORyIsImVtYWlsIjoibmlyYW5zaGlAdHJ1ZWZvdW5kcnkuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInByZWZlcnJlZF91c2VybmFtZSI6Im5pcmFuc2hpLXRmeSIsImFwcGxpY2F0aW9uSWQiOiJmODBiOTFlMC0yYWM4LTRiMDMtOGUwYi1lODhlNzg0NGZkMTEiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyIsInJvbGVzIjpbXSwic2lkIjoiOTJjZGUyYTEtY2I2NS00NWJjLWI0NDAtNzVmNjEyNzEzNjI2IiwiYXV0aF90aW1lIjoxNzAxMTA1NDM4LCJ0aWQiOiJmODBiOTFlMC0yYWM4LTRiMDMtOGUwYi1lODhlNzg0NGZkMTEiLCJtZW1iZXJzaGlwcyI6W10sInRlbmFudE5hbWUiOiJ0cnVlZm91bmRyeSIsInVzZXJUeXBlIjoidXNlciIsInVzZXJuYW1lIjoibmlyYW5zaGktdGZ5In0.Ovv4IgEN7RSLqBSnGGP4F7CQY1oBoMYhH-NFr4ky38IbHhpfybrud_8M0uEsNtErgGOFiK_6Y2eQcvlRGeNa1ld_42LZYZBlCI4UCf5Za2hCh2v3-HhSzZDhOius1mQu5wBYk-c2_1fk2lZle2gaVsUix48_CsEsLyoMmKY4fnc6HoDXb3FCNWi_4E_3za7EMR51e_do2JLqgU7Z1Bu9rxg0pcYcXVx1DCwrVu2kpfNxZ3bHnJDVLUIQIhoXGcJOiGAqWiz-vSl512cCRyXPfZ_gkaVY6vIyediy3fwJngqOlY-SmN3YtIFnC5TMdLOQJM9P_FSf2zGiubUQYv-SKw",
#     },
#     json = {
#         "messages": [
#             {"role": "system", "content": "You are an AI bot."},
#             {"role": "user", "content":"Enter your prompt here"}
#         ],
#         "model":
#             {
#                 "name": "open-ai-account/gpt-3-5-turbo",
#                 "parameters":
#                 {
#                     "temperature": 0.5,
#                     "maximum_length": 200,
#                     "top_p": 1.0,
#                     "presence_penalty": 0.0,
#                     "frequency_penalty": 0.0
#                 }
#             }
#     }
# )
# data = response.json()
# text = data.get('text')
# print(text)


# import requests
# import sseclient
# import json 
# endpoint = 'https://api.together.xyz/v1/completions'
# response = requests.post(endpoint, json={
#     "model": "togethercomputer/CodeLlama-34b-Instruct",
#     "max_tokens": 512,
#     "prompt": "[INST] HIIII [/INST]",
#     "request_type": "language-model-inference",
#     "temperature": 0.7,
#     "top_p": 0.7,
#     "top_k": 50,
#     "repetition_penalty": 1,
#     "stop": [
#         "?",
#         "I",
#         "</s>",
#         "[INST]"
#     ],
#     "negative_prompt": "",
#     "sessionKey": "353f87d3a237d33a540803f82328af73bc0e243f",
#     "stream": True
# }, headers={
#     "Authorization": "Bearer cab10756f89a0d074d013fd4c3af1a003eb1e492edb782cedd6949be4ce1fe54",
# }, stream=True)

# # response = requests.post(url, json=payload, headers=headers, stream=True)
# response.raise_for_status()

# client = sseclient.SSEClient(response)
# for event in client.events():
#     if event.data == "[DONE]":
#         break

#     partial_result = json.loads(event.data)
#     token = partial_result["choices"][0]["text"]
#     print(token, end="", flush=True)     


# import json
# import os

# import requests
# import sseclient

# url = "https://api.together.xyz/inference"
# model = "togethercomputer/RedPajama-INCITE-7B-Chat"
# prompt = "Tell me a story\n\n"

# print(f"Model: {model}")
# print(f"Prompt: {repr(prompt)}")
# print("Repsonse:")
# print()

# payload = {
#     "model": model,
#     "prompt": prompt,
#     "max_tokens": 512,
#     "temperature": 0.7,
#     "top_p": 0.7,
#     "top_k": 50,
#     "repetition_penalty": 1,
#     "stream_tokens": True,
# }
# headers = {
#     "accept": "application/json",
#     "content-type": "application/json",
#     "Authorization": f"Bearer cab10756f89a0d074d013fd4c3af1a003eb1e492edb782cedd6949be4ce1fe54",
# }

# response = requests.post(url, json=payload, headers=headers, stream=True)
# response.raise_for_status()

# client = sseclient.SSEClient(response)
# for event in client.events():
#     if event.data == "[DONE]":
#         break

#     partial_result = json.loads(event.data)
#     token = partial_result["choices"][0]["text"]
#     print(token, end="", flush=True)     


# exec('''
# def my_generator(n):
#     # initialize counter
#     value = 0

#     # loop until counter is less than n
#     while value < n:

#         # produce the current value of the counter
#         yield value

#         # increment the counter
#         value += 1
#      '''
# )
# genr = my_generator(5)


# import json
# import os

# import requests
# import sseclient

# url = "https://api.together.xyz/api/v1/embeddings"
# model = "togethercomputer/bert-base-uncased"
# prompt = "Tell me a story"

# print(f"Model: {model}")
# print(f"Prompt: {repr(prompt)}")
# print("Repsonse:")
# print()

# payload = {
#     "model": model,
#     "input": prompt
# }
# headers = {
#     "accept": "application/json",
#     "content-type": "application/json",
#     "Authorization": f"Bearer cab10756f89a0d074d013fd4c3af1a003eb1e492edb782cedd6949be4ce1fe54",
# }

# response = requests.post(url, json=payload, headers=headers, stream=True)
# response.raise_for_status()

# client = sseclient.SSEClient(response)
# for event in client.events():
#     if event.data == "[DONE]":
#         break
#     print("ev")
#     print(event)
#     partial_result = json.loads(event.data)
#     token = partial_result["choices"][0]["text"]
#     print(token, end="", flush=True) 
# print(response.json())



# import requests

# response = requests.post(
#     "op/api/inference/text",
#     headers = {
#         "Authorization": "Bearer <Add your API KEY here>",
#     },
#     json = {
#         "prompt": "[INST] Enter your prompt here [/INST]",
#         "model":
#                 {
#                     "name": "truefoundry-public/CodeLlama-Instruct(13B)",
#                     "parameters": {
#                         "temperature": 0.7,
#                         "maximum_length": 500,
#                         "top_p": 0.95,
#                         "top_k": 50,
#                         "repetition_penalty": 1.2,
#                         "stop_sequences": [
#                             "</s>"
#                         ]
#                     }
#                 }
#     }
# )
# data = response.json()
# text = data.get('text')
# print(text)



# def fun(a: int = 4, b:int =5):
#     exec("""
# def fun2():
#     print('a')
# fun2()
# """)

# fun()
# exec("""
# def fun2():
#     print('a')
# fun2()
# """)
# print(fun2())

# def create_internal_function():
#     # Define the name and source code of the internal function as strings
#     internal_function_name = "internal_function"
#     # a = 1
#     internal_function_code = """
# a = 1
# def {}():
#     b=1
#     print(a)
#     print("This is an internal function")
# """.format(internal_function_name)

#     # Execute the source code using exec within the local namespace
#     local_namespace = {}
#     exec(internal_function_code, local_namespace)
#     print(local_namespace)
#     # Retrieve the internal function from the local namespace
#     internal_function = local_namespace.get(internal_function_name)

#     # Call the internal function
#     internal_function()
#     print(a)

# # Call the function to create and execute the internal function
# create_internal_function()

# Attempting to call internal_function outside create_internal_function will result in an error
# internal_function()

completion_function_string = """
def completion(model_config, prompt, model_parameters):
    import boto3
    import json
    brt = boto3.client(service_name='bedrock-runtime')

    body = json.dumps({
        "prompt": prompt,
        "max_gen_len": model_parameters['maximum_length'],
        "temperature": model_parameters['temperature'],
        "top_p": model_parameters['top_p'],
    })   
    model_id = model_config['model_id'] 
    accept = 'application/json'
    contentType = 'application/json'

    response = brt.invoke_model(body=body, modelId=model_id, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())
    return response_body['generation']
"""

stream_completion_function_string = """
def stream_completion(model_config, prompt, model_parameters):
    import boto3
    import json
    brt = boto3.client(service_name='bedrock-runtime')

    body = json.dumps({
        "prompt": prompt,
        "max_gen_len": model_parameters['maximum_length'],
        "temperature": model_parameters['temperature'],
        "top_p": model_parameters['top_p'],
    })   
    model_id = model_config['model_id'] 
    modelId = 'meta.llama2-13b-chat-v1'
    accept = 'application/json'
    contentType = 'application/json'

    response = brt.invoke_model_with_response_stream(body=body, modelId=model_id, accept=accept, contentType=contentType)
    stream = response.get("body")
    if stream:
        for event in stream:
            chunk = event.get("chunk")
            if chunk:
                chunk_obj = json.loads(chunk.get("bytes").decode())
                text = chunk_obj["generation"]
                yield text
"""

# class CustomInferenceManager:
#     def stream_processor(self, inference_response_generator):
#         for item in inference_response_generator:
#             print(item)

#     def text_generation(self, inference_request):
#         model_config = inference_request['model_details']['config']
#         local_namespace = {}
#         exec(completion_function_string, local_namespace)
#         # Retrieve the internal function from the local namespace
#         internal_function = local_namespace.get("completion")

#         # Call the internal function
#         return internal_function(model_config, "how can you help me?", {
#             "maximum_length": inference_request['new_model_parameters']['maximum_length'],
#             "temperature": inference_request['new_model_parameters']['temperature'],
#             "top_p": inference_request['new_model_parameters']['top_p']
#         })
    
#     def stream_generation(self, inference_request):
#         model_config = inference_request['model_details']['config']
#         local_namespace = {}
#         exec(stream_completion_function_string, local_namespace)
#         # Retrieve the internal function from the local namespace
#         internal_function = local_namespace.get("stream_completion")

#         # Call the internal function
#         return internal_function(model_config, "how can you help me?", {
#             "maximum_length": inference_request['new_model_parameters']['maximum_length'],
#             "temperature": inference_request['new_model_parameters']['temperature'],
#             "top_p": inference_request['new_model_parameters']['top_p']
#         })

# inference_manager = CustomInferenceManager()
# response = inference_manager.text_generation({
#     'model_details': {
#         'config': {
#             'model_id': "meta.llama2-13b-chat-v1"
#         }
#     }, 
#     'new_model_parameters': {
#         'maximum_length': 100,
#         'temperature': 0.1,
#         'top_p': 0.9
#     }
# })
# print(response)
# generator = inference_manager.stream_generation(
#     {
#     'model_details': {
#         'config': {
#             'model_id': "meta.llama2-13b-chat-v1"
#         }
#     }, 
#     'new_model_parameters': {
#         'maximum_length': 100,
#         'temperature': 0.1,
#         'top_p': 0.9
#     }
# }
# )
# inference_manager.stream_processor(generator)



# import requests

# response = requests.post(
#     "https://app.devtest.truefoundry.tech/api/llm/api/inference/chat",
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImd0eSI6WyJhdXRob3JpemF0aW9uX2NvZGUiXSwia2lkIjoibHNXSUM1a2RTVXVteDVySDk2RHpsV1hQbElNIn0.eyJhdWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJleHAiOjE3MDI1NDY4NDAsImlhdCI6MTcwMTk0MjA0MCwiaXNzIjoidHJ1ZWZvdW5kcnkuY29tIiwic3ViIjoiMWVmNGFlMWUtZDE2OC00Y2Q3LWJkNzMtODlmZWU1NmVjYzM3IiwianRpIjoiMDM3MzEzMmQtYjUzZS00ZDMxLTg1M2ItZWY5MmI5MjEzNGI4IiwiYXV0aGVudGljYXRpb25UeXBlIjoiR09PR0xFIiwiZW1haWwiOiJuaXJhbnNoaUB0cnVlZm91bmRyeS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoibmlyYW5zaGkiLCJhcHBsaWNhdGlvbklkIjoiODk1MjUzYWYtZWM5ZC00YmU2LTgzZDEtNmYyNDhlNjQ0ZTc5Iiwic2NvcGUiOiJvcGVuaWQgb2ZmbGluZV9hY2Nlc3MiLCJyb2xlcyI6WyJ0ZW5hbnQtYWRtaW4iXSwic2lkIjoiNjE2YWI2NGMtZGZiNC00NjNhLWI0ZGEtY2JhZmQzYWUxY2I5IiwiYXV0aF90aW1lIjoxNzAxOTQyMDQwLCJ0aWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJtZW1iZXJzaGlwcyI6W10sInRlbmFudE5hbWUiOiJ0cnVlZm91bmRyeSIsInVzZXJUeXBlIjoidXNlciIsInVzZXJuYW1lIjoibmlyYW5zaGkifQ.H3l54Su_o5hoHTzSXQqfs12tIRYFlYxoiB36X0yZHrMfKDnGDGdITOVqjGUx00FWFzzcIduHwxbt6bKcpTGir_fyx_H5TjzwobI5vBfNAQ4NqI8vwMTSw8zWqW3USRICoWFtKn0HnbnzaZZF6GRbhiy_O_ejOUcJoAXSZs4BsxDq4n8GPuBWgYcNR2-Iv7jOJScs-b9srqnYTh-Ei8WpjfeL74c6fFac1CKm0Rw7QUZASG7412sD510Tmtat3uyshjmSCDsaSNTpIqF9z6Y7anKwB27RZRjEevU98--PfST_GZu726l3hlrza2iFGDflRhsfpVKTpkv4aiqMJ3oK8A",
#     },
#     json = {
#         "messages": [
#             {"role": "system", "content": "You are an AI bot."},
#             {"role": "user", "content":"Enter your prompt here"}
#         ],
#         "model":
#                 {
#                     "name": "truefoundry-public/Falcon-Instruct(40B)",
#                     "parameters": {
#                         "temperature": 0.75,
#                         "maximum_length": 200,
#                         "top_p": 1.0,
#                         "repetition_penalty": 1.0,
#                         "stop_sequences": [
#                             "</s>",
#                             "User",
#                             "<|endoftext|>"
#                         ]
#                     }
#                 }
#     }
# )
# data = response.json()
# text = data.get('text')
# print(text)



from  openai import OpenAI, AzureOpenAI
from openai._exceptions import OpenAIError
# openai.completions.create(api_type='azure')
# client = OpenAI(api_key='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', base_url=None)
# print(client.base_url)
# print(openai)
# client = OpenAI(api_key='sk-EfgZ8lVFIFKoSZ4Gq7kHT3BlbkFJTcgBpTs53En5oDPaNgg')
# print(client.base_url)
# # client.api_key = 
# print(client.api_key)
# try:
#     client.completions.create(
#     model="gpt-3.5-turbo-instruct",
#     prompt="Say this is a test",
#     max_tokens=7,
#     temperature=0
#     )
# except OpenAIError as e:
#       print("err")
#       print(e)
# except Exception as e:
#       print(e)
# client = AzureOpenAI(api_version="2023-05-15", api_key="6a6484661f884870b19b5e3069b156c5", azure_endpoint='https://gateway-test.openai.azure.com/')
# resp = client.completions.create(
#   model="nikp-test",
#   prompt="hi",
#   max_tokens=7,
#   temperature=0.3,
# )
# print(resp.choices[0].text)



import requests

code = """
import requests 
def embedding_generation(texts, model_config, model_parameters, provider_account_config):
    print(provider_account_config.get("tfy_api_key"))
    print(texts)
    response = requests.post(
        "https://app.devtest.truefoundry.tech/api/llm/api/inference/embedding",
        headers = {
            "Authorization": "Bearer " + provider_account_config.get("tfy_api_key"),
        },
        json = {
            "input": texts,
            "model":
                    {
                        "name": "openai-main/text-embedding-ada-002"
                    }
        }
    )
    data = response.json()
    embedddings = data.get('embeddings')
    return embedddings
"""
# response = requests.post(
#     "http://localhost:5002/api/provider-account/",
#     headers={
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImd0eSI6WyJhdXRob3JpemF0aW9uX2NvZGUiXSwia2lkIjoibHNXSUM1a2RTVXVteDVySDk2RHpsV1hQbElNIn0.eyJhdWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJleHAiOjE3MDI4MTUyNTIsImlhdCI6MTcwMjIxMDQ1MiwiaXNzIjoidHJ1ZWZvdW5kcnkuY29tIiwic3ViIjoiMTIwMjNlZGEtZmE0Yy00M2NiLWEyZGEtOTViMjk0OTE5M2ExIiwianRpIjoiN2E4Y2VkZmMtOWZmYS00YjM2LTliOTUtZmNjMTk4MGUzMDc5IiwiYXV0aGVudGljYXRpb25UeXBlIjoiR09PR0xFIiwiZW1haWwiOiJha2FzaEB0cnVlZm91bmRyeS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWthc2gtdXNlciIsImFwcGxpY2F0aW9uSWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyIsInJvbGVzIjpbInRlbmFudC1hZG1pbiIsInRlbmFudC1zdXBlci1hZG1pbiIsInRydWVmb3VuZHJ5LXN1cGVyLWFkbWluIl0sInNpZCI6ImUwNzE3ZTRlLTk3MDktNDljYi04NDY3LWU3NDU1YTdiNzlhYSIsImF1dGhfdGltZSI6MTcwMjIxMDQ1MiwidGlkIjoiODk1MjUzYWYtZWM5ZC00YmU2LTgzZDEtNmYyNDhlNjQ0ZTc5IiwibWVtYmVyc2hpcHMiOltdLCJ0ZW5hbnROYW1lIjoidHJ1ZWZvdW5kcnkiLCJ1c2VyVHlwZSI6InVzZXIiLCJ1c2VybmFtZSI6ImFrYXNoLXVzZXIifQ.nTGGAU1jPbifAjH_JpRAlOQsS0i_Npucq2sT_cawdsBJdOzOFl22b7XWDHev6IYpXeazIfoyRae099QlZdb9KPDdRY85nHHDEuQ6kHwkriWShi1mBdEV5jeIRiaWthMCK4QH4wjy023BPIDwAr04nrUz8rGU4MZ9zpxuT_MnNkMaF35coMXeWOTlR3ajjaK0V5cebdPzx7qeqWaUhBbzSlKzngmXF6nn734tDRgEVNnTP9KhjZszRIgWQ2Fbpfm9AsMVqgTNCDAWat-OrDTxx6YG4SUzGNV3uZJfTd9YT3TFQcvNihdsXePLhM0lBSKwVaGG4rtDNtmLpx1GouckOw",
#     },
#     json={
#         "name": "niranshi-custom",
#         "provider": "custom",
#         "config": {
#             "type": "custom",
#             "provider_info": {
#                 "tfy_host": "https://app.devtest.truefoundry.com",
#                 "tfy_api_key": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImd0eSI6WyJhdXRob3JpemF0aW9uX2NvZGUiXSwia2lkIjoibHNXSUM1a2RTVXVteDVySDk2RHpsV1hQbElNIn0.eyJhdWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJleHAiOjE3MDI4MTUyNTIsImlhdCI6MTcwMjIxMDQ1MiwiaXNzIjoidHJ1ZWZvdW5kcnkuY29tIiwic3ViIjoiMTIwMjNlZGEtZmE0Yy00M2NiLWEyZGEtOTViMjk0OTE5M2ExIiwianRpIjoiN2E4Y2VkZmMtOWZmYS00YjM2LTliOTUtZmNjMTk4MGUzMDc5IiwiYXV0aGVudGljYXRpb25UeXBlIjoiR09PR0xFIiwiZW1haWwiOiJha2FzaEB0cnVlZm91bmRyeS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWthc2gtdXNlciIsImFwcGxpY2F0aW9uSWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyIsInJvbGVzIjpbInRlbmFudC1hZG1pbiIsInRlbmFudC1zdXBlci1hZG1pbiIsInRydWVmb3VuZHJ5LXN1cGVyLWFkbWluIl0sInNpZCI6ImUwNzE3ZTRlLTk3MDktNDljYi04NDY3LWU3NDU1YTdiNzlhYSIsImF1dGhfdGltZSI6MTcwMjIxMDQ1MiwidGlkIjoiODk1MjUzYWYtZWM5ZC00YmU2LTgzZDEtNmYyNDhlNjQ0ZTc5IiwibWVtYmVyc2hpcHMiOltdLCJ0ZW5hbnROYW1lIjoidHJ1ZWZvdW5kcnkiLCJ1c2VyVHlwZSI6InVzZXIiLCJ1c2VybmFtZSI6ImFrYXNoLXVzZXIifQ.nTGGAU1jPbifAjH_JpRAlOQsS0i_Npucq2sT_cawdsBJdOzOFl22b7XWDHev6IYpXeazIfoyRae099QlZdb9KPDdRY85nHHDEuQ6kHwkriWShi1mBdEV5jeIRiaWthMCK4QH4wjy023BPIDwAr04nrUz8rGU4MZ9zpxuT_MnNkMaF35coMXeWOTlR3ajjaK0V5cebdPzx7qeqWaUhBbzSlKzngmXF6nn734tDRgEVNnTP9KhjZszRIgWQ2Fbpfm9AsMVqgTNCDAWat-OrDTxx6YG4SUzGNV3uZJfTd9YT3TFQcvNihdsXePLhM0lBSKwVaGG4rtDNtmLpx1GouckOw",
#             },
#             "provider_code": {"code_string": code},
#         },
#         "provider_account_id": "4f36c0b0f7cb4312bb317dadd99625f1"
#     },
# )
# data = response.json()
# print(data)

# import json
# code1 = "\nimport requests\n\nresponse = requests.post(\n    \"http://localhost:5002/api/inference/embedding\",\n    headers = {\n        \"Authorization\": \"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImd0eSI6WyJhdXRob3JpemF0aW9uX2NvZGUiXSwia2lkIjoibHNXSUM1a2RTVXVteDVySDk2RHpsV1hQbElNIn0.eyJhdWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJleHAiOjE3MDI4MTUyNTIsImlhdCI6MTcwMjIxMDQ1MiwiaXNzIjoidHJ1ZWZvdW5kcnkuY29tIiwic3ViIjoiMTIwMjNlZGEtZmE0Yy00M2NiLWEyZGEtOTViMjk0OTE5M2ExIiwianRpIjoiN2E4Y2VkZmMtOWZmYS00YjM2LTliOTUtZmNjMTk4MGUzMDc5IiwiYXV0aGVudGljYXRpb25UeXBlIjoiR09PR0xFIiwiZW1haWwiOiJha2FzaEB0cnVlZm91bmRyeS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWthc2gtdXNlciIsImFwcGxpY2F0aW9uSWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyIsInJvbGVzIjpbInRlbmFudC1hZG1pbiIsInRlbmFudC1zdXBlci1hZG1pbiIsInRydWVmb3VuZHJ5LXN1cGVyLWFkbWluIl0sInNpZCI6ImUwNzE3ZTRlLTk3MDktNDljYi04NDY3LWU3NDU1YTdiNzlhYSIsImF1dGhfdGltZSI6MTcwMjIxMDQ1MiwidGlkIjoiODk1MjUzYWYtZWM5ZC00YmU2LTgzZDEtNmYyNDhlNjQ0ZTc5IiwibWVtYmVyc2hpcHMiOltdLCJ0ZW5hbnROYW1lIjoidHJ1ZWZvdW5kcnkiLCJ1c2VyVHlwZSI6InVzZXIiLCJ1c2VybmFtZSI6ImFrYXNoLXVzZXIifQ.nTGGAU1jPbifAjH_JpRAlOQsS0i_Npucq2sT_cawdsBJdOzOFl22b7XWDHev6IYpXeazIfoyRae099QlZdb9KPDdRY85nHHDEuQ6kHwkriWShi1mBdEV5jeIRiaWthMCK4QH4wjy023BPIDwAr04nrUz8rGU4MZ9zpxuT_MnNkMaF35coMXeWOTlR3ajjaK0V5cebdPzx7qeqWaUhBbzSlKzngmXF6nn734tDRgEVNnTP9KhjZszRIgWQ2Fbpfm9AsMVqgTNCDAWat-OrDTxx6YG4SUzGNV3uZJfTd9YT3TFQcvNihdsXePLhM0lBSKwVaGG4rtDNtmLpx1GouckOw\",\n    },\n    json = {\n        \"input\": 'hello',\n        \"model\":\n                {\n                    \"name\": \"niranshi-custom/try-embed\",\n                    \"parameters\": {}\n                }\n    }\n)\ndata = response.json()\nembeddings = data.get('embeddings')\nprint(embeddings)\n"
# exec(code1)



# import requests

# response = requests.post(
#     "http://localhost:5002/api/inference/text",
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImd0eSI6WyJhdXRob3JpemF0aW9uX2NvZGUiXSwia2lkIjoibHNXSUM1a2RTVXVteDVySDk2RHpsV1hQbElNIn0.eyJhdWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJleHAiOjE3MDI4MTUyNTIsImlhdCI6MTcwMjIxMDQ1MiwiaXNzIjoidHJ1ZWZvdW5kcnkuY29tIiwic3ViIjoiMTIwMjNlZGEtZmE0Yy00M2NiLWEyZGEtOTViMjk0OTE5M2ExIiwianRpIjoiN2E4Y2VkZmMtOWZmYS00YjM2LTliOTUtZmNjMTk4MGUzMDc5IiwiYXV0aGVudGljYXRpb25UeXBlIjoiR09PR0xFIiwiZW1haWwiOiJha2FzaEB0cnVlZm91bmRyeS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWthc2gtdXNlciIsImFwcGxpY2F0aW9uSWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyIsInJvbGVzIjpbInRlbmFudC1hZG1pbiIsInRlbmFudC1zdXBlci1hZG1pbiIsInRydWVmb3VuZHJ5LXN1cGVyLWFkbWluIl0sInNpZCI6ImUwNzE3ZTRlLTk3MDktNDljYi04NDY3LWU3NDU1YTdiNzlhYSIsImF1dGhfdGltZSI6MTcwMjIxMDQ1MiwidGlkIjoiODk1MjUzYWYtZWM5ZC00YmU2LTgzZDEtNmYyNDhlNjQ0ZTc5IiwibWVtYmVyc2hpcHMiOltdLCJ0ZW5hbnROYW1lIjoidHJ1ZWZvdW5kcnkiLCJ1c2VyVHlwZSI6InVzZXIiLCJ1c2VybmFtZSI6ImFrYXNoLXVzZXIifQ.nTGGAU1jPbifAjH_JpRAlOQsS0i_Npucq2sT_cawdsBJdOzOFl22b7XWDHev6IYpXeazIfoyRae099QlZdb9KPDdRY85nHHDEuQ6kHwkriWShi1mBdEV5jeIRiaWthMCK4QH4wjy023BPIDwAr04nrUz8rGU4MZ9zpxuT_MnNkMaF35coMXeWOTlR3ajjaK0V5cebdPzx7qeqWaUhBbzSlKzngmXF6nn734tDRgEVNnTP9KhjZszRIgWQ2Fbpfm9AsMVqgTNCDAWat-OrDTxx6YG4SUzGNV3uZJfTd9YT3TFQcvNihdsXePLhM0lBSKwVaGG4rtDNtmLpx1GouckOw",
#     },
#     json = {
#         "prompt": "hiiii",
#         "model":
#                 {
#                     "name": "openai-main/gpt-3-5-turbo",
#                     "parameters": {
#                         "temperature": 0.5,
#                         "maximum_length": 200,
#                         "top_p": 1.0,
#                         "presence_penalty": 0.0,
#                         "frequency_penalty": 0.0
#                     }
#                 }
#     }
# )
# data = response.json()
# text = data.get('text')
# print(text)

code_string = """
import requests 
import json

def text_generation(prompt, model_config, model_parameters, provider_account_config):
    if model_config.get('model_server') == "tgi":
        response = requests.post(
            f"{model_config.get('model_url')}/generate",
            headers = {
                "Authorization": "Bearer " + provider_account_config.get("tfy_api_key"),
            },
            json = {
                "inputs": prompt,
                "parameters": {
                    "best_of": 1,
                    "decoder_input_details": True,
                    "details": True,
                    "do_sample": True,
                    "max_new_tokens": model_parameters.get('maximum_length') if model_parameters.get('maximum_length') is not None else 100,
                    "repetition_penalty": 1.03 if model_parameters.get('repetition_penalty') is None else model_parameters.get('repetition_penalty'),
                    "return_full_text": False,
                    "seed": None,
                    "stop": model_parameters.get('stop_sequences') if model_parameters.get('stop_sequences') is not None else [],
                    "temperature": model_parameters.get('temperature') if model_parameters.get('temperature') is not None else 0.5,
                    "top_k": model_parameters.get('top_k') if model_parameters.get('top_k') is not None else 10,
                    "top_p": model_parameters.get('top_p') if model_parameters.get('top_p') is not None else 0.95,
                    "truncate": None,
                    "typical_p": 0.95,
                    "watermark": True
                }    
            }
        )
        resp = response.json()
        return resp.get('generated_text')
    if model_config.get('model_server') == "vllm":
        response = requests.post(
            f"{model_config.get('model_url')}/generate",
            headers = {
                "Authorization": "Bearer " + provider_account_config.get("tfy_api_key"),
            },
            json = {
                "prompt": prompt,
                "stream": False,
                "n": 1,
                "best_of": 1,
                "presence_penalty": 0 if model_parameters.get('presence_penalty') is None else model_parameters.get('presence_penalty'),
                "frequency_penalty": 0 if model_parameters.get('frequency_penalty') is None else model_parameters.get('frequency_penalty'),
                "repetition_penalty": 1 if model_parameters.get('repetition_penalty') is None else model_parameters.get('repetition_penalty'),
                "temperature": 1 if model_parameters.get('temperature') is None else model_parameters.get('temperature'),
                "top_p": 1 if model_parameters.get('top_p') is None else model_parameters.get('top_p'),
                "top_k": -1 if model_parameters.get('top_k') is None else model_parameters.get('top_k'),
                "min_p": 0,
                "use_beam_search": False,
                "length_penalty": 1,
                "early_stopping": False,
                "stop": [] if model_parameters.get('stop_sequences') is None else model_parameters.get('stop_sequences'),
                "ignore_eos": False,
                "max_tokens": model_parameters.get('maximum_length') if model_parameters.get('maximum_length') is not None else 100,
                "logprobs": 0,
                "prompt_logprobs": 0,
                "skip_special_tokens": True,
                "spaces_between_special_tokens": True,
                "return_full_text": True,
                "details": {
                    "prompt_token_ids": False,
                    "prompt_text": False,
                    "output_token_ids": False,
                    "output_text": False
                }
            }
        )
        resp = response.json()
        return resp.get('text')[0]
    
def embedding_generation(input, model_config, model_parameters, provider_account_config):
    if model_config.get('model_server') == "tei":
        response = requests.post(
            f"{model_config.get('model_url')}/embeddings",
            headers = {
                "Authorization": "Bearer " + provider_account_config.get("tfy_api_key"),
            },
            json = {
                "input": input
            }
        )
        resp = response.json()
        embeddings = [embed["embedding"] for embed in resp['data']]
        return embeddings
    if model_config.get('model_server') == "ml_server":
        if isinstance(input, str):
            input = [input]
        response = requests.post(
            f"{model_config.get('model_url')}/v2/models/{model_config.get('model_name')}/infer/simple",
            headers = {
                "Authorization": "Bearer " + provider_account_config.get("tfy_api_key"),
            },
            json = {
                "inputs": input
            }
        )
        resp = response.json()
        return resp
    
def text_stream_generation(prompt, model_config, model_parameters, provider_account_config):
    if model_config.get('model_server') == "tgi":
        response = requests.post(
            f"{model_config.get('model_url')}/generate_stream",
            headers = {
                "Authorization": "Bearer " + provider_account_config.get("tfy_api_key"),
            },
            json = {
                "inputs": prompt,
                "parameters": {
                    "best_of": 1,
                    "details": True,
                    "do_sample": True,
                    "max_new_tokens": model_parameters.get('maximum_length') if model_parameters.get('maximum_length') is not None else 100,
                    "repetition_penalty": 1.03 if model_parameters.get('repetition_penalty') is None else model_parameters.get('repetition_penalty'),
                    "return_full_text": False,
                    "seed": None,
                    "stop": model_parameters.get('stop_sequences') if model_parameters.get('stop_sequences') is not None else [],
                    "temperature": model_parameters.get('temperature') if model_parameters.get('temperature') is not None else 0.5,
                    "top_k": model_parameters.get('top_k') if model_parameters.get('top_k') is not None else 10,
                    "top_p": model_parameters.get('top_p') if model_parameters.get('top_p') is not None else 0.95,
                    "truncate": None,
                    "typical_p": 0.95,
                    "watermark": True
                }, 
            }
        )
        for line in response.iter_lines():
            data = str(line, "utf-8")
            if not data.startswith("data:"):
                continue
            json_data = json.loads(data.lstrip("data:"))
            if json_data["token"]["special"]:
                continue
            yield json_data["token"]["text"]
    if model_config.get('model_server') == "vllm":
        response = requests.post(
            f"{model_config.get('model_url')}/generate",
            headers = {
                "Authorization": "Bearer " + provider_account_config.get("tfy_api_key"),
            },
            json = {
                "prompt": prompt,
                "stream": False,
                "n": 1,
                "best_of": 1,
                "presence_penalty": 0 if model_parameters.get('presence_penalty') is None else model_parameters.get('presence_penalty'),
                "frequency_penalty": 0 if model_parameters.get('frequency_penalty') is None else model_parameters.get('frequency_penalty'),
                "repetition_penalty": 1 if model_parameters.get('repetition_penalty') is None else model_parameters.get('repetition_penalty'),
                "temperature": 1 if model_parameters.get('temperature') is None else model_parameters.get('temperature'),
                "top_p": 1 if model_parameters.get('top_p') is None else model_parameters.get('top_p'),
                "top_k": -1 if model_parameters.get('top_k') is None else model_parameters.get('top_k'),
                "min_p": 0,
                "use_beam_search": False,
                "length_penalty": 1,
                "early_stopping": False,
                "stop": [] if model_parameters.get('stop_sequences') is None else model_parameters.get('stop_sequences'),
                "ignore_eos": False,
                "max_tokens": model_parameters.get('maximum_length') if model_parameters.get('maximum_length') is not None else 100,
                "logprobs": 0,
                "prompt_logprobs": 0,
                "skip_special_tokens": True,
                "spaces_between_special_tokens": True,
                "return_full_text": True,
                "details": {
                    "prompt_token_ids": False,
                    "prompt_text": False,
                    "output_token_ids": False,
                    "output_text": False
                }
            }
        )
        resp = response.json()
        for a in resp.get('text')[0].split(" "):
            yield a
            yield " "

"""

exec(code_string)

# resp = text_stream_generation("hello", {'model_server': 'tgi', 'model_url': 'https://test-tgi-model-llama123.ml.demo.truefoundry.cloud'}, 
#                 {'maximum_length': 100, 'temperature': 0.1, 'top_p': 0.9, 'repetition_penalty': 1.0, "stop_sequences": ["</s>", "User"]},
#                 {'tfy_api_key': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImd0eSI6WyJhdXRob3JpemF0aW9uX2NvZGUiXSwia2lkIjoibHNXSUM1a2RTVXVteDVySDk2RHpsV1hQbElNIn0.eyJhdWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJleHAiOjE3MDI4MTUyNTIsImlhdCI6MTcwMjIxMDQ1MiwiaXNzIjoidHJ1ZWZvdW5kcnkuY29tIiwic3ViIjoiMTIwMjNlZGEtZmE0Yy00M2NiLWEyZGEtOTViMjk0OTE5M2ExIiwianRpIjoiN2E4Y2VkZmMtOWZmYS00YjM2LTliOTUtZmNjMTk4MGUzMDc5IiwiYXV0aGVudGljYXRpb25UeXBlIjoiR09PR0xFIiwiZW1haWwiOiJha2FzaEB0cnVlZm91bmRyeS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWthc2gtdXNlciIsImFwcGxpY2F0aW9uSWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyIsInJvbGVzIjpbInRlbmFudC1hZG1pbiIsInRlbmFudC1zdXBlci1hZG1pbiIsInRydWVmb3VuZHJ5LXN1cGVyLWFkbWluIl0sInNpZCI6ImUwNzE3ZTRlLTk3MDktNDljYi04NDY3LWU3NDU1YTdiNzlhYSIsImF1dGhfdGltZSI6MTcwMjIxMDQ1MiwidGlkIjoiODk1MjUzYWYtZWM5ZC00YmU2LTgzZDEtNmYyNDhlNjQ0ZTc5IiwibWVtYmVyc2hpcHMiOltdLCJ0ZW5hbnROYW1lIjoidHJ1ZWZvdW5kcnkiLCJ1c2VyVHlwZSI6InVzZXIiLCJ1c2VybmFtZSI6ImFrYXNoLXVzZXIifQ.nTGGAU1jPbifAjH_JpRAlOQsS0i_Npucq2sT_cawdsBJdOzOFl22b7XWDHev6IYpXeazIfoyRae099QlZdb9KPDdRY85nHHDEuQ6kHwkriWShi1mBdEV5jeIRiaWthMCK4QH4wjy023BPIDwAr04nrUz8rGU4MZ9zpxuT_MnNkMaF35coMXeWOTlR3ajjaK0V5cebdPzx7qeqWaUhBbzSlKzngmXF6nn734tDRgEVNnTP9KhjZszRIgWQ2Fbpfm9AsMVqgTNCDAWat-OrDTxx6YG4SUzGNV3uZJfTd9YT3TFQcvNihdsXePLhM0lBSKwVaGG4rtDNtmLpx1GouckOw'})
# for a in resp:
#     print(a)


# resp = text_stream_generation("hello", {'model_server': 'vllm', 'model_url': 'https://cvs-part-data-zephyr-cvs-finetuning-8000.ml.demo.truefoundry.cloud'}, 
#                 {'maximum_length': 100, 'temperature': 0.1, 'top_p': 0.9, 'repetition_penalty': 1.0, "stop_sequences": ["</s>", "User"]},
#                 {'tfy_api_key': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImd0eSI6WyJhdXRob3JpemF0aW9uX2NvZGUiXSwia2lkIjoibHNXSUM1a2RTVXVteDVySDk2RHpsV1hQbElNIn0.eyJhdWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJleHAiOjE3MDI4MTUyNTIsImlhdCI6MTcwMjIxMDQ1MiwiaXNzIjoidHJ1ZWZvdW5kcnkuY29tIiwic3ViIjoiMTIwMjNlZGEtZmE0Yy00M2NiLWEyZGEtOTViMjk0OTE5M2ExIiwianRpIjoiN2E4Y2VkZmMtOWZmYS00YjM2LTliOTUtZmNjMTk4MGUzMDc5IiwiYXV0aGVudGljYXRpb25UeXBlIjoiR09PR0xFIiwiZW1haWwiOiJha2FzaEB0cnVlZm91bmRyeS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWthc2gtdXNlciIsImFwcGxpY2F0aW9uSWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyIsInJvbGVzIjpbInRlbmFudC1hZG1pbiIsInRlbmFudC1zdXBlci1hZG1pbiIsInRydWVmb3VuZHJ5LXN1cGVyLWFkbWluIl0sInNpZCI6ImUwNzE3ZTRlLTk3MDktNDljYi04NDY3LWU3NDU1YTdiNzlhYSIsImF1dGhfdGltZSI6MTcwMjIxMDQ1MiwidGlkIjoiODk1MjUzYWYtZWM5ZC00YmU2LTgzZDEtNmYyNDhlNjQ0ZTc5IiwibWVtYmVyc2hpcHMiOltdLCJ0ZW5hbnROYW1lIjoidHJ1ZWZvdW5kcnkiLCJ1c2VyVHlwZSI6InVzZXIiLCJ1c2VybmFtZSI6ImFrYXNoLXVzZXIifQ.nTGGAU1jPbifAjH_JpRAlOQsS0i_Npucq2sT_cawdsBJdOzOFl22b7XWDHev6IYpXeazIfoyRae099QlZdb9KPDdRY85nHHDEuQ6kHwkriWShi1mBdEV5jeIRiaWthMCK4QH4wjy023BPIDwAr04nrUz8rGU4MZ9zpxuT_MnNkMaF35coMXeWOTlR3ajjaK0V5cebdPzx7qeqWaUhBbzSlKzngmXF6nn734tDRgEVNnTP9KhjZszRIgWQ2Fbpfm9AsMVqgTNCDAWat-OrDTxx6YG4SUzGNV3uZJfTd9YT3TFQcvNihdsXePLhM0lBSKwVaGG4rtDNtmLpx1GouckOw'})

# for a in resp:
#     print(a)

# embedding_generation("12334", {'model_server': 'tei', 'model_url': 'https://embed-model-test-nikhil-ws-8000.tfy-ctl-euwe1-devtest.devtest.truefoundry.tech'},None,
#     {'tfy_api_key': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImd0eSI6WyJhdXRob3JpemF0aW9uX2NvZGUiXSwia2lkIjoibHNXSUM1a2RTVXVteDVySDk2RHpsV1hQbElNIn0.eyJhdWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJleHAiOjE3MDI4MTUyNTIsImlhdCI6MTcwMjIxMDQ1MiwiaXNzIjoidHJ1ZWZvdW5kcnkuY29tIiwic3ViIjoiMTIwMjNlZGEtZmE0Yy00M2NiLWEyZGEtOTViMjk0OTE5M2ExIiwianRpIjoiN2E4Y2VkZmMtOWZmYS00YjM2LTliOTUtZmNjMTk4MGUzMDc5IiwiYXV0aGVudGljYXRpb25UeXBlIjoiR09PR0xFIiwiZW1haWwiOiJha2FzaEB0cnVlZm91bmRyeS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWthc2gtdXNlciIsImFwcGxpY2F0aW9uSWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyIsInJvbGVzIjpbInRlbmFudC1hZG1pbiIsInRlbmFudC1zdXBlci1hZG1pbiIsInRydWVmb3VuZHJ5LXN1cGVyLWFkbWluIl0sInNpZCI6ImUwNzE3ZTRlLTk3MDktNDljYi04NDY3LWU3NDU1YTdiNzlhYSIsImF1dGhfdGltZSI6MTcwMjIxMDQ1MiwidGlkIjoiODk1MjUzYWYtZWM5ZC00YmU2LTgzZDEtNmYyNDhlNjQ0ZTc5IiwibWVtYmVyc2hpcHMiOltdLCJ0ZW5hbnROYW1lIjoidHJ1ZWZvdW5kcnkiLCJ1c2VyVHlwZSI6InVzZXIiLCJ1c2VybmFtZSI6ImFrYXNoLXVzZXIifQ.nTGGAU1jPbifAjH_JpRAlOQsS0i_Npucq2sT_cawdsBJdOzOFl22b7XWDHev6IYpXeazIfoyRae099QlZdb9KPDdRY85nHHDEuQ6kHwkriWShi1mBdEV5jeIRiaWthMCK4QH4wjy023BPIDwAr04nrUz8rGU4MZ9zpxuT_MnNkMaF35coMXeWOTlR3ajjaK0V5cebdPzx7qeqWaUhBbzSlKzngmXF6nn734tDRgEVNnTP9KhjZszRIgWQ2Fbpfm9AsMVqgTNCDAWat-OrDTxx6YG4SUzGNV3uZJfTd9YT3TFQcvNihdsXePLhM0lBSKwVaGG4rtDNtmLpx1GouckOw'}
# )

# resp = embedding_generation("op", {'model_server': 'ml_server', 'model_url': 'https://e5-small-v2-cpu-gusto-ws.ml.demo.truefoundry.cloud', 'model_name':'e5-small-v2-cpu'},None,
#                      {'tfy_api_key': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImd0eSI6WyJhdXRob3JpemF0aW9uX2NvZGUiXSwia2lkIjoibHNXSUM1a2RTVXVteDVySDk2RHpsV1hQbElNIn0.eyJhdWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJleHAiOjE3MDI4MTUyNTIsImlhdCI6MTcwMjIxMDQ1MiwiaXNzIjoidHJ1ZWZvdW5kcnkuY29tIiwic3ViIjoiMTIwMjNlZGEtZmE0Yy00M2NiLWEyZGEtOTViMjk0OTE5M2ExIiwianRpIjoiN2E4Y2VkZmMtOWZmYS00YjM2LTliOTUtZmNjMTk4MGUzMDc5IiwiYXV0aGVudGljYXRpb25UeXBlIjoiR09PR0xFIiwiZW1haWwiOiJha2FzaEB0cnVlZm91bmRyeS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWthc2gtdXNlciIsImFwcGxpY2F0aW9uSWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyIsInJvbGVzIjpbInRlbmFudC1hZG1pbiIsInRlbmFudC1zdXBlci1hZG1pbiIsInRydWVmb3VuZHJ5LXN1cGVyLWFkbWluIl0sInNpZCI6ImUwNzE3ZTRlLTk3MDktNDljYi04NDY3LWU3NDU1YTdiNzlhYSIsImF1dGhfdGltZSI6MTcwMjIxMDQ1MiwidGlkIjoiODk1MjUzYWYtZWM5ZC00YmU2LTgzZDEtNmYyNDhlNjQ0ZTc5IiwibWVtYmVyc2hpcHMiOltdLCJ0ZW5hbnROYW1lIjoidHJ1ZWZvdW5kcnkiLCJ1c2VyVHlwZSI6InVzZXIiLCJ1c2VybmFtZSI6ImFrYXNoLXVzZXIifQ.nTGGAU1jPbifAjH_JpRAlOQsS0i_Npucq2sT_cawdsBJdOzOFl22b7XWDHev6IYpXeazIfoyRae099QlZdb9KPDdRY85nHHDEuQ6kHwkriWShi1mBdEV5jeIRiaWthMCK4QH4wjy023BPIDwAr04nrUz8rGU4MZ9zpxuT_MnNkMaF35coMXeWOTlR3ajjaK0V5cebdPzx7qeqWaUhBbzSlKzngmXF6nn734tDRgEVNnTP9KhjZszRIgWQ2Fbpfm9AsMVqgTNCDAWat-OrDTxx6YG4SUzGNV3uZJfTd9YT3TFQcvNihdsXePLhM0lBSKwVaGG4rtDNtmLpx1GouckOw'})

# print(resp)
# import requests
# requests.post(
#     "https://app.devtest.truefoundry.tech/api/llm/api/provider-account/",
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImd0eSI6WyJhdXRob3JpemF0aW9uX2NvZGUiXSwia2lkIjoibHNXSUM1a2RTVXVteDVySDk2RHpsV1hQbElNIn0.eyJhdWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJleHAiOjE3MDI4MTUyNTIsImlhdCI6MTcwMjIxMDQ1MiwiaXNzIjoidHJ1ZWZvdW5kcnkuY29tIiwic3ViIjoiMTIwMjNlZGEtZmE0Yy00M2NiLWEyZGEtOTViMjk0OTE5M2ExIiwianRpIjoiN2E4Y2VkZmMtOWZmYS00YjM2LTliOTUtZmNjMTk4MGUzMDc5IiwiYXV0aGVudGljYXRpb25UeXBlIjoiR09PR0xFIiwiZW1haWwiOiJha2FzaEB0cnVlZm91bmRyeS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWthc2gtdXNlciIsImFwcGxpY2F0aW9uSWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyIsInJvbGVzIjpbInRlbmFudC1hZG1pbiIsInRlbmFudC1zdXBlci1hZG1pbiIsInRydWVmb3VuZHJ5LXN1cGVyLWFkbWluIl0sInNpZCI6ImUwNzE3ZTRlLTk3MDktNDljYi04NDY3LWU3NDU1YTdiNzlhYSIsImF1dGhfdGltZSI6MTcwMjIxMDQ1MiwidGlkIjoiODk1MjUzYWYtZWM5ZC00YmU2LTgzZDEtNmYyNDhlNjQ0ZTc5IiwibWVtYmVyc2hpcHMiOltdLCJ0ZW5hbnROYW1lIjoidHJ1ZWZvdW5kcnkiLCJ1c2VyVHlwZSI6InVzZXIiLCJ1c2VybmFtZSI6ImFrYXNoLXVzZXIifQ.nTGGAU1jPbifAjH_JpRAlOQsS0i_Npucq2sT_cawdsBJdOzOFl22b7XWDHev6IYpXeazIfoyRae099QlZdb9KPDdRY85nHHDEuQ6kHwkriWShi1mBdEV5jeIRiaWthMCK4QH4wjy023BPIDwAr04nrUz8rGU4MZ9zpxuT_MnNkMaF35coMXeWOTlR3ajjaK0V5cebdPzx7qeqWaUhBbzSlKzngmXF6nn734tDRgEVNnTP9KhjZszRIgWQ2Fbpfm9AsMVqgTNCDAWat-OrDTxx6YG4SUzGNV3uZJfTd9YT3TFQcvNihdsXePLhM0lBSKwVaGG4rtDNtmLpx1GouckOw",
#     },
#     json= {
#         "name": "test-tfy-self-hosted",
#         "provider_account_id": "d66ce1e34a1141798581bbeaceb4f12b",
#         "provider": "custom",
#         "config": {
#             "type": "custom",
#             "provider_info": {
#                 "tfy_api_key": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImd0eSI6WyJhdXRob3JpemF0aW9uX2NvZGUiXSwia2lkIjoibHNXSUM1a2RTVXVteDVySDk2RHpsV1hQbElNIn0.eyJhdWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJleHAiOjE3MDI4MTUyNTIsImlhdCI6MTcwMjIxMDQ1MiwiaXNzIjoidHJ1ZWZvdW5kcnkuY29tIiwic3ViIjoiMTIwMjNlZGEtZmE0Yy00M2NiLWEyZGEtOTViMjk0OTE5M2ExIiwianRpIjoiN2E4Y2VkZmMtOWZmYS00YjM2LTliOTUtZmNjMTk4MGUzMDc5IiwiYXV0aGVudGljYXRpb25UeXBlIjoiR09PR0xFIiwiZW1haWwiOiJha2FzaEB0cnVlZm91bmRyeS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWthc2gtdXNlciIsImFwcGxpY2F0aW9uSWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyIsInJvbGVzIjpbInRlbmFudC1hZG1pbiIsInRlbmFudC1zdXBlci1hZG1pbiIsInRydWVmb3VuZHJ5LXN1cGVyLWFkbWluIl0sInNpZCI6ImUwNzE3ZTRlLTk3MDktNDljYi04NDY3LWU3NDU1YTdiNzlhYSIsImF1dGhfdGltZSI6MTcwMjIxMDQ1MiwidGlkIjoiODk1MjUzYWYtZWM5ZC00YmU2LTgzZDEtNmYyNDhlNjQ0ZTc5IiwibWVtYmVyc2hpcHMiOltdLCJ0ZW5hbnROYW1lIjoidHJ1ZWZvdW5kcnkiLCJ1c2VyVHlwZSI6InVzZXIiLCJ1c2VybmFtZSI6ImFrYXNoLXVzZXIifQ.nTGGAU1jPbifAjH_JpRAlOQsS0i_Npucq2sT_cawdsBJdOzOFl22b7XWDHev6IYpXeazIfoyRae099QlZdb9KPDdRY85nHHDEuQ6kHwkriWShi1mBdEV5jeIRiaWthMCK4QH4wjy023BPIDwAr04nrUz8rGU4MZ9zpxuT_MnNkMaF35coMXeWOTlR3ajjaK0V5cebdPzx7qeqWaUhBbzSlKzngmXF6nn734tDRgEVNnTP9KhjZszRIgWQ2Fbpfm9AsMVqgTNCDAWat-OrDTxx6YG4SUzGNV3uZJfTd9YT3TFQcvNihdsXePLhM0lBSKwVaGG4rtDNtmLpx1GouckOw"
#             },
#             "provider_code": {
#                     "code_string": code_string
#                 },
#         }
#     }
# )


# import requests

# response = requests.post(
#     "http://localhost:5002/api/inference/text",
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImd0eSI6WyJhdXRob3JpemF0aW9uX2NvZGUiXSwia2lkIjoibHNXSUM1a2RTVXVteDVySDk2RHpsV1hQbElNIn0.eyJhdWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJleHAiOjE3MDI4MTUyNTIsImlhdCI6MTcwMjIxMDQ1MiwiaXNzIjoidHJ1ZWZvdW5kcnkuY29tIiwic3ViIjoiMTIwMjNlZGEtZmE0Yy00M2NiLWEyZGEtOTViMjk0OTE5M2ExIiwianRpIjoiN2E4Y2VkZmMtOWZmYS00YjM2LTliOTUtZmNjMTk4MGUzMDc5IiwiYXV0aGVudGljYXRpb25UeXBlIjoiR09PR0xFIiwiZW1haWwiOiJha2FzaEB0cnVlZm91bmRyeS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWthc2gtdXNlciIsImFwcGxpY2F0aW9uSWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyIsInJvbGVzIjpbInRlbmFudC1hZG1pbiIsInRlbmFudC1zdXBlci1hZG1pbiIsInRydWVmb3VuZHJ5LXN1cGVyLWFkbWluIl0sInNpZCI6ImUwNzE3ZTRlLTk3MDktNDljYi04NDY3LWU3NDU1YTdiNzlhYSIsImF1dGhfdGltZSI6MTcwMjIxMDQ1MiwidGlkIjoiODk1MjUzYWYtZWM5ZC00YmU2LTgzZDEtNmYyNDhlNjQ0ZTc5IiwibWVtYmVyc2hpcHMiOltdLCJ0ZW5hbnROYW1lIjoidHJ1ZWZvdW5kcnkiLCJ1c2VyVHlwZSI6InVzZXIiLCJ1c2VybmFtZSI6ImFrYXNoLXVzZXIifQ.nTGGAU1jPbifAjH_JpRAlOQsS0i_Npucq2sT_cawdsBJdOzOFl22b7XWDHev6IYpXeazIfoyRae099QlZdb9KPDdRY85nHHDEuQ6kHwkriWShi1mBdEV5jeIRiaWthMCK4QH4wjy023BPIDwAr04nrUz8rGU4MZ9zpxuT_MnNkMaF35coMXeWOTlR3ajjaK0V5cebdPzx7qeqWaUhBbzSlKzngmXF6nn734tDRgEVNnTP9KhjZszRIgWQ2Fbpfm9AsMVqgTNCDAWat-OrDTxx6YG4SUzGNV3uZJfTd9YT3TFQcvNihdsXePLhM0lBSKwVaGG4rtDNtmLpx1GouckOw",
#     },
#     json = {
#         "prompt": "Enter your prompt here",
#         "model":
#                 {
#                     "name": "truefoundry-public/Mixtral-8x(7B)",
#                     "parameters": {
#                         "temperature": 1.0,
#                         "maximum_length": 128,
#                         "top_p": 1.0,
#                         "top_k": 50,
#                         "presence_penalty": 0.0,
#                         "frequency_penalty": 0.0,
#                         "stop_sequences": [
#                             "</s>"
#                         ]
#                     }
#                 }
#     }
# )
# data = response.json()
# text = data.get('text')
# print(text)

# import voyageai
# voyageai.api_key = None  # add you Voyage API KEY
# documents = [
#     "The Mediterranean diet emphasizes fish, olive oil, and vegetables, believed to reduce chronic diseases.",
#     "Photosynthesis in plants converts light energy into glucose and produces essential oxygen.",
#     "20th-century innovations, from radios to smartphones, centered on electronic advancements.",
#     "Rivers provide water, irrigation, and habitat for aquatic species, vital for ecosystems.",
#     "Apple’s conference call to discuss fourth fiscal quarter results and business updates is scheduled for Thursday, November 2, 2023 at 2:00 p.m. PT / 5:00 p.m. ET.",
#     "Shakespeare's works, like 'Hamlet' and 'A Midsummer Night's Dream,' endure in literature."
# ]

# # Embed the documents
# def fun():
#     embeddings = voyageai.aget_embeddings(["documents"], model="voyage-01", api_key="pa-mghE896kKm3nN61pxwGqyRP5l5axbaJiPR1SZNHpuA8")
#     print(embeddings)
# fun()

# import json
# import os

# import requests
# import sseclient

# url = "https://api.together.xyz/inference"
# model = "togethercomputer/llama-2-70b"
# prompt = "HIII"

# print(f"Model: {model}")
# print(f"Prompt: {repr(prompt)}")
# print("Repsonse:")
# print()

# payload = {
#     "model": model,
#     "prompt": prompt,
#     "max_tokens": 512,
#     "temperature": 0.9,
#     "top_p": 0.95,
#     "top_k": 100,
#     "repetition_penalty": 1,
#     "stream_tokens": False,
#     "stop": ["</s>"],
# }
# headers = {
#     "accept": "application/json",
#     "content-type": "application/json",
#     "Authorization": f"Bearer cab10756f89a0d074d013fd4c3af1a003eb1e492edb782cedd6949be4ce1fe54",
# }

# response = requests.post(url, json=payload, headers=headers, stream=True)
# response.raise_for_status()
# print(response.json())

# import tiktoken
# encoding = tiktoken.get_encoding("cl100k_base")
# num_tokens = encoding.encode("\nUser")
# for a in num_tokens:
#     print(a)
#     print("\n")
# import requests

# response = requests.post(
#     "http://localhost:5002/api/inference/chat",
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImd0eSI6WyJhdXRob3JpemF0aW9uX2NvZGUiXSwia2lkIjoibHNXSUM1a2RTVXVteDVySDk2RHpsV1hQbElNIn0.eyJhdWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJleHAiOjE3MDI4MTUyNTIsImlhdCI6MTcwMjIxMDQ1MiwiaXNzIjoidHJ1ZWZvdW5kcnkuY29tIiwic3ViIjoiMTIwMjNlZGEtZmE0Yy00M2NiLWEyZGEtOTViMjk0OTE5M2ExIiwianRpIjoiN2E4Y2VkZmMtOWZmYS00YjM2LTliOTUtZmNjMTk4MGUzMDc5IiwiYXV0aGVudGljYXRpb25UeXBlIjoiR09PR0xFIiwiZW1haWwiOiJha2FzaEB0cnVlZm91bmRyeS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWthc2gtdXNlciIsImFwcGxpY2F0aW9uSWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJzY29wZSI6Im9wZW5pZCBvZmZsaW5lX2FjY2VzcyIsInJvbGVzIjpbInRlbmFudC1hZG1pbiIsInRlbmFudC1zdXBlci1hZG1pbiIsInRydWVmb3VuZHJ5LXN1cGVyLWFkbWluIl0sInNpZCI6ImUwNzE3ZTRlLTk3MDktNDljYi04NDY3LWU3NDU1YTdiNzlhYSIsImF1dGhfdGltZSI6MTcwMjIxMDQ1MiwidGlkIjoiODk1MjUzYWYtZWM5ZC00YmU2LTgzZDEtNmYyNDhlNjQ0ZTc5IiwibWVtYmVyc2hpcHMiOltdLCJ0ZW5hbnROYW1lIjoidHJ1ZWZvdW5kcnkiLCJ1c2VyVHlwZSI6InVzZXIiLCJ1c2VybmFtZSI6ImFrYXNoLXVzZXIifQ.nTGGAU1jPbifAjH_JpRAlOQsS0i_Npucq2sT_cawdsBJdOzOFl22b7XWDHev6IYpXeazIfoyRae099QlZdb9KPDdRY85nHHDEuQ6kHwkriWShi1mBdEV5jeIRiaWthMCK4QH4wjy023BPIDwAr04nrUz8rGU4MZ9zpxuT_MnNkMaF35coMXeWOTlR3ajjaK0V5cebdPzx7qeqWaUhBbzSlKzngmXF6nn734tDRgEVNnTP9KhjZszRIgWQ2Fbpfm9AsMVqgTNCDAWat-OrDTxx6YG4SUzGNV3uZJfTd9YT3TFQcvNihdsXePLhM0lBSKwVaGG4rtDNtmLpx1GouckOw"
#     },
#     json = {
#         "messages": [
#             {"role": "system", "content": "You are an AI bot."},
#             {"role": "user", "content":"Enter your prompt here"}
#         ],
#         "model":
#                 {
#                     "name": "truefoundry-public/Falcon-Instruct(40B)",
#                     "parameters": {
#                         "temperature": 0.75,
#                         "maximum_length": 200,
#                         "top_p": 1.0,
#                         "repetition_penalty": 1.0,
#                         "stop_sequences": [
#                             "</s>",
#                             "User",
#                             "<|endoftext|>"
#                         ]
#                     }
#                 }
#     }
# )
# data = response.json()
# text = data.get('text')
# print(text)


# import together
# together.api_key = "cab10756f89a0d074d013fd4c3af1a003eb1e492edb782cedd6949be4ce1fe54"
# prediction = together.Complete.create(
#             model="togethercomputer/falcon-40b-instruct",
#             prompt="You are an AI bot.User: Enter your prompt here\n\nAssistant:",
#             temperature=0.75,
#             max_tokens=200,
#             top_p=1.0,
#             stop=[
#                             "the",
#                             "User",
#                             "<|endoftext|>"
#                         ],
#             repetition_penalty=1.0
#         )
# output = prediction["output"]["choices"][0]["text"]
# print(output)


# print("omg")
# output = together.Complete.create(
#   prompt = "<human>: What are Isaac Asimov's Three Laws of Robotics?\n<bot>:", 
#   model = "togethercomputer/RedPajama-INCITE-7B-Instruct", 
#   max_tokens = 256,
#   temperature = 0.8,
#   top_k = 60,
#   top_p = 0.6,
#   repetition_penalty = 1.1,
#   stop = ['<human>:', '\n\n']
# )

# # print generated text
# print(output['output']['choices'][0]['text'])

# def text_generation(prompt: str, model_config: dict, model_parameters: dict, provider_account_config: dict):
#     """

#     :param prompt: The prompt to generate text from
#     :param model_config: The model configuration stored in the details of model config
#     :param model_parameters: The model parameters
#     :param provider_account_config: The provider account configuration stored in provider info of config field in provider account
#     :return: The generated text
#     """

# def text_stream_generation(prompt: str, model_config: dict, model_parameters: dict, provider_account_config: dict):
#     """

#     :param prompt: The prompt to generate text from
#     :param model_config: The model configuration stored in the details of model config
#     :param model_parameters: The model parameters
#     :param provider_account_config: The provider account configuration stored in provider info of config field in provider account
#     :return: The generator that yields the tokens
#     """

# class ChatRole(str, Enum):
#     system = "system"
#     user = "user"
#     assistant = "assistant"


# class ChatMessage(Base):
#     role: ChatRole
#     content: str

# def chat_generation(messages: List[ChatMessage], model_config: dict, model_parameters: dict, provider_account_config: dict):
#     """

#     :param messages: The list of messages to generate text from
#     :param model_config: The model configuration stored in the details of model config
#     :param model_parameters: The model parameters
#     :param provider_account_config: The provider account configuration stored in provider info of config field in provider account
#     :return: The generated text
#     """
    
# def chat_stream_generation(messages: List[ChatMessage], model_config: dict, model_parameters: dict, provider_account_config: dict):
#     """

#     :param messages: The list of messages to generate text from
#     :param model_config: The model configuration stored in the details of model config
#     :param model_parameters: The model parameters
#     :param provider_account_config: The provider account configuration stored in provider info of config field in provider account
#     :return: The generator that yields the tokens
#     """

# def embedding_generation(texts: Union[str, List[str], List[int], List[List[int]]], model_config: dict, model_parameters: dict, provider_account_config: dict) -> List[List[float]]:
#     """
#     Generate text from a prompt using a model

#     :param messages: The prompt to generate text from
#     :param model_config: The model configuration stored in the details of model config
#     :param model_parameters: The model parameters
#     :param provider_account_config: The provider account configuration stored in provider info of config field in provider account
#     :return: The list of list of floating point numbers representing the embeddings
#     """


# from openai import OpenAI

# client = OpenAI(api_key="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")
# stream = client.chat.completions.create(
#     model="gpt-4",
#     messages=[{"role": "user", "content": 'hii'}],
#     stream=True,
# )
# print(stream)
# for chunk in stream:
#     print(chunk)
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")


# import requests
# import json
# # Note: use sseclient-py and NOT sseclient
# import sseclient

# response = requests.post(
#     "http://localhost:5002/api/inference/openai/completions",
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImd0eSI6WyJhdXRob3JpemF0aW9uX2NvZGUiXSwia2lkIjoibHNXSUM1a2RTVXVteDVySDk2RHpsV1hQbElNIn0.eyJhdWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJleHAiOjE3MDI4ODUyNzUsImlhdCI6MTcwMjI4MDQ3NSwiaXNzIjoidHJ1ZWZvdW5kcnkuY29tIiwic3ViIjoiMWVmNGFlMWUtZDE2OC00Y2Q3LWJkNzMtODlmZWU1NmVjYzM3IiwianRpIjoiNjgyMWVhYzctNDg0Yy00MjA3LTgyMzQtMmVhNjExNjZlMWU5IiwiYXV0aGVudGljYXRpb25UeXBlIjoiUElORyIsImVtYWlsIjoibmlyYW5zaGlAdHJ1ZWZvdW5kcnkuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInByZWZlcnJlZF91c2VybmFtZSI6Im5pcmFuc2hpIiwiYXBwbGljYXRpb25JZCI6Ijg5NTI1M2FmLWVjOWQtNGJlNi04M2QxLTZmMjQ4ZTY0NGU3OSIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIiwicm9sZXMiOlsidGVuYW50LWFkbWluIl0sInNpZCI6ImI3M2YxMjUzLWJkNmQtNGM4Ny1iY2MwLTI5NzVmZTIzNWJkYiIsImF1dGhfdGltZSI6MTcwMjI4MDQ3NSwidGlkIjoiODk1MjUzYWYtZWM5ZC00YmU2LTgzZDEtNmYyNDhlNjQ0ZTc5IiwibWVtYmVyc2hpcHMiOltdLCJ0ZW5hbnROYW1lIjoidHJ1ZWZvdW5kcnkiLCJ1c2VyVHlwZSI6InVzZXIiLCJ1c2VybmFtZSI6Im5pcmFuc2hpIn0.Krgb1xPegMq5ji84NGV7xIk0vO1y7ZQiuT4tL386rdCuwqp6fKloS2gMjQLTeb14hEK9ervSlhDVM44W2x-a1tF4i8JlpxHkBLAU5fZdjigGweqyRTrIOULkZQhfMIboBmwtInf99jAVUa4H_DpTX_vMpC9BqkG01JS23rswejp6Uibqdg-27HOSl0MVzkUBE37OCK7tV8J-WTOk0m81ls9yeNCr6lbqT2JaOBVNpY7sAitoF7m6atyGMH50UPptmDk1YXYq611RkFvOTQRQb67bZJIQs_AhNdamSH7TSwrfVvOSxge2bXxQx1lrRwqmWRBzSG5PJjHWMjVlG9pNqg",
#     },
#     json = {
#                     "model": "truefoundry-public/Llama-2(7B)",
#                     "prompt": "Enter your prompt here",
#                     "temperature": 0.7,
#                     "max_tokens": 500,
#                     "top_p": 0.95,
#                     "top_k": 50,
#                     "repetition_penalty": 1.2,
#                     "stop": [
#                         "</s>"
#                     ]
#                 },
# )
# response = response.json()
# output = response['choices'][0]['text']
# print(output)

# print("\n\n")

# import requests
# import json
# # Note: use sseclient-py and NOT sseclient
# import sseclient

# response = requests.post(
#     "http://localhost:5002/api/inference/openai/completions",
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImd0eSI6WyJhdXRob3JpemF0aW9uX2NvZGUiXSwia2lkIjoibHNXSUM1a2RTVXVteDVySDk2RHpsV1hQbElNIn0.eyJhdWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJleHAiOjE3MDI4ODUyNzUsImlhdCI6MTcwMjI4MDQ3NSwiaXNzIjoidHJ1ZWZvdW5kcnkuY29tIiwic3ViIjoiMWVmNGFlMWUtZDE2OC00Y2Q3LWJkNzMtODlmZWU1NmVjYzM3IiwianRpIjoiNjgyMWVhYzctNDg0Yy00MjA3LTgyMzQtMmVhNjExNjZlMWU5IiwiYXV0aGVudGljYXRpb25UeXBlIjoiUElORyIsImVtYWlsIjoibmlyYW5zaGlAdHJ1ZWZvdW5kcnkuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInByZWZlcnJlZF91c2VybmFtZSI6Im5pcmFuc2hpIiwiYXBwbGljYXRpb25JZCI6Ijg5NTI1M2FmLWVjOWQtNGJlNi04M2QxLTZmMjQ4ZTY0NGU3OSIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIiwicm9sZXMiOlsidGVuYW50LWFkbWluIl0sInNpZCI6ImI3M2YxMjUzLWJkNmQtNGM4Ny1iY2MwLTI5NzVmZTIzNWJkYiIsImF1dGhfdGltZSI6MTcwMjI4MDQ3NSwidGlkIjoiODk1MjUzYWYtZWM5ZC00YmU2LTgzZDEtNmYyNDhlNjQ0ZTc5IiwibWVtYmVyc2hpcHMiOltdLCJ0ZW5hbnROYW1lIjoidHJ1ZWZvdW5kcnkiLCJ1c2VyVHlwZSI6InVzZXIiLCJ1c2VybmFtZSI6Im5pcmFuc2hpIn0.Krgb1xPegMq5ji84NGV7xIk0vO1y7ZQiuT4tL386rdCuwqp6fKloS2gMjQLTeb14hEK9ervSlhDVM44W2x-a1tF4i8JlpxHkBLAU5fZdjigGweqyRTrIOULkZQhfMIboBmwtInf99jAVUa4H_DpTX_vMpC9BqkG01JS23rswejp6Uibqdg-27HOSl0MVzkUBE37OCK7tV8J-WTOk0m81ls9yeNCr6lbqT2JaOBVNpY7sAitoF7m6atyGMH50UPptmDk1YXYq611RkFvOTQRQb67bZJIQs_AhNdamSH7TSwrfVvOSxge2bXxQx1lrRwqmWRBzSG5PJjHWMjVlG9pNqg",
#     },
#     json = 
#                 {
#                     "model": "truefoundry-public/Llama-2(13B)",
#                     "prompt": "Enter your prompt here",
#                     "temperature": 0.7,
#                     "max_tokens": 10,
#                     "top_p": 0.95,
#                     "top_k": 50,
#                     "repetition_penalty": 1.2,
#                     "stop": [
#                         "</s>"
#                     ],
#                     "stream": True
#                 },
#     stream=True
# )
# client = sseclient.SSEClient(response)
# for event in client.events():
#     if event.data != "[DONE]":
#         print(json.loads(event.data)["choices"][0]["text"])


# response = requests.post(
#     "https://api.openai.com/v1/chat/completions",
#     headers = {
#         "accept": "application/json",
#     "content-type": "application/json",
#         "Authorization": "Bearer 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",
#     },
#     json = 
#                 {
#      "model": "gpt-4",
#      "messages": [{"role": "user", "content": "Say this is a test!"}],
#      "temperature": 0.7,
#      "stream": True,
#    },
#     stream=True
# )
# client = sseclient.SSEClient(response)
# for event in client.events():
#     print(event.data)



# # import requests

# # url = "https://api.fireworks.ai/inference/v1/completions"

# # payload = {
# #     "max_tokens": 16,
# #     "temperature": 1,
# #     "top_p": 1,
# #     "n": 1,
# #     "frequency_penalty": 0,
# #     "presence_penalty": 0,
# #     "stream": True,
# #     "logprobs": 0,
# #     "stop": "string",
# #     "echo": False,
# #     "model": "accounts/fireworks/models/llama-v2-7b",
# #     "prompt": "The sky is",
# #     "context_length_exceeded_behavior": "truncate",
# #     "top_k": 50
# # }
# # headers = {
# #     "accept": "application/json",
# #     "content-type": "application/json",
# #     "authorization": "Bearer tDHne9IUk0YAhWwHl7eeGAkzxjUCjR8MLdDt25D2qEkrJYd3"
# # }

# # response = requests.post(url, json=payload, headers=headers, stream=True)

# # for chunk in response:
# #     print(chunk)
    

# import requests
# import json
# # Note: use sseclient-py and NOT sseclient
# import sseclient

# response = requests.post(
#     "http://localhost:5002/api/inference/openai/embeddings",
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImd0eSI6WyJhdXRob3JpemF0aW9uX2NvZGUiXSwia2lkIjoibHNXSUM1a2RTVXVteDVySDk2RHpsV1hQbElNIn0.eyJhdWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJleHAiOjE3MDI4ODUyNzUsImlhdCI6MTcwMjI4MDQ3NSwiaXNzIjoidHJ1ZWZvdW5kcnkuY29tIiwic3ViIjoiMWVmNGFlMWUtZDE2OC00Y2Q3LWJkNzMtODlmZWU1NmVjYzM3IiwianRpIjoiNjgyMWVhYzctNDg0Yy00MjA3LTgyMzQtMmVhNjExNjZlMWU5IiwiYXV0aGVudGljYXRpb25UeXBlIjoiUElORyIsImVtYWlsIjoibmlyYW5zaGlAdHJ1ZWZvdW5kcnkuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInByZWZlcnJlZF91c2VybmFtZSI6Im5pcmFuc2hpIiwiYXBwbGljYXRpb25JZCI6Ijg5NTI1M2FmLWVjOWQtNGJlNi04M2QxLTZmMjQ4ZTY0NGU3OSIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIiwicm9sZXMiOlsidGVuYW50LWFkbWluIl0sInNpZCI6ImI3M2YxMjUzLWJkNmQtNGM4Ny1iY2MwLTI5NzVmZTIzNWJkYiIsImF1dGhfdGltZSI6MTcwMjI4MDQ3NSwidGlkIjoiODk1MjUzYWYtZWM5ZC00YmU2LTgzZDEtNmYyNDhlNjQ0ZTc5IiwibWVtYmVyc2hpcHMiOltdLCJ0ZW5hbnROYW1lIjoidHJ1ZWZvdW5kcnkiLCJ1c2VyVHlwZSI6InVzZXIiLCJ1c2VybmFtZSI6Im5pcmFuc2hpIn0.Krgb1xPegMq5ji84NGV7xIk0vO1y7ZQiuT4tL386rdCuwqp6fKloS2gMjQLTeb14hEK9ervSlhDVM44W2x-a1tF4i8JlpxHkBLAU5fZdjigGweqyRTrIOULkZQhfMIboBmwtInf99jAVUa4H_DpTX_vMpC9BqkG01JS23rswejp6Uibqdg-27HOSl0MVzkUBE37OCK7tV8J-WTOk0m81ls9yeNCr6lbqT2JaOBVNpY7sAitoF7m6atyGMH50UPptmDk1YXYq611RkFvOTQRQb67bZJIQs_AhNdamSH7TSwrfVvOSxge2bXxQx1lrRwqmWRBzSG5PJjHWMjVlG9pNqg",
#     },
#     json = 
#                 {
#                     "model": "openai-main/text-embedding-ada-002",
#                     "input": "helloooo"
#                 },
# )
# print(response)
# data = response.json()
# output = [embed['embedding'] for embed in data['data']]
# print(output)
# client = sseclient.SSEClient(response)
# for event in client.events():
#     if event.data != "[DONE]":
#         data = json.loads(event.data)
#         print(data['choices'][0]['delta']['content'], end="")


# import requests
# import json
# # Note: use sseclient-py and NOT sseclient
# import sseclient

# response = requests.post(
#     "http://localhost:5002/api/inference/openai/chat/completions",
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImd0eSI6WyJhdXRob3JpemF0aW9uX2NvZGUiXSwia2lkIjoibHNXSUM1a2RTVXVteDVySDk2RHpsV1hQbElNIn0.eyJhdWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJleHAiOjE3MDI4ODUyNzUsImlhdCI6MTcwMjI4MDQ3NSwiaXNzIjoidHJ1ZWZvdW5kcnkuY29tIiwic3ViIjoiMWVmNGFlMWUtZDE2OC00Y2Q3LWJkNzMtODlmZWU1NmVjYzM3IiwianRpIjoiNjgyMWVhYzctNDg0Yy00MjA3LTgyMzQtMmVhNjExNjZlMWU5IiwiYXV0aGVudGljYXRpb25UeXBlIjoiUElORyIsImVtYWlsIjoibmlyYW5zaGlAdHJ1ZWZvdW5kcnkuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInByZWZlcnJlZF91c2VybmFtZSI6Im5pcmFuc2hpIiwiYXBwbGljYXRpb25JZCI6Ijg5NTI1M2FmLWVjOWQtNGJlNi04M2QxLTZmMjQ4ZTY0NGU3OSIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIiwicm9sZXMiOlsidGVuYW50LWFkbWluIl0sInNpZCI6ImI3M2YxMjUzLWJkNmQtNGM4Ny1iY2MwLTI5NzVmZTIzNWJkYiIsImF1dGhfdGltZSI6MTcwMjI4MDQ3NSwidGlkIjoiODk1MjUzYWYtZWM5ZC00YmU2LTgzZDEtNmYyNDhlNjQ0ZTc5IiwibWVtYmVyc2hpcHMiOltdLCJ0ZW5hbnROYW1lIjoidHJ1ZWZvdW5kcnkiLCJ1c2VyVHlwZSI6InVzZXIiLCJ1c2VybmFtZSI6Im5pcmFuc2hpIn0.Krgb1xPegMq5ji84NGV7xIk0vO1y7ZQiuT4tL386rdCuwqp6fKloS2gMjQLTeb14hEK9ervSlhDVM44W2x-a1tF4i8JlpxHkBLAU5fZdjigGweqyRTrIOULkZQhfMIboBmwtInf99jAVUa4H_DpTX_vMpC9BqkG01JS23rswejp6Uibqdg-27HOSl0MVzkUBE37OCK7tV8J-WTOk0m81ls9yeNCr6lbqT2JaOBVNpY7sAitoF7m6atyGMH50UPptmDk1YXYq611RkFvOTQRQb67bZJIQs_AhNdamSH7TSwrfVvOSxge2bXxQx1lrRwqmWRBzSG5PJjHWMjVlG9pNqg",
#     },
#     json = 
#                 {
#                     "model": "openai-main/gpt-3-5-turbo",
#                     "messages": [{"role": "user", "content": "Say this is a test!"}],
#                     "max_tokens": 200,
#                     "top_p": 1.0,
#                     "presence_penalty": 0.0,
#                     "frequency_penalty": 0.0,
#                     "stream": True
#                 },
#     stream=True
# )

# client = sseclient.SSEClient(response)
# for event in client.events():
#     if event.data != "[DONE]":
#         data = json.loads(event.data)
#         print(data['choices'][0]['delta']['content'], end="")



# import requests
# import json
# # Note: use sseclient-py and NOT sseclient
# import sseclient

# response = requests.post(
#     "test/api/inference/openai/completions",
#     headers = {
#         "Authorization": "Bearer <Add your API KEY here>",
#     },
#     json = {
#     "stream": True,
#         "model": "truefoundry-public/Zephyr-Beta(7B)",
#         "prompt": "<|system|>\\n</s>\\n<|user|>\\nEnter your prompt here</s>\\n<|assistant|>",
#         "temperature": 0.8,
#         "max_tokens": 128,
#         "top_p": 0.95,
#         "top_k": 50,
#         "presence_penalty": 1.0,
#         "stop": [
#             "</s>"
#         ]
# },
#     stream=True
# )

# client = sseclient.SSEClient(response)
# for event in client.events():
#     if event.data != "[DONE]":
#         data = json.loads(event.data)
#         print(data['choices'][0]['text'], end="")


# import google.generativeai as palm
# from google.generativeai.client import _ClientManager

# client = _ClientManager()
# client.configure(api_key="ya29.a0AfB_byCXct22k6-vlHNqP7AkpY2QpsXcuxwbnKM0BuAhRd_p5q5HUW1_ScgJD1XEIgOjp_iBRG9ebGvSBT7uWREJrkeUuuWOf8HiUlJFBruFWe9yhQ6h6qLkvM1PD-rp8KjW85ypT1X5CeblO7K5YqmWwp_A4x4eEQlj-k_vY6N6aCgYKAcwSARMSFQHGX2MiVYxrESiXJiWTh0AqFQDEMQ0179")

# x = 'What do squirrels eat?'
# model = "models/embedding-gecko-001"


# # Create an embedding
# # embedding_x = palm.generate_embeddings(model=model, text=x)
# embedding_x = client.client_config
# print(client)
# palm.generate_embeddings(model=model, text=x, client=client.get_default_client("text"))

# from  openai import OpenAI, AzureOpenAI
# # # openai.completions.create(api_type='azure')
# try:
#     client = OpenAI(api_key='sk-EfgZ8lVFIFKoSZ4Gq7kHT3BlbkFJTcgBpTs53En5oDPaNgg')
#     resp = client.completions.create(
#     model="text-davinci-003",
#     prompt="Say this is a test"
#     )
#     for event in resp:
#         print(event)
# except OpenAIError as e:
#     print(e.args )
#     print(e)
# print(client.base_url)
# print(openai)
import asyncio
from openai import AsyncOpenAI
print("hiiii")
async def fun():
    client = AsyncOpenAI(api_key='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImd0eSI6WyJhdXRob3JpemF0aW9uX2NvZGUiXSwia2lkIjoibHNXSUM1a2RTVXVteDVySDk2RHpsV1hQbElNIn0.eyJhdWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJleHAiOjE3MDM0OTMyNTksImlhdCI6MTcwMjg4ODQ1OSwiaXNzIjoidHJ1ZWZvdW5kcnkuY29tIiwic3ViIjoiMWVmNGFlMWUtZDE2OC00Y2Q3LWJkNzMtODlmZWU1NmVjYzM3IiwianRpIjoiMDU5NWQ0NjEtZTcwZC00ZTAxLWEwMmMtYjNiMmM0NDMyYmM4IiwiYXV0aGVudGljYXRpb25UeXBlIjoiR09PR0xFIiwiZW1haWwiOiJuaXJhbnNoaUB0cnVlZm91bmRyeS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoibmlyYW5zaGkiLCJhcHBsaWNhdGlvbklkIjoiODk1MjUzYWYtZWM5ZC00YmU2LTgzZDEtNmYyNDhlNjQ0ZTc5Iiwic2NvcGUiOiJvcGVuaWQgb2ZmbGluZV9hY2Nlc3MiLCJyb2xlcyI6WyJ0ZW5hbnQtYWRtaW4iXSwic2lkIjoiZWY2NDFmNmItNDAwMS00NjAzLWEzZjMtNTlhZTc4OGU3MzcxIiwiYXV0aF90aW1lIjoxNzAyODg4NDU5LCJ0aWQiOiI4OTUyNTNhZi1lYzlkLTRiZTYtODNkMS02ZjI0OGU2NDRlNzkiLCJtZW1iZXJzaGlwcyI6W10sInRlbmFudE5hbWUiOiJ0cnVlZm91bmRyeSIsInVzZXJUeXBlIjoidXNlciIsInVzZXJuYW1lIjoibmlyYW5zaGkifQ.caBZSpeTD34sq7V6GXohhDCGrLz-hi9oP6YB6fgYDDGvjPiYmo9SIHKwNmIMOO3r9kmZE-1YQsvZ0uw99dtPnyDejDVAFiOVH6_y4kXdQ0L-UvqqfH8uOLbjwnJcaGxdjtSUlZgWTo0nNkX1yPIOF_ykl82NbEw6vkrO_mLhmEhC6_VsoFqasLCVAJ9PZSssGGcmQBR0QBgSUw37PAdUqnmxoCvaaARjaBfDXqB2zFmnz1-rNXnahTbylOZViJSKPIx8T74jhl0zPx1q9eIRDgrRhLHSo0P4yHUgsFCgnwxzMbwa9MCCx_SbqbJo9zb1VSP5hL727sDHuxCxPgzhrw', base_url="http://localhost:5002/api/inference/openai")
    try:
        resp = await client.completions.create(
        model="truefoundry-public/Llama-2(7B)",
        prompt="Say this is a test",
        stream=True
        )
        print(resp)
        async for a in resp:
            print("yes")
            print(a)
    except Exception as e:
        print(e)
        print(e.args)
asyncio.run(fun())
# client = AzureOpenAI(api_version="2023-05-15", api_key="6a6484661f884870b19b5e3069b156c5", azure_endpoint='https://gateway-test.openai.azure.com/')
# resp = client.completions.create(
#   model="nikp-test",
#   prompt="hi",
#   max_tokens=7,
#   temperature=0.3,
# )
# print(resp.choices[0].text)
    


dotenv.load_dotenv(".env")
@app.get("/")
async def root():
    await asyncio.sleep(0.1)
    return {"message": "Hello World"}
