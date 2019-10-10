from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from starlette.config import Config
import uvicorn
import os
from fastai import *
from fastai.vision import *
import urllib
from io import BytesIO
import aiohttp

async def get_bytes(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()

app = Starlette(debug=True)

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['*'], allow_methods=['*'])

### EDIT CODE BELOW ###

answer_question_1 = """
Underfitting: if our training data is not enough we will not be able to generalize, that means that our model will not be able to predict due to the lack of information
Overfitting: its when our model learns a bunch of particular cases that we provide but its incapable of recognizing new slightly different data

"""

answer_question_2 = """
We use it when the loss function is non-linear, and allow us to find the lowest value of a function. How it works: before anything the algorithm choose a random value of the
function and with every iterarion and using the gradient to know in wich direction to proced and learning rate to get magnitude of the step, updates the function so we get
closer to the lowest point.
"""

answer_question_3 = """
The main goal of regression is to analyze and predict variables using more variables. training with datasets as a start to predict continuous-valued output
"""


model_50 = load_learner('.', file='export.pkl')

@app.route("/api/answers_to_hw", methods=["GET"])
async def answers_to_hw(request):
    return JSONResponse([answer_question_1, answer_question_2, answer_question_3])

@app.route("/api/class_list", methods=["GET"])
async def class_list(request):
    return JSONResponse([ 'nes','supern','n64','gamecube' ])

@app.route("/api/classify", methods=["POST"])
async def classify_url(request):
    body = await request.json()
    url_to_predict = body["url"]

    bytes = await get_bytes(url_to_predict)
    img = open_image(BytesIO(bytes))
    preds, _, _ = model_50.predict(img)

    return JSONResponse({
        "predictions": str(preds),
    })

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ['PORT']))
