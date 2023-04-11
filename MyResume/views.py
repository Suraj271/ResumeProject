from django.shortcuts import render

# Create your views here.


def aboutme_view(request):

    return render(request , 'aboutme.html')

def skills_view(request):

    skills = {

        'Python' : 60,
        'Java' : 40,
        'SQL' : 80,
        'HTML' : 70,

    }

    context = {'skills' : skills}


    return render(request , 'skills.html' , context)


def project_view(request):

    project = {

        'pro1' : {'sr' : 1 , 'topic': 'Online Restaurant Management System' , 'Technology' : 'Python,SQL,HTML,CSS' },
        'pro2' : {'sr' : 2 , 'topic': 'Online Food Ordering System' , 'Technology' : 'Python,SQL'},
        "pro3" : {'sr' : 3 , 'topic': 'Bank Management System' , 'Technology' : 'Python,SQL'},

    }

    context = {'project' : project}


    return render(request , 'projects.html' , context)


def qualification_view(request):


    study = {
        'SSC' : {'sr' : 1 , 'study' : 'SSC' , 'Board' : 'Maharashtra' , 'Year' : 2017},
        'HSC' : {'sr' : 2 , 'study' : 'HSC' , 'Board' : 'Maharashtra' , 'Year' : 2019},
        'BSC' : {'sr' : 3 , 'study' : 'BSC-IT' , 'Board' : 'Mumbai' , 'Year' : 2022}
    }

    context = {'study' : study}


    return render(request , 'qualification.html' , context)


def experience_view(request):

    return render(request , 'experience.html')


def contact_view(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        p = request.POST.get("purpose")


        print(name)
        print(email)
        print(p)

        context = {'name' : name}

        return render(request , 'thanks.html' , context)


    return render(request , 'contact.html')
