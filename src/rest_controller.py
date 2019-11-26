from temp_controller import TempController
from encoder import EnhancedJSONEncoder
import json

temp_cont = TempController()


async def handle_request(request, response):
    if request.method == 'GET':
        current_step = temp_cont.get_step()
        return response(json.dumps(current_step, cls=EnhancedJSONEncoder), mimetype="application/json")
    elif request.method == 'POST':
        data = await request.json
        try:
            current_step = temp_cont.add_step(data)
        except TypeError as e:
            message = "Bad Request " + str(e)
            return message, 400
        return response(json.dumps(current_step, cls=EnhancedJSONEncoder), mimetype="application/json")
    elif request.method == 'PUT':
        current_step = temp_cont.get_step()
        return response(json.dumps(current_step, cls=EnhancedJSONEncoder), mimetype="application/json")
    elif request.method == 'DELETE':
        current_step = temp_cont.delete_step()
        return response(json.dumps(current_step, cls=EnhancedJSONEncoder), mimetype="application/json")
    else:
        return "method not allowed", 405


async def handle_start_request(request, response):
    temp_cont.run_step()
    return response('This is the response')

async def handle_stop_request(request, response):
    print('Stop Request')
    temp_cont.stop()
    return response('Stop Request')


