from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db.models import Sum

from catalog.forms import SongForm


from catalog.models import Song
from billing.models import Purchase

@staff_member_required
def dashboard_home(request):

    songs_count = Song.objects.filter(
        deleted_at__isnull=True
    ).count()

    users_count = User.objects.count()

    purchases_count = Purchase.objects.count()

    revenue = Purchase.objects.aggregate(
        total=Sum('song__price')
    )['total'] or 0

    recent_purchases = Purchase.objects.select_related(
    'user', 'song'
).order_by('-purchase_date')[:5]

    context = {
        'songs_count': songs_count,
        'users_count': users_count,
        'purchases_count': purchases_count,
        'revenue': revenue,
        'recent_purchases': recent_purchases,
    }

    return render(request, 'dashboard/home.html', context)

@staff_member_required
def users_list(request):
    users = User.objects.all().order_by('-date_joined')

    users_count = users.count()

    admins_count = User.objects.filter(is_staff=True).count()

    context = {
        'users': users,
        'users_count': users_count,
        'admins_count': admins_count,
    }

    return render(request, 'dashboard/users.html', context)

@staff_member_required
@require_POST
def toggle_user_status(request, user_id):
    user = get_object_or_404(User, id=user_id)

    # Запрещаем блокировать собственный аккаунт
    if user == request.user:
        messages.error(request, 'Нельзя изменить статус собственного аккаунта.')
        return redirect('users_list')

    # Меняем статус на противоположный
    user.is_active = not user.is_active
    user.save()

    if user.is_active:
        messages.success(request, 'Пользователь разблокирован.')
    else:
        messages.success(request, 'Пользователь заблокирован.')
    return redirect('users_list')


@staff_member_required
@require_POST
def toggle_user_role(request, user_id):
    user = get_object_or_404(User, id=user_id)

    # Не разрешаем менять собственную роль
    if user == request.user:
        messages.error(request, 'Нельзя изменить собственную роль.')
        return redirect('users_list')

    # Не разрешаем изменять роль суперпользователя
    if user.is_superuser:
        messages.error(request, 'Нельзя изменить роль суперпользователя.')
        return redirect('users_list')

    user.is_staff = not user.is_staff
    user.save()

    if user.is_staff:
        messages.success(request, 'Права администратора выданы.')
    else:
        messages.success(request, 'Права администратора сняты.')
    return redirect('users_list')


@staff_member_required
def purchases_list(request):
    purchases = Purchase.objects.select_related(
        'user', 'song'
    ).order_by('-purchase_date')

    purchases_count = purchases.count()
    revenue = purchases.aggregate(
        total=Sum('song__price')
    )['total'] or 0

    context = {
        'purchases': purchases,
        'purchases_count': purchases_count,
        'revenue': revenue,
    }

    return render(request, 'dashboard/purchases.html', context)

@staff_member_required
def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('dashboard_home')
    else:
        form = SongForm()

    return render(request, 'dashboard/add_song.html', {
        'form': form
    })