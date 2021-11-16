from django.views import View
from django.http  import JsonResponse

from clinics.models import Clinic


class ClinicDetailView(View):
    def get(self, request, clinic_id):
        try:
            clinic = Clinic.objects.get(id=clinic_id)
            data = {
                "name": clinic.name,
                "id": clinic.id,
                "duration": clinic.duration,
                "scope": clinic.scope,
                "type": clinic.type,
                "institution": clinic.institution,
                "trial": clinic.trial,
                "subjects": clinic.subjects,
                "department": clinic.department
            }

            return JsonResponse({"data": data}, status=200)

        except Clinic.DoesNotExist:
            return JsonResponse({"message": "CLINIC_NOT_FOUND"}, status=404)
