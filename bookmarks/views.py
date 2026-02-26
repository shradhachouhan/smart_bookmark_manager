from rest_framework import viewsets
from .models import Bookmark
from .serializers import BookmarkSerializer
from django.shortcuts import render, redirect, get_object_or_404

class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer


# ---------- Frontend Views ----------

def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    return render(request, "bookmarks/list.html", {"bookmarks": bookmarks})

def bookmark_add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        url = request.POST.get("url")
        Bookmark.objects.create(title=title, url=url)
        return redirect("bookmark_list")
    return render(request, "bookmarks/add.html")

def bookmark_edit(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    if request.method == "POST":
        bookmark.title = request.POST.get("title")
        bookmark.url = request.POST.get("url")
        bookmark.save()
        return redirect("bookmark_list")
    return render(request, "bookmarks/edit.html", {"bookmark": bookmark})

def bookmark_delete(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    bookmark.delete()
    return redirect("bookmark_list")