from kit_vitriz import *
B="base"
outs=[]
v=affiche("florist","Une photo\nsur WhatsApp.\nVotre post\nest en ligne.","Pour les commerçants, artisans et indépendants qui n'ont pas le temps de publier.")
print(render(page(v,B),"v1.jpg","v1.html"))
v=etape("phone","Vous faites votre métier.","On s'occupe du post.","01 / 03","Vous photographiez","Un bouquet, un plat, un chantier terminé. Une photo, deux mots. C'est tout.","Votre message",("puce","arrivage du jour"),position="40% center")
print(render(page(v,B),"v2.jpg","v2.html"))
v=metier("bakery","Vous avez déjà","de quoi publier.","Boulangerie · exemple","fournée du matin","Les premières miches sortent du four, croûte bien dorée et mie alvéolée. Les croissants suivent de près. Passez les chercher encore tièdes.")
print(render(page(v,B),"v3.jpg","v3.html"))
v=citation("hairdresser","Je ne sais jamais quoi écrire sous mes photos.","Vous n'avez plus à écrire.","Envoyez la photo et deux mots sur WhatsApp. VITRIZ rédige un post dans votre style, sans rien inventer. Vous répondez OUI.")
print(render(page(v,B),"v4.jpg","v4.html"))
