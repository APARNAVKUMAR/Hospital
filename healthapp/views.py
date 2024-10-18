from .forms import BookingForm
from .models import News, Department
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.
def home_view(request):
    return render(request, 'index.html')
def about_view(request):
    return render(request, 'about.html')
def team_view(request):
    department = Department.objects.all()
    return render(request, 'team.html', {"department": department})
def news_view(request):
    news = News.objects.all()
    return render(request, 'news.html', {"news": news})
def appointment_view(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the form data
            form.save()

            # Send appointment confirmation email
            recipient = form.cleaned_data.get('book_email')
            subject = 'Your Appointment Details'
            context = {
                'book_name': form.cleaned_data.get('book_name'),
                'book_dep': form.cleaned_data.get('book_dep'),
                'book_date': form.cleaned_data.get('book_date').strftime('%Y-%m-%d'),
            }
            html_message = render_to_string('appointment_email.html', context)
            send_mail(subject, '', settings.EMAIL_HOST_USER, [recipient], html_message=html_message)

            messages.success(request, 'Appointment confirmed! Check your email for details.')
            form = BookingForm()

    return render(request, 'appointment.html', {"form": form})

