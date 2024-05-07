from django.shortcuts import render
from app.models import *
# Create your views here.
def innerEquiJoins(request):
    JDED=Emp.objects.select_related('deptno').all() # WHEN WE WANT TO FETCH THE ALL ROWS
    JDED=Emp.objects.select_related('deptno').filter(ename='SMITH') # WHEN WE WANT TO FETCH ENAME='SMITH'
    d={'JDED':JDED}

    return render(request,'innerEquiJoins.html',d)