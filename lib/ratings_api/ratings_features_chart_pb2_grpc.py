# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ratings_features_chart_pb2 as ratings__features__chart__pb2


class ChartStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetChart = channel.unary_unary(
                '/ratings.features.chart.Chart/GetChart',
                request_serializer=ratings__features__chart__pb2.GetChartRequest.SerializeToString,
                response_deserializer=ratings__features__chart__pb2.GetChartResponse.FromString,
                )


class ChartServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetChart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChartServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetChart': grpc.unary_unary_rpc_method_handler(
                    servicer.GetChart,
                    request_deserializer=ratings__features__chart__pb2.GetChartRequest.FromString,
                    response_serializer=ratings__features__chart__pb2.GetChartResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ratings.features.chart.Chart', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Chart(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetChart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ratings.features.chart.Chart/GetChart',
            ratings__features__chart__pb2.GetChartRequest.SerializeToString,
            ratings__features__chart__pb2.GetChartResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
