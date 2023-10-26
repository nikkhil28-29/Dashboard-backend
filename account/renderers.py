
#imp- if there is any kind of error(wromg pass, blank left.....) , it will come in ErrorDetail.
from rest_framework import renderers
import json

class MyUserRenderers(renderers.JSONRenderer):
  charset='utf-8'
  def render(self, data, accepted_media_type=None, renderer_context=None):
    response = ''
    if 'ErrorDetail' in str(data):
      response = json.dumps({'errors':data})
    else:
      response = json.dumps(data)
    
    return response
