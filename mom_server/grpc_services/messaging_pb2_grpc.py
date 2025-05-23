# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from mom_server.grpc_services import messaging_pb2 as mom__server_dot_grpc__services_dot_messaging__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in mom_server/grpc_services/messaging_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class MessagingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReplicateMessage = channel.unary_unary(
                '/messaging.MessagingService/ReplicateMessage',
                request_serializer=mom__server_dot_grpc__services_dot_messaging__pb2.MessageRequest.SerializeToString,
                response_deserializer=mom__server_dot_grpc__services_dot_messaging__pb2.MessageResponse.FromString,
                _registered_method=True)
        self.CreateTopic = channel.unary_unary(
                '/messaging.MessagingService/CreateTopic',
                request_serializer=mom__server_dot_grpc__services_dot_messaging__pb2.TopicRequest.SerializeToString,
                response_deserializer=mom__server_dot_grpc__services_dot_messaging__pb2.TopicResponse.FromString,
                _registered_method=True)
        self.DeleteTopic = channel.unary_unary(
                '/messaging.MessagingService/DeleteTopic',
                request_serializer=mom__server_dot_grpc__services_dot_messaging__pb2.TopicRequest.SerializeToString,
                response_deserializer=mom__server_dot_grpc__services_dot_messaging__pb2.TopicResponse.FromString,
                _registered_method=True)
        self.ListTopics = channel.unary_unary(
                '/messaging.MessagingService/ListTopics',
                request_serializer=mom__server_dot_grpc__services_dot_messaging__pb2.EmptyRequest.SerializeToString,
                response_deserializer=mom__server_dot_grpc__services_dot_messaging__pb2.TopicsListResponse.FromString,
                _registered_method=True)
        self.CreateQueue = channel.unary_unary(
                '/messaging.MessagingService/CreateQueue',
                request_serializer=mom__server_dot_grpc__services_dot_messaging__pb2.QueueRequest.SerializeToString,
                response_deserializer=mom__server_dot_grpc__services_dot_messaging__pb2.QueueResponse.FromString,
                _registered_method=True)
        self.DeleteQueue = channel.unary_unary(
                '/messaging.MessagingService/DeleteQueue',
                request_serializer=mom__server_dot_grpc__services_dot_messaging__pb2.QueueRequest.SerializeToString,
                response_deserializer=mom__server_dot_grpc__services_dot_messaging__pb2.QueueResponse.FromString,
                _registered_method=True)
        self.ListQueues = channel.unary_unary(
                '/messaging.MessagingService/ListQueues',
                request_serializer=mom__server_dot_grpc__services_dot_messaging__pb2.EmptyRequest.SerializeToString,
                response_deserializer=mom__server_dot_grpc__services_dot_messaging__pb2.QueuesListResponse.FromString,
                _registered_method=True)
        self.SendMessageToQueue = channel.unary_unary(
                '/messaging.MessagingService/SendMessageToQueue',
                request_serializer=mom__server_dot_grpc__services_dot_messaging__pb2.QueueMessageRequest.SerializeToString,
                response_deserializer=mom__server_dot_grpc__services_dot_messaging__pb2.MessageResponse.FromString,
                _registered_method=True)


class MessagingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ReplicateMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTopic(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTopic(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTopics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateQueue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteQueue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListQueues(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMessageToQueue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MessagingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReplicateMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicateMessage,
                    request_deserializer=mom__server_dot_grpc__services_dot_messaging__pb2.MessageRequest.FromString,
                    response_serializer=mom__server_dot_grpc__services_dot_messaging__pb2.MessageResponse.SerializeToString,
            ),
            'CreateTopic': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTopic,
                    request_deserializer=mom__server_dot_grpc__services_dot_messaging__pb2.TopicRequest.FromString,
                    response_serializer=mom__server_dot_grpc__services_dot_messaging__pb2.TopicResponse.SerializeToString,
            ),
            'DeleteTopic': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTopic,
                    request_deserializer=mom__server_dot_grpc__services_dot_messaging__pb2.TopicRequest.FromString,
                    response_serializer=mom__server_dot_grpc__services_dot_messaging__pb2.TopicResponse.SerializeToString,
            ),
            'ListTopics': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTopics,
                    request_deserializer=mom__server_dot_grpc__services_dot_messaging__pb2.EmptyRequest.FromString,
                    response_serializer=mom__server_dot_grpc__services_dot_messaging__pb2.TopicsListResponse.SerializeToString,
            ),
            'CreateQueue': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateQueue,
                    request_deserializer=mom__server_dot_grpc__services_dot_messaging__pb2.QueueRequest.FromString,
                    response_serializer=mom__server_dot_grpc__services_dot_messaging__pb2.QueueResponse.SerializeToString,
            ),
            'DeleteQueue': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteQueue,
                    request_deserializer=mom__server_dot_grpc__services_dot_messaging__pb2.QueueRequest.FromString,
                    response_serializer=mom__server_dot_grpc__services_dot_messaging__pb2.QueueResponse.SerializeToString,
            ),
            'ListQueues': grpc.unary_unary_rpc_method_handler(
                    servicer.ListQueues,
                    request_deserializer=mom__server_dot_grpc__services_dot_messaging__pb2.EmptyRequest.FromString,
                    response_serializer=mom__server_dot_grpc__services_dot_messaging__pb2.QueuesListResponse.SerializeToString,
            ),
            'SendMessageToQueue': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessageToQueue,
                    request_deserializer=mom__server_dot_grpc__services_dot_messaging__pb2.QueueMessageRequest.FromString,
                    response_serializer=mom__server_dot_grpc__services_dot_messaging__pb2.MessageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'messaging.MessagingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('messaging.MessagingService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class MessagingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ReplicateMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/messaging.MessagingService/ReplicateMessage',
            mom__server_dot_grpc__services_dot_messaging__pb2.MessageRequest.SerializeToString,
            mom__server_dot_grpc__services_dot_messaging__pb2.MessageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateTopic(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/messaging.MessagingService/CreateTopic',
            mom__server_dot_grpc__services_dot_messaging__pb2.TopicRequest.SerializeToString,
            mom__server_dot_grpc__services_dot_messaging__pb2.TopicResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteTopic(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/messaging.MessagingService/DeleteTopic',
            mom__server_dot_grpc__services_dot_messaging__pb2.TopicRequest.SerializeToString,
            mom__server_dot_grpc__services_dot_messaging__pb2.TopicResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListTopics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/messaging.MessagingService/ListTopics',
            mom__server_dot_grpc__services_dot_messaging__pb2.EmptyRequest.SerializeToString,
            mom__server_dot_grpc__services_dot_messaging__pb2.TopicsListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateQueue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/messaging.MessagingService/CreateQueue',
            mom__server_dot_grpc__services_dot_messaging__pb2.QueueRequest.SerializeToString,
            mom__server_dot_grpc__services_dot_messaging__pb2.QueueResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteQueue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/messaging.MessagingService/DeleteQueue',
            mom__server_dot_grpc__services_dot_messaging__pb2.QueueRequest.SerializeToString,
            mom__server_dot_grpc__services_dot_messaging__pb2.QueueResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListQueues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/messaging.MessagingService/ListQueues',
            mom__server_dot_grpc__services_dot_messaging__pb2.EmptyRequest.SerializeToString,
            mom__server_dot_grpc__services_dot_messaging__pb2.QueuesListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SendMessageToQueue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/messaging.MessagingService/SendMessageToQueue',
            mom__server_dot_grpc__services_dot_messaging__pb2.QueueMessageRequest.SerializeToString,
            mom__server_dot_grpc__services_dot_messaging__pb2.MessageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
