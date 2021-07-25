from django.shortcuts import render
from django.contrib.postgres.search import (
    SearchQuery,
    SearchVector,
    SearchRank
)
from django.views.generic import ListView
from django.db.models import Q

from .models import ViralTweet


class SearchResults(ListView):
    model = ViralTweet
    context_object_name = "tweets"
    template_name = "search_tweets.html"

    def get_queryset(self):
        query = self.request.GET.get("q")

        if query:

            search_vector = SearchVector("user_handle") + SearchVector("tweet")

            search_query = SearchQuery(query)
            return (
                ViralTweet.objects.annotate(rank=SearchRank(search_vector, search_query))
                .order_by("-rank")
            )

        else:
            return ViralTweet.objects.all()