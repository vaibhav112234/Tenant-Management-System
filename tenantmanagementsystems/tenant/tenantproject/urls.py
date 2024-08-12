from django.urls import path,include

from .import views
urlpatterns = [

    path('',views.index),

    path('register',views.Register),
    path('registration',views.registration),

    path('dashboard',views.dashboard),


    path('add_tenant',views.add_tenant),
    path('add',views.add),
    path('view_tenant', views.view_tenant),
    path('tenant_delete', views.tenant_delete),
    path('tenant_edit', views.tenant_edit),
    path('update_data', views.update_data),


    path('Logout',views.Logout),


    path('main_add',views.main_add),
    path('addition',views.addition),
    path('main_view',views.main_view),
    path('main_delete', views.main_delete),
    path('main_edit', views.main_edit),
    path('update_main', views.update_main),


    path('profile',views.profile),
    path('profile_edit',views.profile_edit),
    path('update_profile',views.update_profile),








    path('sub_add',views.sub_add),
    path('additions',views.additions),
    path('sub_view',views.sub_view),
    path('sub_delete', views.sub_delete),
    path('sub_edit', views.sub_edit),
    path('update_sub',views.update_sub),
    path('previous_reading',views.previous_reading),


    path('tanker_add',views.tanker_add),
    path('tanker_addition',views.tanker_addition),
    path('tanker_view', views.tanker_view),
    path('tanker_delete',views.tanker_delete),
    path('tanker_edit', views.tanker_edit),
    path('update_tanker', views.update_tanker),



    path('report',views.report),
    path('monthly_report',views.monthly_report),
    path('tanker_report',views.tanker_report),
    path('search',views.search),
    path('main_search',views.main_search),
]
