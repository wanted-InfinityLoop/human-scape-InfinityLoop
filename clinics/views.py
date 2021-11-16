from datetime import datetime, timedelta

from django.db.models import Q
from django.views     import View
from django.http      import JsonResponse

from clinics.models import Clinic


class ClinicDetailView(View):
    def get(self, request, clinic_id):
        try:
            clinic = Clinic.objects.get(id=clinic_id)

            if not clinic.is_active:
                return JsonResponse({"message": "CLINIC_NOT_FOUND"}, status=404)

            data = {
                "name"       : clinic.name,
                "id"         : clinic.id,
                "duration"   : clinic.duration,
                "scope"      : clinic.scope,
                "type"       : clinic.type,
                "institution": clinic.institution,
                "trial"      : clinic.trial,
                "subjects"   : clinic.subjects,
                "department" : clinic.department,
                "updated_at" : clinic.updated_at.strftime("%Y-%m-%d %H:%M:%S")
            }

            return JsonResponse({"data": data}, status=200)

        except Clinic.DoesNotExist:
            return JsonResponse({"message": "CLINIC_NOT_FOUND"}, status=404)


class ClinicListView(View):
    def get(self, request):
        try:
            page_num = int(request.GET.get("page", 1))
            limit    = 10
            start    = (page_num - 1) * limit
            end      = page_num * limit

            q = Q(updated_at__gt=datetime.now() - timedelta(days=7))

            clinics_unfiltered = Clinic.objects.all()
            clinics_filtered   = Clinic.objects.filter(q).filter(is_active=True)[start:end]

            if not clinics_filtered.exists():
                return JsonResponse({"result": "NOT_MATCHING_DATA"}, status=404)

            result = {
                "data": [
                    {
                        "name"       : clinic.name,
                        "id"         : clinic.id,
                        "duration"   : clinic.duration,
                        "scope"      : clinic.scope,
                        "type"       : clinic.type,
                        "institution": clinic.institution,
                        "trial"      : clinic.trial,
                        "subjects"   : clinic.subjects,
                        "department" : clinic.department,
                        "updated_at" : clinic.updated_at.strftime("%Y-%m-%d %H:%M:%S")
                    }
                    for clinic in clinics_filtered
                ],
                "general_information": {
                    "count"      : clinics_filtered.count(),
                    "total_count": clinics_unfiltered.count(),
                    "page"       : page_num,
                    "total_page" : clinics_unfiltered.count() // limit + 1, 
                    "per_page"   : limit,
                },
            }

            return JsonResponse({"result": result}, status=200)

        except ValueError:
            return JsonResponse({"result": "WRONG_PAGE_NUMBER"}, status=400)
