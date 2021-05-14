from django.shortcuts import render
# from django.views.generic import ListView
from .models import Exhibition


# class ExhibitionList(ListView):
#     model = Exhibition
#     ordering = '-pk'
#     paginate_by = 5
#
#     def get_context_data(self, **kwargs):
#         context = super(ExhibitionList, self).get_context_data()
#         context['categories'] = Category.objects.all()
#         context['no_category_post_count'] = Post.objects.filter(category=None).count()
# return context


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
    def exhibition_list_page(request):
        # post = Post.objects.get(pk=pk)

        return render(
            request,
            'arta_front_develop/ARTA_User_exhibition_list.html',
            {
                # 'post': post,
            }
        )

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
    def piece_detail_page(request):
        return render(
            request,
            'arta_front_develop/ARTA_User_exhibition_show.html',
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