from django.test import TestCase, Client

from clinics.models import Clinic


class ClinicDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        Clinic.objects.create(
            id         ="C160046",
            name       ="우울증 진단/치료 의사결정 보조시스템 개발을 위한 뇌영상-오믹스 기반 빅데이터 구축 및 임상 검증 연구",
            duration   ="51개월",
            scope      ="국내다기관",
            type       ="관찰연구",
            institution="고려대학교 안암병원",
            trial      ="Case-control",
            subjects   ="300",
            department ="Psychiatry"
        )

    def tearDown(self):
        Clinic.objects.all().delete()

    def test_get_clinic_detail_success(self):
        response = self.client.get("/clinics/C160046")

        clinic = Clinic.objects.get(id="C160046")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "data" :{
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
            }
        )

    def test_get_clinic_not_found(self):
        response = self.client.get("/clinics/B160043")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"message": "CLINIC_NOT_FOUND"})
