from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import Staff

# Create your views here.
@login_required
def home(request):

    staff_info=Staff.objects.all()

    staff_dict={'staffs':staff_info}


    return render(request, 'accounts/home.html',context=staff_dict)
