from django.shortcuts import render
from django.http import *
from django.urls import reverse

from .models import *
from .forms import *
# Create your views here.


def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


def flight(request,flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request,'flights/flight.html', {
        'flight':flight,
        'passengers': flight.passengers.all(),
        'non_passengers': Passenger.objects.exclude(flights=flight).all()
    })


def dpassenger(request, flight_id, passenger_id):
    if request.method == "GET":
        flight = Flight.objects.get(pk=flight_id)
        flight.passengers.remove(passenger_id)
        return HttpResponseRedirect(reverse('flights:flight', args=(flight_id,)))


def book(request,flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=request.POST["passenger"])
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flights:flight", args=(flight_id,)))


def edit(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    eform = FlightForm(instance=flight)
    if request.method == "POST":
        f = FlightForm(request.POST)
        if f.is_valid():
            new = f.save(commit=False)
            new.id = flight_id
            new.save()
            f.save_m2m()
            return HttpResponseRedirect(reverse("flights:flight", args=(flight_id,)))
        else:
            eform = f
    return render(request, 'flights/edit.html',{
        'flight': flight,
        'form': eform,
    })


def delete(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    if request.method == "GET":
        flight.delete()
    return HttpResponseRedirect(reverse("flights:index"))


def add(request):
    form = FlightForm()
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("flights:index"))
    return render(request, 'flights/add.html',{
        'form': form,
    })


def add_passenger(request):
    form = PassengerForm()
    if request.method == "POST":
        form = PassengerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('flights:index'))
    return render(request, 'flights/add-passenger.html', {
        "form":form
    })


def passengers(request):
    passengers = Passenger.objects.all()
    return render(request, 'flights/passengers.html',{
        'passengers':passengers
    })

def edit_passenger(request, passenger_id):
    passenger = Passenger.objects.get(pk=passenger_id)
    form = PassengerForm(instance=passenger)
    if request.method == "POST":
        form = PassengerForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.id = passenger_id
            new.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('flights:passengers'))
    return render(request, 'flights/edit-passenger.html', {
        'passenger': passenger,
        'form':form,
    })

def passenger(request, passenger_id):
    passenger = Passenger.objects.get(pk=passenger_id)
    flights = passenger.flights.all()
    return render(request, 'flights/passenger.html', {
        'passenger': passenger,
        'flights': flights,
    })

