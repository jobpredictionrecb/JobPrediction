from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf
from .models import Resume_Model
from .forms import ResumeForm


def resume_view(request):
    user_detail1 = request.session.get('user_detail1')
    if not user_detail1:
        user_detail1 = {}

    if request.method=="POST":
        pform = ResumeForm(request.POST, request.FILES)
        fname = request.POST.get('stu_fname')
        mname = request.POST.get('stu_mname')
        lname = request.POST.get('stu_lname')
        number = request.POST.get('number')
        email = request.POST.get('email')
        link = request.POST.get('link')
        career = request.POST.get('career')
        pform.save()
        #images = Resume_Model.objects.all()
        user_detail1 = {
            'fname':fname,
            'mname':mname,
            'lname':lname,
            'number':number,
            'email':email,
            'link':link,
            'career':career,
            #'images':images
        }
        #return render(request,'ResumeBuilder/resume_pdf.html',user_detail)
        request.session['user_detail1']= user_detail1
        return render(request,'ResumeBuilder/skills.html')
        #return redirect("/resumebuilder/pdf")

    else:
        pform = ResumeForm()
        return render(request, 'ResumeBuilder/resume_html.html',{'pform':pform})

def skill_view(request):
    user_detail1 = request.session.get('user_detail1')
    if not user_detail1:
        user_detail1 = {}
    if request.method == "POST":
        soft_skill = request.POST['soft-skill']
        user_detail = {
            'soft-skill': soft_skill
        }


class GeneratePDF(View):
    def get(self, request):
        user_detail1 = request.session.get('user_detail1')
        if not user_detail1:
            user_detail1 = {}
        if request.method == "POST":
            soft_skill = request.POST['soft-skill']
            user_detail = {
                'soft-skill': soft_skill
            }
            template = get_template('ResumeBuilder/resume_pdf.html')
            user_detail = request.session.get('user_detail')
            html = template.render(user_detail)
            pdf = render_to_pdf('ResumeBuilder/resume_pdf.html', user_detail)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                #filename = "Ravi_%s.pdf" %("12341231")
                filename = "%s_Resume.pdf" %( user_detail['fname']+user_detail['mname']+user_detail['lname'] )


                #exe = "_Resume.pdf"
            #filename = {{ request.user.first_name }} + exe
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

