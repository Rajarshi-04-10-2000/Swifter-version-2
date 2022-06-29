from webstar.models import Tranporter, Company
from django.db.models import Q


def CalculateVehical(query1):
    cname = Company.objects.get(user_name=query1)
    c_g_type = cname.g_type
    c_weight = cname.weight
    tname = Tranporter.objects.filter(
        Q(permit_wt__gte=c_weight) & Q(v_status="Available") & Q(v_type=c_g_type))
    return tname


def CalculatePrice(query1):
    temp = CalculateVehical(query1)
    tname = Tranporter.objects.get(dname=temp[0])
    cname = Company.objects.get(user_name=query1)
    c_weight = int(cname.weight)
    tname.permit_wt = str(int(tname.permit_wt) - c_weight)
    tname.save()
    price = int(cname.dist)*50
    return price
