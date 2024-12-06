from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import QuerySet
from django.shortcuts import redirect, render
from ..models import Doctors,Appointment
from ..forms import AppointmentForm
@login_required
def book_appointment(request):
    doctors = Doctors.objects.all()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            doctor= form.cleaned_data['doctor_name']
            appointment_date = form.cleaned_data['appointment_date']
            # doctor = Doctors.objects.get(name=doctor_name)
            patient = request.user.patients
            appointment= form.save(commit=False)
            appointment.patient_name= patient
            appointment.patient_mobile= patient.mobile
            appointment.doctor_name= doctor
            appointment.save()

            messages.success(request,
                             f'Your appointment with Dr. {doctor.name} has been booked for {appointment_date}.')
            return redirect('home')
        else:
            messages.error(request,'key in the infomation')
    else:

        form = AppointmentForm()



    return render(request, 'appointment.html',{'form':form , 'doctors':doctors})

