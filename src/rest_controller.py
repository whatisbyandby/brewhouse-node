from step_controller import StepController
from encoder import EnhancedJSONEncoder
import json

step_cont = StepController()



async def handle_request(request, response):
    if request.method == 'GET':
        current_step = step_cont.get_steps()
        return response(json.dumps(current_step, cls=EnhancedJSONEncoder), mimetype="application/json")
    elif request.method == 'POST':
        data = await request.json
        try:
            current_step = step_cont.set_steps(data)
        except TypeError as e:
            message = "Bad Request " + str(e)
            return message, 400
        return response(json.dumps(current_step, cls=EnhancedJSONEncoder), mimetype="application/json")
    else:
        return "method not allowed", 405


async def handle_start_request(request, response):
    started = step_cont.start()
    if started:
        return response('Started the steps')
    else:
        return response('There were no steps to start')


async def handle_stop_request(request, response):
    print('Stop Request')
    step_cont.stop()
    return response('Stop Request')


