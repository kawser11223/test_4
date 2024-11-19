from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import F
from .models import Task, UserTask, Profile,User_Withdraw
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request,'index.html')





def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        referral_code = request.POST.get('referral_code', None)

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('sign-Extreme')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('sign-Extreme')
            else:
             
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

               
                if referral_code:
                    try:
                        referrer = Profile.objects.get(referral_code=referral_code)
                        
                        referrer.referred_count = F('referred_count') + 1
                        
                        referrer.points = F('points') + 0.1
                        referrer.save()

                        messages.success(request, "Referral code applied successfully!")
                    except Profile.DoesNotExist:
                        messages.warning(request, "Invalid referral code.")

              
                Profile.objects.create(user=user)

                return redirect('login-Extreme')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('sign-Extreme')

    return render(request, 'sign.html')


@login_required
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        secret_code = request.POST['secret_code']

        
        if secret_code == task.secret_code:
            if UserTask.objects.filter(user=request.user, task=task).exists():
                messages.warning(request, "You have already completed this task.")
                return redirect('task-list')

           
            UserTask.objects.create(user=request.user, task=task)
            profile = Profile.objects.get(user=request.user)

        
            profile.points = F('points') + 0.2
            
            profile.save()

            messages.success(request, "Task completed successfully! You earned 0.2.")
            return redirect('task-list')
        else:
            messages.error(request, "Invalid secret code. Please try again.")
            return redirect('complete-task', task_id=task_id)

    return render(request, 'task2.html', {'task': task})



def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        input_username = request.POST['username']
        input_password = request.POST['password']

        user = auth.authenticate(username=input_username, password=input_password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashbord-Extreme')
        else:
            messages.error(request, "Invalid username or password!")
            return render(request, 'login.html')



@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task.html', {'tasks': tasks})




@login_required
def w_points(request):
    if request.method == 'POST':
        try:
            
            subtract_value = float(request.POST.get('subtract_value', 0))  
            address_value = request.POST.get('address_value')  
            
            
            if subtract_value <= 0:
                messages.error(request, " Must be withdrawal 10 usdt.")
                return redirect('w-points')

            
            profile, created = Profile.objects.get_or_create(user=request.user)

            if subtract_value > profile.points:
                messages.error(request, "Insufficient balance for withdrawal.")
                return redirect('w-points')

            
            profile.points -= subtract_value
            profile.save()

            
            User_Withdraw.objects.create(
                w_amount=subtract_value,
                address=address_value,
                user=request.user
            )

            
            messages.success(request, "Successfully withdrawn!")
            return redirect('w-points')

        except ValueError:
            messages.error(request, "Invalid input. Please enter a valid number.")
            return redirect('w-points')

  
    return render(request, 'w.html')





@login_required
def top_users(request):
    
    top_profiles = Profile.objects.order_by('-points')[:10] 
    return render(request, 'top_user.html', {'top_profiles': top_profiles})

@login_required
def dash(request):
    profile = Profile.objects.get(user=request.user)  
   
    truncated_points = str(profile.points)[:4]

    return render(request, 'dash.html', {
        'profile': profile,
        'truncated_points': truncated_points,
    })
