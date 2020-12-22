# microservice for various generic meterological functions

from flask import Flask, jsonify, request

import windrose
import met_funcs
import call_rest_api


app = Flask(__name__)
version = '1.0.0'

# fixme : this does not give info about the actual exception
@app.errorhandler(500)
def error_handling(error):
    answer = {}
    answer['Error'] = str(error)
    response = jsonify(answer, 500)
    return response

# an endpoint that can be polled with little overhead
@app.route('/status')
def status():
    answer = {}
    answer['status'] = 'OK'
    answer['version'] = version
    response = jsonify(answer)

    return response


@app.route('/wind_deg_to_wind_rose')
def get_wind_rose_api():
    answer = {}

    wind_deg = int(request.args.get('wind_deg', None))

    wind_rose_id, wind_rose = windrose.get_wind_rose(wind_deg)

    # Put in the calling parameters to aid debugging
    answer['wind_deg'] = wind_deg
    answer['wind_rose_id'] = wind_rose_id
    answer['wind_rose'] = wind_rose

    response = jsonify(answer)

    return response


@app.route('/wind_deg_to_quadrant')
def wind_deg_to_quadrant_api():
    answer = {}

    wind_deg = int(request.args.get('wind_deg', None))

    wind_quadrant = met_funcs.wind_deg_to_quadrant(wind_deg)

    # Put in the calling parameters to aid debugging
    answer['wind_deg'] = wind_deg

    answer['wind_quadrant'] = wind_quadrant

    response = jsonify(answer)

    return response


@app.route('/wind_deg_to_wind_dir')
def wind_deg_to_wind_dir_api():
    answer = {}

    wind_deg = int(request.args.get('wind_deg', None))

    wind_dir = 'GOT TO HERE'
    # Rest call to met_funcs microservice
    query = {'wind_deg': wind_deg}
    response_dict = call_rest_api.call_rest_api('http://127.0.0.1:9500/wind_deg_to_wind_rose', query)
    if response_dict is None:
        return None
    wind = response_dict['wind_rose_id']

    # Put in the calling parameters to aid debugging
    answer['wind_deg'] = wind_deg
    answer['wind_dir'] = wind_dir

    response = jsonify(answer)

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9500)
