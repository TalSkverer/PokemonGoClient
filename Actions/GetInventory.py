import ResponseEnvelop_pb2
from Util import NetUtil
from Requests import GetInventoryRequest_pb2
from Responses import GetInventoryResponse_pb2

class GetInventory(object):
	
	def __init__(self, raw_request, url, logger=None):
		self.request = raw_request
		self.url = url
		self.logger = logger
	

	def _handle_response(self, response):
		response_envelop = ResponseEnvelop_pb2.ResponseEnvelop()
		response_envelop.ParseFromString(response.content)
		get_inventory_response = GetInventoryResponse_pb2.GetInventoryResponse()
		get_inventory_response.ParseFromString(response_envelop.responses[0])
		assert get_inventory_response

		if self.logger:
			self.logger.info("Received GET_INVENTORY response:\r\n")
			self.logger.debug("%s" % get_inventory_response)
		return get_inventory_response

	
	def get(self):
		data = self.request.SerializeToString()

		if self.logger:
			self.logger.info("Sending GET_INVENTORY request:\r\n")
			self.logger.debug("%s" % self.request)
		return self._handle_response(NetUtil.request("POST", self.url, data))