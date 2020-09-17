"""trivia_app URL Configuration




Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from first import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name ='index'),
    path('question_one/',views.question_one, name='question_one'),
    path('question_two/',views.question_two, name='question_two'),
    path('index_submission/',views.index_submission, name='index_submission'),
    path('question_one_submission/',views.question_one_submission, name='question_one_submission'),
  
    url('summary',views.summary),
]
