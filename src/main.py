from quart import Quart, request, Response
import rest_controller

app = Quart(__name__)


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
async def root():
    response = await rest_controller.handle_request(request, Response)
    return response


@app.route('/start')
async def start():
    print('Start request')
    response = await rest_controller.handle_start_request(request, Response)
    return response

@app.route('/stop')
async def stop():
    print('Stop Request')
    response = await rest_controller.handle_stop_request(request, Response)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
