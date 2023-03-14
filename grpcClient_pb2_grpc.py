# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import grpcClient_pb2 as grpcClient__pb2


class InvoicerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddTxToBlockchain = channel.unary_unary(
                '/Invoicer/AddTxToBlockchain',
                request_serializer=grpcClient__pb2.CreateTx.SerializeToString,
                response_deserializer=grpcClient__pb2.CreateResponse.FromString,
                )
        self.GetLastBlock = channel.unary_unary(
                '/Invoicer/GetLastBlock',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=grpcClient__pb2.CreateResponse.FromString,
                )
        self.GetBlockchain = channel.unary_unary(
                '/Invoicer/GetBlockchain',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=grpcClient__pb2.CreateResponse.FromString,
                )
        self.GetUserTxHistory = channel.unary_unary(
                '/Invoicer/GetUserTxHistory',
                request_serializer=grpcClient__pb2.User.SerializeToString,
                response_deserializer=grpcClient__pb2.CreateResponse.FromString,
                )


class InvoicerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddTxToBlockchain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLastBlock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlockchain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserTxHistory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InvoicerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddTxToBlockchain': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTxToBlockchain,
                    request_deserializer=grpcClient__pb2.CreateTx.FromString,
                    response_serializer=grpcClient__pb2.CreateResponse.SerializeToString,
            ),
            'GetLastBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLastBlock,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=grpcClient__pb2.CreateResponse.SerializeToString,
            ),
            'GetBlockchain': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlockchain,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=grpcClient__pb2.CreateResponse.SerializeToString,
            ),
            'GetUserTxHistory': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserTxHistory,
                    request_deserializer=grpcClient__pb2.User.FromString,
                    response_serializer=grpcClient__pb2.CreateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Invoicer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Invoicer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddTxToBlockchain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Invoicer/AddTxToBlockchain',
            grpcClient__pb2.CreateTx.SerializeToString,
            grpcClient__pb2.CreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLastBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Invoicer/GetLastBlock',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            grpcClient__pb2.CreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlockchain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Invoicer/GetBlockchain',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            grpcClient__pb2.CreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserTxHistory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Invoicer/GetUserTxHistory',
            grpcClient__pb2.User.SerializeToString,
            grpcClient__pb2.CreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
