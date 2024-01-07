from uuid import uuid4
from pytils.translit import slugify
from django.contrib.auth.mixins import AccessMixin
from django.contrib import messages
from django.shortcuts import redirect

def unique_slugify(instance, slug):
    """
    Генератор уникальных SLUG для моделей, в случае существования такого SLUG.
    """
    model = instance.__class__
    unique_slug = slugify(slug)
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{unique_slug}-{uuid4().hex[:8]}'
    return unique_slug


class ProfileRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.is_authenticated:
            if request.user != self.get_object() or request.user.is_staff:
                messages.info(request, 'Изменение профиля доступно только автору!')
                return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class AuthorRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.is_authenticated:
            if request.user != self.get_object().author or not request.user.is_staff:
                messages.info(request, 'Изменение и удаление статьи доступно только автору')
                return redirect('home')
        return super().dispatch(request, *args, **kwargs)