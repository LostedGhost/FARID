from django.shortcuts import render, redirect
from manager.models import *

# Create your views here.
def handle404(request, exception):
    user_id = request.session.get("user_id", None)
    error = request.session.get('error')
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    return render(request, 'administration/error/404.html', {'user': user, 'error': error})

def handle500(request):
    return render(request, 'administration/error/500.html')

def index(request):
    sites = SiteTouristique.objects.all()
    histoires = Histoire.objects.all()
    events = Evenement.objects.all()
    ressources = RessourceNaturelle.objects.all()
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    if request.POST:
        if "recherche" in request.POST:
            recherche = request.POST.get("recherche", None)
            if recherche:
                return redirect(f"/recherche/{recherche}")
            else:
                pass
        return redirect("/")
    return render(request, 'rendu/index.html', {
        "user": user,
        "sites": sites,
        "histoires": histoires,
        "events":events,
        "ressources":ressources,
    })

def sites(request):
    sites = SiteTouristique.objects.all()
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    if request.POST:
        if "recherche" in request.POST:
            recherche = request.POST.get("recherche", None)
            if recherche:
                return redirect(f"/recherche/{recherche}")
            else:
                pass
        return redirect("/site-touristique")
    return render(request, 'rendu/sites.html', {
        "user": user,
        "sites": sites,
    })

def view_site(request, id):
    site = SiteTouristique.objects.get(id=id)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    if request.POST:
        if "recherche" in request.POST:
            recherche = request.POST.get("recherche", None)
            if recherche:
                return redirect(f"/recherche/{recherche}")
            else:
                pass
        elif "comment" in request.POST:
            commentaire = request.POST.get("comment", None)
            com = CommentaireSite(site=site, user=user, contenu=commentaire)
            com.save()
            return redirect(f"/sites/view_site/{site.id}")
        return redirect("/site-touristique")

    return render(request, 'rendu/view/site.html', {
        "user": user,
        "site": site,
    })

def ressources(request):
    ressources = RessourceNaturelle.objects.all()
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    if request.POST:
        if "recherche" in request.POST:
            recherche = request.POST.get("recherche", None)
            if recherche:
                return redirect(f"/recherche/{recherche}")
            else:
                pass
        return redirect("/site-touristique")
    return render(request, 'rendu/ressources.html', {
        "user": user,
        "ressources": ressources,
    })

def view_res(request, id):
    res = RessourceNaturelle.objects.get(id=id)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    if request.POST:
        if "recherche" in request.POST:
            recherche = request.POST.get("recherche", None)
            if recherche:
                return redirect(f"/recherche/{recherche}")
            else:
                pass
        elif "comment" in request.POST:
            commentaire = request.POST.get("comment", None)
            com = CommentaireRessource(ressource=res, user=user, contenu=commentaire)
            com.save()
            return redirect(f"/ressources/view_res/{res.id}")
        return redirect("/ressources")
    return render(request, 'rendu/view/ressource.html', {
        "user": user,
        "res": res,
    })


def histoires(request):
    histoires = Histoire.objects.all()
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    if request.POST:
        if "recherche" in request.POST:
            recherche = request.POST.get("recherche", None)
            if recherche:
                return redirect(f"/recherche/{recherche}")
            else:
                pass
        return redirect("/histoires")
    return render(request, 'rendu/histoires.html', {
        "user": user,
        "histoires":histoires,
    })

def view_hist(request, id):
    hist = Histoire.objects.get(id=id)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    if request.POST:
        if "recherche" in request.POST:
            recherche = request.POST.get("recherche", None)
            if recherche:
                return redirect(f"/recherche/{recherche}")
            else:
                pass
        elif "comment" in request.POST:
            commentaire = request.POST.get("comment", None)
            com = CommentaireHistoire(histoire=hist, user=user, contenu=commentaire)
            com.save()
            return redirect(f"/histoires/view_hist/{hist.id}")
        return redirect("/histoires")
    return render(request, 'rendu/view/histoire.html', {
        "user": user,
        "hist": hist,
    })

def events(request):
    events = Evenement.objects.all()
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    if request.POST:
        if "recherche" in request.POST:
            recherche = request.POST.get("recherche", None)
            if recherche:
                return redirect(f"/recherche/{recherche}")
            else:
                pass
        return redirect("/events")
    return render(request, 'rendu/events.html', {
        "user": user,
        "events": events
    })

def view_event(request, id):
    event = Evenement.objects.get(id=id)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    if request.POST:
        if "recherche" in request.POST:
            recherche = request.POST.get("recherche", None)
            if recherche:
                return redirect(f"/recherche/{recherche}")
            else:
                pass
        elif "comment" in request.POST:
            commentaire = request.POST.get("comment", None)
            com = CommentaireEvent(event=event, user=user, contenu=commentaire)
            com.save()
            return redirect(f"/events/view_event/{event.id}")
        return redirect("/events")
    return render(request, 'rendu/view/event.html', {
        "user": user,
        "event": event,
    })


def about(request):
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    if request.POST:
        if "recherche" in request.POST:
            recherche = request.POST.get("recherche", None)
            if recherche:
                return redirect(f"/recherche/{recherche}")
            else:
                pass
        return redirect("/events")
    return render(request, 'rendu/about.html', {
        "user": user
    })

def recherche(request, mot_recherche):
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    resultats = {}
    resultats["sites"] = SiteTouristique.objects.filter(nom__contains=mot_recherche).union(SiteTouristique.objects.filter(description__contains=mot_recherche))
    resultats["ressources"] = RessourceNaturelle.objects.filter(nom__contains=mot_recherche).union(RessourceNaturelle.objects.filter(description__contains=mot_recherche))
    resultats["histoires"] = Histoire.objects.filter(libelle__contains=mot_recherche).union(Histoire.objects.filter(contenu__contains=mot_recherche))
    resultats["events"] = Evenement.objects.filter(nom__contains=mot_recherche).union(Evenement.objects.filter(description__contains=mot_recherche))
    l = 0
    for el in resultats:
        l += len(resultats[el])
    resultats["len"] = l
    if request.POST:
        if "recherche" in request.POST:
            recherche = request.POST.get("recherche", None)
            if recherche and recherche not in [".", "/"]:
                return redirect(f"/recherche/{recherche}")
            else:
                pass
        return redirect(f"/recherche/{mot_recherche}")
    return render(request, 'rendu/recherche.html', {
        "user": user,
        "resultats": resultats,
    })

def signin(request):
    error = request.session.pop('error', None)
    if request.POST:
        nom = request.POST.get("nom", None)
        prenom = request.POST.get("prenom", None)
        date_naissance = request.POST.get("date_naissance", None)
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        re_password = request.POST.get("re_password", None)
        sexe = bool(int(request.POST.get("sexe",None)))
        if Utilisateur.objects.filter(email=email).exists():
            request.session["error"] = "Cet email est déjà utilisé !!!"
            return redirect("/signin")
        if password != re_password:
            request.session["error"] = "Les deux mots de passe ne correspendent pas !!!"
            return redirect("/signin")
        u = Utilisateur(nom=nom, prenom=prenom, email=email, date_naissance=date_naissance, password=chiffrement_cesar(password), sexe=sexe, profil_id=2)
        u.save()
        return redirect("/login")
    return render(request, 'rendu/signin.html',{
        "error": error
    })

def login(request):
    error = request.session.pop('error', None)
    if request.POST:
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        u = Utilisateur.objects.filter(email=email)
        if not u.exists():
            request.session["error"] = "Cet email n'existe pas!!! Veuillez vous inscrire"
            return redirect("/login")
        else:
            u = u.first()
        if u.true_pass() == password:
            request.session["user_id"] = u.id
            return redirect("/")
        else:
            request.session["error"] = "Mauvais mot de passe!!! Veuillez réessayer"
            return redirect("/login")
    return render(request, 'rendu/login.html',{
        "error": error
    })

def logout(request):
    request.session.clear()
    return redirect("/")

def profil(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    if request.POST:
        if "recherche" in request.POST:
            recherche = request.POST.get("recherche", None)
            if recherche:
                return redirect(f"/recherche/{recherche}")
            else:
                pass
        else:
            if "photo" in request.FILES or "password" in request.POST:
                if "photo" in request.FILES:
                    photo = request.FILES["photo"]
                else:
                    photo = None
                password = request.POST.get("password", None)
                if photo:
                    user.photo = photo
                if password and len(password) >= 4:
                    user.password = chiffrement_cesar(password)
                else:
                    request.session["error"] = "Mot de passe incorrecte!!!"
                user.save()
        return redirect("/profil")
                

    return render(request, 'administration/profil.html', {
        "user": user,
        "error": error,
        "success": success
    })


############################## SITES TOURISTIQUES
def liste_sites(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    sites = SiteTouristique.objects.all()
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    
    return render(request, 'administration/sites/list.html', {
        "sites": sites,
        "user": user,
        "error": error,
        "success": success
    })

def ajout_site(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    communes = Commune.objects.all()
    if request.POST:
        nom = request.POST.get("nom", None)
        description = request.POST.get("description", None)
        commune = request.POST.get("commune", None)
        if commune == "":
            request.session["error"] = "Veuillez choisir une commune!!!"
            return redirect("/sites/add")
        commune = Commune.objects.get(id=int(commune))
        site = SiteTouristique(nom=nom, description=description, commune=commune)
        
        if "photo" in request.FILES:
            site.save()
            sitePhoto = PhotoSite(image=request.FILES["photo"], site=site, is_first=True)
            sitePhoto.save()
        else:
            request.session["error"] = "Veuillez choisir une photo!!!"
            return redirect("/sites/add")
        return redirect("/sites/list")
        
    return render(request,"administration/sites/add.html", {
        "user": user,
        "error": error,
        "success": success,
        "communes": communes
    })
        
def delete_site(request, id):
    site = SiteTouristique.objects.get(id=id)
    site.delete()
    request.session["success"] = "Le site tourisque a bien été supprimé!!!"
    return redirect("/sites/list")

def edit_site(request, id):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    site = SiteTouristique.objects.get(id=id)
    communes = Commune.objects.all()
    if request.POST:
        nom = request.POST.get("nom", None)
        description = request.POST.get("description", None)
        commune = request.POST.get("commune", None)
        if commune == "":
            request.session["error"] = "Veuillez choisir une commune!!!"
            return redirect(f"/sites/edit/{id}")
        commune = Commune.objects.get(id=int(commune))
        site.nom = nom
        site.description = description
        site.commune = commune
        if "photo" in request.FILES:
            photo = PhotoSite.objects.get(site=site, is_first=True)
            photo.image = request.FILES["photo"]
            photo.save()
        if "others_images" in request.FILES:
            images = request.FILES.getlist("others_images")
            if len(images) > 0:
                old_photos = site.other_pictures()
                for ph in old_photos:
                    ph.delete()
            for img in images:
                photo = PhotoSite(image=img, site=site)
                photo.save()
        site.save()
        request.session["success"] = "Le site a bien été modifié!!!"
        return redirect("/sites/list")
    return render(request,"administration/sites/edit.html", {
        "user": user,
        "error": error,
        "success": success,
        "site": site,
        "communes": communes
    })

################################### RESSOURCES NATURELLES
def liste_ressources(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    ressources = RessourceNaturelle.objects.all()
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    
    return render(request, 'administration/ressources/list.html', {
        "ressources": ressources,
        "user": user,
        "error": error,
        "success": success
    })

def ajout_ressource(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    communes = Commune.objects.all()
    if request.POST:
        nom = request.POST.get("nom", None)
        description = request.POST.get("description", None)
        commune = request.POST.get("commune", None)
        if commune == "":
            request.session["error"] = "Veuillez choisir une commune!!!"
            return redirect("/ressources/add")
        commune = Commune.objects.get(id=int(commune))
        res = RessourceNaturelle(nom=nom, description=description, commune=commune)
        
        if "photo" in request.FILES:
            res.save()
            resPhoto = PhotoRessourceNaturelle(image=request.FILES["photo"], ressource=res, is_first=True)
            resPhoto.save()
        else:
            request.session["error"] = "Veuillez choisir une photo!!!"
            return redirect("/ressources/add")
        return redirect("/ressources/list")
        
    return render(request,"administration/ressources/add.html", {
        "user": user,
        "error": error,
        "success": success,
        "communes": communes
    })
        
def delete_ressource(request, id):
    site = RessourceNaturelle.objects.get(id=id)
    site.delete()
    request.session["success"] = "La ressource naturelle a bien été supprimée !!!"
    return redirect("/ressources/list")

def edit_ressource(request, id):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    res = RessourceNaturelle.objects.get(id=id)
    communes = Commune.objects.all()
    if request.POST:
        nom = request.POST.get("nom", None)
        description = request.POST.get("description", None)
        commune = request.POST.get("commune", None)
        if commune == "":
            request.session["error"] = "Veuillez choisir une commune!!!"
            return redirect(f"/sites/edit/{id}")
        commune = Commune.objects.get(id=int(commune))
        res.nom = nom
        res.description = description
        res.commune = commune
        if "photo" in request.FILES:
            photo = PhotoRessourceNaturelle.objects.get(ressource=res, is_first=True)
            photo.image = request.FILES["photo"]
            photo.save()
        if "others_images" in request.FILES:
            images = request.FILES.getlist("others_images")
            if len(images) > 0:
                old_photos = res.other_pictures()
                for ph in old_photos:
                    ph.delete()
            for img in images:
                photo = PhotoRessourceNaturelle(image=img, ressource=res)
                photo.save()
        res.save()
        request.session["success"] = "La ressource naturelle a bien été modifiée !!!"
        return redirect("/ressources/list")
    return render(request,"administration/ressources/edit.html", {
        "user": user,
        "error": error,
        "success": success,
        "res": res,
        "communes": communes
    })

################################### HISTOIRES
def liste_histoires(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    histoires = Histoire.objects.all()
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    
    return render(request, 'administration/histoires/list.html', {
        "histoires": histoires,
        "user": user,
        "error": error,
        "success": success
    })

def ajout_histoire(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    if request.POST:
        nom = request.POST.get("nom", None)
        description = request.POST.get("description", None)
        hist = Histoire(libelle=nom, contenu=description)
        
        if "photo" in request.FILES:
            hist.save()
            histPhoto = PhotoHistoire(image=request.FILES["photo"], histoire=hist, is_first=True)
            histPhoto.save()
        else:
            request.session["error"] = "Veuillez choisir une photo!!!"
            return redirect("/histoires/add")
        return redirect("/histoires/list")
        
    return render(request,"administration/histoires/add.html", {
        "user": user,
        "error": error,
        "success": success
    })
        
def delete_histoire(request, id):
    site = Histoire.objects.get(id=id)
    site.delete()
    request.session["success"] = "L'histoire a bien été supprimée !!!"
    return redirect("/histoires/list")

def edit_histoire(request, id):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    hist = Histoire.objects.get(id=id)
    if request.POST:
        nom = request.POST.get("nom", None)
        description = request.POST.get("description", None)
        hist.libelle = nom
        hist.contenu = description
        if "photo" in request.FILES:
            photo = PhotoHistoire.objects.get(histoire=hist, is_first=True)
            photo.image = request.FILES["photo"]
            photo.save()
        if "others_images" in request.FILES:
            images = request.FILES.getlist("others_images")
            if len(images) > 0:
                old_photos = hist.other_pictures()
                for ph in old_photos:
                    ph.delete()
            for img in images:
                photo = PhotoHistoire(image=img, histoire=hist)
                photo.save()
        hist.save()
        request.session["success"] = "L'histoire a bien été modifiée !!!"
        return redirect("/histoires/list")
    return render(request,"administration/histoires/edit.html", {
        "user": user,
        "error": error,
        "success": success,
        "hist": hist
    })

################################### EVENEMENTS
def liste_events(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    events = Evenement.objects.all()
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    
    return render(request, 'administration/events/list.html', {
        "events": events,
        "user": user,
        "error": error,
        "success": success
    })

def ajout_event(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    communes = Commune.objects.all()
    if request.POST:
        nom = request.POST.get("nom", None)
        description = request.POST.get("description", None)
        commune = request.POST.get("commune", None)
        if commune == "":
            request.session["error"] = "Veuillez choisir une commune!!!"
            return redirect("/events/add")
        commune = Commune.objects.get(id=int(commune))
        date_deroulement = request.POST.get("date_debut", None)
        date_deroulement = text_to_date(str(date_deroulement))
        date_fin = request.POST.get("date_fin", None)
        if date_fin:
            date_fin = text_to_date(str(date_fin))
            diff_jours = nombre_de_jours(date_deroulement, date_fin)
            if diff_jours < 0:
                request.session["error"] = "La date de fin ne peut pas être antérieure à la date de déroulement!"
                return redirect("/events/add")
        else:
            date_fin = None
        event = Evenement(nom=nom, description=description, commune=commune, date_deroulement=date_deroulement, date_fin=date_fin)
        
        if "photo" in request.FILES:
            event.save()
            eventPhoto = PhotoEvenement(image=request.FILES["photo"], event=event, is_first=True)
            eventPhoto.save()
        else:
            request.session["error"] = "Veuillez choisir une photo!!!"
            return redirect("/events/add")
        return redirect("/events/list")
        
    return render(request,"administration/events/add.html", {
        "user": user,
        "error": error,
        "success": success,
        "communes": communes
    })
        
def delete_event(request, id):
    site = Evenement.objects.get(id=id)
    site.delete()
    request.session["success"] = "L'évènement a bien été supprimé !!!"
    return redirect("/events/list")

def edit_event(request, id):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    event = Evenement.objects.get(id=id)
    communes = Commune.objects.all()
    if request.POST:
        nom = request.POST.get("nom", None)
        description = request.POST.get("description", None)
        commune = request.POST.get("commune", None)
        if commune == "":
            request.session["error"] = "Veuillez choisir une commune!!!"
            return redirect(f"/events/edit/{id}")
        commune = Commune.objects.get(id=int(commune))
        date_deroulement = request.POST.get("date_debut", None)
        date_fin = request.POST.get("date_fin", None)
        date_fin = text_to_date(str(date_fin))
        diff_jours = nombre_de_jours(date_deroulement, date_fin)
        if diff_jours < 0:
            request.session["error"] = "La date de fin ne peut pas être antérieure à la date de déroulement!"
            return redirect(f"/events/edit/{id}")
        event.nom = nom
        event.description = description
        event.commune = commune
        event.date_deroulement = date_deroulement
        event.date_fin = date_fin
        if "photo" in request.FILES:
            photo = PhotoEvenement.objects.get(event=event, is_first=True)
            photo.image = request.FILES["photo"]
            photo.save()
        if "others_images" in request.FILES:
            images = request.FILES.getlist("others_images")
            if len(images) > 0:
                old_photos = event.other_pictures()
                for ph in old_photos:
                    ph.delete()
            for img in images:
                photo = PhotoEvenement(image=img, event=event)
                photo.save()
        event.save()
        request.session["success"] = "L'évènement a bien été modifié !!!"
        return redirect("/events/list")
    return render(request,"administration/events/edit.html", {
        "user": user,
        "error": error,
        "success": success,
        "event": event,
        "communes": communes
    })

################################# CIRCUITS
def liste_circuits(request):
    circuits = Circuit.objects.all()
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    return render(request,"administration/circuits/list.html", {
        "user": user,
        "error": error,
        "success": success,
        "circuits": circuits
    })

def ajout_circuit(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    if request.POST:
        nom = request.POST.get("nom", None)
        description=  request.POST.get("description", None)
        cout = request.POST.get("cout", None)
        cir = Circuit(nom=nom, description=description, cout=int(cout))
        cir.save()
        request.session["success"] = "Le circuit a bien été ajouté !!!"
        return redirect("/circuits/list")
    return render(request,"administration/circuits/add.html", {
        "user": user,
        "error": error,
        "success": success,
    })

def delete_circuit(request, id):
    site = Circuit.objects.get(id=id)
    site.delete()
    request.session["success"] = "Le circuit a bien été supprimé !!!"
    return redirect("/circuits/list")

def edit_circuit(request, id):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    cir = Circuit.objects.get(id=id)
    if request.POST:
        nom = request.POST.get("nom", None)
        description=  request.POST.get("description", None)
        cout = request.POST.get("cout", None)
        cir.nom = nom
        cir.description = description
        cir.cout = int(cout)
        cir.save()
        request.session["success"] = "Le circuit a bien été modifié !!!"
        return redirect("/circuits/list")
    return render(request,"administration/circuits/edit.html", {
        "user": user,
        "error": error,
        "success": success,
        "cir": cir
    })

def organize_circuit(request, id):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    cir = Circuit.objects.get(id=id)
    l_sites = cir.sites().values_list('site_id', flat=True)
    sites = []
    for s in SiteTouristique.objects.all():
        if s.id not in l_sites:
            sites.append(s)
    l_res = cir.ressources().values_list('res_id', flat=True)
    ressources = []
    for r in RessourceNaturelle.objects.all():
        if r.id not in l_res:
            ressources.append(r)
    l_event = cir.events().values_list('event_id', flat=True)
    events = []
    for e in Evenement.objects.all():
        if e.id not in l_event:
            events.append(e)
    if request.POST:
        site = request.POST.get("site", None)
        res = request.POST.get("res", None)
        event = request.POST.get("event", None)
        if not site and not res and not event and request.POST:
            request.session["error"] = "Veuillez sélectionner au moins un élément"
            return redirect(f"/circuits/organize/{cir.id}")
        if site:
            s = SiteTouristique.objects.get(id=int(site))
            p = PointCircuit(circuit=cir, site=s, ordre=cir.last_ordre()+1)
            p.save()
            return redirect(f"/circuits/organize/{cir.id}")
        if res:
            r = RessourceNaturelle.objects.get(id=int(res))
            p = PointCircuit(circuit=cir, res=r, ordre=cir.last_ordre()+1)
            p.save()
            return redirect(f"/circuits/organize/{cir.id}")
        if event:
            e = Evenement.objects.get(id=int(event))
            p = PointCircuit(circuit=cir, event=e, ordre=cir.last_ordre()+1)
            p.save()
            return redirect(f"/circuits/organize/{cir.id}")
    return render(request, "administration/circuits/organize.html",{
        "user": user,
        "error": error,
        "success": success,
        "cir": cir,
        "sites": sites,
        "ressources": ressources,
        "events": events,
    })

def save_organize(request, id):
    circuit = Circuit.objects.get(id=id)
    if circuit.is_special:
        circuit.cout = circuit.longueur() * PRICE_BY_POINT
        circuit.save()
    return redirect("/circuits_VIP")

def delete_point_circuit(request, id):
    point = PointCircuit.objects.get(id=id)
    circuit_id = point.circuit.id
    point.delete()
    request.session["success"] = "Le point du circuit a bien été supprimé !!!"
    return redirect(f"/circuits/organize/{circuit_id}")

def circuits(request):
    circuits = Circuit.objects.all().filter(is_special=False)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    if request.POST:
        if "recherche" in request.POST:
            recherche = request.POST.get("recherche", None)
            if recherche:
                return redirect(f"/recherche/{recherche}")
            else:
                pass
        return redirect("/site-touristique")
    return render(request, 'rendu/view/circuits.html', {
        "user": user,
        "circuits": circuits,
    })

def circuit(request, id):
    cir = Circuit.objects.get(id=id)
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    return render(request, 'rendu/view/circuit.html', {
        "user": user,
        "error": error,
        "success": success,
        "cir": cir,
    })

def save_reservation(request, circuit_id):
    transaction_id = request.GET.get("transaction_id", None)
    cir = Circuit.objects.get(id=circuit_id)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    reservation = Reservation(circuit=cir, user=user, transaction_id=transaction_id, montant_paye=cir.cout)
    reservation.save()
    return redirect("/mes_reservations")

def mes_reservations(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    reservations = Reservation.objects.filter(user=user)
    return render(request, 'administration/reservations/mes_reservations.html', {
        "user": user,
        "error": error,
        "success": success,
        "reservations": reservations
    })

def cloture_res(request, id):
    reservation = Reservation.objects.get(id=id)
    reservation.statut = True
    reservation.save()
    request.session["success"] = f"La réservation a bien été clôturée !!"
    return redirect("/mes_reservations")

def reservations(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    reservations = Reservation.objects.all()
    return render(request, 'administration/reservations/list.html', {
        "user": user,
        "error": error,
        "success": success,
        "reservations": reservations
    })

def delete_comment_site(request, id):
    comment = CommentaireSite.objects.get(id=id)
    site_id = comment.site.id
    comment.delete()
    return redirect(f"/sites/view_site/{site_id}")

def delete_comment_hist(request, id):
    comment = CommentaireHistoire.objects.get(id=id)
    hist_id = comment.histoire.id
    comment.delete()
    return redirect(f"/histoires/view_hist/{hist_id}")

def delete_comment_res(request, id):
    comment = CommentaireRessource.objects.get(id=id)
    res_id = comment.ressource.id
    comment.delete()
    return redirect(f"/ressources/view_res/{res_id}")

def delete_comment_event(request, id):
    comment = CommentaireEvent.objects.get(id=id)
    event_id = comment.event.id
    comment.delete()
    return redirect(f"/events/view_event/{event_id}")

def circuits_VIP(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    circuits = Circuit.objects.filter(is_special=True, user=user)
    return render(request, 'administration/circuits/VIP.html', {
        "user": user,
        "error": error,
        "success": success,
        "circuits": circuits
    })

def circuit_VIP_add(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    user_id = request.session.get("user_id", None)
    user = None
    if user_id is not None:
        user = Utilisateur.objects.get(id=user_id)
    if request.POST:
        nom = request.POST.get("nom", None)
        description = request.POST.get("description", None)
        circuit = Circuit(nom=nom, description=description, user=user, is_special=True)
        circuit.save()
        request.session["success"] = "Le circuit étant ajouté, ajoutez maintenant les lieux et activités !"
        return redirect("/circuits_VIP")
    return render(request, 'administration/circuits/VIP_add.html',{
        "user": user,
        "error": error,
        "success": success
    })