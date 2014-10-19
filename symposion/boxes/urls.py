from django.conf.urls import patterns, include, url


urlpatterns = patterns("symposion.boxes.views",
    url(r"^([-\w]+)/edit/$", "box_edit", name="box_edit"),
)
