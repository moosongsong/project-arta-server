from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Exhibition, Category, Material, Piece


class ExhibitionList(ListView):
    model = Exhibition
    ordering = '-pk'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ExhibitionList, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


class ExhibitionDetail(DetailView):
    model = Exhibition

    def get_context_data(self, **kwargs):
        context = super(ExhibitionDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        # context['categories'] = Category.objects.all()
        return context


class PieceDetail(DetailView):
    model = Piece

    def get_context_data(self, **kwargs):
        context = super(PieceDetail, self).get_context_data()
        return context


class SinglePage:
    def landing_page(request):
        return render(
            request,
            'arta_front_develop/ARTA_main_page.html'
        )

    def about_page(request):
        return render(
            request,
            'arta_front_develop/ARTA_introduction.html'
        )


class ExhibitionPage:
    def exhibition_detail_page(request, pk):
        return render(
            request,
            'arta_front_develop/ARTA_User_exhibition_show.html',
            {
                #
            }
        )

    def about_page(request, pk):
        return render(
            request,
            'single_page/about.html'
        )


class LikePage:
    def all_like_page(request):
        return render(
            request,
            'arta_front_develop/ARTA_LikePage.html',
            {
                #
            }
        )


class PiecePage:
    def piece_detail_page(request, pk):
        return render(
            request,
            'arta_front_develop/ARTA_User_piece_show.html',
            {
                #
            }
        )


class SearchPage:
    def search_page(request):
        return render(
            request,
            'arta_front_develop/ARTA_search_page.html',
            {
                #
            }
        )

    def search_result_page(request, key):
        return render(
            request,
            'arta_front_develop/ARTA_search_result.html',
            {
                #
            }
        )
