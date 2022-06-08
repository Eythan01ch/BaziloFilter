# Create your views here.
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from BaziloLeadProcessor.LeadProcessor.leadProcessor import LeadProcessor
from BaziloLeadProcessor.serializers import LeadSerializer, NewLeadSerializer


class LeadAddView(CreateAPIView):

	serializer_class = LeadSerializer
	permission_classes = [IsAuthenticated]
	authentication_classes = [TokenAuthentication]

	def post(self, *args, **kwargs):

		lead_serializer = NewLeadSerializer(data=self.request.data)
		if lead_serializer.is_valid():
			lead_processor = LeadProcessor(
				email=lead_serializer.validated_data['email'],
				phone=lead_serializer.validated_data['phone'],
				ip=lead_serializer.validated_data['ip'],
				fname=lead_serializer.validated_data['fname'],
				lname=lead_serializer.validated_data['lname'],
			)
			lead_obj = lead_processor.process_lead()
			serializer = LeadSerializer(lead_obj, many=False)

			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(lead_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
