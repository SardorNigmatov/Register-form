from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UsersForm
from .models import Users

def register(request):
    """Foydalanuvchi formasi orqali ma'lumotlarni yuborish va formani ko'rsatish."""
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()  # Yaroqli formadagi ma'lumotlarni bazaga saqlash
            return redirect(reverse('success'))  # Muvaffaqiyatli sahifaga yo'naltirish
    else:
        form = UsersForm()  # GET so'rovda bo'sh forma ko'rsatiladi

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def success(request):
    """Forma yuborilgandan keyin muvaffaqiyat sahifasini ko'rsatadi."""
    return render(request, 'success.html')


def main(request):
    """Asosiy sahifada barcha foydalanuvchilarni ko'rsatadi."""
    users = Users.objects.all()
    context = {
        'users': users
    }
    return render(request, 'main.html', context)
