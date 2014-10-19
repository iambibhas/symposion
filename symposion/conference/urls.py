from django.conf.urls import patterns, include, url


urlpatterns = patterns("symposion.conference.views",
    url(r"^users/$", "user_list", name="user_list"),
)
