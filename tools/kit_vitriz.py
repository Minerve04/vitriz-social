"""Kit visuel VITRIZ — posts réseaux sociaux 1080 x 1350 (portrait).

Charte : bleu canard #0E7490, encre #10262C, fond clair #F4F8F8, accent ambre #F5B942,
polices Space Grotesk (titres) et Inter (texte).

Usage :
    from kit_vitriz import *
    inner = header("L'ASTUCE DU LUNDI") + title("...") + subtitle("...") + chat([...]) + cta()
    html = page(shell(inner, fond="clair"), fontdir="node_modules/@fontsource")   # aperçu local
    render(html, "post.jpg")
    depot = page_depot(shell(inner, fond="clair"), "titre")                     # version à déposer
"""
import html as _h

W, H = 1080, 1350
C = dict(teal="#0E7490", teal_dark="#0B5C73", ink="#10262C", muted="#4A5F66", paper="#F4F8F8",
         white="#FFFFFF", rule="#D3E2E5", amber="#F5B942", wa_out="#D9FDD3", wa_in="#FFFFFF",
         wa_bg="#EFE7DE")
D = "'Space Grotesk', sans-serif"
T = "'Inter', sans-serif"


def e(s):
    return _h.escape(s, quote=True)


def nb(t):
    """Espaces insécables avant la ponctuation haute française."""
    for a, b in ((" :", " :"), (" ;", " ;"), (" ?", " ?"), (" !", " !"),
                 (" %", " %"), (" €", " €"), ("« ", "« "), (" »", " »")):
        t = t.replace(a, b)
    return t


def logo(color):
    return f'''<div style="display:flex;align-items:center;gap:14px;">
<svg width="44" height="44" viewBox="0 0 100 100"><rect width="100" height="100" rx="22" fill="{C['teal'] if color != C['white'] else C['white']}"/>
<path d="M50 18 Q54 46 82 50 Q54 54 50 82 Q46 54 18 50 Q46 46 50 18Z" fill="{C['white'] if color != C['white'] else C['teal']}"/></svg>
<div style="font-family:{D};font-weight:700;font-size:34px;letter-spacing:0.06em;color:{color};">VITRIZ</div></div>'''


def header(rubrique, fond="clair"):
    col = C['ink'] if fond == "clair" else C['white']
    tag_bg = C['teal'] if fond == "clair" else C['amber']
    tag_fg = C['white'] if fond == "clair" else C['ink']
    return f'''<div style="display:flex;justify-content:space-between;align-items:center;">
{logo(col)}
<div style="font-family:{T};font-weight:600;font-size:19px;letter-spacing:0.12em;background:{tag_bg};color:{tag_fg};padding:10px 18px;border-radius:999px;">{e(rubrique)}</div></div>'''


def title(t, fond="clair", size=78, accent=None):
    """t peut contenir <em>…</em> pour la partie en couleur (passée telle quelle)."""
    col = C['ink'] if fond == "clair" else C['white']
    acc = accent or (C['teal'] if fond == "clair" else C['amber'])
    t = t.replace("<em>", f'<span style="color:{acc};">').replace("</em>", "</span>")
    return f'''<h1 style="margin:56px 0 0 0;font-family:{D};font-weight:700;font-size:{size}px;line-height:1.04;letter-spacing:-0.02em;color:{col};">{t}</h1>'''


def subtitle(t, fond="clair", size=29):
    col = C['muted'] if fond == "clair" else "#CFE6EA"
    return f'''<p style="margin:26px 0 0 0;font-family:{T};font-size:{size}px;line-height:1.4;color:{col};max-width:900px;">{e(t)}</p>'''


def chat(messages, height=None, emoji="🥐"):
    """Maquette de conversation WhatsApp. messages = [(sens, texte)] ; sens 'out' (commerçant), 'in' (VITRIZ),
    'photo' (vignette photo envoyée, texte = légende de la vignette)."""
    rows = []
    for sens, txt in messages:
        if sens == "photo":
            rows.append(f'''<div style="align-self:flex-end;background:{C['wa_out']};border-radius:18px 18px 4px 18px;padding:8px;max-width:62%;box-shadow:0 1px 1px rgba(0,0,0,.08);">
<div style="position:relative;width:300px;height:190px;border-radius:12px;background:linear-gradient(135deg,#F7C59F 0%,#E58F65 45%,#9C5B3B 100%);display:flex;align-items:flex-end;justify-content:flex-start;">
<div style="position:absolute;left:0;right:0;top:22px;text-align:center;font-size:92px;line-height:1;">{emoji}</div>
<div style="position:relative;margin:10px;font-family:{T};font-size:17px;color:#fff;background:rgba(0,0,0,.35);padding:4px 10px;border-radius:8px;">📷 {e(txt)}</div></div></div>''')
        else:
            out = sens == "out"
            rows.append(f'''<div style="align-self:{'flex-end' if out else 'flex-start'};background:{C['wa_out'] if out else C['wa_in']};border-radius:{'18px 18px 4px 18px' if out else '18px 18px 18px 4px'};padding:14px 18px;max-width:78%;font-family:{T};font-size:23px;line-height:1.38;color:#111B21;box-shadow:0 1px 1px rgba(0,0,0,.08);">{e(nb(txt))}</div>''')
    hs = f"height:{height}px;" if height else ""
    return f'''<div style="margin-top:0;{hs}background:{C['wa_bg']};border-radius:28px;padding:26px 26px 30px 26px;display:flex;flex-direction:column;gap:14px;border:1px solid rgba(0,0,0,.06);">
<div style="display:flex;align-items:center;gap:12px;padding-bottom:10px;border-bottom:1px solid rgba(0,0,0,.08);">
<div style="width:40px;height:40px;border-radius:50%;background:{C['teal']};display:flex;align-items:center;justify-content:center;"><svg width="22" height="22" viewBox="0 0 100 100"><path d="M50 12 Q55 45 88 50 Q55 55 50 88 Q45 55 12 50 Q45 45 50 12Z" fill="#fff"/></svg></div>
<div style="font-family:{T};font-weight:600;font-size:21px;color:#111B21;">VITRIZ</div>
<div style="font-family:{T};font-size:17px;color:#667781;">sur WhatsApp</div></div>
{''.join(rows)}</div>'''


def points(items, fond="clair"):
    """Liste de 2 à 4 points : [(titre, texte)]."""
    col = C['ink'] if fond == "clair" else C['white']
    mut = C['muted'] if fond == "clair" else "#CFE6EA"
    num_bg = C['teal'] if fond == "clair" else C['amber']
    num_fg = C['white'] if fond == "clair" else C['ink']
    cells = []
    for i, (t, d) in enumerate(items, 1):
        cells.append(f'''<div style="display:flex;gap:26px;align-items:flex-start;padding:26px 0;{'border-top:1px solid ' + (C['rule'] if fond == 'clair' else 'rgba(255,255,255,.18)') + ';' if i > 1 else ''}">
<div style="flex:none;width:58px;height:58px;border-radius:16px;background:{num_bg};color:{num_fg};font-family:{D};font-weight:700;font-size:30px;display:flex;align-items:center;justify-content:center;">{i}</div>
<div><div style="font-family:{D};font-weight:700;font-size:34px;line-height:1.15;color:{col};">{e(nb(t))}</div>
<div style="margin-top:8px;font-family:{T};font-size:25px;line-height:1.4;color:{mut};">{e(nb(d))}</div></div></div>''')
    return f'<div>{"".join(cells)}</div>'


def quote(t, auteur, fond="clair"):
    """Grande citation (objection ou phrase type d'un commerçant, jamais attribuée à une personne réelle)."""
    col = C['ink'] if fond == "clair" else C['white']
    acc = C['teal'] if fond == "clair" else C['amber']
    return f'''<div style="margin-top:0;border-left:8px solid {acc};padding-left:36px;">
<div style="font-family:{D};font-weight:500;font-size:56px;line-height:1.16;color:{col};">{e(nb("« " + t + " »"))}</div>
<div style="margin-top:20px;font-family:{T};font-size:24px;color:{acc};font-weight:600;">{e(auteur)}</div></div>'''


def middle(*blocs, gap=40):
    """Zone centrale qui occupe tout l'espace libre entre le titre et le bandeau final, contenu centré verticalement."""
    return f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:{gap}px;padding:44px 0;">{"".join(blocs)}</div>'


def cta(texte="Essai gratuit 7 jours, sans carte bancaire", fond="clair"):
    bg = C['ink'] if fond == "clair" else C['white']
    fg = C['white'] if fond == "clair" else C['ink']
    return f'''<div style="flex:none;display:flex;justify-content:space-between;align-items:center;background:{bg};border-radius:24px;padding:28px 34px;">
<div style="font-family:{T};font-weight:600;font-size:27px;color:{fg};">{e(nb(texte))}</div>
<div style="font-family:{D};font-weight:700;font-size:34px;color:{C['amber'] if fond == 'clair' else C['teal']};">vitriz.fr →</div></div>'''


def shell(inner, fond="clair"):
    bg = C['paper'] if fond == "clair" else C['teal']
    deco = ""
    if fond != "clair":
        deco = f'<div style="position:absolute;right:-220px;top:-220px;width:620px;height:620px;border-radius:50%;background:{C["teal_dark"]};opacity:.55;"></div>'
    return f'''<div style="position:relative;overflow:hidden;width:{W}px;height:{H}px;box-sizing:border-box;padding:68px 72px 64px 72px;background:{bg};">
{deco}<div style="position:relative;height:100%;display:flex;flex-direction:column;">{inner}</div></div>'''


def page(inner, fontdir):
    f = fontdir.rstrip("/")
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face{{font-family:'Space Grotesk';src:url('{f}/space-grotesk/files/space-grotesk-latin-500-normal.woff2');font-weight:500}}
@font-face{{font-family:'Space Grotesk';src:url('{f}/space-grotesk/files/space-grotesk-latin-700-normal.woff2');font-weight:700}}
@font-face{{font-family:'Inter';src:url('{f}/inter/files/inter-latin-400-normal.woff2');font-weight:400}}
@font-face{{font-family:'Inter';src:url('{f}/inter/files/inter-latin-600-normal.woff2');font-weight:600}}
body{{margin:0}}</style></head><body>{inner}</body></html>"""


def page_depot(inner, titre="VITRIZ"):
    """Page à déposer dans le dépôt Minerve04/vitriz-social (a-publier/<date>.html) : polices dans ../fonts/."""
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>{e(titre)}</title><style>
@font-face{{font-family:'Space Grotesk';src:url('../fonts/space-grotesk-latin-500-normal.woff2');font-weight:500}}
@font-face{{font-family:'Space Grotesk';src:url('../fonts/space-grotesk-latin-700-normal.woff2');font-weight:700}}
@font-face{{font-family:'Inter';src:url('../fonts/inter-latin-400-normal.woff2');font-weight:400}}
@font-face{{font-family:'Inter';src:url('../fonts/inter-latin-600-normal.woff2');font-weight:600}}
body{{margin:0}}</style></head><body>{inner}</body></html>"""


def render(html_str, out_path, html_path="post.html"):
    """Rend la page en JPEG 1080x1350 (scale 1, qualité 90) et renvoie un dict de contrôles."""
    import os
    from playwright.sync_api import sync_playwright
    open(html_path, "w", encoding="utf-8").write(html_str)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        pg.goto("file://" + os.path.abspath(html_path))
        pg.wait_for_timeout(400)
        checks = pg.evaluate("""() => {
          const root = document.body.firstElementChild;
          const inner = root.lastElementChild;
          return {scrollH: document.documentElement.scrollHeight, scrollW: document.documentElement.scrollWidth,
                  innerOverflow: inner.scrollHeight > inner.clientHeight + 1,
                  fonts: [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight)};
        }""")
        pg.screenshot(path=out_path, type="jpeg", quality=90, clip={"x": 0, "y": 0, "width": W, "height": H})
        b.close()
    checks["ok"] = checks["scrollH"] <= H and checks["scrollW"] <= W and not checks["innerOverflow"]
    return checks
