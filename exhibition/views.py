from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Exhibition, Category, Material, Piece, Comment, GuestBook, ExhibitionLike, PieceLike
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q


class SinglePage:
    def landing_page(request):
        return render(
            request,
            'exhibition/ARTA_main_page.html'
        )

    def about_page(request):
        return render(
            request,
            'exhibition/ARTA_introduction.html'
        )

    def login_page(request):
        return render(
            request,
            'exhibition/ARTA_User_login.html'
        )

    # 여기서 test할 파일 집어넣어서 하시오.
    def test_page(request):
        return render(
            request,
            # add pages here
            'exhibition/ARTA_User_login.html'
        )


class ExhibitionList(ListView):
    model = Exhibition
    ordering = '-pk'
    paginate_by = 5
    template_name = 'exhibition/ARTA_User_exhibition_list.html'

    def get_context_data(self, **kwargs):
        context = super(ExhibitionList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['materials'] = Material.objects.all()
        return context


class ExhibitionDetail(DetailView):
    model = Exhibition

    template_name = 'exhibition/ARTA_User_exhibition_show.html'

    def get_context_data(self, **kwargs):
        context = super(ExhibitionDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


class PieceList(ListView):
    model = Piece
    ordering = 'pk'
    paginate_by = 8

    def get_queryset(self):
        exhibition_id = self.kwargs['pk']
        piece_list = Piece.objects.filter(Q(exhibition_id=exhibition_id))
        return piece_list

    def get_context_data(self, **kwargs):
        context = super(PieceList, self).get_context_data()
        pk = self.kwargs['pk']
        context['exhibition'] = get_object_or_404(Exhibition, pk=pk)
        context['categories'] = Category.objects.all()
        context['materials'] = Material.objects.all()
        return context


class PieceDetail(DetailView):
    model = Piece
    template_name = 'exhibition/ARTA_User_piece_show.html'

    def get_context_data(self, **kwargs):
        context = super(PieceDetail, self).get_context_data()
        return context


class CommentManage:
    def new_comment(request, pk):
        if request.user.is_authenticated:
            piece = get_object_or_404(Piece, pk=pk)

            if request.method == 'POST':
                comment = Comment(content=request.POST.get('content'), piece=piece, user=request.user)
                comment.save()
                messages.warning(request, "댓글을 성공적으로 등록했습니다.")
                return redirect(comment.get_absolute_url())
            else:
                return redirect(piece.get_absolute_url())
        else:
            return PermissionDenied

    def delete_comment(request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        piece = comment.piece
        if request.user.is_authenticated and request.user == comment.user:
            comment.delete()
            messages.warning(request, "댓글이 성공적으로 삭제되었습니다.")
            return redirect(piece.get_absolute_url())
        else:
            raise PermissionDenied


class GuestbookManage:
    def new_guestbook(request, pk):
        if request.user.is_authenticated:
            exhibition = get_object_or_404(Exhibition, pk=pk)

            if request.method == 'POST':
                guestbook = GuestBook(content=request.POST.get('content'), exhibition=exhibition, user=request.user)
                guestbook.save()
                messages.warning(request, "방명록을 성공적으로 등록했습니다.")
                return redirect(guestbook.get_absolute_url())
            else:
                return redirect(exhibition.get_absolute_url())
        else:
            return PermissionDenied

    def delete_guestbook(request, pk):
        guestbook = get_object_or_404(GuestBook, pk=pk)
        exhibition = guestbook.exhibition
        if request.user.is_authenticated and request.user == guestbook.user:
            guestbook.delete()
            messages.warning(request, "방명록이 성공적으로 삭제되었습니다.")
            return redirect(exhibition.get_absolute_url())
        else:
            raise PermissionDenied


class LikeManage:
    def exhibition_like(request, pk):
        if request.user.is_authenticated:
            exhibition = get_object_or_404(Exhibition, pk=pk)
            olderLike = ExhibitionLike.objects.filter(exhibition=exhibition, user=request.user)

            if olderLike:
                return redirect(exhibition.get_absolute_url())

            like = ExhibitionLike(exhibition=exhibition, user=request.user)
            like.save()
            return redirect(like.get_absolute_url())
        else:
            return PermissionDenied

    def exhibition_dislike(request, pk):
        like = get_object_or_404(ExhibitionLike, pk=pk)
        exhibition = like.exhibition
        if request.user.is_authenticated and request.user == like.user:
            like.delete()
            return redirect(exhibition.get_absolute_url())
        else:
            return PermissionDenied

    def piece_like(request, pk):
        if request.user.is_authenticated:
            piece = get_object_or_404(Piece, pk=pk)
            olderLike = PieceLike.objects.filter(piece=piece, user=request.user)
            if olderLike:
                return redirect(piece.get_absolute_url())

            like = PieceLike(piece=piece, user=request.user)
            like.save()
            return redirect(like.get_absolute_url())
        else:
            return PermissionDenied

    def piece_dislike(request, pk):
        like = get_object_or_404(PieceLike, pk=pk)
        piece = like.piece
        if request.user.is_authenticated and request.user == like.user:
            like.delete()
            return redirect(piece.get_absolute_url())
        else:
            return PermissionDenied


class LikePieceList(ListView):
    model = PieceLike
    template_name = 'exhibition/ARTA_LikePiecePage.html'

    def get_context_data(self, **kwargs):
        context = super(LikePieceList, self).get_context_data()
        return context


class LikeExhibitionList(ListView):
    model = ExhibitionLike
    template_name = 'exhibition/ARTA_LikeExhibitionPage.html'

    def get_context_data(self, **kwargs):
        context = super(LikeExhibitionList, self).get_context_data()
        return context


class ExhibitionSearch(ListView):
    model = Exhibition
    template_name = 'exhibition/ARTA_search_result.html'
    paginate_by = 6

    def get_queryset(self):
        q = self.kwargs['q']
        piece_list = Exhibition.objects.filter(
            Q(name__contains=q) | Q(category__smallName__contains=q)).distinct()
        return piece_list

    def get_context_data(self, **kwargs):
        context = super(ExhibitionSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'{q}'
        return context


class PieceSearch(ListView):
    model = Piece
    template_name = 'exhibition/ARTA_search_result.html'
    paginate_by = 6

    def get_queryset(self):
        q = self.kwargs['q']
        piece_list = Piece.objects.filter(Q(name__contains=q) | Q(author__contains=q) | Q(major__contains=q)).distinct()
        return piece_list

    def get_context_data(self, **kwargs):
        context = super(PieceSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'{q}'
        return context


class SearchPage:
    def search_page(request):
        return render(
            request,
            'exhibition/ARTA_search_page.html',
            {
                #
            }
        )


class CategoryManage:
    def category_page(request, slug):
        category = Category.objects.get(slug=slug)

        return render(
            request,
            'exhibition/ARTA_User_exhibition_list.html',
            {
                'exhibition_list': Exhibition.objects.filter(category=category),
                'categories': Category.objects.all(),
                'category': category,
            }
        )
