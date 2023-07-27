from django.urls import path

from langcorrect.posts.api.views import PostReplyCreateUpdateAPIView
from langcorrect.posts.views import post_detail_view, post_list_view, post_update_view

app_name = "posts"
urlpatterns = [
    path("", view=post_list_view, name="list"),
    path("~post_reply/", PostReplyCreateUpdateAPIView.as_view(), name="create-update-reply"),
    path("<str:slug>/", view=post_detail_view, name="detail"),
    path("<str:slug>/update/", view=post_update_view, name="update"),
]
