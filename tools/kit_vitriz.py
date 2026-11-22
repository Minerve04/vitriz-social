"""Kit visuel VITRIZ v2 — posts 1080 x 1350, calqué sur la page d'accueil de vitriz.fr.

Langage visuel du site : grandes photos de commerces (assets/*.webp, personnes fictives générées), titres Space Grotesk
(700 pour la 1re ligne, 400 ardoise pour la 2e), petit surtitre Inter 600 en capitales bleu canard, cartes en verre
dépoli (blanc translucide, flou, coins 28 px), puce verte « message WhatsApp » avec icône photo et double coche,
bouton pilule bleu canard avec flèche.

Quatre mises en page, chacune renvoie le contenu de la page (à passer à page() pour l'aperçu, page_depot() pour le dépôt) :
  affiche(...)   : la couverture du site — photo plein cadre, titre blanc géant, carte « Votre métier. Vos mots. »
  etape(...)     : la section « Comment ça marche » — fond clair, titre deux tons, photo arrondie + carte WhatsApp
  metier(...)    : « Vous avez déjà de quoi publier » — photo d'un métier + aperçu du post rédigé par VITRIZ
  citation(...)  : une objection de commerçant sur photo sombre + carte réponse

Photos disponibles (nom sans extension) : florist, phone, flowers, bakery, hairdresser, craftsman, restaurant, boutique.
Les personnes des photos sont fictives : chaque visuel porte « Image illustrative ».
"""
import html as _h

W, H = 1080, 1350
TEAL, INK, SLATE, PAPER, LINE = "#0E7490", "#10262C", "#3C5158", "#F4F8F8", "#D5E6EA"
MINT_BG, MINT_FG = "#E6F7EA", "#1F6B3E"
D = "'Space Grotesk', sans-serif"
T = "'Inter', sans-serif"
PHOTOS = ("florist", "phone", "flowers", "bakery", "hairdresser", "craftsman", "restaurant", "boutique")

ICON = ('<svg width="{s}" height="{s}" viewBox="0 0 1024 1024" style="border-radius:{r}px;display:block">'
        '<rect width="1024" height="1024" fill="#0E7490"/><path fill="#fff" d="M236 170 Q330 560 512 883 Q694 560 788 170 '
        'Q674 508 512 768 Q350 508 236 170 Z"/><path fill="#fff" d="M512 224 Q531 372 630 400 Q531 428 512 575 Q493 428 394 400 '
        'Q493 372 512 224 Z"/></svg>')
ARROW = '<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CAMERA = '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#1F6B3E" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/></svg>'
CHECKS = '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#1F6B3E" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 13l4 4L14 8"/><path d="M10 17l1 0L20 8"/></svg>'
SEND = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#3C5158" stroke-width="1.8" stroke-linejoin="round"><path d="M21 3L3 10.5l7.5 3L14 21z"/><path d="M21 3L10.5 13.5"/></svg>'
SPARK = '<svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#0E7490" stroke-width="1.6" stroke-linejoin="round"><path d="M12 3c.6 4.2 2.8 6.4 7 7-4.2.6-6.4 2.8-7 7-.6-4.2-2.8-6.4-7-7 4.2-.6 6.4-2.8 7-7z"/><path d="M19 15.5c.25 1.6 1 2.35 2.5 2.5-1.5.25-2.25 1-2.5 2.5-.25-1.5-1-2.25-2.5-2.5 1.5-.15 2.25-.9 2.5-2.5z"/></svg>'
OK = '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#1F6B3E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l4 4 10-10"/></svg>'


def e(s):
    return _h.escape(s, quote=True)


def nb(t):
    """Espaces insécables avant la ponctuation haute française."""
    for a, b in ((" :", " :"), (" ;", " ;"), (" ?", " ?"), (" !", " !"),
                 (" %", " %"), (" €", " €"), ("« ", "« "), (" »", " »")):
        t = t.replace(a, b)
    return t


def tx(s):
    return e(nb(s)).replace("\n", "<br>")


def _photo(nom, pos="center"):
    assert nom in PHOTOS, f"photo inconnue : {nom}"
    return f"url('{{ASSETS}}/{nom}.webp')", pos


def logo(couleur="#fff", taille=52):
    return (f'<div style="display:flex;align-items:center;gap:16px;">{ICON.format(s=taille, r=int(taille * .24))}'
            f'<div style="font-family:{D};font-weight:700;font-size:{int(taille * .78)}px;letter-spacing:.01em;color:{couleur};">VITRIZ</div></div>')


def surtitre(t, couleur=TEAL, point=False):
    dot = f'<span style="display:inline-block;width:9px;height:9px;border-radius:50%;background:{couleur};margin-right:14px;vertical-align:middle;"></span>' if point else ""
    return f'<div style="font-family:{T};font-weight:600;font-size:21px;letter-spacing:.06em;text-transform:uppercase;color:{couleur};">{dot}{e(t)}</div>'


def bouton(t="Essayer 7 jours gratuits", fond=TEAL, texte="#fff"):
    return (f'<div style="display:inline-flex;align-items:center;gap:18px;background:{fond};color:{texte};border-radius:999px;'
            f'padding:24px 36px;font-family:{T};font-weight:700;font-size:27px;box-shadow:0 10px 30px rgba(14,116,144,.28);">'
            f'{e(t)}{ARROW.format(s=28, c=texte)}</div>')


def verre(contenu, largeur, pad="30px 32px", fond="rgba(255,255,255,.84)", rayon=28):
    return (f'<div style="width:{largeur}px;box-sizing:border-box;background:{fond};backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);'
            f'border:1px solid rgba(255,255,255,.6);border-radius:{rayon}px;padding:{pad};box-shadow:0 24px 60px rgba(16,38,44,.22);">{contenu}</div>')


def puce_whatsapp(t):
    return (f'<div style="display:flex;align-items:center;gap:16px;background:{MINT_BG};border-radius:18px;padding:20px 22px;">{CAMERA}'
            f'<div style="flex:1;font-family:{T};font-size:27px;color:{MINT_FG};">{tx(t)}</div>{CHECKS}</div>')


def mention(couleur="rgba(255,255,255,.7)"):
    return f'<div style="font-family:{T};font-size:17px;color:{couleur};">Image illustrative</div>'


def pied(sombre=True):
    c = "#fff" if sombre else INK
    return (f'<div style="display:flex;align-items:center;justify-content:space-between;">'
            f'<div style="display:flex;align-items:center;gap:26px;">{bouton()}'
            f'<div style="font-family:{D};font-weight:700;font-size:32px;color:{c};">vitriz.fr</div></div>'
            f'{mention("rgba(255,255,255,.7)" if sombre else "#7A8D93")}</div>')


def _cadre(fond, contenu):
    return (f'<div style="position:relative;overflow:hidden;width:{W}px;height:{H}px;box-sizing:border-box;background:{fond};">'
            f'{contenu}</div>')


# ---------------------------------------------------------------- 1. AFFICHE (couverture du site)
def affiche(photo, titre, texte, surtitre_txt="VITRIZ · Votre savoir-faire, partagé",
            carte=("Votre métier. Vos mots.", "Un post qui vous ressemble."), position="62% center", taille_titre=104):
    """titre : lignes séparées par \\n (4 lignes courtes au plus, ex. "Une photo\\nsur WhatsApp.\\nVotre post\\nest en ligne.")."""
    img, _ = _photo(photo)
    fond = (f'<div style="position:absolute;inset:0;background-image:{img};background-size:cover;background-position:{position};"></div>'
            f'<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,30,36,.88) 0%,rgba(10,30,36,.62) 48%,rgba(10,30,36,.10) 100%);"></div>'
            f'<div style="position:absolute;inset:0;background:linear-gradient(0deg,rgba(10,30,36,.80) 0%,rgba(10,30,36,0) 42%);"></div>')
    carte_html = ""
    if carte:
        carte_html = (f'<div style="position:absolute;right:64px;top:300px;">' + verre(
            f'<div style="display:flex;gap:20px;align-items:flex-start;">{SPARK}<div>'
            f'<div style="font-family:{T};font-weight:700;font-size:28px;color:{INK};white-space:nowrap;">{tx(carte[0])}</div>'
            f'<div style="margin-top:6px;font-family:{T};font-size:22px;color:{SLATE};">{tx(carte[1])}</div></div></div>', 470, "26px 30px", rayon=24) + '</div>')
    corps = (f'<div style="position:absolute;inset:0;padding:72px 72px 70px 72px;display:flex;flex-direction:column;">'
             f'{logo()}'
             f'<div style="flex:1;display:flex;flex-direction:column;justify-content:flex-end;padding-bottom:56px;">'
             f'{surtitre(surtitre_txt, "#fff", point=True)}'
             f'<h1 style="margin:30px 0 0 0;font-family:{D};font-weight:500;font-size:{taille_titre}px;line-height:1.02;letter-spacing:-.015em;color:#fff;">{tx(titre)}</h1>'
             f'<p style="margin:34px 0 0 0;max-width:780px;font-family:{T};font-size:30px;line-height:1.45;color:rgba(255,255,255,.88);">{tx(texte)}</p></div>'
             f'{pied(True)}</div>')
    return _cadre(INK, fond + carte_html + corps)


# ---------------------------------------------------------------- 2. ÉTAPE (comment ça marche)
def etape(photo, titre, titre2, numero, etape_titre, etape_texte, carte_label, carte_corps,
          surtitre_txt="Votre quotidien, en plus simple", position="center"):
    """carte_corps : ("puce", "arrivage du jour") pour un message WhatsApp, ("oui", "Répondez OUI pour publier") pour la validation,
    ou ("texte", "…") pour un extrait de post rédigé."""
    img, _ = _photo(photo)
    kind, val = carte_corps
    if kind == "puce":
        inner = puce_whatsapp(val) + f'<div style="margin-top:16px;font-family:{T};font-size:21px;color:{SLATE};">Une photo. Quelques mots. Envoyé.</div>'
    elif kind == "oui":
        inner = (f'<div style="font-family:{T};font-size:30px;color:{SLATE};">{tx(val)}</div>'
                 f'<div style="display:flex;justify-content:flex-end;margin-top:18px;"><div style="display:flex;gap:10px;align-items:center;background:{MINT_BG};'
                 f'border-radius:16px;padding:12px 18px;font-family:{T};font-size:24px;color:{MINT_FG};">OUI {CHECKS}</div></div>'
                 f'<div style="margin-top:18px;display:flex;gap:14px;align-items:center;background:{MINT_BG};border-radius:16px;padding:16px 18px;'
                 f'font-family:{T};font-size:21px;color:{MINT_FG};">{OK}Publié sur Facebook, Instagram et Google</div>')
    else:
        inner = f'<div style="font-family:{T};font-size:24px;line-height:1.5;color:{INK};">{tx(val)}</div>'
    carte = (f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">{SEND}'
             f'<div style="font-family:{T};font-weight:600;font-size:19px;letter-spacing:.06em;text-transform:uppercase;color:{SLATE};">{e(carte_label)}</div></div>{inner}')
    legende = (f'<div style="font-family:{T};font-weight:600;font-size:21px;color:rgba(255,255,255,.85);">{e(numero)}</div>'
               f'<div style="margin-top:6px;font-family:{D};font-weight:700;font-size:44px;line-height:1.1;color:#fff;">{tx(etape_titre)}</div>'
               f'<div style="margin-top:12px;font-family:{T};font-size:24px;line-height:1.45;color:rgba(255,255,255,.9);">{tx(etape_texte)}</div>')
    photo_bloc = (f'<div style="position:relative;flex:1;border-radius:36px;overflow:hidden;background-image:{img};background-size:cover;background-position:{position};">'
                  f'<div style="position:absolute;inset:0;background:linear-gradient(0deg,rgba(10,30,36,.55) 0%,rgba(10,30,36,0) 45%);"></div>'
                  f'<div style="position:absolute;right:30px;top:30px;">{verre(carte, 470, "26px 28px")}</div>'
                  f'<div style="position:absolute;left:30px;bottom:30px;">{verre(legende, 560, "26px 30px", fond="rgba(25,45,52,.62)", rayon=24)}</div>'
                  f'<div style="position:absolute;right:30px;bottom:24px;">{mention()}</div></div>')
    corps = (f'<div style="position:absolute;inset:0;padding:64px 60px 60px 60px;display:flex;flex-direction:column;">'
             f'<div style="display:flex;justify-content:space-between;align-items:center;">{logo(INK, 46)}{surtitre(surtitre_txt)}</div>'
             f'<h1 style="margin:44px 0 40px 0;font-family:{D};font-weight:700;font-size:70px;line-height:1.06;color:{INK};text-align:center;">{tx(titre)}<br>'
             f'<span style="font-weight:400;color:{SLATE};">{tx(titre2)}</span></h1>'
             f'{photo_bloc}'
             f'<div style="margin-top:36px;display:flex;align-items:center;justify-content:center;gap:28px;">{bouton()}'
             f'<div style="font-family:{D};font-weight:700;font-size:32px;color:{INK};">vitriz.fr</div></div></div>')
    return _cadre("#fff", corps)


# ---------------------------------------------------------------- 3. MÉTIER (un post qui lui ressemble)
def metier(photo, titre, titre2, metier_nom, legende, post_texte, surtitre_txt="À chaque métier, son histoire", position="center"):
    """legende : ce que le commerçant envoie sur WhatsApp ; post_texte : extrait du post que VITRIZ pourrait rédiger
    (exemple illustratif, sans prix ni horaire ni nom réel)."""
    img, _ = _photo(photo)
    apercu = (f'<div style="display:flex;align-items:center;gap:16px;">{ICON.format(s=54, r=14)}<div>'
              f'<div style="font-family:{T};font-weight:700;font-size:24px;color:{INK};">{e(metier_nom)}</div>'
              f'<div style="font-family:{T};font-size:19px;color:#7A8D93;">Rédigé par VITRIZ · à l\'instant</div></div></div>'
              f'<div style="margin-top:20px;font-family:{T};font-size:25px;line-height:1.5;color:{INK};">{tx(post_texte)}</div>')
    photo_bloc = (f'<div style="position:relative;flex:1;border-radius:36px;overflow:hidden;background-image:{img};background-size:cover;background-position:{position};">'
                  f'<div style="position:absolute;left:30px;top:30px;">{verre(puce_whatsapp(legende), 460, "10px", rayon=26)}</div>'
                  f'<div style="position:absolute;left:30px;bottom:30px;">{verre(apercu, 640, "28px 30px")}</div>'
                  f'<div style="position:absolute;right:30px;bottom:24px;">{mention()}</div></div>')
    corps = (f'<div style="position:absolute;inset:0;padding:64px 60px 60px 60px;display:flex;flex-direction:column;">'
             f'<div style="display:flex;justify-content:space-between;align-items:center;">{logo(INK, 46)}{surtitre(surtitre_txt)}</div>'
             f'<h1 style="margin:44px 0 40px 0;font-family:{D};font-weight:700;font-size:70px;line-height:1.06;color:{INK};">{tx(titre)}<br>'
             f'<span style="font-weight:400;color:{SLATE};">{tx(titre2)}</span></h1>'
             f'{photo_bloc}'
             f'<div style="margin-top:36px;display:flex;align-items:center;gap:28px;">{bouton()}'
             f'<div style="font-family:{D};font-weight:700;font-size:32px;color:{INK};">vitriz.fr</div></div></div>')
    return _cadre(PAPER, corps)


# ---------------------------------------------------------------- 4. CITATION (ce qu'on entend)
def citation(photo, phrase, reponse_titre, reponse_texte, surtitre_txt="Ce qu'on entend souvent", position="center"):
    img, _ = _photo(photo)
    fond = (f'<div style="position:absolute;inset:0;background-image:{img};background-size:cover;background-position:{position};"></div>'
            f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,30,36,.88) 0%,rgba(10,30,36,.62) 50%,rgba(10,30,36,.90) 100%);"></div>')
    rep = (f'<div style="display:flex;gap:20px;align-items:flex-start;">{SPARK}<div>'
           f'<div style="font-family:{D};font-weight:700;font-size:38px;line-height:1.15;color:{INK};">{tx(reponse_titre)}</div>'
           f'<div style="margin-top:12px;font-family:{T};font-size:26px;line-height:1.5;color:{SLATE};">{tx(reponse_texte)}</div></div></div>')
    corps = (f'<div style="position:absolute;inset:0;padding:72px;display:flex;flex-direction:column;">'
             f'{logo()}'
             f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;">'
             f'{surtitre(surtitre_txt, "#fff", point=True)}'
             f'<div style="margin-top:30px;font-family:{D};font-weight:500;font-size:78px;line-height:1.08;color:#fff;">{tx("« " + phrase + " »")}</div>'
             f'<div style="margin-top:56px;">{verre(rep, 936, "34px 38px")}</div></div>'
             f'{pied(True)}</div>')
    return _cadre(INK, fond + corps)


# ---------------------------------------------------------------- pages et rendu
_FONTS = """@font-face{{font-family:'Space Grotesk';src:url('{f}/space-grotesk-latin-400-normal.woff2');font-weight:400}}
@font-face{{font-family:'Space Grotesk';src:url('{f}/space-grotesk-latin-500-normal.woff2');font-weight:500}}
@font-face{{font-family:'Space Grotesk';src:url('{f}/space-grotesk-latin-700-normal.woff2');font-weight:700}}
@font-face{{font-family:'Inter';src:url('{f}/inter-latin-400-normal.woff2');font-weight:400}}
@font-face{{font-family:'Inter';src:url('{f}/inter-latin-600-normal.woff2');font-weight:600}}
@font-face{{font-family:'Inter';src:url('{f}/inter-latin-700-normal.woff2');font-weight:700}}"""


def _page(inner, fonts, assets, titre):
    return (f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>{e(titre)}</title><style>{_FONTS.format(f=fonts)}'
            f'body{{margin:0}}</style></head><body>{inner.replace("{ASSETS}", assets)}</body></html>')


def page(inner, base=".", titre="VITRIZ"):
    """Aperçu local : base = dossier contenant fonts/ et assets/ (le dépôt cloné, ou une copie)."""
    return _page(inner, f"{base}/fonts", f"{base}/assets", titre)


def page_depot(inner, titre="VITRIZ"):
    """Page à déposer dans le dépôt Minerve04/vitriz-social (a-publier/<date>.html)."""
    return _page(inner, "../fonts", "../assets", titre)


def render(html_str, out_path, html_path="post.html"):
    """Rend la page en JPEG 1080x1350 et renvoie des contrôles (ok = pas de débordement, polices et images chargées)."""
    import os
    from playwright.sync_api import sync_playwright
    open(html_path, "w", encoding="utf-8").write(html_str)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        pg.goto("file://" + os.path.abspath(html_path))
        pg.wait_for_timeout(700)
        c = pg.evaluate("""async () => { await document.fonts.ready;
          const imgs = [...document.querySelectorAll('[style*="background-image"]')].map(d => getComputedStyle(d).backgroundImage);
          const over = [...document.querySelectorAll('h1,p,div')].filter(d => d.scrollWidth > d.clientWidth + 2 && getComputedStyle(d).overflow !== 'hidden' && d.clientWidth > 0).length;
          return {scrollH: document.documentElement.scrollHeight, scrollW: document.documentElement.scrollWidth, imgs: imgs.length, horiz: over,
                  fonts: [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family.replaceAll('"','') + ' ' + f.weight)}; }""")
        pg.screenshot(path=out_path, type="jpeg", quality=90, clip={"x": 0, "y": 0, "width": W, "height": H})
        b.close()
    c["ok"] = c["scrollH"] <= H and c["scrollW"] <= W and c["horiz"] == 0
    return c
