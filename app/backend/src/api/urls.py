from django.urls import path, include


urlpatterns = [
    path('account/', include('account.urls')),
    path('lobby/', include('lobby.urls')),
    path('recomentadions/', include('recommendations.urls')),
    path('video/', include('video.urls')),
]
