from datetime import datetime

from clinics.models import Clinic
from core.openapi import OpenAPI
from core.utils import convert_int_or_none
from my_settings import OPEN_API_KEY


def insert_clinical_trial_information():
    results = OpenAPI(OPEN_API_KEY).get_clinical_trial()
    data_list = results["data"]
    clinic_infos = [[clinic, False] for clinic in Clinic.objects.all()]

    for data in data_list:
        if not Clinic.objects.filter(id=data["과제번호"]).exists():
            subjects = convert_int_or_none(data["전체목표연구대상자수"])

            Clinic.objects.create(
                id=data["과제번호"],
                name=data["과제명"],
                duration=data["연구기간"],
                scope=data["연구범위"],
                type=data["연구종류"],
                trial=data["임상시험단계(연구모형)"],
                subjects=subjects,
                department=data["진료과"],
            )
            print(data["과제번호"], " has created!", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print("====================")

        else:
            subjects = convert_int_or_none(data["전체목표연구대상자수"])

            for clinic in clinic_infos:
                if clinic[0].id == data["과제번호"]:
                    clinic[1] = True
                    has_changed = False

                    if clinic[0].name != data["과제명"]:
                        clinic[0].name = data["과제명"]
                        has_changed = True

                    if clinic[0].duration != data["연구기간"]:
                        clinic[0].duration = data["연구기간"]
                        has_changed = True

                    if clinic[0].scope != data["연구범위"]:
                        clinic[0].scope = data["연구범위"]
                        has_changed = True

                    if clinic[0].type != data["연구종류"]:
                        clinic[0].type = data["연구종류"]
                        has_changed = True

                    if clinic[0].trial != data["임상시험단계(연구모형)"]:
                        clinic[0].trial = data["임상시험단계(연구모형)"]
                        has_changed = True

                    if clinic[0].subjects != subjects:
                        clinic[0].subjects = subjects
                        has_changed = True

                    if clinic[0].department != data["진료과"]:
                        clinic[0].department = data["진료과"]
                        has_changed = True

                    if not clinic[0].is_active:
                        clinic[0].is_active = True
                        has_changed = True
                        print(clinic[0].id, " has reactive!", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

                    if has_changed:
                        clinic[0].save()
                        print(clinic[0].id, " has changed!", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                        print("====================")

            for clinic in clinic_infos:
                if clinic[0].id == data["과제번호"]:
                    if not clinic[1] and clinic[0].is_active:
                        clinic[0].is_active = False
                        clinic[0].save()
                        print(clinic[0].id, " has soft deleted!", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                        print("====================")

    print("cron job finished!", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "\n====================")
    