from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Room, Booking  
from .forms import NewUserForm, RoomForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import Room
from django.contrib.auth.forms import AuthenticationForm 
from django.views.decorators.csrf import csrf_protect

def home(request):
    return render(request, "home.html")
    
def index(request):
    rooms_with_bookings = []
    rooms = Room.objects.all()
    for room in rooms:
        bookings = Booking.objects.filter(room=room)
        rooms_with_bookings.append({"room": room, "bookings": bookings})
    return render(request, "index.html", {"rooms_with_bookings": rooms_with_bookings})

def create_room(request):  
    if request.method == "POST":  
        form = RoomForm(request.POST)  
        if form.is_valid():  
            form.save()  
            messages.success(request, "Room Added Successfully.")
            return redirect('index')   
    else:  
        form = RoomForm()  
    return render(request,'create_room.html',{'form':form})  

def edit_class(request, id):  
    room = Room.objects.get(id=id)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            room.save()
            messages.success(request, "Room Updated Successfully.")
            return redirect('index')
    else:
        form = RoomForm(instance=room)
    return render(request,'create_room.html', {'form':form})

def delete_room(request, id):
    room = Room.objects.get(id=id)  
    room.delete() 
    messages.success(request, "Room Delted Successfully.") 
    return redirect("index") 

def make_booking(request, room_id):
    room = Room.objects.get(pk=room_id)
    if request.method == 'POST':
        guest_name = request.POST['guest_name']
        check_in_date = request.POST['check_in_date']
        check_out_date = request.POST['check_out_date']
        booking = Booking.objects.create(room=room, guest_name=guest_name, check_in_date=check_in_date, check_out_date=check_out_date)
        return render(request, 'booking_confirmation.html', {'booking': booking})
    return render(request, 'make_booking.html', {'room': room})

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful Registration. Invalid Creadentials.")
    form = NewUserForm()
    return render(request, "register.html", context={"register_form":form})

@csrf_protect
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "login.html", context={"login_form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")


