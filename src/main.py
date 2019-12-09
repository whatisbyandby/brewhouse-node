import os
from dotenv import load_dotenv
from quart import Quart, request, Response
import rest_controller


app = Quart(__name__)
load_dotenv()


@app.route('/step', methods=['GET', 'POST'])
async def step():
    response = await rest_controller.handle_request(request, Response)
    return response


@app.route('/start', methods=['POST'])
async def start():
    response = await rest_controller.handle_start_request(request, Response)
    return response


@app.route('/stop', methods=['POST'])
async def stop():
    response = await rest_controller.handle_stop_request(request, Response)
    return response


if __name__ == '__main__':
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))
