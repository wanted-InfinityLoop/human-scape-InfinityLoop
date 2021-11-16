from django.views import View
from django.http  import JsonResponse

from clinics.models import Clinic


class ClinicDetailView(View):
    def get(self, request, clinic_id):
        try:
            clinic = Clinic.objects.get(id=clinic_id)

            if not clinic.is_active:
                return JsonResponse({"message": "CLINIC_CAN'T_FOUND"}, status=404)

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


class ClinicListView(View):
    def get(self, request):
        try:
            page_num = int(request.GET.get('page', 1))
            limit    = 5
            start    = (page_num-1) * limit
            end      = page_num     * limit
            
            clinics = Clinic.objects.all()[start:end]
            
            result = {
                "current_count" : len(clinics),
                "data" : [
                    {
                        "name" : clinic.name,
                        "id" : clinic.id,
                        "duration" : clinic.duration,
                        "scope" : clinic.scope,
                        "type" : clinic.type,
                        "institution" : clinic.institution,
                        "trial" : clinic.trial,
                        "subjects" : clinic.subjects,
                        "department" : clinic.department
                    } for clinic in clinics
                ],
                "match_count" : len(Clinic.objects.all()),
                "page" : page_num,
                "per_page" : len(clinics),
                "total_count" : len(Clinic.objects.all())
            }
            
            return JsonResponse({"result" : result}, status=200)
        
        except ValueError:
            return JsonResponse({"result" : "WRONG_PAGE_NUMBER"}, status=400)
