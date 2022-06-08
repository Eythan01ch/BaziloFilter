from rest_framework import serializers

from BaziloLeadProcessor.models import Lead, LeadEmailInfo, LeadPhoneInfo


EXCLUDES = ['updated_at', 'is_deleted']


class LeadEmailInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = LeadEmailInfo
		exclude = EXCLUDES


class LeadPhoneInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = LeadPhoneInfo
		exclude = EXCLUDES


class LeadSerializer(serializers.ModelSerializer):
	lead_email_info = LeadEmailInfoSerializer(required=False)
	lead_phone_info = LeadPhoneInfoSerializer(required=False)

	class Meta:
		model = Lead
		exclude = EXCLUDES


class NewLeadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lead
		exclude = EXCLUDES
