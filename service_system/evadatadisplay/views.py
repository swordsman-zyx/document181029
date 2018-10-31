import json
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from evadatadisplay.models import EvaDataDisplay
# from record.models import Record
# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class EvaluationView(View):
    def get(self, request, user_id):
        eva_record = EvaDataDisplay.objects.filter(user_id=user_id)
        print(eva_record.values())
        # for i in eva_record.values():
        #     print(json.dumps(i))

        return HttpResponse(status=200)

    # 用户作出评价   需要参数为json格式 如 ’{"record_id":"123","star_num":"5","word_eva":"qeweqwewqqw"}‘
    def put(self, request):
        eva_json = request.body.decode()
        eva_dict = json.loads(eva_json)
        EvaDataDisplay.objects.filter(eva_id=EvaDataDisplay.objects.
                                      get(record_id=eva_dict["record_id"]).eva_id).\
            update(
                   star_num=eva_dict["star_num"],
                   word_eva=eva_dict["word_eva"],
                   eva_state="已评价"
                   )
        return HttpResponse(status=201)

        # 创建评价的方法
        # EvaDataDisplay.objects.create(record_id=record.record_id,
        #                               user_id=record.user_id,
        #                               user_name=record.user_name,
        #                               server_id=record.server_id,
        #                               server_name=record.server_name,
        #                               star_num=5
        #                               )
        # return HttpResponse(status=201)


@method_decorator(csrf_exempt, name='dispatch')
class DataDisplayView(View):
    pass
