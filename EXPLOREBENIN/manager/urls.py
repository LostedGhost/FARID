from django.urls import path
from manager import views

urlpatterns = [
    path(r'', views.index, name="home"),
    path(r'site-touristique', views.sites, name="sites"),
    path(r'ressources', views.ressources, name="ressources"),
    path(r'histoires', views.histoires, name="histoires"),
    path(r'events', views.events, name="events"),
    path(r'about', views.about, name="about"),
    path(r'recherche/<str:mot_recherche>', views.recherche, name="recherche"),
    path(r'signin', views.signin, name="signin"),
    path(r'login', views.login, name="login"),
    path(r'logout', views.logout, name="logout"),
    path(r'profil', views.profil, name="profil"),
    
    path(r'sites/list', views.liste_sites, name="liste_sites"),
    path(r'sites/add', views.ajout_site, name="ajout_site"),
    path(r'sites/delete/<int:id>', views.delete_site, name="delete_site"),
    path(r'sites/edit/<int:id>', views.edit_site, name="edit_site"),
    path(r'sites/view_site/<int:id>', views.view_site, name="view_site"),
    
    
    path(r'ressources/list', views.liste_ressources, name="liste_ressources"),
    path(r'ressources/add', views.ajout_ressource, name="ajout_ressource"),
    path(r'ressources/delete/<int:id>', views.delete_ressource, name="delete_ressource"),
    path(r'ressources/edit/<int:id>', views.edit_ressource, name="edit_ressource"),
    path(r'ressources/view_res/<int:id>', views.view_res, name="view_res"),
    
    path(r'histoires/list', views.liste_histoires, name="liste_histoires"),
    path(r'histoires/add', views.ajout_histoire, name="ajout_histoire"),
    path(r'histoires/delete/<int:id>', views.delete_histoire, name="delete_histoire"),
    path(r'histoires/edit/<int:id>', views.edit_histoire, name="edit_histoire"),
    path(r'histoires/view_hist/<int:id>', views.view_hist, name="view_hist"),
    
    path(r'events/list', views.liste_events, name="liste_events"),
    path(r'events/add', views.ajout_event, name="ajout_event"),
    path(r'events/delete/<int:id>', views.delete_event, name="delete_event"),
    path(r'events/edit/<int:id>', views.edit_event, name="edit_event"),
    path(r'events/view_event/<int:id>', views.view_event, name="view_event"),
    
    path(r'circuits/list', views.liste_circuits, name="liste_circuits"),
    path(r'circuits/add', views.ajout_circuit, name="ajout_circuit"),
    path(r'circuits/delete/<int:id>', views.delete_circuit, name="delete_circuit"),
    path(r'circuits/edit/<int:id>', views.edit_circuit, name="edit_circuit"),
    path(r'circuits/organize/<int:id>', views.organize_circuit, name="organize_circuit"),
    path(r'circuits/delete_point_circuit/<int:id>', views.delete_point_circuit, name="delete_point_circuit"),
    path(r'save_organize/<int:id>', views.save_organize, name="save_organize"),
    path(r'circuits', views.circuits, name="circuits"),
    path(r'circuit/<int:id>', views.circuit, name="circuit"),
    path(r'valid_reservation/<int:circuit_id>', views.save_reservation, name="save_reservation"),
    path(r'mes_reservations', views.mes_reservations, name="mes_reservations"),
    path(r'cloture_res/<int:id>', views.cloture_res, name="cloture_res"),
    path(r'reservations/list', views.reservations, name="reservations"),
    path(r'circuits_VIP', views.circuits_VIP, name="circuits_VIP"),
    path(r'circuit_VIP_add', views.circuit_VIP_add, name="circuit_VIP_add"),
    
    path(r'deleteCommentSite/<int:id>', views.delete_comment_site, name="delete_comment_site"),
    path(r'deleteCommentHist/<int:id>', views.delete_comment_hist, name="delete_comment_hist"),
    path(r'deleteCommentRes/<int:id>', views.delete_comment_res, name="delete_comment_res"),
    path(r'deleteCommentEv/<int:id>', views.delete_comment_event, name="delete_comment_event"),
    
]