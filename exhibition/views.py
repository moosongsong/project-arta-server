from django.shortcuts import render
from django.views.generic import ListView
from .models import Exhibition


class ExhibitionList(ListView):
    model = Exhibition
    ordering = '-pk'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ExhibitionList, self).get_context_data()
        # context['categories'] = Category.objects.all()
        # context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context
